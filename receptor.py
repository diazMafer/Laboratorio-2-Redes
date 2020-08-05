"""
Universidad del Valle de Guatemala
Redes 
Autores: Ana Hernandez y Maria Fernanda López
"""

import socket        
from bitarray import bitarray
from zlib import crc32
from Hamming import *



def fletcher_checksum(message):
    checksum = crc32(message)
    f_check = open("checksum.txt", "r")
    checksum_sent = f_check.readline()
    f_check.close()
    print('checksum sent ', checksum_sent, ' checksum read ', checksum)
    if str(checksum) != str(checksum_sent):
        return False
    return True

def receive_safe_message_fc(message):
    has_errors = fletcher_checksum(message)
    # intentar decodificar 
    try:
        sent_text = bitarray(message.decode()).tobytes().decode()
    except:
        # sent_text = unicode(bitarray(message).tobytes(), errors='ignore')
        # sent_text = bitarray(message).tobytes().decode('cp1252')
        sent_text = bitarray(message.decode('cp1252')).tobytes().decode('cp1252')
    # sent_text = bitarray(message).tobytes().decode('utf-8')
    # print('message ', message, ' type ', type(message), ' decoded msg ', bitarray(message.decode()).tobytes())
    # sent_text = bitarray(message.decode()).tobytes().decode()
    return [has_errors, sent_text]

def decode_message(message):
    try:
        sent_text = bitarray(message.decode()).tobytes().decode()
    except:
        # sent_text = unicode(bitarray(message).tobytes(), errors='ignore')
        # sent_text = bitarray(message).tobytes().decode('cp1252')
        sent_text = bitarray(message.decode('cp1252')).tobytes().decode('cp1252')
    # sent_text = bitarray(message).tobytes().decode('utf-8')
    # print('message ', message, ' type ', type(message), ' decoded msg ', bitarray(message.decode()).tobytes())
    # sent_text = bitarray(message.decode()).tobytes().decode()
    return sent_text

def receive_message(msg, method):
    # if true -> message has no errors
    # if false -> message has errors
    if method == "c":
        has_errors, rec_msg = receive_safe_message_fc(msg)
        if has_errors == False:
            print("El mensaje enviado fue recibido con errores.")
            print("Mensaje recibido: ", rec_msg)
        else:
            print("El mensaje enviado fue recibido correctamente.")
            print("Mensaje recibido: ", rec_msg)
    else:
        result = hammingCorrection(list(msg))
        finalMessage = ' '.join(map(str, result)) 
        rec_msg = decode_message((finalMessage.replace(" ", "")).encode())
        print("Mensaje recibido: ", rec_msg)


s = socket.socket()

s.bind(("localhost", 9990)) 
s.listen(1) 
c, addr_socketc = s.accept() 

print("Conexion desde", addr_socketc)

exit_str = bytes('exit', 'utf-8')
# recibir_objeto
while True:
    recibido = c.recv(1024) 
    # print("recv", recibido)
    if recibido == exit_str:
        break
    elif recibido == ''.encode():
        continue
    data = recibido.decode('utf-8').split('/')
    method = data[0]
    message = data[1]
    if (method == "h"):
        receive_message(message, method)
    else:
        receive_message(message.encode(), method)

c.close()
s.close()
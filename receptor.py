"""
Universidad del Valle de Guatemala
Redes 
Autores: Ana Hernandez y Maria Fernanda López
"""

import socket        
from Fletcher import *      
from bitarray import bitarray
from zlib import crc32

# recibido = '010100001101111011011000110000100100001001110011011011110111100100100000001100001011010110011000000100'

def fletcher_checksum(message):
    checksum = crc32(message)
    f_check = open("checksum.txt", "r")
    checksum_sent = f_check.read()
    if checksum != checksum_sent:
        return False
    return True

def receive_safe_message_fc(message):
    has_errors = fletcher_checksum(message)
    # intentar decodificar 
    # try:
    #     sent_text = (message).decode()
    # except:
    #     # sent_text = unicode(bitarray(message).tobytes(), errors='ignore')
    #     # sent_text = bitarray(message).tobytes().decode('cp1252')
    #     sent_text = (message).decode()
    # sent_text = bitarray(message).tobytes().decode('utf-8')
    sent_text = (message).decode()
    return [has_errors, sent_text]

def receive_message(msg):
    # if true -> message has no errors
    # if false -> message has errors
    has_errors, rec_msg = receive_safe_message_fc(msg)
    if not has_errors:
        print("El mensaje enviado fue recibido con errores.")
        print("Mensaje recibido: ", rec_msg)
    else:
        print("El mensaje enviado fue recibido correctamente.")
        print("Mensaje recibido: ", rec_msg)

s = socket.socket()

s.bind(("localhost", 9990)) 
s.listen(1) 
c, addr_socketc = s.accept() 

print("Conexion desde", addr_socketc)

# recibir_objeto
recibido = c.recv(1024) 

print((recibido.decode('ascii')))
receive_message(recibido)

c.close()
s.close()
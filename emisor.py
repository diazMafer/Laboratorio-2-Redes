"""
Universidad del Valle de Guatemala
Redes 
Autores: Ana Hernandez y Maria Fernanda
"""
import socket
import math
from Hamming import *
from bitarray import bitarray
from zlib import crc32

s = socket.socket()
s.connect(("localhost", 9990))

def read_message():
    ba = bitarray()
    message = str(input("Ingrese mensaje a enviar: "))
    ba.frombytes(message.encode('utf-8'))
    print(ba)
    data = ""
    for bit in ba:
        data = data + str(int(bit))
    return data

def send_safe_message(message):
    s.send(bytes(message, "utf-8"))

def generateNoise(message):
    x = len(message)
    print(x)
    if (x < 100):
        return message
    else:
        count = math.floor(x/100)
        s = list(message)
        for z in range(0, count):
            c = z + 0
            if (s[c] == "0"):
                print(s[c])
                s[c] = "1"
            else:
                print(s[c])
                s[c] = "0"
                
        print("".join(s))
        return str("".join(s))
 
data = read_message()
# para CRC32 checksum
f_checksum = open("checksum.txt", "w")
print(crc32(data.encode()))
f_checksum.write(str(crc32(data.encode())))
# para verificación de Hamming 
hmsg = Hamming.hammingMessage(data)
print(hmsg + '\n')
nmsg = generateNoise(hmsg)
result = Hamming.hammingCode(nmsg)
finalMessage = ""
send_safe_message(data)
# if (result == 0):
#     print("El mensaje a enviar no cuenta con ningun error")
#     #aqui debe ir el paso de decode hamming code
#     send_safe_message(nmsg)
# elif result == -1:
#     #aqui igual debe ir paso de decode hamming code
#     send_safe_message(nmsg)
#     print ("No se pudo detectar el error")
# else:
#     print(result)
#     finalMessage = str(result)
#     send_safe_message(finalMessage)

# s.close()
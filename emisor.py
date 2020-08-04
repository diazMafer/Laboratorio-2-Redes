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
    data = ""
    for bit in ba:
        data = data + str(int(bit))
    return data

def send_safe_message(message):
    s.send(bytes(message, "utf-8"))

def generateNoise(message):
    x = len(message)
    if (x < 100):
        return message
    else:
        count = math.floor(x/100)
        s = list(message)
        for z in range(0, count):
            c = z * 100
            if (s[c] == "0"):
                s[c] = "1"
            else:
                s[c] = "0"
                
        return str("".join(s))
 
data = read_message()
# para CRC32 checksum
f_checksum = open("checksum.txt", "w")
f_checksum.write(str(crc32(data.encode())))

# para verificación de Hamming 
hmsg = hammingCodes(data)
lstring = ' '.join(map(str, hmsg)) 
nmsg = generateNoise(lstring)
lnmsg = nmsg.split()
result = hammingCorrection(lnmsg)
finalMessage = ' '.join(map(str, result)) 

send_safe_message(finalMessage)


s.close()
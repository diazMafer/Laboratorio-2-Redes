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
import time

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
    msg = message.split("/")[1]
    method = message.split("/")[0] + "/"
    s.send(bytes(method, "utf-8") + bytes(msg, "utf-8"))

def generateNoise(message):
    # print("genereando ruido ....")
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
 
def checkHamming():
    data = read_message()
    hmsg = hammingCodes(data)
    lstring = ' '.join(map(str, hmsg)) 
    lnmsg = generateNoise(lstring)
    fmessage = 'h' + '/' + lnmsg.replace(" ", "")
    send_safe_message(fmessage)

def checkSum():
    data = read_message()
    # para CRC32 checksum
    f_checksum = open("checksum.txt", "w")
    f_checksum.write(str(crc32(data.encode())))
    f_checksum.close()
    time.sleep(2)
    nmsg = generateNoise(data.encode())
    fmessage = 'c' + '/' + nmsg
    send_safe_message(fmessage)

def exit_send():
    s.send(bytes('exit', "utf-8"))
    s.close()

def test_hamming(msg):
    ba = bitarray()
    ba.frombytes(msg.encode('utf-8'))
    data = ""
    for bit in ba:
        data = data + str(int(bit))
    hmsg = hammingCodes(data)
    lstring = ' '.join(map(str, hmsg)) 
    lnmsg = generateNoise(lstring)
    fmessage = 'h' + '/' + lnmsg.replace(" ", "")
    send_safe_message(fmessage)

def test_crc32(msg):
    ba = bitarray()
    message = msg
    ba.frombytes(message.encode('utf-8'))
    data = ""
    for bit in ba:
        data = data + str(int(bit))
    f_checksum = open("checksum.txt", "w")
    f_checksum.write(str(crc32(data.encode())))
    f_checksum.close()
    nmsg = generateNoise(data)
    fmessage = 'c' + '/' + nmsg
    send_safe_message(fmessage)

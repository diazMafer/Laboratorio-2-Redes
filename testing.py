from emisor import *
import time

s = open('oraciones.txt')                                                                                       
sentences = []                                                                                                  

for i in range(25): 
    sentences.append(s.readline()) 

results = [ True for i in range(11) ] + [ False for i in range(19) ]

# test CRC32
for msg in sentences:
    time.sleep(1)
    test_crc32(msg[:-1])

# test hamming 
for msg in sentences:
    test_hamming(msg[:-1])

exit_send()

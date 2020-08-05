from emisor import *

s = open('oraciones.txt')                                                                                       
sentences = []                                                                                                  

for i in range(30): 
    sentences.append(s.readline()) 

results = [ True for i in range(10) ] + [ False for i in range(20) ]

# test CRC32
for msg in sentences:
    test_crc32(msg[:-1])

# test hamming 
for msg in sentences:
    test_hamming(msg[:-1])

exit_send()
# stats para CRC32
test_crc = open('results_crc.txt', 'r')
crc_vals = []
crc_times = []
for i in range(30):
    line = test_crc.readline().split(";")
    crc_vals.append(line[0])
    crc_times.append(line[1])

# comparacion de cuantos errores detecto que eran errores
wrong = 0
avg_time = 0
for i in range(30):
    if crc_vals[i] != str(results[i]):
        wrong += 1
    avg_time += crc_times[i]

print('------------------- STATS CRC32 -------------------')
print('Min time:', min(crc_times))
print('Max time:', max(crc_times))
print('Avg time:', str(avg_time/30))
print('Incorrectly detected:', str(wrong))
print('Correctly detected:', str(30-wrong))
print('Accuracy:', str(((30-wrong)/30)*100) + '%')
print('---------------------------------------------------')
test_crc.close()

#stats para Hamming
test_ham = open('results_ham.txt', 'r')
ham_str = []
ham_times = []
for i in range(30):
    line = test_crc.readline().split(";")
    ham_str.append(line[0])
    ham_times.append(line[1])
# comparacion de cuantos errores detecto que eran errores
wrong = 0
avg_time = 0
for i in range(30):
    if ham_str[i] != str(results[i]):
        wrong += 1
    avg_time += ham_times[i]

print('------------------ STATS HAMMING ------------------')
print('Min time:', min(ham_times))
print('Max time:', max(ham_times))
print('Avg time:', str(avg_time/30))
print('Incorrectly detected:', str(wrong))
print('Correctly detected:', str(30-wrong))
print('Accuracy:', str(((30-wrong)/30)*100) + '%')
print('---------------------------------------------------')
    
test_ham.close()
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# stats para CRC32
test_crc = open('results_crc.txt', 'r')
crc_vals = []
crc_times = []
for i in range(30):
    line = test_crc.readline()[:-1].split(";")
    try:
        crc_vals.append(line[0])
        crc_times.append(float(line[1]))
    except:
        continue
test_crc.close()
# comparacion de cuantos errores detecto que eran errores
wrong = 0
avg_time = 0

for i in range(len(crc_times)):
    if crc_vals[i] != 'False':
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

#stats para Hamming
test_ham = open('results_ham.txt', 'r')
s = open('oraciones.txt')                                                                                       
sentences = []                                                                                                  
for i in range(22): 
    sentences.append(s.readline()) 


ham_str = []
ham_times = []
for i in range(22):
    line = test_ham.readline()[:-1].split(";")
    ham_str.append(line[0])
    ham_times.append(float(line[1]))
# comparacion de cuantos errores detecto que eran errores
wrong = 0
avg_time = 0
for i in range(22):
    if ham_str[i] != sentences[i]:
        wrong += 1
    avg_time += ham_times[i]

print('------------------ STATS HAMMING ------------------')
print('Min time:', min(ham_times))
print('Max time:', max(ham_times))
print('Avg time:', str(avg_time/22))
print('Incorrectly corrected:', str(wrong))
print('Correctly corrected:', str(22-wrong))
print('Accuracy:', str(((22-wrong)/22)*100) + '%')
print('---------------------------------------------------') 
    
test_ham.close()

def times():
    asistencia = ['CRC2', 'Hamming']
    men_means = [min(crc_times), max(crc_times)]
    women_means = [min(ham_times), max(ham_times)]

    x = np.arange(len(asistencia))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Min')
    rects2 = ax.bar(x + width/2, women_means, width, label='Max')
    ax.set_ylabel('Tiempo')
    ax.set_title('Tiempos maximos y minimos ')
    ax.set_xticks(x)
    ax.set_xticklabels(asistencia)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.show()

def crc2Graph():
    #Definimos una lista con paises como string
    etiquetas = ['0-100', '100-200', '200 < ']
    #Definimos una lista con ventas como entero
    wrong = 0
    for i in range(10):
        if crc_vals[i] != 'False':
            wrong += 1

    wrong1 = 0
    for i in range(11,20):
        if crc_vals[i] != 'False':
            wrong1 += 1
    
    wrong2 = 0
    for i in range(21,30):
        if crc_vals[i] != 'False':
            wrong2 += 1

   
    res1 = [wrong, wrong1, wrong2]
    res2 = [int(10-wrong), int(10-wrong1), int(10-wrong2)]

    x = np.arange(len(etiquetas))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, res1, width, label='Correctos')
    rects2 = ax.bar(x + width/2, res2, width, label='Incorrectos')
    ax.set_ylabel('Cantidad de bits')
    ax.set_title('Aciertos y Desaciertos CRC2')
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig('doble_barra.png')
    #Mostramos la grafica con el metodo show()
    plt.show()

times()
crc2Graph()
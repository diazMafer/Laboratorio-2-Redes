from emisor import *
import os


def menu():
	print ("Selecciona un algoritmo a utilizar")
	print ("\t1. Corrector - Hamming Code")
	print ("\t2. Verificador - Check Sum")
	print ("\t3. Salir")



while True:
	# Mostramos el menu
	menu()

	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		checkHamming()
	elif opcionMenu=="2":
		checkSum()
	elif opcionMenu=="3":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
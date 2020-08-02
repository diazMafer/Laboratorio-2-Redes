"""
Universidad del Valle de Guatemala
Redes 
Autores: Ana Hernandez y Maria Fernanda
"""
import socket
s = socket.socket()
s.connect(("localhost", 9999))
s.send(bytes("mensaje del cliente", "utf-8"))

# s.close()
"""
Universidad del Valle de Guatemala
Redes 
Autores: Ana Hernandez y Maria Fernanda
"""

import socket              

s = socket.socket()

s.bind(("localhost", 9990)) 
s.listen(1) 
c, addr_socketc = s.accept() 

print("Conexion desde", addr_socketc)

recibido = c.recv(1024) 
print(recibido.decode("utf-8"))


c.close()
s.close()
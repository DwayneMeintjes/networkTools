import random
import socket

password = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*)(_+-=}{][:,./?'

i = 0

size = int(input("Enter password size: "))

while i < size:
    password += random.choice(chars)
    
print("Generated Password: \t" + password + "\n")

server = socket.socket(socket.SOCK_STREAM, socket.AF_INET)

host = input("Enter remote host: ")
port = int("Enter port to send the data through: ")


server.connect((host,port))
while True:
    server.send(password.encode())

server.close()



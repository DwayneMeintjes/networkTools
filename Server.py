import socket

port = 6000
s = socket.socket()
host = socket.gethostname()
s.bind((host,port))
s.listen(10)


print ("Server Listening...")

while True:
    conn, addr = s.accept()
    print ("Got connection from", addr)
    data = conn.recv(1024)
    print("Server received", repr(data))

    filename="C:\Users\R3ZURR3CTI0N\Downloads\Gantt213.xlsx"

    f = open(filename, "rb")
    l = f.read(1024)
    while (l):
        conn.send(l)
        print("Sent ", repr(l))
        l = f.read(1024)
    f.close()

    print("Done sending")
    conn.send("Thank you for connecting")
    conn.close()

    
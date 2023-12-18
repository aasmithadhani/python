import socket

def mpm ():
    host = '127.0.0.1'
    port = 6000
    s = socket.socket()
    s.connect((host,port))
    print("connection established !!")
    while True:
        try:
            print()
            x = input("Enter new message")
            y = x.encode('ascii')
            s.send(y)
            print()
            data = s.recv(1024)
            d = data.decode('ascii')
            print("server",d)

        except KeyboardInterrupt:
            print()
            print("connection terminated")
            s.send('connection from client terminated'.encode('ascii'))
            break

mpm()

import socket
s=socket.socket()
port=3000
#id="client"
s.connect(('127.0.0.1',port))
s.recv(1024)
s.send("abcd 3001".encode())
s.close()
s=socket.socket()
port=3001
s.bind(('',port))
s.listen(5)
c,addr=s.accept()
c.send(" ".encode())
print(c.recv(1024).decode())
s.close()
c.close()
print("after removal of server")
s=socket.socket()
port=3001
s.bind(('',port))
s.listen(5)
c,addr=s.accept()
c.send(" ".encode())
print(c.recv(1024).decode())
s.close()
c.close()
print("after adding server")
s=socket.socket()
port=3001
s.bind(('',port))
s.listen(5)
c,addr=s.accept()
c.send(" ".encode())
print(c.recv(1024).decode())
s.close()
c.close()
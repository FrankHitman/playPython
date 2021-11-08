import socket

HOST = '127.0.0.1'
PORT = 50006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('connected to ' + HOST + ':' + str(PORT))
s.sendall('Hello, world')
print('sent data')
data = s.recv(1024)
print 'Received', repr(data)
s.close()

# Franks-Mac:port_forward frank$ python client.py
# connected to 127.0.0.1:50006
# sent data
# Received 'server response: Hello, world proxy-append1 proxy-append2'
# Franks-Mac:port_forward frank$ python client.py
# connected to 127.0.0.1:50006
# sent data
# Received 'server response: Hello, world proxy-append1 proxy-append2'
# Franks-Mac:port_forward frank$
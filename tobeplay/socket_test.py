#encoding=utf-8
import socket
import datetime

HOST='0.0.0.0'
PORT=3434

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr=s.accept()
    print str(addr)
    dt=datetime.datetime.now()
    conn.send(str(dt))
    print('send time,',str(dt))
    conn.close()

# Echo server program
import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    try:
        conn, addr = s.accept()
        print 'Connected by', addr
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall("server response: " + data)
    except KeyboardInterrupt:
        print('user terminate')
        break
    except Exception as e:
        print('run into error: {}'.format(e))
        continue
    finally:
        conn.close()

# Franks-Mac:port_forward frank$ python server.py
# Connected by ('127.0.0.1', 53169)
# Connected by ('127.0.0.1', 53171)
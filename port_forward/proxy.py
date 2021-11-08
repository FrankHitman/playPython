import socket

if __name__ == '__main__':
    local_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_s.bind(('127.0.0.1', 50006))
    local_s.listen(5)

    while True:
        try:
            from_conn, addr = local_s.accept()
            print('connection from {}'.format(addr))
            from_data = from_conn.recv(1024)
            if not from_data:
                break

            to_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            to_s.connect(('127.0.0.1', 50007))
            to_s.sendall(from_data + ' proxy-append1')
            to_data = to_s.recv(1024)

            from_conn.sendall(to_data + ' proxy-append2')
        except KeyboardInterrupt:
            print('user terminate')
            break
        except Exception as e:
            print('error {}'.format(e))
            continue
        finally:
            from_conn.close()
            to_s.close()

# Franks-Mac:port_forward frank$ python proxy.py
# connection from ('127.0.0.1', 53168)
# connection from ('127.0.0.1', 53170)
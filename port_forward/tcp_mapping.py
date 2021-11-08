# -*- coding: utf-8 -*-
# tcp mapping created by hutaow(hutaow.com) at 2014-08-31
# 参考自 https://windard.com/project/2017/03/10/Proxy-In-Python

import socket
import threading

# 端口映射配置信息
REMOTE_IP = '22.22.22.22'
REMOTE_PORT = 12345
LOCAL_IP = '0.0.0.0'
LOCAL_PORT = 3290

# 接收数据缓存大小
PKT_BUFF_SIZE = 102400


# 调试日志封装
def send_log(content):
    print(content)


# 单向流数据传递
def tcp_mapping_worker(conn_receiver, conn_sender):
    while True:
        try:
            data = conn_receiver.recv(PKT_BUFF_SIZE)
        except Exception as e:
            send_log('Event: receive Connection closed: {}'.format(e))
            break

        if not data:
            send_log('Info: No more data is received.')
            break

        try:
            conn_sender.sendall(data)
        except Exception as e:
            send_log('Error: Failed sending data: {}'.format(e))
            break

        # send_log('Info: Mapping data > %s ' % repr(data))
        send_log('Info: Mapping > %s -> %s > %d bytes.' % (
            conn_receiver.getpeername(), conn_sender.getpeername(), len(data)))

    conn_receiver.close()
    conn_sender.close()


# 端口映射请求处理
def tcp_mapping_request(local_conn, remote_ip, remote_port):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        remote_socket.connect((remote_ip, remote_port))
        send_log('connect to remote server: {}:{}'.format(remote_ip,remote_port))
    except Exception as e:
        local_conn.close()
        send_log('Error: Unable to connect to the remote server: {}'.format(e))
        return

    # first transmit data from local to remote
    threading.Thread(target=tcp_mapping_worker, args=(local_conn, remote_socket)).start()

    threading.Thread(target=tcp_mapping_worker, args=(remote_socket, local_conn)).start()


# 端口映射函数
def tcp_mapping(remote_ip, remote_port, local_ip, local_port):
    local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_server.bind((local_ip, local_port))
    local_server.listen(5)

    send_log('Event: Starting mapping service on ' + local_ip + ':' + str(local_port) + ' ...')

    while True:
        try:
            (local_conn, local_addr) = local_server.accept()
        except KeyboardInterrupt:
            send_log('user quit program')
            break
        except Exception as e:
            send_log('local connection run into error: {}'.format(e))
            continue

        send_log('Event: Receive mapping request from %s:%d.' % local_addr)

        threading.Thread(target=tcp_mapping_request, args=(local_conn, remote_ip, remote_port)).start()

    local_server.close()


# 主函数
if __name__ == '__main__':
    tcp_mapping(REMOTE_IP, REMOTE_PORT, LOCAL_IP, LOCAL_PORT)

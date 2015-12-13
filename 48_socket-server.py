'''
原始Python服务器

一个socket包含四个地址信息: 两台计算机的IP地址和两个进程所使用的端口(port)：
1) IP地址用于定位计算机，
2) 而port用于定位进程 (一台计算机上可以有多个进程分别使用不同的端口)。

'''

'''
TCP socket

服务器端，我们使用bind()方法来赋予socket以固定的地址和端口，并使用listen()方法来被动的监听该端
口。当有客户尝试用connect()方法连接的时候，服务器使用accept()接受连接，从而建立一个连接的socket。
'''
import socket

# Address
HOST = ''
PORT = 8001

reply = 'Yes'

# Configure socket
# socket.socket()创建一个socket对象，并说明socket使用的是IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) 

# passively wait, 3: maximum number of connections in the queue
s.listen(3)
# accept and establish connection
coon, addr = s.accept()
# receive message
request = coon.recv(1024)

print('request = ',request)
print('Connected by = ', addr)

coon.sendall(reply)
coon.close()

'''
然后用另一台电脑作为客户，我们主动使用connect()方法来搜索服务器端的IP地址(在Linux中，你可以用$ifconfig来查询自己的IP地址)和端口，以便客户可以找到服务器，并建立连接。
'''


import socket 

HOST = '127.0.0.1'
PORT = 8001

request = 'can you help me?'

# Configure socket
# socket.socket()创建一个socket对象，并说明socket使用的是IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) 

# 3.* socket.send 传递的数据必须是bytes。
# 发送和接收数据时需要做下编码转换。
s.sendall(request.encode())
reply = s.recv(1024)
print('reply is ',reply.decode())

s.close()

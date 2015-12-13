'''
HTTP协议利用请求-回应(request-response)的方式来使用TCP socket。
客户端向服务器发一段文本作为request，服务器端在接收到request之后，向客户端发送一段文本作为response。
在完成了这样一次request-response交易之后，TCP socket被废弃。下次的request将建立新的socket。
request和response本质上说是两个文本，只是HTTP协议对这两个文本都有一定的格式要求。

127.0.0.1:8000
'''

# 现在，我们写出一个HTTP服务器端：

# 服务器会根据request向客户传输的两条信息text_content和pic_content中的一条
'''
整个response分为起始行(start line), 头信息(head)和主体(body)三部分。

1、 起始行： (HTTP/1.x 200 OK)
    他实际上又由空格分为三个片段：
(1) HTTP/1.x表示所使用的HTTP版本
(2) 200表示状态(status code)，200是HTTP协议规定的，表示服务器正常接收并处理请求
(3) OK是供人来阅读的status code。

2、 头信息：(Content-Type: text/html)
    跟随起始行，它和主体之间有一个空行。
    这里的text_content或者pic_content都只有一行的头信息，text_content用来表示主体信息的类型为html文本。
    pic_content的头信息(Content-Type: image/jpg)说明主体的类型为jpg图片(image/jpg)。

3、 主体
    主体信息为html或者jpg文件的内容。
'''

'''
我们会用浏览器作为客户端。request由客户端程序发给服务器。
尽管request也可以像response那样分为三部分，request的格式与response的格式并不相同。
request由客户发送给服务器，比如下面是一个request：
        GET /test.jpg HTTP/1.x
        Accept: text/*
起始行可以分为三部分，第一部分为请求方法(request method)，第二部分是URL，第三部分为HTTP版本。
request method可以有GET， PUT， POST， DELETE， HEAD。最常用的为GET和POST。GET是请求服务器发送资源给客户，POST是请求服务器接收客户送来的数据。
当我们打开一个网页时，我们通常是使用GET方法；当我们填写表格并提交时，我们通常使用POST方法。
第二部分为URL，它通常指向一个资源(服务器上的资源或者其它地方的资源)。像现在这样，就是指向当前服务器的当前目录的test.jpg。

按照HTTP协议的规定，服务器需要根据请求执行一定的操作。
正如我们在服务器程序中看到的，我们的Python程序先检查了request的方法，随后根据URL的不同，来生成不同的response(text_content或者pic_content)。随后，这个response被发送回给客户端。
'''

import socket

# Address
HOST = ''
PORT = 8000

# Prepare HTTP response
text_content = '''HTTP/1.x 200 OK       
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg','rb')
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
pic_content = pic_content.encode('utf-8') + f.read()
f.close()

# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()

    # python3.4 return 的是byte类型，python2 return 的是str类型，应该加 decode('utf-8')
    request    = conn.recv(1024).decode('utf-8')
    method    = request.split(' ')[0]
    src            = request.split(' ')[1]

    # deal with GET method
    if method == 'GET':
        # ULR    
        if src == '/test.jpg':
            content = pic_content
        else: content = bytes(text_content,'gbk')

        print('Connected by', addr)
        print('Request is:', request)
        conn.sendall(content)
    # close connection
    conn.close()
'''
SocketServer

首先使用SocketServer包来方便的架设服务器。

在上面使用socket的过程中，我们先设置了socket的类型，然后依次调用bind(),listen(),accept()，最后使用while循环来让服务器不断的接受请求。

上面的这些步骤可以通过SocketServer包来简化。

SocketServer:
'''

import socketserver

HOST = ''
PORT = 8000

text_content = '''
HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
<script type="text/javascript"
src="http://blog.plotcup.com/a/"http://127.0.0.1:35729/livereload.js"></script>
</head>
<html>

<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form> 
</html>
'''

f = open('test.jpg','rb')
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''

# TypeError: Can't convert 'bytes' object to str implicitly 加'.encode('utf-8')'
pic_content = pic_content.encode('utf-8') + f.read()
f.close()
# This class defines response to each request
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        # TypeError: Type str doesn't support the buffer API
        request = self.request.recv(1024).decode('utf-8')

        print('Connected by',self.client_address[0])
        print('Request is', request)

        method     = request.split(' ')[0]
        src        = request.split(' ')[1]

        if method == 'GET':
            if src == '/test.jpg':
                content = pic_content
            # TypeError: 'str' does not support the buffer interface
            else: content = bytes(text_content,'gbk')
            self.request.sendall(content)

        if method == 'POST':
            form = request.split('\r\n')
            idx = form.index('')             # Find the empty line
            entry = form[idx:]               # Main content of the request

            value = entry[-1].split('=')[-1]
            # TypeError: 'str' does not support the buffer interface
            self.request.sendall(bytes(text_content+ '\n <p>' + value + '</p>','gbk') )
            ######
            # More operations, such as put the form into database
            # ...
            ######


# Create the server
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
# Start the server, and work forever
server.serve_forever()
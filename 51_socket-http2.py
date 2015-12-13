'''
页面新增了表格和提交(submit)按钮。在表格中输入aa并提交，页面显示出aa。
'''

# encoding: utf-8

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
<p>Wow, Python Server,尉勇强</p>
<IMG src="test.jpg"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form> 
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
    if method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')             # Find the empty line
        entry = form[idx:]               # Main content of the request

        value = entry[-1].split('=')[-1]
        conn.sendall(bytes(text_content + '\n <p>尉勇强' + value + '</p>','gbk'))
    # close connection
    conn.close()
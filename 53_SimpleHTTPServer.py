'''
SimpleHTTPServer: 使用静态文件来回应请求

HTTP协议基于TCP协议，但增加了更多的规范。这些规范，虽然限制了TCP协议的功能，但大大提高了信息封装和提取的方便程度。

对于一个HTTP请求(request)来说，它包含有两个重要信息：请求方法和URL。

请求方法(request method)       URL                操作
GET                           /                  发送text_content
GET                           /text.jpg          发送pic_content
POST                          /                  分析request主体中包含的value(实际上是我们填入表格的内容); 发送text_content和value
'''

'''
根据请求方法和URL的不同，一个大型的HTTP服务器可以应付成千上万种不同的请求。

在Python中，我们可以使用SimpleHTTPServer包和CGIHTTPServer包来规定针对不同请求的操作。
其中，SimpleHTTPServer可以用于处理GET方法和HEAD方法的请求。它读取request中的URL地址，找到对应的静态文件，分析文件类型，用HTTP协议将文件发送给客户。Python

在Python3.X 中，python -m SimpleHTTPServer 更改为：python3 -m http.server
'''
import socketserver
import http.server

HOST = ''
PORT = 8000

# Create the server, SimpleHTTPRequestHander is pre-defined handler in SimpleHTTPServer package
server = socketserver.TCPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)
# Start the server
server.serve_forever()

'''
这里的程序不能处理POST请求。我会在后面使用CGI来弥补这个缺陷。

值得注意的是，Python服务器程序变得非常简单：
将内容存放于静态文件，并根据URL为客户端提供内容，这让内容和服务器逻辑分离。每次更新内容时，我可以只修改静态文件，而不用停止整个Python服务器。

这些改进也付出代价：
在原始程序中，request中的URL只具有指导意义，我可以规定任意的操作。
在SimpleHTTPServer中，操作与URL的指向密切相关。
我用自由度，换来了更加简洁的程序。
'''













'''
CGIHTTPServer：使用静态文件或者CGI来回应请求

CGIHTTPServer包中的CGIHTTPRequestHandler类继承自SimpleHTTPRequestHandler类，所以可以用来代替上面的例子，来提供静态文件的服务。
此外，CGIHTTPRequestHandler类还可以用来运行CGI脚本。

'''

'''
CGI (Common Gateway Interface)

CGI是服务器和应用脚本之间的一套接口标准。
它的功能是让服务器程序运行脚本程序，将程序的输出作为response发送给客户。
总体的效果，是允许服务器动态的生成回复内容，而不必局限于静态文件。

支持CGI的服务器程接收到客户的请求，根据请求中的URL，运行对应的脚本文件。
服务器会将HTTP请求的信息和socket信息传递给脚本文件，并等待脚本的输出。脚本的输出封装成合法的HTTP回复，发送给客户。

服务器和CGI脚本之间的通信要符合CGI标准。
CGI的实现方式有很多，比如说使用Apache服务器与Perl写的CGI脚本，或者Python服务器与shell写的CGI脚本。
'''

'''
为了使用CGI，我们需要使用BaseHTTPServer包中的HTTPServer类来构建服务器。
'''
'''
在Python 3.x中，BaseHTTPServer, SimpleHTTPServer, CGIHTTPServer整合到http.server包，SocketServer改名为socketserver
'''
import http.server

HOST = ''
PORT = 8001

# Create the server, CGIHTTPRequestHandler is pre-defined handler
server = http.server.HTTPServer((HOST, PORT), http.server.CGIHTTPRequestHandler)
# Start the server
server.serve_forever()
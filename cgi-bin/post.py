'''
cgi包用于提取请求中包含的表格信息。脚本只负责将所有的结果输出到标准输出(使用print)。
CGIHTTPRequestHandler会收集这些输出，封装成HTTP回复，传送给客户端。

对于POST方法的请求，它的URL需要指向一个CGI脚本(也就是在cgi-bin或者ht-bin中的文件)。
CGIHTTPRequestHandler继承自SimpleHTTPRequestHandler，所以也可以处理GET方法和HEAD方法的请求。
此时，如果URL指向CGI脚本时，服务器将脚本的运行结果传送到客户端；当此时URL指向静态文件时，服务器将文件的内容传送到客户端。
'''

import cgi

form = cgi.FieldStorage()

# Output to stdout, CGIHttpServer will take this as response to the client
print("Content-Type: text/html")     # HTML is following
print()                              # blank line, end of headers
print("<p>Hello world!</p>")         # Start of content
print("<p>" +  repr(form['firstname']) + "</p>")
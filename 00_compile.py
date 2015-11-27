'''
编译其他Python文件

cmd 窗口下，编译方法：

>>python 00_compile.py
生成 .pyc 文件（eg:01_HelloWorld.cpython-33.pyc）

>>python -O -m py_compile 01_HelloWorld.py
生成 .pyo 文件（eg:01_HelloWorld.cpython-33.pyo）
'''

import py_compile
py_compile.compile("01_HelloWorld.py")
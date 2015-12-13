'''
在Python中，我们通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序。

subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。
另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。

使用subprocess包中的函数创建子进程的时候，要注意:
1) 在创建子进程之后，父进程是否暂停，并等待子进程运行。
2) 函数返回什么
3) 当returncode不为0时，父进程如何处理。
'''

'''
subprocess.call()
父进程等待子进程完成
返回退出信息(returncode，相当于exit code，见Linux进程基础)

 

subprocess.check_call()
父进程等待子进程完成
返回0
检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try...except...来检查(见Python错误处理)。

 

subprocess.check_output()
父进程等待子进程完成
返回子进程向标准输出的输出结果
检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try...except...来检查。
'''

import subprocess
rc = subprocess.call(["ls","-l"])

import subprocess
out = subprocess.call("ls -l", shell=True)
out = subprocess.call("cd ..", shell=True)
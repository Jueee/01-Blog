'''
模块(module)
在Python中，一个.py文件就构成一个模块。通过模块，你可以调用其它文件中的程序。

Python会在以下路径中搜索它想要寻找的模块：
1.程序所在的文件夹
2.标准库的安装路径
3.操作系统环境变量 PYTHONPATH 所包含的路径
'''
# 引入模块 first
import first
# 引入模块 first，并将模块 first 重命名为 fir
import first as fir
# 从模块 first 中引入 laugh 对象。
# 调用 module 中对象时，即可直接使用function，而不是 module.function。
from first import laugh

for i in range(10):
    #引入模块后，可以通过模块.对象的方式来调用引入模块中的某个对象。
    print("time : ", i)
    first.laugh()
    fir.laugh()
    laugh()

'''
模块包

可以将功能相似的模块放在同一个文件夹（比如说this_dir）中，构成一个模块包。通过

import this_dir.module

引入this_dir文件夹中的module模块。

该文件夹中必须包含一个__init__.py的文件，提醒Python，该文件夹为一个模块包。__init__.py可以是一个空文件。
'''


#在python脚本里面使用那些不再PYTHONPATH上的第三方包或是自己编写的模块
import sys
sys.path.append('E:/360/Python/PythonCode/88Apply')
import timeFormat


'''
使用pth文件，让python方便的import自己写的模块

有时候我们正在修改或调试的程序会是一个库，为修改方便，我们可能不大希望把它放到 site-packages 下面，而是更愿意把它保留在原始的工程目录中，以方便 IDE 和版本控制工具进行管理。那么怎么能让 Python 运行环境找到这个库呢？

原理上， Python 运行环境查找库文件时本质是对 sys.path 列表的遍历，如果我们想给运行环境注册新的类库进来，

要么得用代码给 sys.path 列表增加新路径；
要么得调整 PYTHONPATH 环境变量；
要么就得把库文件复制到已经在 sys.path 设置中的路径中去（比如 site-packages 目录）；
这些方法都不够方便。最简单的办法是用 .pth 文件来实现。Python 在遍历已知的库文件目录过程中，如果见到一个 .pth 文件，就会将文件中所记录的路径加入到 sys.path 设置中，于是 .pth 文件说指明的库也就可以被 Python 运行环境找到了。
'''
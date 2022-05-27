# Python Virtualenv
### 为啥要学python
假设要你实现一个函数，用来完成两个数的“某种运算”，具体的运算类型作为函数的参数传入，然后该函数返回运算结果。比如：
```
Foo("+", 2, 4)　# 返回 6
Foo("*", 3, 5)　# 返回 15
```
python的动态与化繁为简特性
```
def Foo(op, n1, n2) :
    return eval( "%d %s %d" % (n1, op, n2) )
```
### 目的
- 如果有多个python的项目，而且可能会用到想同第三方包的不同版本
- 避免对系统目录下的python环境的污染

### 安装
```
pip install virtualenv

# ubuntu
apt install -y python-virtualenv
```
 
if python version >= 3.3, venv is a ember command to replace virtualenv
````
python3 -m venv <myenvname>
````
### 使用
```
virtualenv new_folder_name
```
执行之后会在当前目录生成一个新命名的目录，目录内包括一些基本的python解释器和第三方包，例如pip。

如果某一个包下载很慢，不想在虚拟环境（venv）里面重新下载一遍怎么办?
```
virtualenv --system-site-packages venv
# 会把系统目录中所安装的包都索引到 venv 目录里面
```
如果不需要了索引系统环境的package了，怎么办？
```
vi venv/pyvenv.cfg 
# set include-system-site-packages = false
```

virtualenv can specify python version 
```
virtualenv --python=/usr/bin/python2.6 <path/to/new/virtualenv/>
```

激活虚拟环境
```
# 类unix
source bin/activate
# windows
\path\to\env\Scripts\activate

# 进入虚拟环境之后，pip install所安装的包都只在虚拟环境的目录中存在
# 强制安装已有的包，并指定版本
pip install —ignore-installed pymodbus==1.2
```
退出虚拟环境
```
deactivate
```

### 对于当前项目的使用启示
阅读a8-application项目时候，会有很多import的error，并且import的包不存在pypi中。如何处理？

可以通过以上方法创建venv，然后把common目录中的内容拷贝到 `venv/Lib/site-packages/` 目录下面

另外a8-application 没有一个总的第三方package索引文件。可以通过 `pip freeze > requirements.txt` 生成。

以后要安装的时候可以使用requirement文件一次性安装所需package。通过 -r 参数指定。
以下通过 -i 参数用豆瓣的源替换掉官方的源 pypi.python.org/simple ，可以加快下载速度。
```
pip install -r pip_requirements.txt -i https://pypi.douban.com/simple
```



# 学习第一个函数 输出(打印)函数 print
# 相关文档：https://www.runoob.com/python3/python-func-print.html

# print (text, sep=' ', end='\n', file=file, flush=false)
# print (输出内容可用,来输出多个内容, 设置间隔符，默认为空格, 设置输出结束结尾，默认为\n换行符, 写入的文件对象, 输出是否缓存)

print (10) # 整数
print (10.5) # 小数
print ('hello world') # 输出字符串，单引号
print ("hello","world", sep=",") # 输出字符串，双引号，输出为 hello,world
print (10 + 10.5) # 包含运算符的表达式

# 学习第二个函数 打开文件函数 open
# 相关文档：https://www.runoob.com/python3/python3-func-open.html
# file 必需，文件路径
# mode 打开模式包含以下
# t 文本模式 x 写模式 b 二进制模式 + 打开一个文件，可读可写 U 通用换行模式
# r 只读模式，文件指针在开头 rb 二进制只读 r+ 读写模式 r+ 读写模式，文件指针在开头 rb+ 二进制读写，文件指针在开头
# w 只写模式，文件不存在会创建 wb 二进制写入，通用于图片 w+ 读写模式，文件不存在会创建 wb+ 二进制读写，，文件不存在会创建，通用于图片
# a 继写模式，文件指针在结尾 ab 二进制继写 a+ 读写模式 ab+ 二进制读写，文件指针在结尾

# open (file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=true, opener=None)
# open (文件路径, 文件模式，可忽略不写mode, 设置缓冲, 文本编码，默认utf8, 报错级别, 区分换行符, 传入的file参数类型, 未知)

f = open ("D:\msg.txt", "a+") # 使用打开函数打开一个位置于C:\，且命名为msg.txt的文件，并且模式为读写，存入 f 变量
print ("hello","world", file = f) # 输出 hello world 输出至 f 变量，相当于写入文本到指定 msg.txt 的文件
f.close () # 关闭这个文件，相当于释放这个资源

import glob#处理文件列表的外部模块
import shutil #文件操作，高级目录和文件操作模块
import os


a=os.path.abspath("a3.py")#返回完整的路径名称
print(a)

b=os.path.basename(a)#返回路径名称的最后一个文件名或者目录名称
print(b)

c=os.path.dirname(a)#返回指定路径名称的上层完整路径名称
print(c)

d=os.path.exists(a)#指定某一指定的路径或文件是否存在
print(d)

e=os.path.getsize(a)#返回指定文件的文件大小
print(e)

f=os.path.isabs(a)#检查指定的文件路径是否为完整的路径名称（绝对路径）
print(f)

g=os.path.isfile(a)#检查指定的路径是否为文件
print(g)

h=os.path.isdir(a)#检查指定的路径是否为目录
print(h)

i=os.path.split(a)#把绝对路径的文件和上层路径分开（取出文件名）
print(i)

j=os.path.splitdrive(a)#把绝对路径的磁盘驱动器和下层路径分开（取出磁盘驱动器）
print(j)

k=os.path.join('E:', '\\IDEA\\Python\\Workspace\\xuexi\\a3.py')#把路径和文件名正确的结合成完整路径
print(k)

files=glob.glob('a*.py')#利用python获取全部的文件名
for f in files:
    print(os.path.abspath(f))

we=os.walk(a)
print(we)

os.system("cp a3.py test.py")#直接将指令交给计算机系统执行

shutil.copyfile("a6.py","a.py")#将前一个文件复制给后一个文件，不包括文件权限
shutil.copy("a6.py","__init__.py")#将前一个文件复制给后一个文件（含有文件的权限属性）
shutil.copy2("a6.py","_init_.py")#将前一个文件复制给后一个文件俺（含有文件的全部属性）
shutil.copytree()#把整个目录s（包含里面的全部内容）复制一份到d中
shutil.rmtree()#删除指定目录中的所有内容
shutil.move()#将s这个目录的或文件搬移到d中
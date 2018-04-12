#fp=open("文件名","文件打开模式")“r”为读取，“w”为写入，“a”也为写入，将写入的内容放到原内容之后

##read()把所有的文件内容以字符串的形式读入到变量中
#readline()一次只读取文件的一行文本，同样也是返回一个字符串
##readlines()把每一行拆开放在每一个支付变量中，并以列表的形式汇聚在一起

fp=open("txt.txt","r+",encoding='utf-8')
zop=fp.readlines()
fp.close()
i=1
for d in zop:
    print("d{}：{}".format(i,d),end="")
    i+=1




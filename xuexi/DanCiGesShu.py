#统计一个文档中单词出现的次数
import re
fp=open("txt.txt","r")
article=fp.read()
new_article=re.sub("[^a-zA-Z\s]","",article)
words=new_article.split()
word_counts={}
for word in words:
    if word in word_counts:
        word_counts[word]=word_counts[word]+1#.upper将英文转化成大写
    else:
        word_counts[word]=1
key_list=list(word_counts.keys())
key_list.sort()
for key in key_list:
    if word_counts:
        print("{}:{}".format(key,word_counts[key]))



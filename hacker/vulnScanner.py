#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    global connSkt
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)#IPv4协议，TCP链接（面向链接的可靠字节流），创建一个链接对象
        connSkt.connect((tgtHost, tgtPort))#链接到主机，连接到tgtHost的远程套接字
        connSkt.send('ViolentPython\r\n')#将数据发送到套接字
        results = connSkt.recv(100)#接受套接字的数据，数据以字符串的形式返回，100位最大的数据量
        screenLock.acquire()

        print('[+] %d/tcp open'%tgtPort)
        print ('[+] ' + str(results))
    except:
        screenLock.acquire()
        print ('[-] %d/tcp closed'%tgtPort)
    finally:
        screenLock.release()
        connSkt.close()



def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)#获取主机的名称
    except:
        print("[-] Cannot resolve '%s': Unknown host".format(tgtHost))
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print ('\n[+] Scan Results for:%d,%d,%d '.format(tgtName[0],tgtName[1],tgtName[2]))
    except:
        print ('\n[+] Scan Results for: ' + tgtIP)

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()

def main():
    parser = argparse.ArgumentParser(description='usage prog '+'--h <target host> --p <target port>')
    parser.add_argument('--h', type=str,dest='tgtHost', help='specify target host')
    parser.add_argument('--p', type=str,dest='tgtPort', help='specify target port[s] separated by comma')

    options = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)



    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()

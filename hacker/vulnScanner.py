#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    global connSkt
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+] %d/tcp open'.format(tgtPort))
        print ('[+] ' + str(results))
    except:
        screenLock.acquire()
        print ('[-] %d/tcp closed'.format(tgtPort))
    finally:
        screenLock.release()
        connSkt.close()



def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host".format(tgtHost))
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print ('\n[+] Scan Results for: ' + tgtName[0])
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

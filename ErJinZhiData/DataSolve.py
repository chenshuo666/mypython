#!/usr/env/env python
# -*- coding: cp936 -*-
'''''
add Head Infomation for pcm file
'''
import sys
import struct
import os




def geneHeadInfo(sampleRate, bits, sampleNum):
    '''''
    ����ͷ��Ϣ����Ҫ�����ʣ�ÿ��������λ����������wav�Ĳ������ֽ���
    '''
    rHeadInfo = '\x52\x49\x46\x46'
    fileLength = struct.pack('i', sampleNum + 36)
    rHeadInfo += fileLength
    rHeadInfo += '\x57\x41\x56\x45\x66\x6D\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00'
    rHeadInfo += struct.pack('i', sampleRate)
    rHeadInfo += struct.pack('i', sampleRate * bits / 8)
    rHeadInfo += '\x02\x00'
    rHeadInfo += struct.pack('H', bits)
    rHeadInfo += '\x64\x61\x74\x61'
    rHeadInfo += struct.pack('i', sampleNum)
    return rHeadInfo


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("usage: python {} inFile sampleRate bits outFile".format(sys.argv[0]))
        sys.exit(1)

    fout = open(sys.argv[4], 'wb')  # �ö����Ƶ�д��ģʽ
    # fout.write(struct.pack('4s','\x66\x6D\x74\x20')) #д��һ������Ϊ4�Ĵ���������Ķ���������Ϊ 66 6D 74 20
    # Riff_flag,afd,fad,afdd, = struct.unpack('4c',fin.read(4)) #�����ĸ��ֽڣ�ÿһ����������һ����ĸ
    # open(sys.argv[4],'wb').write(struct.pack('4s','fmt ')) #���ַ��������ɶ����ƺ���д��
    # open(sys.argv[4],'wb').write('\x3C\x9C\x00\x00\x57') #ֱ��д����������ݣ�3C 9C 00 00 57
    # fout.write(struct.pack('i',6000)) #д��6000�Ķ�������ʽ

    # check whether inFile has head-Info
    fin = open(sys.argv[1], 'rb')
    Riff_flag, = struct.unpack('4s', fin.read(4))
    if Riff_flag == 'RIFF':
        print("{} ��ͷ��Ϣ".format(sys.argv[1]))
        fin.close()
        sys.exit(0)
    else:
        print("{} û��ͷ��Ϣ".format(sys.argv[1]))
        fin.close()
        # ������
        sampleRate = int(sys.argv[2])
        # bitλ
        bits = int(sys.argv[3])

        fin = open(sys.argv[1], 'rb')
        startPos = fin.tell()
        fin.seek(0, os.SEEK_END)
        endPos = fin.tell()
        sampleNum = (endPos - startPos)
        print(sampleNum)
        headInfo = geneHeadInfo(sampleRate, bits, sampleNum)
        fout.write(headInfo)
        fin.seek(os.SEEK_SET)
        fout.write(fin.read())
        fin.close()
        fout.close()
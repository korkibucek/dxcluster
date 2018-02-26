#!/usr/bin/python3

import socket
import sys
import telnetlib

tn = telnetlib.Telnet("dxc.9a5k.com", "7373")

tn.read_until(b"Please enter your call:", 2)
tn.write(b"\n")

tn.read_until(b"=>", 2)
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

tn.close


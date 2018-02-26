#!/usr/bin/python3

import socket
import sys
import telnetlib

tn = telnetlib.Telnet("127.0.0.1")

tn.read_until(b"Username :", 2)
tn.write(b"\n")

tn.read_until(b"Password :", 2)
tn.write(b"\n")

tn.read_until(b"=>", 2)
tn.write(b"exit\n")

tn.close


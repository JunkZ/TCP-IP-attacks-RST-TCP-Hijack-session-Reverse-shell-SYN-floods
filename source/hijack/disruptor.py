#!/usr/bin/python
from scapy.all import *

ip = IP(src="10.0.2.9", dst="10.0.2.10")
tcp = TCP(sport=23, dport=44556, flags="S", seq=3496454775, ack=2090725312)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)

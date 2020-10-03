#!/usr/bin/python
from scapy.all import *

ip = IP(src="10.0.2.10", dst="10.0.2.9")

tcp = TCP(sport=45234, dport=23, flags="A", seq=1236792574, ack=4254435987)

data= "Hello World"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)

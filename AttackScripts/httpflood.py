import sys
import socket
from scapy.all import *

target_ip="e.f.g.h"
target_port=80

syn=IP(dst=target_ip)/TCP(dport=target_port, flags='S')	#SYN packet built
syn_ack=sr1(syn)	#SYN sent, SYN-ACK received

getStr="GET / HTTP/1.1\r\nHost:"+target_ip+"\r\n\r\n"	#Get request

p=IP(dst=target_ip)/TCP(dport=target_port, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags="A")/getStr
#ACK packet built

sr1(p, verbose=0)	#ACK sent
#3 way handshaking is done now

send(IP(dst=target_ip)/TCP(dport=target_port, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq+1, flags="PA")/getStr, loop=1, verbose=0)

#PA -> post ACK, A -> ACK, SA -> SYN-ACK, S -> SYN 
#https://stackoverflow.com/questions/4750793/python-scapy-or-the-like-how-can-i-create-an-http-get-request-at-the-packet-leve
#https://stackoverflow.com/questions/47790325/3-way-handshake-and-get-request-using-scapy-in-python

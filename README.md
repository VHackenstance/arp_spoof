<h3>ARP Spoof</h3>
<h4>Create an ARP Spoofer to test the first step process of On-path Attacks.</h4>
<p>
Exploit the ARP Protocol, become the Person in the Middle of an On-path Attack.  
Redirect the requests and response packet from the Router, through yourself, 
to the Target Host, and vice averse.
</p>
<img src="/assets/images/arp_spoof_diagram1.png" width="450" height="225">
<p>
We can use arpspoof package to give a basic idea of our goals here.
</p>
<p>
</p>
<h4>First target the Client (victim) machine.</h4>
<p></p>
<p><b>arpspoof -i</b> [<i>INTERFACE</i>] <b>-t</b> [<i>INTERFACE_IP</i>] [<i>GATEWAY_IP</i>]</p>
<p><b>arpspoof -i <i>eth0</i> -t <i>192.168.63.174 192.168.63.2</i></b></p> 

<h4>Second: to target the Router (gateway) IP, reverse the IPs.
<p><b>arpspoof -i</b> [<i>INTERFACE</i>] <b>-t</b> [<i>GATEWAY_IP</i>] [<i>TARGET_IP</i>]</p>
arpspoof -i [interface] -t [Gateway IP] [target IP (interface)] 
<p><b>arpspoof -i <i>eth0</i> -t <i>192.168.1.254 192.168.1.72</i></b></p>

<h4>Enable port forwarding on Linux</h4>
<p>As the computer is not a router, this will allow packets to flow through it.</p>
<h4>:~# echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward  </h4>

<img src="/assets/images/arp_spoof_diagram2.png" width="450" height="225">

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

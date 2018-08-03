# network_scanner_with_python
This program uses Python 3.x

The module used in this program are:

1.ipaddress
2.socket
3.netifaces
4.subprocess

It is build to run in Linux platform.

Purpose: It scans for used and unused ips on a network.

How it works:

First, it gets the ip address of the hsot machine with the subnet mask. Then it finds the network. Next, it pings all the possible host ips to see if they are alive. 

As the program uses ICMP to see if a machine is alive, thats why, if the ICMP reply is off on that machine it won't respond. To tackle this problem you can use Reverse-ARP.

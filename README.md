# Custom-Network-Topology
Created a custom network topology using mininet python APIs as given below.

No. of hosts: M
No. of switches: N
All the switches are connected to each other

Odd hosts can only talk to each other and even hosts can talk to each other
All the communication are throttled to 1 mbps for odd hosts and 2 mbps for even hosts

Instructions for executing

> sudo python create.py N M
> pingall

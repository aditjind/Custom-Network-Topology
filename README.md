Custom topology using mininet.
Name: Aditya Jindal
Roll No.: 201230010

To Run:

sudo python create.py <number of switches> <number of hosts per switch>
The topology gets loaded and mininet console is opened.

On another console run:
1. Move into the pox directory located in the home directory. 
2. Type ./pox forwarding.l2_pairs
This starts the pox controller for learning mechanism.

On the mininet console:
1. Type pingall to see the ping responses. Odd nodes ping to odd numbered nodes and even nodes ping to even numbered nodes only.
2. Type iperf h1 h3 to see the t bandwidth allocated to the link. For odd numbered nodes, it is set to 1Mbps and for even numbered nodes, it is set to 2Mbps.
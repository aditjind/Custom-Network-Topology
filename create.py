from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import time
from mininet.node import Controller
import os
import sys
from mininet.link import TCLink
from mininet.node import RemoteController

hosts = []
switches = []
links = []

num_hosts_per_switch = int(sys.argv[2])
num_switches = int(sys.argv[2])
num_hosts = num_hosts_per_switch * num_switches
even_subnet = '10.0.0.'
odd_subnet = '11.1.0.'

def defineTopology():
  net = Mininet(autoStaticArp=True, link=TCLink)

  info("**** Adding Controller ****\n")
  net.addController(controller=RemoteController)

  info("**** Adding Hosts ****\n")
  odd = True
  for i in range(num_hosts):
    if odd == True:
      hosts.append(net.addHost('h'+str(i+1), ip=odd_subnet+str(i+1) ))
      odd = False
    else:
      hosts.append(net.addHost('h'+str(i+1), ip=even_subnet+str(i+1) ))
      odd = True

  info("**** Adding Switches ****\n")
  for i in range(num_switches):
    switches.append(net.addSwitch('s'+str(i+1)))

  info("**** Adding Links ****\n")
  k = 0
  for i in range(num_switches):
    for j in range(num_hosts_per_switch):
      links.append(net.addLink(hosts[k], switches[i]))
      k += 1

  info('**** Allocating Bandwidth ****\n')
  odd_bw = True
  for i in range(len(links)):
    if odd_bw == True:
      links[i].intf1.config(bw=1)
      odd_bw = False
    else:
      links[i].intf1.config(bw=2)
      odd_bw = True

  for i in range(num_switches-1):
    links.append(net.addLink(switches[i], switches[i+1]))

  info('**** Starting Network ****\n')
  net.start()

  info('**** Running CLI ****\n')
  CLI(net)

  info('**** Stopping Network ****\n')
  net.stop()

if __name__ == '__main__':
  setLogLevel('info')
  defineTopology()
Contact GitHub 
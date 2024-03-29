#!/usr/bin/python

from __future__ import print_function

import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Intf
from mininet.node import Controller

class NetworkTopo( Topo ):
    # Builds network topology
    def build( self, **_opts ):

        s = []
        for i in range(8):
            s.append(self.addSwitch ( f's{i}', failMode='standalone' ))

        # Adding hosts
        H1 = self.addHost( 'H1', ip='192.168.0.1/28' )
        H2 = self.addHost( 'H2', ip='192.168.1.2/28' )
        
        # Connecting hosts to switches
        self.addLink(H1, s[5])
        self.addLink(s[5], s[1])
        self.addLink(s[5], s[2])
        self.addLink(s[2], s[7])
        self.addLink(H2, s[7])
        self.addLink(H1, s[4])
        self.addLink(s[4], s[3])
        self.addLink(s[3], s[0])
        self.addLink(s[5], s[0])
        self.addLink(s[0], H2)
        self.addLink(s[6], s[3])
        self.addLink(s[6], H2)


def run():

    topo = NetworkTopo()
    
    net = Mininet( topo=topo, controller=None )
    net.staticArp()
    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()

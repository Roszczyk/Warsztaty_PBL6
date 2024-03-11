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
        H2 = self.addHost( 'H2', ip='192.168.0.2/28' )
        
        # Connecting hosts to switches
        self.addLink(H1, s[5], delay="3ms")
        self.addLink(s[5], s[1], delay="1ms")
        self.addLink(s[5], s[2], delay="2ms")
        self.addLink(s[2], s[7], delay="4ms")
        self.addLink(H2, s[7], delay="1ms")
        self.addLink(H1, s[4], delay="3ms")
        self.addLink(s[4], s[3], delay="2ms")
        self.addLink(s[3], s[0], delay="5ms")
        self.addLink(s[5], s[0], delay="3ms")
        self.addLink(s[0], H2, delay="1ms")
        self.addLink(s[6], s[3], delay="1ms")
        self.addLink(s[6], H2, delay="1ms")


def run():

    topo = NetworkTopo()
    
    net = Mininet( topo=topo, controller=None )
    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()

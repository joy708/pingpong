#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy import *
from scapy.all import *
import random

pckt = rdpcap('all_10_masked.pcap')


def write(pkt):
    wrpcap('all_on_off_masked.pcap', pkt, append=True)  # appends packet to output file


# time = pckt[85000].time
# count = 0.3183

tcon = 0.012
tcon2 = 0.035
flag = 1
time = pckt[0].time
for pkt in pckt:
    pkt.time = time+tcon
    time = time+tcon
    write(pkt)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy import *
from scapy.all import *
import random

pckt = rdpcap('amazon_on_off_10.pcap')
dlink = rdpcap('dlink_cluster.pcap')
tplinkPlug = rdpcap('tpplug_cluster.pcap')
tpBulb = rdpcap('tpbulb_cluster.pcap')
kwiset = rdpcap('kwiset_cluster.pcap')


def write(pkt):
    wrpcap('removed_sign_amazon_plot.pcap', pkt, append=True)  # appends packet to output file


# time = pckt[85000].time
# count = 0.3183

tcon = 0.012
tcon2 = 0.0350
flag = 1
time = pckt[0].time
for pkt in pckt:
    if flag == 1:
        time = pkt.time
        count = 0
        rand = random.randint(416,600)
        while count < rand:
            choice = random.randint(0, 50005)
            choice = choice%4
            if choice == 0:
                for dmp in dlink:
                    dmp.time = time + tcon
                    time = dmp.time
                    write(dmp)
                    count = count + 1
            if choice == 1:
                for dmp in tplinkPlug:
                    dmp.time = time + tcon
                    time = dmp.time
                    write(dmp)
                    count = count + 1
            if choice == 2:
                for dmp in tpBulb:
                    dmp.time = time + tcon
                    time = dmp.time
                    write(dmp)
                    count = count + 1
            if choice == 3:
                for dmp in kwiset:
                    dmp.time = time + tcon
                    time = dmp.time
                    write(dmp)
                    count = count + 1
        flag = 0

    if len(pkt) == 1099:
        flag = 1
    if len(pkt) == 1179:
    	flag = 3
    if flag == 3 and len(pkt) == 1514 :
        flag = 2
    if(flag == 2) and len(pkt) == 103:
    	flag = 1

    pkt.time = time + tcon
    time = pkt.time
    write(pkt)

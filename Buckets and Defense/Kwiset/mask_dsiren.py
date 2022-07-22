#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy import *
from scapy.all import *
import random

pckt = rdpcap('dsiren_on_off_10.pcap')
dlink = rdpcap('dlink_cluster.pcap')
tplinkPlug = rdpcap('tpplug_cluster.pcap')
tpBulb = rdpcap('tpbulb_cluster.pcap')
kwiset = rdpcap('kwiset_cluster.pcap')
amazon = rdpcap('amazon_plug_bucket.pcap')


def write(pkt):
    wrpcap('removed_sign_dsiren.pcap', pkt, append=True)  # appends packet to output file


# time = pckt[85000].time
# count = 0.3183

tcon = 0.012
tcon2 = 0.0350
flag = 1
time = pckt[0].time
for pkt in pckt:
    if flag == 1:
        count = 0
        while count < 5:
            choice = random.randint(0, 50005)
            choice = choice%4
            if choice == 0:
                for dmp in dlink:
                    if count < 5:
                        dmp.time = time + tcon2
                        time = dmp.time
                        write(dmp)
                        count = count + 1
            if choice == 1:
                for dmp in tplinkPlug:
                    if count < 5:
                        dmp.time = time + tcon2
                        time = dmp.time
                        write(dmp)
                        count = count + 1
            if choice == 2:
                for dmp in amazon:
                    if count < 5:
                        dmp.time = time + tcon2
                        time = dmp.time
                        write(dmp)
                        count = count + 1
            if choice == 3:
                for dmp in kwiset:
                   if count < 5:
                        dmp.time = time + tcon2
                        time = dmp.time
                        write(dmp)
                        count = count + 1
        flag = 0

    if len(pkt) == 1076:
        flag = 1
    if len(pkt) == 1023:
        flag = 1
    

    pkt.time = time + tcon
    time = pkt.time
    write(pkt)

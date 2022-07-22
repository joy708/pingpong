from scapy import *
from scapy.all import *

pckt = rdpcap("amazon_on_off_10.pcap")
pcktDump = rdpcap("dlink_cluster.pcap")

def write(pkt):
    wrpcap('test.pcap', pkt, append=True)  #appends packet to output file

#time = pckt[85000].time
#count = 0.3183

tcon = 0.012
tcon2 = 0.0350
flag = 1
time = pckt[0].time
for pkt in pckt:
	if flag == 1:
		
		for dmp in pcktDump:
			dmp.time = time + tcon2
			time = dmp.time
			write(dmp)
		for dmp in pcktDump:
			dmp.time = time + tcon2
			time = dmp.time
			write(dmp)
		for dmp in pcktDump:
			dmp.time = time + tcon2
			time = dmp.time
			write(dmp)
		
		
		
		
		flag = 0
	
	if len(pkt) == 1099:
		flag = 1

	pkt.time = time + tcon
	time = pkt.time
	write(pkt)


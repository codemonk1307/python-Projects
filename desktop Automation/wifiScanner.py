from scapy.all import *
from threading import Thread
import pandas
import time
import os

networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])

networks.set_index("BSSID", inplace=True)

def callback(packet):
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        ssid =packet[Dot11Elt].info.decode()

        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
        
        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)
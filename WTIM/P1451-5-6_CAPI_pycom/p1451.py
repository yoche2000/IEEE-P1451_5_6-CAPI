import pycom
import network
from network import Sigfox
import socket
import ubinascii
from teds_util import *

## This code constducts a

class WTIM:
    def __init__(self):
        self.phy_teds, self.sen_teds  = csv_parse()       #Read TEDS from CSVs in the SD card
        self.sigfoxmode = self.phy_teds["sigfoxmode"][1]
        self.id = ubinascii.unhexlify(self.phy_teds["id"][1])
        self.pac = ubinascii.unhexlify(self.phy_teds["pac"][1])
        self.encryption = self.phy_teds["encryption"][1]
        self.rcz = self.phy_teds["rcz"][1]
        self.downlink = self.phy_teds["downlink"][1]
        self.powerclass = self.phy_teds["powerclass"][1]
        self.keepalive = self.phy_teds["keepalive"][1]
        self.payloadtype = self.phy_teds["payloadtype"][1]

    def __str__(self):
        d = self.__dict__
        d.pop('sen_teds', None)
        d.pop('phy_teds', None)
        return(d)

    def get_phy_teds(self):                          #Print TEDS
        """
        :get_phy_teds: Printing the Physical TEDS of the P1451.5.6 Standardized object.
        """
        print("[SYS] Printing Physical TEDS")
        print_teds(self.phy_teds)

    def get_sen_teds(self):
        """
        :get_phy_teds: Printing the Physical TEDS of the P1451.5.6 Standardized object.
        """
        print("[SYS] Printing Sensor TEDS")
        print_teds(self.sen_teds)

    def connect(self):

        reg_map = {'1':Sigfox.RCZ1, '2':Sigfox.RCZ2, '3':Sigfox.RCZ3, '4':Sigfox.RCZ4,}
        mod_map = {'1':Sigfox.SIGFOX, '0':'Sigfox.FSK'}

        if (self.sigfoxmode == "1"):
            sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=reg_map[self.rcz])
            if(self.downlink == "1"):
                sigfox.public_key(True)
            self.socket = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
            self.socket.setblocking(True)


            if (self.downlink == "0"):
                s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

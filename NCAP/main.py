"""
API user 1
usr = '635f76d255fe214928391bda'
pwd = 'ac13f4f402733ae6e98575b785c85fb'

API user 2
usr = '635f80370c606d2eddb54bb3'
pwd = 'd659b4d8fa50b1414d4527c151994cf9'

API user 3
usr = '635fa185ca93a25bd60ea721'
pwd = 'f8e539277262f572ae0e734d657e015c'
"""

from p1451 import NCAP

if __name__ == '__main__':

    usr = '635fa185ca93a25bd60ea721'
    pwd = 'f8e539277262f572ae0e734d657e015c'

    ncap = NCAP(ep='https://api.sigfox.com/v2/',
                usr=usr,
                pwd=pwd)

    ncap.verify(id="417E4C", path="sigfox_phy_teds.csv")
    ncap.verify(id="417E4A", path="sigfox_phy_teds.csv")
    ncap.verify(id="4195E7", path="sigfox_phy_teds.csv")
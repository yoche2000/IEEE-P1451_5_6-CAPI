from p1451 import NCAP

if __name__ == '__main__':

    usr = ''        #Put your username here
    pwd = ''        #Put your credential here

    ncap = NCAP(ep='https://api.sigfox.com/v2/',
                usr=usr,
                pwd=pwd)

    ncap.verify(id="417E4C", path="sigfox_phy_teds.csv")
    ncap.verify(id="417E4A", path="sigfox_phy_teds.csv")
    ncap.verify(id="4195E7", path="sigfox_phy_teds.csv")
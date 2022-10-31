# CAPI and NCAP
##Introduction
In the IEEE P1451.5.6 standard, NCAP is the [Sigfox Cloud](https://backend.sigfox.com/), the centralized network server opperated by Sigfox. 
Since NCAP is unified for the IEEE P1451.5.6 standard, this CAPI can be used to work with any WTIM.

##Dependence
Since the CAPI has to retrieve the information about WTIMS, the CAPI will be utilizing the Sigfox API.
Therefore, a user/password pair is required to successfully use the CAPI.

##CPI Structure
1. NCAP is the main class of this API. Import the class NCAP() from p1451.py
```
from p1451 import NCAP
```
2. Initiate a NCAP() object using the endpoint (a url), username (login), and pasword to the Sigfox Cloud
```
ncap = NCAP(ep='https://api.sigfox.com/v2/',
            usr=usr,
            pwd=pwd)
```
3. Use the verify() method under the ncap object to verify a WTIM using its *id*. The parameters passed in should 
```
ncap.verify(id="417E4C", path="sigfox_phy_teds.csv")
```

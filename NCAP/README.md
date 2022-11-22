# CAPI and NCAP
## Introduction
In the IEEE P1451.5.6 standard, NCAP is the [Sigfox Cloud](https://backend.sigfox.com/), the centralized network server operated by Sigfox. 
Since NCAP is unified for the IEEE P1451.5.6 standard, this CAPI is capable of universal use. 

![Sigfox Structure](https://i.imgur.com/5I1UNPt.jpg)

## Sigfox Cloud/Backend
Since the CAPI has to retrieve the information about WTIMS, the CAPI will be utilizing the Sigfox API. 
Therefore, a user/password pair is required to successfully use the CAPI, which is able to be attained from [Sigfox Backend](https://backend.sigfox.com/auth/login). Go to ***Group*** -> ***Select a group*** -> ***API ACCESS***, as shown in the image below:

![get_usr_pwd](https://i.imgur.com/LZUHMIt.jpg)

Reference: [Sigfox Documentation](https://support.sigfox.com/docs/api-documentation)

## CPI Structure
1. NCAP is the main class of this API. Import the class [NCAP](https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/blob/0478db50ed85e9f11e0e8988b53eef2fe9099732/NCAP/p1451.py#L4) from [p1451.py](https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/blob/main/NCAP/p1451.py)
```
from p1451 import NCAP
```
2. Create an [NCAP](https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/blob/0478db50ed85e9f11e0e8988b53eef2fe9099732/NCAP/p1451.py#L4) object.
```
ncap = NCAP(ep="https://api.sigfox.com/v2/",	#Sigfox Cloud API Endpoint, V2 as default
            usr=usr,				# "login" assigned by Sigfox Cloud API
            pwd=pwd)				# "password" assigned by Sigfox Cloud API
```
3. Use the [verify()](https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/blob/0478db50ed85e9f11e0e8988b53eef2fe9099732/NCAP/p1451.py#L43) method of the NCAP object to verify a WTIM.
```
##id is the device id of a WTIM, Sigfox device, to be verified, in HEX
##path is the path to the TEDS stored in NCAP to be verified

ncap.verify(id="XXXXXX", path="./my_phyteds.csv")
```

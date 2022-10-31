# p1451.5.6_pycom_CAPI

WTIM in P1451.5.6 are Sigfox device. Since Sigfox devices are compatible with different libraries and languages, it is adequate to have different CAPI for different WTIM. Despite the difference, theb WTIM CAPI should have the same structure. 
* A class WTIM() to construct a Sigfox Entity
* A function to read the TEDS stored in WTIM, and apply the configuration accordingly.
* A method connect() under the class WTIM to initiate the connection between WTIM and NCAP(Sigfox Cloud).

## CAPIs for WTIM
The CAPI for different devices are located under the folder. The IEEE P1451.5.6 CAPI support the following development boards:
* [Pycom](https://pycom.io/) - https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/tree/main/WTIM/P1451-5-6_CAPI_pycom


# IEEE-P1451_5_6-CAPI 
## Introduction
This project is the Communication API (CAPI) of the [IEEE P1451.5.6 Standard](https://standards.ieee.org/ieee/1451.5.6/10612/).

The IEEE P1451.5.6 Standard is the [Sigfox](https://www.sigfox.com/en) branch of the [P1451 Standard][1]. 
**Transducer Interface Module** (TIM) and **Network Capable Application Processor** (NCAP) are the main components of the [P1451 family of standards][1], where Transducer Electronic Data Sheets (TEDS) are a set of specifications stored for transducers (e.g., transducer identification, calibration, correction data, and manufacturer-related information), specified in P1451.0. 

![image info](https://i.imgur.com/qxkqput.jpg)
</p>
<p align = "center">
Fig.1 - The P1451 Family of Standards
</p>

Under IEEE P1451.5 standard, the P1451 standard branch for wireless technologies, the IEEE P1451.5.6 focuses on the technology of Sigfox.
In a sigfox network, the Wireless TIM (WTIM) is a Sigfox device and the NCAP is the Sigfox Cloud. 
THe main work of the working group is the P1451.5.6 Physical TEDS (PHYTEDS) which describes the physical/rado behavior of Sigfox devices. Other TEDS in the P1451 family of standards can also be used, for instance, the Sensor TEDS (SenTEDS) while indicates the specifications of sensors.

![image info](https://i.imgur.com/t16MEgb.jpg)
</p>
<p align = "center">
Fig.2 - Structure of a P1451.5.6 Standardized System
</p>

The specifications properties for the P1451.5.6, their length and available values of TEDS are defined by the standard.
The CAPI enables the verification of P1451.5.6 standardized devices on the NCAP side.

## IEEE P1451.5.6 Communication API
The Communication API (CAPI) works on both the NCAP side and WTIM side. 
The NCAP side of the CAPI works together with the Sigfox Coud. 
Since Sigfox Cloud is the only centralized NCAP for Sigfox systens, the NCAP CAPI is universal. 
The structure and code of the NCAP CAPI can be found under [/NCAP][2].
Since there are different development boards supporting Sigfox, there are different API built for different boards. 
The structure and code of the WTIM CAPIs can be found under [/WTIM][4].

![image info](https://i.imgur.com/bOsUcT3.jpg)
</p>
<p align = "center">
Fig.3 - P1451.5.6 TEDS and CAPI Working Flow
</p>

## Structure of P1451.5.6 CAPI
### P1451.5.6 TEDS
* A P1451.5.6 Transducer Electronic Data Sheet (TEDS) is a set of specifications for the WTIM
* PhyTEDS specify the radio configuration of the Sigfox device (WTIM).
* SenTEDS specify the behavior of the sensors attached to the device (This TEDS is references to P1451.0 and not overarched by the P1451.5.6 standard).
* The specifications of P1451.5.6 TEDS and examples are located under [here][3]. 
### P1451.5.6 NCAP CAPI 
* The CAPI can be run from anywhere with access to the Sigfox Cloud.
* The NCAP uses the API to retrieve the behavior of a Sigfox device from the Sigfox Cloud. 
* If the retrieved information matches the indicated TEDS stored im NCAP, the WTIM will be marked as verified; else, the WTIM is unverified.
### P1451.5.6 WTIM CAPI
* The CAPI should be run on the development board or Sigfox device.
* Different Development Board will have its own CAPI, as the codes are different.
* The device should read the information written in PhyTEDS and perform the specification accordingly to achieve plug-and-play.

[1]: https://en.wikipedia.org/wiki/IEEE_1451
[2]: https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/tree/main/NCAP
[3]: https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/tree/main/Example%20TEDS
[4]: https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/tree/main/WTIM

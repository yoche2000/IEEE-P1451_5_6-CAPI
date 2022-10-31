# IEEE-P1451_5_6-CAPI (TBR)
## Introduction
This project is the Communication API for the IEEE P1451.5.6 Standard.
The IEEE P1451.5.6 Standard is the Sigfox Branch of the [P1451 Standard][1]
Wireless TIM and NCAP are the main components of the [P1451 family of standards][1].
In a sigfox network, the WTIM is a Sigfox Device and the NCAP is the Sigfox Cloud.
The communication API enables the verification of P1451.5.6 sttandardized devices on the NCAP side.

## Architecture of the IEEE P1451.5.6 API
The CAPI works on both the NCAP sida and WTIM side. 
The NCAP works together with the Sigfox Coud. 
Since there is only one centralized network server for Sigfox, there is only one NCAP CAPI. 
The structure and code of the NCAP CAPI can be found under [/NCAP][2].
Since there are different development board supporting Sigfox, there are different API built for different boards. 
The structure and code of the WTIM CAPI can be found under [/WTIM][4].

## CAPI Functions
#### TEDS
* A P1451.5.6 Transducer Electronic Datasheet (TEDS) is a set of specifications of a Sigfox Device
* Physical TEDS specify the radio configuration of the device.
* Sensor TEDS specify the behavior of the sensors attached to the device. 
* The specifications of P1451.5.6 TEDS and examples can be found [here][3]. 
#### CAPI for NCAP
* VThe NCAP uses the API to retrieve the behavior of a Sigfox device from the Sigfox Cloud. 
* If the retrieved information matches the indicated TEDS stored im NCAP, the WTIM will be marked as verified; else, the WTIM is unverified.
#### CAPI for WTI
* Different Development Board will have its own CAPI, as the codes are different.
* The device should read the information written in TEDS and perform the specification accordingly to achieve plug-and-play

[1]: https://en.wikipedia.org/wiki/IEEE_1451
[2]: https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/tree/main/NCAP
[3]: https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/tree/main/Example%20TEDS
[4]: https://github.com/yoche2000/IEEE-P1451_5_6-CAPI/tree/main/WRIM

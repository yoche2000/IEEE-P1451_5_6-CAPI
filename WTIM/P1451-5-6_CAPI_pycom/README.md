# p1451.5.6_pycom_CAPI

This python library is a library for [Pycom](https://docs.pycom.io/firmwareapi/micropython/) devices to implement IEEE P1451.5.6 standardization. It affiliates to the [P1451.5.6 working Group](https://standards.ieee.org/ieee/1451.5.6/10612/) for prototyping the standard. The [Transducer Electronic Datasheet (TEDS)](../../Example%20TEDS) should be generated in CSV format and stored in WTIM (Pycom), of which the format should be in compliance with the P1451.5 standard and the P1451.0 standard.

P.S. This API is written in micropython, the Pycom version of python. For the use of micropytion and its modules and libraries, please refer to [here](https://docs.pycom.io/firmwareapi/pycom/).

## CAPI Example

1. Generate a P1451 object. The WTIM object will be generated using the data in the 2 TEDS files stored in the WTIM.
```
  from p1451 import WTIM

  my1451 = WTIM()
```
2. Use following methods to print the teds of an WTIM object.
```
  >>> my1451.get_phy_teds()     #physical TEDS
  >>> my1451.get_sen_teds()     #sensor TEDS
```
3. P1451 objects can be printed, transforming the data structure into strings. Attributes of the object will be printed.
```
  >>> print(my1451)
```
4. Using the connect() method of the class P1451 will connect the Pycom board to Sigfox Cloud in a plug-and-play fashion. The data in to Physical TEDS has to be valid to successfully connect the pycom Board to the server.
```
  my1451.connect()
```
5. After connecting TEDS objects, the Sigfox socket object will be stored in the "socket" attribute of the object. It can be used to send messages and receive messages with the send() method.

```
  ##Example program: Send the message "test" every hour to the Sigfox Cloud.

  while True:
      payload = b'test'
      my1451.socket.send(payload)
      time.sleep(3600)
```
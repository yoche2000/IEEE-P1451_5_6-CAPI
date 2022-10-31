# p1451.5.6_pycom_CAPI

This python library is a library for Pycom devices to implement IEEE P1451.5.6 standardization. It affiliates to the P1451.5.6 working Group for prototyping the standard. The Transducer Electronic Datasheet (TEDS) should be generated in CSV format and stored in WTIM (Pycom), of which the format should be in compliance with the P1451.5.6 standard and the P1451.0 standard.

1. Generate a P1451 object. The object will be generated using the data in the 2 TEDS files stored in the WTIM.
```
  my1451 = WTIM()
```
2. Use following methods to print the teds of an P1451 opject.
```
  >>> my1451.get_phy_teds()     #physical TEDS
  >>> my1451.get_sen_teds()     #sensor TEDS
```
3. P1451 objects can be printed, transforming the data structure into a string. Attributes of the object will be printed.
```
  >>> print(my1451)
```
4. Using the connect() method of the class P1451 will connect the Pycom board to Sigfox Cloud in a plug-and-play fashion. The data in to Pysical TEDS has to be valid to successfully connect the pycom Board to the server.
```
  my1451.connect()
```
5. After connecting TEDS objects, the Sigfox socket will be stored in the "socket" attribute of the object. It can be used to send messages and receive messages.

```
  ##Example program: Send the message "test" every hour to the Sigfox Cloud.

  while True:
      payload = b'test'
      my1451.socket.send(payload)
      time.sleep(3600)
```

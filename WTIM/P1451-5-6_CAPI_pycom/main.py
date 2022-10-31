from p1451 import WTIM
import time

print("[SYS] Welcome to 1451.5.6 Standard Demo for Pycom")
my1451 = WTIM()
my1451.get_phy_teds()
my1451.get_sen_teds()
my1451.connect()

'''
  while True:
      payload = b'test'
      my1451.socket.send(payload)
      time.sleep(3600)
'''

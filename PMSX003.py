"""
set normal mode
Run for 60 seconds
In a circular queue, grab the min, max, average of last 32 values for all
set idle mode
return pm values


another driver:
class of pmsa003
set registers
get registers




class pmsa003():
    def __init__(self, dev):
        from machine import UART
        self.uart=UART(1,9600)

    def __exit__(self, exc_type, exc_value, traceback):
        self.uart.close()

    

    # def setActive():
    # def setPassive():
    def set_normal(self):
        normal = b'\x42\x4d\xe4\x00\x01\x01\x74'
        self.uart.write(bytearray(normal))
    def set_standby(self):
        standby = b'\x42\x4d\xe4\x00\x00\x01\x73'
        self.uart.write(bytearray(standby))

    def verify_data(self):
        if not self.data:
            return False
        return True

    def read_data(self):
        while True:
            b = self.serial.read(1)
            if b == b'\x42':
                data = self.serial.read(31)
                if data[0] == b'\x4d':
                    self.data = bytearray(b'\x42' + data)
                    if self.verify_data():
                        return self._PMdata()

    def _PMdata(self):
        d = {}
        d['time'] = datetime.datetime.now()
        d['apm25'] = self.data[6] * 256 + self.data[7]
        d['apm10'] = self.data[4] * 256 + self.data[5]
        d['apm100'] = self.data[8] * 256 + self.data[9]
        return d

if __name__ == '__main__':
    print "starting..."
    con = pmsA003('/dev/ttyAMA0')
    d = con.read_data()
    print(d)
"""
#
# Code adapted from Adafruit's CircuitPython code for the PMS 5003 - https://tinyurl.com/y6nfj5n6
# 
# Getting connectors is not trivial for this interface but this post is invaluable:
# https://romkey.com/2018/11/06/found-plantower-pms3003-pms5003-pms7003-connectors/
# There's also a good breakout of this connector - https://github.com/AKstudios/PMSX003-Breakout
#

import array
from machine import Pin, UART
uart=UART(1,9600)

try:
    import struct
except ImportError:
    import ustruct as struct

# Connect the Sensor's TX pin to the board's RX pin

# Fix everything above this
buffer = []

while True:
    data = uart.read(32)  # read up to 32 bytes
    data = list(data)
    # print("read: ", data)          # this is a bytearray type

    buffer += data

    while buffer and buffer[0] != 0x42:
        buffer.pop(0)

    if len(buffer) > 200:
        buffer = []  # avoid an overrun if all bad data
    if len(buffer) < 32:
        continue

    if buffer[1] != 0x4d:
        buffer.pop(0)
        continue

    frame_len = struct.unpack(">H", bytes(buffer[2:4]))[0]. # >H is a 2 byte Big Endian, unsigned short
    if frame_len != 28:
        buffer = []
        continue

    frame = struct.unpack(">HHHHHHHHHHHHHH", bytes(buffer[4:]))

    pm10_standard, pm25_standard, pm100_standard, pm10_env, \
        pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
        particles_25um, particles_50um, particles_100um, skip, checksum = frame

    check = sum(buffer[0:30])

    if check != checksum:
        buffer = []
        continue

    print("Concentration Units (standard)")
    print("---------------------------------------")
    print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" %
          (pm10_standard, pm25_standard, pm100_standard))
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" % (pm10_env, pm25_env, pm100_env))
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", particles_03um)
    print("Particles > 0.5um / 0.1L air:", particles_05um)
    print("Particles > 1.0um / 0.1L air:", particles_10um)
    print("Particles > 2.5um / 0.1L air:", particles_25um)
    print("Particles > 5.0um / 0.1L air:", particles_50um)
    print("Particles > 10 um / 0.1L air:", particles_100um)
    print("---------------------------------------")

    buffer = buffer[32:]
    # print("Buffer ", buffer)

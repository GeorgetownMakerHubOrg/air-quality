"""
Pascal Girard
# I'd like to create a PMSA003 Class to:
# read data
# set the device into active/passive; normal/idle mode

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
import utime
from machine import I2C, Pin, UART
import neopixel

i2c = I2C(scl=Pin(22), sda=Pin(21))
print('i2c bus shows: ', i2c.scan())
uart1=UART(1,rx=27,tx=26,baudrate=9600)
uart2=UART(2,rx=0,tx=2,baudrate=9600)
utime.sleep(2)
print('uart1 shows:', uart1.read(32))
print('uart2 shows:', uart2.read(32))
RED = (255,0,0); GREEN = (0,255,0); BLUE = (0,0,255)
colors = [RED, GREEN, BLUE]
np = neopixel.NeoPixel(Pin(12), 1)
for color in colors:
	np[0] = color
	np.write()
	utime.sleep(1)
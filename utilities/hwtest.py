import utime
from machine import I2C, Pin, UART, unique_id
import neopixel, machine


id = unique_id()
chipId='{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(id[0], id[1], id[2], id[3], id[4], id[5])
print('chipId shows: ', chipId)
i2c = machine.I2C(scl=Pin(22), sda=Pin(21))
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
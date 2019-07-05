# GNU General Public License <https://www.gnu.org/licenses>
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
# Copyright (c) 2019 F. Pascal Girard
#
# credit for the pack/unpack code & variable names goes to ladyada at Adafruit:
# https://learn.adafruit.com/pm25-air-quality-sensor/circuitpython-code


from machine import UART
from lib.pmsa003 import pmsa003


class pm25(object):
    """
    Convenience wrapper for measurements with the pmsa003 sensor

    Example Usage:
    >> pm25_1 = pm25(1, 26, 27)
    >> pm25_2 = pm25(2, 0, 2)
    >> pm25_1.measure()
    """

    def __init__(self, uart_id, uart_rx, uart_tx, uart_baud=9600):
        # TODO: try/catch, and return -1s when the sensor is not attached
        uart = UART(uart_id, rx=uart_rx, tx=uart_tx, baudrate=uart_baud)
        self.pm = pmsa003.PMSA003(uart)

    def measure(self):
        data = self.pm.read_compensated_data()
        return {
            "pm10-standard": data[0],
            "pm25-standard": data[1],
            "pm100-standard": data[2],
            "pm10-env": data[3],
            "pm25-env": data[4],
            "pm100-env": data[5],
            "particles-03um": data[6],
            "particles-05um": data[7],
            "particles-10um": data[8],
            "particles-25um": data[9],
            "particles-50um": data[10],
            "particles-100um": data[11],
        }

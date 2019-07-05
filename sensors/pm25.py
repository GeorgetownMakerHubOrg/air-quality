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
        self.id = uart_id
        self.pm = pmsa003.PMSA003(uart)

    def measure(self):
        data = self.pm.read_compensated_data()
        return {
            f"pm10-standard-{self.id}": data[0],
            f"pm25-standard-{self.id}": data[1],
            f"pm100-standard-{self.id}": data[2],
            f"pm10-env-{self.id}": data[3],
            f"pm25-env-{self.id}": data[4],
            f"pm100-env-{self.id}": data[5],
            f"particles-03um-{self.id}": data[6],
            f"particles-05um-{self.id}": data[7],
            f"particles-10um-{self.id}": data[8],
            f"particles-25um-{self.id}": data[9],
            f"particles-50um-{self.id}": data[10],
            f"particles-100um-{self.id}": data[11],
        }

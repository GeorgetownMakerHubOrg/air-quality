# The MIT License (MIT)
# Copyright (c) F. Pascal Girard
# https://opensource.org/licenses/MIT
# STIA436 Course - Spring 2019
# Professor Colin McCormick & Father Chris Wagner
#
# credit for the pack/unpack code & variable names goes to ladyada at Adafruit:
# https://learn.adafruit.com/pm25-air-quality-sensor/circuitpython-code
#
# Code could be improved with:
# 1. Functions that put the sensor in either Active/Passive mode
# 2. Functions that put the sensor in Normal/Idle mode
# 3. Use ayncio like this:  https://github.com/kevinkk525/pms5003_micropython
#

from array import array
from ustruct import unpack

class PMSA003:

    def __init__(self, uart):
        if uart is None:
            raise ValueError('A uart object is required.')
        self.uart = uart
        # temporary data holders
        self._resultarray = array("i", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self._buffer = []

    def read_raw_data(self, result):
        self.buffer = []
        data = self.uart.read(32)  # read up to 32 bytes
        if data:
            data = list(data)
            self.buffer += data
            while self.buffer and self.buffer[0] != 0x42:   # get to header
                self.buffer.pop(0)
                print('stripping buffer pre-data')
            if len(self.buffer) == 32 and self.buffer[1] == 0x4d:   # we must have a good frame?
                frame_len = unpack(">H", bytes(self.buffer[2:4]))[0]
                if frame_len == 28:
                    frame = unpack(">HHHHHHHHHHHHHH", bytes(self.buffer[4:]))
                    pm10_standard, pm25_standard, pm100_standard, pm10_env, \
                        pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
                        particles_25um, particles_50um, particles_100um, skip, checksum = frame

                    check = sum(self.buffer[0:30])
                    if check == checksum:
                        result[0] = pm10_standard
                        result[1] = pm25_standard
                        result[2]  = pm100_standard
                        result[3]  = pm10_env
                        result[4]  = pm25_env
                        result[5]  = pm100_env
                        result[6]  = particles_03um
                        result[7]  = particles_05um
                        result[8]  = particles_10um
                        result[9]  = particles_25um
                        result[10] = particles_50um
                        result[11] = particles_100um
                        return result
                    else:
                        self.buffer = []
                        print('bad checksum - ignoring') # need a better way to handle these conditions.
                        return {'bad_check': 1}
                else:
                    self.buffer = []  # eew, let's start over
                    print('incorrect frame length - ignoring')
                    return {'bad_length': 1}
            else:
                self.buffer = []  # eew, let's start over
                print('bad data - ignoring')
                return {'bad_data': 1}
        else:
            self.buffer = []  # eew, let's start over
            print('no data - ignoring')
            return {'no_data': 1}

    def read_compensated_data(self, result=None):
        """ At some point we will want to do some local compensation of data.  

            Args:
                result: an array of length 12 values. Can be called without allocating heap memory

            Returns:
                array with particulate count and concentration levels. 

        """
        self.read_raw_data(self._resultarray)
        pm10_standard, pm25_standard, pm100_standard, pm10_env, \
            pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
                particles_25um, particles_50um, particles_100um = self._resultarray
        #
        # If we wanted to do some data munging, do it here.
        #
        # wrangle_data()

        # return results
        if result:
            result[0]  = pm10_standard,
            result[1]  = pm25_standard,
            result[2]  = pm100_standard,
            result[3]  = pm10_env,
            result[4]  = pm25_env,
            result[5]  = pm100_env,
            result[6]  = particles_03um,
            result[7]  = particles_05um,
            result[8]  = particles_10um,
            result[9]  = particles_25um,
            result[10] = particles_50um,
            result[11] = particles_100um
            return result

        return array("i", (pm10_standard, pm25_standard, pm100_standard, pm10_env, \
            pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
                particles_25um, particles_50um, particles_100um))
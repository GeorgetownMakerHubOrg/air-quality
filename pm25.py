# Pascal Girard
# credit for the pack/unpack code & variable names goes to ladyada at Adafruit:
# https://learn.adafruit.com/pm25-air-quality-sensor/circuitpython-code

import array, struct
from utime import sleep
from machine import Pin, UART

uart=UART(2,rx=16,tx=17,baudrate=9600)

def measure():
    try:
        buffer = []
        data = uart.read(32)  # read up to 32 bytes
        if data:
            data = list(data)
            buffer += data
            while buffer and buffer[0] != 0x42:   # get to header
                buffer.pop(0)
                print('stripping buffer pre-data')
            if len(buffer) == 32 and buffer[1] == 0x4d:   # we must have a good frame?
                frame_len = struct.unpack(">H", bytes(buffer[2:4]))[0]
                if frame_len == 28:
                    frame = struct.unpack(">HHHHHHHHHHHHHH", bytes(buffer[4:]))
                    pm10_standard, pm25_standard, pm100_standard, pm10_env, \
                        pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
                        particles_25um, particles_50um, particles_100um, skip, checksum = frame

                    check = sum(buffer[0:30])
                    if check == checksum:
                        return {                # until i can get more than 10 feeds; can only use 6 for now.
                            "pm10-standard":   pm10_standard,
                            "pm25-standard":   pm25_standard,
                            #"pm100-standard":  pm100_standard,
                            "pm10-env":        pm10_env,
                            "pm25-env":        pm25_env,
                            #"pm100-env":       pm100_env,
                            #"particles-03um":  particles_03um,
                            #"particles-05um":  particles_05um,
                            "particles-10um":  particles_10um,
                            "particles-25um":  particles_25um,
                            #"particles-50um":  particles_50um,
                            #"particles-100um": particles_100um
                            }
                    else:
                        buffer = []
                        print('bad checksum - ignoring')
                        return {'bad_check': 1}
                else:
                    buffer = []  # eew, let's start over
                    print('incorrect frame length - ignoring')
                    return {'bad_length': 1}
            else:
                buffer = []  # eew, let's start over
                print('bad data - ignoring')
                return {'bad_data': 1}
        else:
            buffer = []  # eew, let's start over
            print('no data - ignoring')
            return {'no_data': 1}

    except KeyboardInterrupt:
        pass
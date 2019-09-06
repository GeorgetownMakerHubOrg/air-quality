#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
import time
import subprocess

if sys.version_info < (3, 0):
    input = raw_input


MSG_PROMPT = """
Plug in your device, then press <ENTER>.

WARNING: if your device was already plugging in, then press `Ctrl+C` to cancel
this operation, and restart.
"""


def detect_device(device_glob='/dev/*', wait_time=2.5, wait_interval=10):
    """
    Monitors the list of devices, prompting the user to plug in the device, and
    detects the newly attached device. If no device is found after the
    specified `wait_interval`, then an empty list is returned.

    @param wait_time: amount of time to wait before each device check
    @param wait_interval: number of times to perform the device check
    @return: list of detected devices (eg. ['/dev/tty.usb1234'])
    """

    # list of terminal devices
    ttys_before = glob.glob(device_glob)

    # prompt user to plug in the device, and re-check ttys
    print(MSG_PROMPT)
    input()

    # find new terminal entries, retry until a new device is shown...
    ttys_diff = []
    for i in range(0, wait_interval):
        ttys_new = glob.glob(device_glob)
        ttys_diff = [t for t in ttys_new if t not in ttys_before]
        if ttys_diff:
            break
        else:
            time.sleep(wait_time)
            print("Device not yet detected - Trying again...")

    return ttys_diff


def connect_screen(device, prompt=True, baud=115200):
    """
    Connects to the `screen` multiplexer for specified device

    @param device: target device
    @param prompt: whether or not to prompt the user before connecting
    """
    if prompt:
        print("Press <ENTER> if you would like to connect to this device via `screen`")
        input()
    subprocess.check_output(["screen", device, str(baud)])


if __name__ == "__main__":
    print(detect_device())

import os
import sys
import threading
import time
import subprocess
import logging
import argparse

"""
Script to bootstrap the GUAQ ESP32.

NOTE: we use `subprocess.check_output` as it is supported in Python 2 & 3

Usage:
    $ # Upload files and automatically detect device
    $ python bin/upload.py
    $ # Upload files to specified device
    $ python bin/upload.py --port /dev/tty.usbserial-1410
    $ # Upload files to specified device, and re-install MicroPython
    $ python bin/upload.py --port /dev/tty.usbserial-1410 --reinstall

Dependencies:
    - Ampy
    - esptool.py
"""


class SpinnerThread(threading.Thread):
    """
    Loading icon for long running processes

    > task = threading.Thread(target=long_task)
    > task.start()
    > spinner_thread = SpinnerThread("Testing...")
    > spinner_thread.start()
    > task.join()
    > spinner_thread.stop()
    """

    def __init__(self, message=None):
        super(self).__init__(target=self._spin)
        self._stopevent = threading.Event()
        self._message = message

    def stop(self):
        self._stopevent.set()

    def _spin(self):
        while not self._stopevent.isSet():
            for t in "|/-\\":
                disp_f = "[{}] {}"
                disp = disp_f.format(t, self._message)
                sys.stdout.write(disp)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write("\b" * len(disp))
        sys.stdout.write(disp_f.format("*", self._message) + os.linesep)


def get_dirs_and_files():
    """
    Get all directories and files in the current directory

    @return: tuple of lists of directories and files
    """

    dirs = []
    files = []
    exclude_prefixes = ("__", ".")
    for dirpath, dirnames, filenames in os.walk("."):
        # exclude all dirs starting with exclude_prefixes
        dirnames[:] = [
            dirname for dirname in dirnames if not dirname.startswith(exclude_prefixes)
        ]

        dirs += [dirpath + "/" + d for d in dirnames]
        files += [dirpath + "/" + f for f in filenames if f.endswith(".py")]

    # Uncomment for debug output of the directory/file listings
    #sys.stdout.write("Value: %s" % dirs)
    #sys.stdout.write("Value: %s" % files)

    return (dirs, files)


def ampy_mkdir(device, directory):
    """
    Wrapper around the Ampy command to create a directory
    """
    try:
        logging.info("Creating directory: {}".format(directory))
        subprocess.check_output(
            ["ampy", "-d", "0.5", "--port", device, "mkdir", directory],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        if "Directory already exists" in str(e.output):
            logging.info("Directory, {}, already exists".format(directory))


def ampy_cp(device, file):
    """
    Wrapper around the Ampy command to upload a file
    """
    try:
        logging.info("Uploading file: {}".format(file))
        subprocess.check_output(
            ["ampy", "-d", "0.5", "--port", device, "put", file, file],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        logging.error(e)


def ampy_hwtest(device):
    """
    Wrapper around the Ampy command to run `hwtest.py`, and determine ID

    @return: the hardware ID of the device
    """
    try:
        logging.info("Performing hardware test: {}".format(device))
        r = subprocess.check_output(
            ["ampy", "--port", device, "run", "bin/hwtest.py"],
            stderr=subprocess.STDOUT
        )

        # Python 3 returns bytes
        if sys.version_info >= (3, 0) and isinstance(r, bytes):
            r = str(r, "utf-8")

        # Extracting chip ID from the command output
        chip_id = r.split(os.linesep)[0].split(':')[1].strip()

        logging.info("Device chip ID: {}".format(chip_id))
        return chip_id
    except subprocess.CalledProcessError as e:
        logging.error(e)


def esptool_erase(device):
    """
    Wrapper around the `esptool.py` command to erase flash memory
    """
    try:
        logging.info("Erasing device: {}".format(device))
        subprocess.check_output(
            ["esptool.py", "--port", device, "erase_flash"],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        logging.error(e)


def esptool_flash(device, binary='bin/build/up-firmware.bin'):
    """
    Wrapper around the `esptool.py` command to flash binary

    TODO: add check if file exists
    """
    try:
        logging.info("Flashing device: {} with {}".format(device, binary))
        subprocess.check_output(
            [
                "esptool.py", "--chip", "esp32",
                "--port", device,
                "--baud", "460800",
                "write_flash",
                "--compress",
                "--flash_mod", "dio",
                "--flash_freq", "40m",
                "0x1000",
                binary,
            ],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        logging.error(e)


def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('--reinstall', dest='reinstall', action='store_true')
    parser.add_argument('--port', dest='device')
    args = parser.parse_args()

    # Detect the device when the argument is not provided
    if args.device is None:
        from detect import detect_device
        devices = detect_device()
        if not devices:
            logging.error("No device was detected!")
        else:
            device = devices[0]
    else:
        device = args.device

    logging.info("Target device: {}".format(device))

    # Erase Device & Flash MicroPython

    if args.reinstall:
        esptool_erase(device)
        esptool_flash(device)

    # Create Directories & Upload Python Files

    (dirs, files) = get_dirs_and_files()

    for d in dirs:
        ampy_mkdir(device, d)

    for f in files:
        ampy_cp(device, f)

    # Perform Hardware Test
    device_id = ampy_hwtest(device)

    # Post Hardware ID to Adafruit.io
    from setgrp import io_post
    io_post(device_id)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv)

#!/usr/bin/env python
from datetime import datetime, timedelta
import os
import glob
import time

os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0

    return temp_c

def get_timestamp(dt):
    return int((dt - datetime(1970, 1, 1)).total_seconds())

for i in range(1):
    print(read_temp()), get_timestamp(datetime.utcnow().replace(second=0, microsecond=0))
    time.sleep(1)

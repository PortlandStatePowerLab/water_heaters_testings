import os
import glob
import time
import datetime
import csv

########################  DEFINITIONS  ####################################

def read_temp(device, decimals=1):
    """Reads the temperature from a 1-wire device"""
    while True:
        try:
            timepoint = datetime.datetime.now()
            with open(device, "r") as f:
                lines = f.readlines()

            equals_pos = lines[1].find("t=")
            if equals_pos != -1:
                temp_string = lines[1].strip()[equals_pos + 2:]
                temp = round(float(temp_string) / 1000.0, decimals)
                temp = round(9 / 5 * temp + 32, 3)
                timepoint = datetime.datetime.now()
                return timepoint, temp  # Return timestamp and temperature
        except KeyboardInterrupt:
            break



##############################  MAIN  #############################################


if __name__ == "__main__":
    WH_1 = "28-00043ca024ff"
    WH_2 = "28-00043d6393ff"
    WH_3 = "28-00043d6037ff"
    WH_4 = "28-00043ca043ff"

    device_id_1 = "28-000008e55d0d"  # WH_ALL ambient temp device ID
    device_id_2 = "28-0416c138deff"  # Cold Water temp device ID
    device_id_3 = WH_4  # WH Hot temp device ID **UNIQUE TO EACH WH**

    device_path_1 = f"/sys/bus/w1/devices/{device_id_1}/w1_slave"
    device_path_2 = f"/sys/bus/w1/devices/{device_id_2}/w1_slave"
    device_path_3 = f"/sys/bus/w1/devices/{device_id_3}/w1_slave"

    while True:
        timestamp_1, temperature_1 = read_temp(device_path_1)
        timestamp_2, temperature_2 = read_temp(device_path_2)
        timestamp_3, temperature_3 = read_temp(device_path_3)

        print(f'{timestamp_1.strftime("%H:%M:%S")} | AMBIENT: {temperature_1} F | COLD: {temperature_2} F | HOT: {temperature_3} F')

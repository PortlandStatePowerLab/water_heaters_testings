import os
import glob
import time
import datetime
import csv

########################  DEFINITIONS  ####################################

def read_temp(device, decimals=1, sleeptime=1):
    """Reads the temperature from a 1-wire device"""
    while True:
        try:
            timepoint = datetime.datetime.now()
            with open(device, "r") as f:
                lines = f.readlines()
            while lines[0].strip()[-3:] != "YES":
                time.sleep(0.2)
                with open(device, "r") as f:  # Change to read_temp_raw()
                    lines = f.readlines()
            timepassed = (datetime.datetime.now() - timepoint).total_seconds()
            equals_pos = lines[1].find("t=")
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                temp = round(float(temp_string) / 1000.0, decimals)
                temp = round(9 / 5 * temp + 32, 3)
                print(time.strftime("%H:%M:%S - ") + str(temp) + " F")
                time.sleep(sleeptime - timepassed)
                timepoint = datetime.datetime.now()
                return timepoint, temp  # Return timestamp and temperature
        except KeyboardInterrupt:
            break

def write_to_csv(file_name, temp_data):
    file_path = os.path.join("testlog", file_name)
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csv_writer.writerow(['Timestamp', 'Temperature'])
        csv_writer.writerow(temp_data)


##############################  MAIN  #############################################


if __name__ == "__main__":
    # Specify the 1-wire device
    device_id = "28-000008e51dca"
    device_path = f"/sys/bus/w1/devices/{device_id}/w1_slave"

    DRcom = [['Baseline'], ['Shed'], ['CriticalPeakEvent'], ['GridEmergency']]

    wh_type = input('WH Brand:')
    volume = input('Capacity (gallons):')

    startTime = input('Would you like to start collecting temperature data (y/n)?')

    if startTime.lower() in ['n', 'no', 'N', 'No', 'NO']:
        run_at = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        if datetime.datetime.now() > run_at:
            run_at += datetime.timedelta(days=1)

        delay = (run_at - datetime.datetime.now()).total_seconds()

        print('Temperature data collection will start in ' + str(round(delay / 3600, 2)) + ' hours.   ')
        print(datetime.datetime.now())

        time.sleep(delay)

    for com in DRcom:
        data_name = wh_type + volume + '_TEMPDATA_' + com[0] + '.csv'

        start_time = time.time()
        while time.time() - start_time < 10:  # Stay in the loop for 60 seconds
            timestamp, temperature = read_temp(device_path)
            temp_data = [timestamp.strftime("%Y-%m-%d %H:%M:%S"), temperature]
            write_to_csv(data_name, temp_data)

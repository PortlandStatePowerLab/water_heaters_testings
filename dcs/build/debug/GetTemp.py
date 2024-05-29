import os
import glob
import time
import datetime
import csv

########################  DEFINITIONS  ####################################

def read_temp(device, decimals=1, sleeptime=60):
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
                #print(time.strftime("%H:%M:%S - ") + str(temp) + " F")
                time.sleep(sleeptime - timepassed)
                timepoint = datetime.datetime.now()
                return timepoint, temp  # Return timestamp and temperature
        except KeyboardInterrupt:
            break

def write_to_csv(file_name, temp_data):
    file_path = os.path.join("templog", file_name)
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csv_writer.writerow(['Timestamp', 'AMBIENT_TEMP', 'COLD_TEMP', 'HOT_TEMP'])
        csv_writer.writerow(temp_data)

if not os.path.exists('templog'):
    os.makedirs('templog')


##############################  MAIN  #############################################



if __name__ == "__main__":
    WH_1 = "28-00043d6393ff"
    WH_2 = "28-000008e55d0d"
    WH_3 = "28-00043d6037ff"
    WH_4 = "28-00043ca043ff"

    device_id_1 = "28-000008e55d0d"  # WH_ALL ambient temp device ID
    device_id_2 = "28-0416c138deff"  # Cold Water temp device ID
    device_id_3 = WH_4  # WH Hot temp device ID **UNIQUE TO EACH WH**

    device_path_1 = f"/sys/bus/w1/devices/{device_id_1}/w1_slave"
    device_path_2 = f"/sys/bus/w1/devices/{device_id_2}/w1_slave"
    device_path_3 = f"/sys/bus/w1/devices/{device_id_3}/w1_slave"



    wh_type = input('WH Brand:')
    volume = input('Capacity (gallons):')


    yes = ['y', 'Y', 'yes', 'Yes', 'YES']

    DRcom = []

    baseline = input('Do you want to test Baseline (y/n)?')
    if baseline in yes:
        DRcom.append(['Baseline'])

    shed = input('Do you want to test Shed (y/n)?')
    if shed in yes:
        DRcom.append(['Shed'])

    cpe = input('Do you want to test CriticalPeakEvent (y/n)?')
    if cpe in yes:
        DRcom.append(['CriticalPeakEvent'])

    ge = input('Do you want to test GridEmergency (y/n)?')
    if ge in yes:
        DRcom.append(['GridEmergency'])

    lu = input('do you want to test LoadUp (y/n)?')
    if lu in yes:
        DRcom.append(['LoadUp'])


    print('Testing for the following:')
    for com in DRcom:
        print(com[0])



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
        while time.time() - start_time < 60:  # Stay in the loop for 60 seconds
            timestamp_1, temperature_1 = read_temp(device_path_1)
            timestamp_2, temperature_2 = read_temp(device_path_2)
            timestamp_3, temperature_3 = read_temp(device_path_3)
            temp_data = [timestamp_1.strftime("%Y-%m-%d %H:%M:%S"), temperature_1, temperature_2, temperature_3]

            print(f'{timestamp_1.strftime("%H:%M:%S")} | AMBIENT: {temperature_1} F | COLD: {temperature_2} F | HOT: {temperature_3} F')

            write_to_csv(data_name, temp_data)

import os
import time
import datetime
import csv

def read_temp(device_path, decimals=1, sleeptime=30):
    while True:
        try:
            timepoint = datetime.datetime.now()
            with open(device_path, "r") as f:
                lines = f.readlines()

            # Check if lines is not empty and contains the expected line
            while not lines or lines[0].strip()[-3:] != "YES":
                time.sleep(0.2)
                with open(device_path, "r") as f:
                    lines = f.readlines()

            timepassed = (datetime.datetime.now() - timepoint).total_seconds()
            equals_pos = lines[1].find("t=")
            
            # Check if equals_pos is not -1 before proceeding
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                temp = round(float(temp_string) / 1000.0, decimals)
                temp = round(9 / 5 * temp + 32, 3)
                
                time.sleep(sleeptime - timepassed)
                timepoint = datetime.datetime.now()
                return timepoint, temp
        except KeyboardInterrupt:
            break


def write_to_csv(file_name, temp_data):
    file_path = os.path.join("templog", file_name)
    with open(file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csv_writer.writerow(['Timestamp', 'AMBIENT', 'COLD WATER', 'HOT WATER'])
        csv_writer.writerow(temp_data)


if not os.path.exists('templog'):
    os.makedirs('templog')


if __name__ == "__main__":
    

    WH_1 = "28-00043d6393ff"
    WH_2 = "28-000008e55d0d"
    WH_3 = "28-00043d6037ff"
    WH_4 = "28-00043ca043ff"

    device_id_1 = "28-000008e55d0d"  # WH_ALL ambient temp device ID
    device_id_2 = "28-0416c138deff"  # Cold Water temp device ID
    device_id_3 = WH_1  # WH Hot temp device ID **UNIQUE TO EACH WH**

    device_path_1 = f"/sys/bus/w1/devices/{device_id_1}/w1_slave"
    device_path_2 = f"/sys/bus/w1/devices/{device_id_2}/w1_slave"
    device_path_3 = f"/sys/bus/w1/devices/{device_id_3}/w1_slave"

    wh_type = input('WH Brand:')
    volume = input('Capacity (gallons):')

    startTime = input('Would you like to start collecting temperature data (y/n)?')

    if startTime.lower() in ['n', 'no']:
        run_at = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        if datetime.datetime.now() > run_at:
            run_at += datetime.timedelta(days=1)

        delay = (run_at - datetime.datetime.now()).total_seconds()

        print('Temperature data collection will start in ' + str(round(delay / 3600, 2)) + ' hours.   ')
        print(datetime.datetime.now())

        time.sleep(delay)

    DRcom = [['GridEmergency']]

    for com in DRcom:
        data_name = wh_type + volume + '_TEMPDATA_' + com[0] + '.csv'

        start_time = time.time()
        while time.time() - start_time < 60*60*24*2:  # Stay in the loop for 2 days
            timestamp_1, temperature_1 = read_temp(device_path_1)
            timestamp_2, temperature_2 = read_temp(device_path_2)
            timestamp_3, temperature_3 = read_temp(device_path_3)

            temp_data = [timestamp_1.strftime("%Y-%m-%d %H:%M:%S"), temperature_1, temperature_2, temperature_3]

            current_time = datetime.datetime.now()

            formatted_time = current_time.strftime("%H:%M:%S")

            print(f"{formatted_time} | AMBIENT: {temperature_1} F | COLD: {temperature_2} F | HOT: {temperature_3} F")

            write_to_csv(data_name, temp_data)

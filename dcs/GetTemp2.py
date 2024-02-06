import os
import time
import datetime
import csv

def read_temp(device_path, decimals=1, sleeptime=1):
    while True:
        try:
            timepoint = datetime.datetime.now()
            with open(device_path, "r") as f:
                lines = f.readlines()
            while lines[0].strip()[-3:] != "YES":
                time.sleep(0.2)
                with open(device_path, "r") as f:
                    lines = f.readlines()
            timepassed = (datetime.datetime.now() - timepoint).total_seconds()
            equals_pos = lines[1].find("t=")
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                temp = round(float(temp_string) / 1000.0, decimals)
                temp = round(9 / 5 * temp + 32, 3)
#                print(time.strftime("%H:%M:%S - ") + str(temp) + " F", end=' | ')
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
            csv_writer.writerow(['Timestamp', 'Temperature 1', 'Temperature 2'])
        csv_writer.writerow(temp_data)


if not os.path.exists('templog'):
    os.makedirs('templog')




if __name__ == "__main__":
    # Specify the 1-wire devices
    device_id_1 = "28-000008e51dca"  # WH1 ambient temp device ID
    device_id_2 = "28-0416c138deff"  # Cold Water temp device ID

    device_path_1 = f"/sys/bus/w1/devices/{device_id_1}/w1_slave"
    device_path_2 = f"/sys/bus/w1/devices/{device_id_2}/w1_slave"

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

    for com in ['Baseline', 'Shed', 'CriticalPeakEvent', 'GridEmergency']:
        data_name = f"{wh_type}{volume}_TEMPDATA_{com}.csv"

        start_time = time.time()
        while time.time() - start_time < 60*60*24*2:  # Stay in the loop for 2 days
            timestamp_1, temperature_1 = read_temp(device_path_1)
            timestamp_2, temperature_2 = read_temp(device_path_2)

            temp_data = [timestamp_1.strftime("%Y-%m-%d %H:%M:%S"), temperature_1, temperature_2]

            print(f"Temperature 1: {temperature_1} F | Temperature 2: {temperature_2} F")

            write_to_csv(data_name, temp_data)

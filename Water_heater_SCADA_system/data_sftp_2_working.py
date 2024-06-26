import paramiko
import glob
import os

# Update the next three lines with your
# server's information

host = "131.252.223.182"
username = "hank"
password = "Jbcasf18"

##Establish connection
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
print("Connection made.")

##Find the latest file in directory and store the filename in variable 'file'
files = glob.glob('/home/pi/Water_heater_SCADA_system/Water_heater_SCADA_system/*')
latest_file = max(files, key=os.path.getctime)
print(latest_file)
file = open(latest_file)
remotepath = str(latest_file)

## Make SFTP transfer
sftp = client.open_sftp()
sftp.putfo(file, remotepath, callback=None, confirm=True)
sftp.close()
print("File transfer complete")
client.close()
file.close()


##localpath = "/home/pi/Water_heater_SCADA_system/Water_heater_SCADA_system/Water draw data - " + str(actual_time) + ".txt"
##remotepath = "/home/hank/Water draw data - " + str(actual_time) + ".txt"
##sftp = client.open_sftp()
##sftp.put(localpath, remotepath, callback=None, confirm=True)
##sftp.close()
##print("File transfer complete")
##client.close()


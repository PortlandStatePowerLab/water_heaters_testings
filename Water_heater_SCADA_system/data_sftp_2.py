# Use this script to connect to a client and
# transfer a file from the selected directory


import paramiko

# Update the next three lines with your
# server's information

host = "xxx.xxx.xxx.xxx"
username = "host"
password = "password"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
print("Connection made.")

files = glob.glob('/home/pi/Water_heater_SCADA_system/Water_heater_SCADA_system/*')
latest_file = max(files, key=os.path.getctime)
print(latest_file)
file = open(latest_file)
remotepath = str(latest_file)

sftp = client.open_sftp()
sftp.putfo(file, remotepath, callback=None, confirm=True)
sftp.close()
print("File transfer complete")
client.close()
file.close()




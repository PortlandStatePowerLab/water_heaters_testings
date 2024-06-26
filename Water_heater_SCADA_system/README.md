# Water_heater_SCADA_system
All of the files in the repository were written in Python 3 format. The purpose of this system is to collect data from a client that is connected to a water heater to measure the power and water usage. The water usage is logged via a fluid flow sensor and can be logged to a file in a specific raspberry pi directory. Example: /home/pi/josh/Water_heater_SCADA_system/

The files in this repository perform different functions, but ultimately can be put together in one file that can perform part or all of the task of transferring data from the client back to the database server. There are ways to change how often the data gets logged and transferred back to the server. For example, in the “power_read.py” program the schedule module is used to perform a function every X min.

A network connection must be made to the host server from the client server. Edit the code "data_sftp_2.py" to specify the local file path and remote file path. Paramiko is used to make the connection using the client class. The transfer is made via sftp. https://www.paramiko.org/

water2v4.py - This program can be used to count the cumulative flowmeter pulses to produce the total amount of gallons to flow from the water heater.  

power_read.py - This is a program to extract the power reading from the water heater log made by the CTA program. Then the program tries to write to a file called "Water_heater_data.csv".

Run 'Water_heater_data_tr.py' to perform water draw, log the data, and transfer the data to desired location. This program runs two other python programs in succession to immediately process the data and transfer the file via sftp.




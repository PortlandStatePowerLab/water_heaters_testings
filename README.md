## Current Water Heaters Installed:
- A. O. Smith EWH
- A. O Smith HPWH
- American Standard EWHs
## Soon to be installed:
- Rheem EWHs.
### Requirements:
NOTE: The water draw scripts are compatible with Python2.

- Update the Raspberry Pi Libraries:
    - ```sudo apt update```
    - ```sudo apt upgrade```

- Install WiringPi:
    - ``` wget https://project-downloads.drogon.net/wiringpi-latest.deb```
    - ``` sudo dpkg -i wiringpi-latest.deb```


### Conformance Testing Procedure:
NOTE: The following scripts will run from two terminals.
It is important to run programs from RPI desktop so that they may
run continuously. The program will run in Baseline, Shed, 
Critical Peak Event, and Grid Emergency for 48 hr test periods.
For the first 24 hrs, there will be a scheduled draw. For the 
second 24 hrs, the WH will idle. After the test period, a 
csv will populate with the log data pertaining to each
DR command. 

- Start Commodity Service (Terminal 1):
    - ```cd water_heaters_testings/dcs/build/debug```
    - ```python3 StartCommodity.py```

- Initialize Commands from Controller (Terminal 2):
    - ```cd water_heaters_testings/controller```
    - ```./StartDrawSchedule.sh```

To adjust the draw schedule, you may edit schedule.csv

### If the heartbeat is not working on the DCM or the testbench RPI:
Check the serial port connections.
- DCM --> serial0 should be pointing to AMA0
  - If there is still an issue, make sure the RPI README. In particular,
  make sure to read through the following:
    -```https://github.com/rcdrones/UPSPACK_V3/blob/master/README_en.md```
- Test Bench --> serial0 should be pointing to USB0


### TODO:
Upgrade scripts so it is cmopatible with Python3


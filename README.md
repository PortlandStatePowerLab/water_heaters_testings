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
run continuously.

- Start Commodity Service (Terminal 1):
    - ```cd water_heaters_testings/dcs/build/debug```
    - ```python3 StartCommodity.py```

- Initialize Commands from Controller (Terminal 2):
    - ```cd water_heaters_testings/controller```
    - ```./StartDrawSchedule.sh```

To adjust the draw schedule, you may edit schedule.csv

### Conformance Testing Procedure:
NOTE: The following scripts will run from two terminals.
It is important to run programs from RPI desktop so that they may
run continuously. 

- Start Commodity Service (Terminal 1):
    - ```cd water_heaters_testings/dcs/build/debug```
    - ```python3 StartCommodity.py```

- Initialize Commands from Controller (Terminal 2):
    - ```cd water_heaters_testings/controller```
    - ```./StartDrawSchedule.sh```

To adjust the draw schedule, you may edit schedule.csv


### TODO:
Upgrade scripts so it is cmopatible with Python3


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


### Conformance Test Procedure
NOTE: The following scripts will run from three windows via TMUX.
It is important to run programs from RPI desktop so that they may
run continuously. Running programs from SSH may have issues with
continuous connectivity.

Three scripts need to run simultaneously to collect all necessary data
for Conformance testing. Conformance testing runs for 48 hours. The first
24 hours will use a draw profile. The second 24 hours, the WH will idle.

There are 

The following are the three scripts and run procedures:
- TMUX - running programs from one terminal
      - On the RPI Desktop, open a window and run TMUX. You will need to create three
      separate windows to run the three programs.

      - ```tmux```
      -ctrl+b, %
      -ctrl+b, "
      - To move from window to window: cntrol+b, <up> or <down> or <left> or <right>
      - To close out tmux: ctrl+b, :kill-session
  
- Commodity Service - Collecting WH data from the commodity read
    - Conformance commodity service initiates data collection for any desired mode.
    At the start of the program, you will enter the WH Brand (if it is a HP, write
    HP after brand name), tank volume, and which service you would like to run for
    48 hours each. The data will be collected in the log.csv file as long as it
    is running.
      
      -```cd water_heaters_testings/dcs/build/debug```
      
      -```python3 StartCommodity.py```
      
- Draw Profile - Running a 24-hr draw schedule for each service
    - The draw profile is used to run scheduled water draws by reading CSV files
    The draw controller program has three inputs for draw schedules:
      -Daily draw schedule (Use this one to run the test)
      -Cold water dump, peripheral (Use this one to initialize the cold water
      temperature for an auxiliary WH)
      - Test program (create a sample CSV file to ensure all programs are functioning)
      
      -```cd water_heaters_testings_/controller```
      
      -```./StartDrawSchedule.sh```
      
      - Choose which profile you would like to run.

- Temperature Sensors - Collecting ambient, cold water, and hot water temperatures
    - Three temperatures are collected. You will need to run one temperature script
    to collect all three. The temperature data will be saved to the templog directory.

    -```cd water_heaters_testings/dcs```
    -```python3 GetTemp.py```


### If the heartbeat is not working on the DCM or the testbench RPI:
Check the serial port connections.
- DCM --> serial0 should be pointing to AMA0
  - If there is still an issue, make sure the RPI README. In particular,
  make sure to read through the following:

    -```https://github.com/rcdrones/UPSPACK_V3/blob/master/README_en.md```
    
- Test Bench --> serial0 should be pointing to USB0



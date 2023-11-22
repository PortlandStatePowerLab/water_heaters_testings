## Set Up Temperature Sensor
- Walk through the following tutorial:
- ```https://raspberrypi-guide.github.io/electronics/temperature-monitoring```
- ```sudo modprobe w1-gpio```
- ```sudomodprobe w1-therm```

- Check to see if sensor devices are added:
- ```cd /sys/bus/w1/devices```
- ```ls```

- Enable 1-wire communication
- ```sudo raspi-config```

- Make sure to update the unique device name 28******
- Use the TestTemp.py script to make sure the RPI is set up to measure temperature:
- ```python3 TestTemp.py```

- Once you can confirm temperature can be collected, you are able to run the GetTemp.py script.

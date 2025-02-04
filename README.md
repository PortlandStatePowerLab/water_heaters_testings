## Implementing AdvancedLoadUp in CTA-2045-B-Enabled Water Heaters

This brief guide explains the changes made to the CTA-2045 source code in order to enable the AdvancedLoadUp command (ALU) functionality. ALU allows water heaters to store extra energy beyond their normal operation when useful to grid operation (Refer to CTA-2045-B documentation)

## Prerequisites:

    - CTA-2045-B-enabled Water Heater (any other storage device mentioned in the CTA-2045-B document)
    - Follow the safety precautions highlighted within the CTA-2045-B documentation
    - ALU increases the setpoint temperature, so care must be taken!

## tl;dr

To implement the ALU functionality, do the following steps:

1. Clone this repository.
2. Checkout the ALU branch.
3. Go to ```/dcs/sample2/sample2/``` and open the ```main.cpp``` file.
4. Ensure the correct serial port is specificed in line 116.
5. Go to ```/dcs/```, type ```mkdir -p build/debug```.
6. Go to the newly created debug folder: ```cd build/debug/```
7. In your terminal, type ```cmake -DCMAKE_BUILD_TYPE=Debug -DSAMPLE=1 -DTEST=1 ../../```
8. Type ```make```.

## Implementation Steps

The Advanced Load Up functionality is not created or set at all in the source code, so we need to set it up from scratch.

1. Create Message Classes in this directory ```cea2045/device/message/```:

    - Create the following two files:

        - SetAdvancedLoadUp.h
        - SetAdvancedLoadUp.cpp

2. Update the Device Interface:

    - Update the ```CEA2045DeviceUCM.h``` file in ```cea2045/device``` directory as shown in this repository.
  
3. Implement the message handler:

    - Update the ```processIntermediateMessage()``` function within the ```cea2045/processmessage/ProcessMessageUCM.cpp``` file as shown in this repository.


## Usage

Implement the case letter for your advanced load up command as you see fit. In our case, we decided to implement the advanced load up with ```a``` switching case as follows:

```cpp
case 'a':
{
    unsigned short duration = 60;  // 60 minutes
    unsigned short value = 5;      // 0.5 kWh when units = 100Wh
    unsigned char units = 0x02;    // 100Wh units
    
    device->intermediateSetAdvancedLoadUp(duration, value, units).get();
}
```

## Testing Steps

1. The ```DeviceInfo``` returns, among other parameters, a BitMap capability, which shows if the ```AdvancedLoadUp``` command is supported or not.
   
2. Check the responses: 
   
   - look for success code (0x00).
   - Verify operational state changes to 3 or 6.

## Common Issues

We encountered many issues as we were implementing the advanced load up functionality. For instance:

1. Wrong Message length:
    - Check message structure matches the CTA-2045 documentation.

2. Response Not Processing:
    - Verify opCode1 and opCode2 matching the CTA-2045 documentation.
    - Implement debug messages in the ProcessIntermediateMessage files.

3. State Not Changing:
    - Verify device support advanced load up command (bit 6 in the BitMapCapbility)

## References:

1. Always check the CTA-2045 documentation, refer to page 74 to ensure appropriate responses from the device.
2. We wrote a [progress report](https://github.com/PortlandStatePowerLab/water_heaters_testings/tree/ALU/docs/) that shows our progress as we went through this implementation.
3. Feel free to communicate with us if you encounter any issues.
## Implementing AdvancedLoadUp in CTA-2045-B-Enabled Water Heaters

This brief guide explains the changes made to the CTA-2045-A source code in order to enable the AdvancedLoadUp (ALU) functionality. ALU allows water heaters to store extra energy beyond their normal operating parameters when useful to grid operation (Refer to CTA-2045-B documentation)

### Prerequisites:

    - CTA-2045-B-enabled Water Heater (any other storage device mentioned in the CTA-2045-B docs)
    - Follow the safety precautions highlighted within the CTA-2045-B documentation
    - ALU increases the setpoint temperature, so careful!

### File Structure:

The implementation spans multiple directories and files (Only the changed source files. Main is not a source file!):

```
└── cea2045
    ├── device
    │   ├── CEA2045DeviceUCM.cpp
    │   ├── ICEA2045DeviceUCM.cpp
    │   ├── CEA2045DeviceUCM.h
    │   ├── ICEA2045DeviceUCM.h
    │   ├── message
    │   │   ├── SetCapabilityBit.cpp
    │   │   ├── SetCapabilityBit.h
    ├── message
    │   ├── CEA2045MessageSetCapabilityBitRequest.h
    │   ├── CEA2045SetCapabilityBit.h
    │   ├── ConvertEnums.cpp
    │   └── ConvertEnums.h
    ├── processmessage
    │   ├── IUCM.h
```

### Implementation Steps:
    For the code, check the commit history on Nov/27/2024 between 13:00:00 and 14:00:00.
    - Message Structure (CEA2045MessageSetCapabilityBitRequest.h)
    - Message Implementation (SetCapabilityBit.h)
    - Implementation File (SetCapabilityBit.cpp)
    - Device Interface Update:
        - Add a declaration method in '''ICEA2045DeviceUCM.h'''
        - Implement in CEA2045DeviceUCM.cpp



### Usage:

In the main file, set 0x06 to 0x01. For example:
```cpp
device->intermediateSetCapabilityBit(0x06, 0x01).get()
```

### Testing:
The implementation includes test coverage (within the test folder).
    - Message structures tests.
    - Response handling tests.
    - Integration tests

### Debugging:

    - Always start with checking the CapabilityBit map.
    - Monitor the response codes.

### Implementation Questions:

    - Email: midrar@pdx.edu
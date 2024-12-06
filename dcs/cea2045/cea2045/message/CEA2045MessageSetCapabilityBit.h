#ifndef CEA2045_MESSAGE_SETCAPABILITYBIT_H_
#define CEA2045_MESSAGE_SETCAPABILITYBIT_H_

#include "CEA2045MessageMacros.h"

namespace cea2045 {

struct cea2045SetCapabilityBitRequest {
    unsigned char msgType1;
    unsigned char msgType2;
    unsigned short length;
    unsigned char opCode1;
    unsigned char opCode2;
    unsigned char capabilityBit;
    unsigned char setValue;
    unsigned short checksum;

    MACRO_LENGTH
    MACRO_CHECKSUM
} __attribute__((packed));

// Add these constants
const unsigned char CAPABILITY_BIT_ADVANCED_LOAD_UP = 6;
const unsigned char CAPABILITY_VALUE_ENABLE = 0x01;
const unsigned char CAPABILITY_VALUE_DISABLE = 0x00;

} // namespace cea2045
#endif
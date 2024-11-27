#ifndef CEA2045_MESSAGE_SETCAPABILITYBITREQUEST_H_
#define CEA2045_MESSAGE_SETCAPABILITYBITREQUEST_H_

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

} // namespace cea2045
#endif
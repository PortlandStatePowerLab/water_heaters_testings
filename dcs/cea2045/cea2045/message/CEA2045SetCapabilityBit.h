#ifndef CEA2045_MESSAGE_SETCAPABILITYBIT_H_
#define CEA2045_MESSAGE_SETCAPABILITYBIT_H_

#include "../device/message/Intermediate.h"
#include "../device/message/SetCapabilityBit.h"
// #include "../device/message/Message.h"
#include "ConvertEnums.h"

namespace cea2045 {

class SetCapabilityBit : public Intermediate {
public:
    SetCapabilityBit(unsigned char capabilityBit, unsigned char setValue) : 
        Intermediate(MessageCode::SET_CAPABILITY_BIT_REQUEST, 0x01, 0x03) {
        
        // Add payload to message buffer
        m_message.push_back(capabilityBit);  // Here we set the 0x06, I think. We'll see.
        m_message.push_back(setValue);       // 0x01 is what we need so the ALU is triggered
        
        finalize();
    }
};

}

#endif /* CEA2045_MESSAGE_SETCAPABILITYBIT_H_ */
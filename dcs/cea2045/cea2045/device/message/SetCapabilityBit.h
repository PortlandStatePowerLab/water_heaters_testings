#ifndef CEA2045_DEVICE_MESSAGE_SETCAPABILITYBIT_H_
#define CEA2045_DEVICE_MESSAGE_SETCAPABILITYBIT_H_

#include "../../message/CEA2045MessageSetCapabilityBitRequest.h"
#include "Intermediate.h"

namespace cea2045 {

class SetCapabilityBit : public Intermediate {
private:
    cea2045SetCapabilityBitRequest m_msg;

public:
    SetCapabilityBit(unsigned char capabilityBit, unsigned char setValue);
    virtual ~SetCapabilityBit();

    virtual int getNumBytes();
    virtual unsigned char* getBuffer();
};

} // namespace cea2045
#endif
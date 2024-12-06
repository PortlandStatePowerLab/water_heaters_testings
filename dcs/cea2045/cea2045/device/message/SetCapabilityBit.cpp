#include "../message/SetCapabilityBit.h"
#include <iostream>

namespace cea2045 {

// SetCapabilityBit::SetCapabilityBit(unsigned char capabilityBit, unsigned char setValue) :
//     Intermediate(MessageCode::SET_CAPABILITY_BIT_REQUEST, 0x01, 0x03)  // Inherit from Intermediate
// {
//     m_msg.msgType1 = INTERMEDIATE_MSG_TYP1;
//     m_msg.msgType2 = INTERMEDIATE_MSG_TYP2;
//     m_msg.setLength();
//     m_msg.opCode1 = 0x01;  // Device Information
//     m_msg.opCode2 = 0x03;  // SetCapabilityBit
//     m_msg.capabilityBit = capabilityBit;
//     m_msg.setValue = setValue;

//     m_msg.setChecksum();
// }

SetCapabilityBit::SetCapabilityBit(unsigned char capabilityBit, unsigned char setValue) :
    Intermediate(MessageCode::SET_CAPABILITY_BIT_REQUEST, 0x01, 0x03)
{
    std::cout << "Constructing SetCapabilityBit message:\n";
    m_msg.msgType1 = INTERMEDIATE_MSG_TYP1;
    m_msg.msgType2 = INTERMEDIATE_MSG_TYP2;
    m_msg.length = htobe16(0x04);
    m_msg.opCode1 = 0x01;
    m_msg.opCode2 = 0x03;
    m_msg.capabilityBit = capabilityBit;  // Just use the raw bit number
    m_msg.setValue = setValue;
    m_msg.setChecksum();
    
    std::cout << "Message details:\n"
              << "  length: 0x" << std::hex << m_msg.getLength() << "\n"
              << "  capabilityBit: 0x" << std::hex << (int)m_msg.capabilityBit << "\n"
              << "  setValue: 0x" << std::hex << (int)m_msg.setValue << std::endl;
}
SetCapabilityBit::~SetCapabilityBit()
{
}

int SetCapabilityBit::getNumBytes()
{
    return sizeof(m_msg);
}

unsigned char* SetCapabilityBit::getBuffer()
{
    return (unsigned char*)&m_msg;
}

} /* namespace cea2045 */
#include "SetAdvancedLoadUp.h"

namespace cea2045 {

SetAdvancedLoadUp::SetAdvancedLoadUp(unsigned short duration, unsigned short value, 
                                   unsigned char units) :
    Message(MessageCode::ADVANCED_LOAD_UP_REQUEST)
{
    std::cout << "Creating Advanced Load Up message..." << std::endl;
    std::cout << "Setting message fields:" << std::endl
              << "Duration: " << duration << std::endl
              << "Value: " << value << std::endl
              << "Units: " << (int)units << std::endl;
    
    m_msg.header.msgType1 = INTERMEDIATE_MSG_TYP1;  // 08
    m_msg.header.msgType2 = INTERMEDIATE_MSG_TYP2;  // 02
    m_msg.opCode1 = 0x0C;
    m_msg.opCode2 = 0x00;
    m_msg.duration = htobe16(duration);   // 00 3C for 60 minutes
    m_msg.value = htobe16(value);         // 00 05 for 0.5 kWh
    m_msg.units = units;                  // 02 for 100Wh units

    m_msg.setLength();
    m_msg.setChecksum();
}

SetAdvancedLoadUp::~SetAdvancedLoadUp()
{
}

int SetAdvancedLoadUp::getNumBytes()
{
    return sizeof(m_msg);
}

unsigned char* SetAdvancedLoadUp::getBuffer()
{
    return (unsigned char *)&m_msg;
}

} /* namespace cea2045 */
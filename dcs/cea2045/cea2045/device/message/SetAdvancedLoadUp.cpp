
#include "../message/SetAdvancedLoadUp.h"

namespace cea2045
{

SetAdvancedLoadUp::SetAdvancedLoadUp(unsigned short eventDuration, unsigned short value, unsigned short unit) :
	Message(MessageCode::SET_ADVANCEDLOADUP_REQUEST)
{
	m_msg.msgType1 = INTERMEDIATE_MSG_TYP1;
	m_msg.msgType2 = INTERMEDIATE_MSG_TYP2;
	m_msg.setLength();
	m_msg.opCode1 = 0x0C;
	m_msg.opCode2 = 0x00;
	m_msg.eventDuration = eventDuration;
	m_msg.unit = (unsigned char)unit;

	m_msg.setChecksum();
}

//======================================================================================

SetAdvancedLoadUp::~SetAdvancedLoadUp()
{
}

//======================================================================================

int SetAdvancedLoadUp::getNumBytes()
{
	return sizeof(m_msg);
}

//======================================================================================

unsigned char* SetAdvancedLoadUp::getBuffer()
{
	return (unsigned char *)&m_msg;
}

} /* namespace cea2045 */

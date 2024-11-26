
#ifndef CEA2045_CEA2045_MESSAGE_CEA2045MESSAGESETADVANCEDLOADUPREQUEST_H_
#define CEA2045_CEA2045_MESSAGE_CEA2045MESSAGESETADVANCEDLOADUPREQUEST_H_

#include "CEA2045MessageMacros.h"

namespace cea2045 {

struct cea2045SetAdvancedLoadUpRequest
{
	unsigned char msgType1;
	unsigned char msgType2;
	unsigned short length;
	unsigned char opCode1;
	unsigned char opCode2;
	unsigned char eventDuration;
	unsigned short value;
	unsigned short unit;
	unsigned short checksum;

	void seteventDuration(unsigned char value)
	{
		eventDuration = htobe16(value);
	}

	void setvalue(unsigned short Value)
	{
		value = htobe16(Value);
	}

	void setSetpoint2(unsigned short value)
	{
		unit = htobe16(value);
	}

	MACRO_LENGTH
	MACRO_CHECKSUM
} __attribute__((packed));

}
#endif /* CEA2045_CEA2045_MESSAGE_CEA2045MESSAGESETADVANCEDLOADUPREQUEST_H_ */

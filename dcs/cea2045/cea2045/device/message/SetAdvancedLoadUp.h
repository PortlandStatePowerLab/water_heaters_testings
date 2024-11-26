
#ifndef CEA2045_CEA2045_DEVICE_MESSAGE_SETADVANCEDLOADUP_H_
#define CEA2045_CEA2045_DEVICE_MESSAGE_SETADVANCEDLOADUP_H_

#include "../../message/CEA2045MessageSetAdvancedLoadUpRequest.h"
#include "../message/Message.h"

namespace cea2045
{

class SetAdvancedLoadUp: public Message
{
private:
	cea2045SetAdvancedLoadUpRequest m_msg;

public:
	SetAdvancedLoadUp(unsigned short evenetDuration, unsigned short value, unsigned short unit);
	virtual ~SetAdvancedLoadUp();

	virtual int getNumBytes();
	virtual unsigned char *getBuffer();
};

} /* namespace cea2045 */

#endif /* CEA2045_CEA2045_DEVICE_MESSAGE_SETADVANCEDLOADUP_H_ */

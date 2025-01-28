#ifndef CEA2045_SETADVANCEDLOADUP_H_
#define CEA2045_SETADVANCEDLOADUP_H_

#include "Message.h"
#include "../../util/Checksum.h"
#include "../../message/CEA2045Message.h"

namespace cea2045 {

class SetAdvancedLoadUp : public Message {
private:
    struct SetAdvancedLoadUpMsg {
        struct cea2045MessageHeader header;
        unsigned char opCode1;
        unsigned char opCode2;
        unsigned short duration;
        unsigned short value;
        unsigned char units;
        unsigned short checksum;

        void setLength() {
            header.length = htobe16(7);  // Fixed length from spec example
        }

        void setChecksum() {
            this->checksum = Checksum::calculate((unsigned char*)this, 
                sizeof(SetAdvancedLoadUpMsg) - sizeof(unsigned short));
        }
    } __attribute__((packed));

    SetAdvancedLoadUpMsg m_msg;

public:
    SetAdvancedLoadUp(unsigned short duration, unsigned short value, unsigned char units);
    virtual ~SetAdvancedLoadUp();

    virtual int getNumBytes();
    virtual unsigned char *getBuffer();
};

} /* namespace cea2045 */

#endif /* CEA2045_SETADVANCEDLOADUP_H_ */
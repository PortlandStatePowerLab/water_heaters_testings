/*
 * reference:  https://github.com/epri-dev/CTA-2045-UCM-CPP-Library.git
 * UCMImpl.cpp
 *
 *  Created on: Aug 26, 2015
 *      Original Author: dupes
 *      Modifying Author: Midrar Adham
 */

#include "UCMImpl.h"
#include "easylogging++.h"

#include <cea2045/util/MSTimer.h>

#include <chrono>

#include <iostream>

#include <fstream>


using namespace std;

UCMImpl::UCMImpl(): trans(100)
{
	m_sgdMaxPayload = cea2045::MaxPayloadLengthCode::LENGTH2;
	//trans = mcp3008(100); // channel number
}

//======================================================================================

UCMImpl::~UCMImpl()
{
}

//======================================================================================

bool UCMImpl::isMessageTypeSupported(cea2045::MessageTypeCode messageType)
{
	LOG(INFO) << "message type supported received: " << (int)messageType;

	if (messageType == cea2045::MessageTypeCode::NONE)
		return false;

	return true;
}

//======================================================================================

cea2045::MaxPayloadLengthCode UCMImpl::getMaxPayload()
{
	LOG(INFO) << "max payload request received";

	return cea2045::MaxPayloadLengthCode::LENGTH4096;
}

//======================================================================================

void UCMImpl::processMaxPayloadResponse(cea2045::MaxPayloadLengthCode maxPayload)
{
	LOG(INFO) << "max payload response received";

	m_sgdMaxPayload = maxPayload;
}

//======================================================================================

void UCMImpl::processDeviceInfoResponse(cea2045::cea2045DeviceInfoResponse* message)
{
	LOG(INFO) << "device info response received";

	LOG(INFO) << "    device type: " << message->getDeviceType();
	LOG(INFO) << "      vendor ID: " << message->getVendorID();

	LOG(INFO) << "  firmware date: "
			<< 2000 + (int)message->firmwareYear20xx << "-" << (int)message->firmwareMonth << "-" << (int)message->firmwareDay;
}

//======================================================================================

void UCMImpl::processCommodityResponse(cea2045::cea2045CommodityResponse* message)
{
	LOG(INFO) << "commodity response received.  count: " << message->getCommodityDataCount();
    time_t t = time(0);
    // opeen file
    ofstream out;
    out.open("log.csv",ios_base::out|ios_base::app);

	int count = message->getCommodityDataCount();


        string ti = asctime((localtime(&t)));
        ti.pop_back();
	out<<ti<<", ";
	for (int x = 0; x < count; x++)
	{
		cea2045::cea2045CommodityData *data = message->getCommodityData(x);

		LOG(INFO) << "commodity data: " << x;
		LOG(INFO) << "        code: " << (int)data->commodityCode;
		LOG(INFO) << "  cumulative: " << data->getCumulativeAmount();
		LOG(INFO) << "   inst rate: " << data->getInstantaneousRate();
		out<<(int)data->commodityCode<<", ";
		out<<data->getCumulativeAmount()<<", "<<data->getInstantaneousRate()<<", ";
	}
	out<<trans.GetCurrent()*240<<", ";
}

//======================================================================================

void UCMImpl::processAckReceived(cea2045::MessageCode messageCode)
{
	LOG(INFO) << "ack received: " << (int)messageCode;

	switch (messageCode)
	{

	case cea2045::MessageCode::SUPPORT_DATALINK_MESSAGES:
		LOG(INFO) << "supports data link messages";
		break;

	case cea2045::MessageCode::SUPPORT_INTERMEDIATE_MESSAGES:
		LOG(INFO) << "supports intermediate messages";
		break;

	default:
		break;
	}
}

//======================================================================================

void UCMImpl::processNakReceived(cea2045::LinkLayerNakCode nak, cea2045::MessageCode messageCode)
{
	LOG(WARNING) << "nak received";

	if (nak == cea2045::LinkLayerNakCode::UNSUPPORTED_MESSAGE_TYPE)
	{
		switch (messageCode)
		{

		case cea2045::MessageCode::SUPPORT_DATALINK_MESSAGES:
			LOG(WARNING) << "does not support data link";
			break;

		case cea2045::MessageCode::SUPPORT_INTERMEDIATE_MESSAGES:
			LOG(WARNING) << "does not support intermediate";
			break;

		default:
			break;
		}
	}
}

//======================================================================================

void UCMImpl::processOperationalStateReceived(cea2045::cea2045Basic *message)
{
    ofstream out;
    out.open("log.csv",ios_base::out|ios_base::app);
	LOG(INFO) << "operational state received " << (int)message->opCode2;
    out<<(int)message->opCode2<<"\n";
}

//======================================================================================

void UCMImpl::processAppAckReceived(cea2045::cea2045Basic* message)
{
	LOG(INFO) << "app ack received";
}

//======================================================================================

void UCMImpl::processAppNakReceived(cea2045::cea2045Basic* message)
{
	LOG(INFO) << "app nak received. Reason "<< (int)message->opCode2;
}

//======================================================================================

void UCMImpl::processAppCustomerOverride(cea2045::cea2045Basic* message)
{
	LOG(INFO) << "app cust override received: " << (int)message->opCode2;
}

//======================================================================================

void UCMImpl::processIncompleteMessage(const unsigned char *buffer, unsigned int numBytes)
{
	LOG(WARNING) << "incomplete message received: " << numBytes;
}

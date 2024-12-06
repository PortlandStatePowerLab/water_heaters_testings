// =====================================================================================
// Copyright (c) 2016, Electric Power Research Institute (EPRI)
// All rights reserved.
//
// libcea2045 ("this software") is licensed under BSD 3-Clause license.
//
// Redistribution and use in source and binary forms, with or without modification,
// are permitted provided that the following conditions are met:
//
// *  Redistributions of source code must retain the above copyright notice, this
//    list of conditions and the following disclaimer.
//
// *  Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
//
// *  Neither the name of EPRI nor the names of its contributors may
//    be used to endorse or promote products derived from this software without
//    specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
// ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
// IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
// INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
// NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
// PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
// WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
// OF SUCH DAMAGE.
//
// This EPRI software incorporates work covered by the following copyright and permission
// notices. You may not use these works except in compliance with their respective
// licenses, which are provided below.
//
// These works are provided by the copyright holders and contributors "as is" and any express or
// implied warranties, including, but not limited to, the implied warranties of merchantability
// and fitness for a particular purpose are disclaimed.
//
// This software relies on the following libraries and licenses:
//
// #########################################################################################
// Boost Software License, Version 1.0
// #########################################################################################
//
// * catch++ v1.2.1 (https://github.com/philsquared/Catch)
//
// Boost Software License - Version 1.0 - August 17th, 2003
//
// Permission is hereby granted, free of charge, to any person or organization
// obtaining a copy of the software and accompanying documentation covered by
// this license (the "Software") to use, reproduce, display, distribute,
// execute, and transmit the Software, and to prepare derivative works of the
// Software, and to permit third-parties to whom the Software is furnished to
// do so, all subject to the following:
//
// The copyright notices in the Software and this entire statement, including
// the above license grant, this restriction and the following disclaimer,
// must be included in all copies of the Software, in whole or in part, and
// all derivative works of the Software, unless such copies or derivative
// works are solely in the form of machine-executable object code generated by
// a source language processor.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
// SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
// FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
// ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
// DEALINGS IN THE SOFTWARE.
//
// #########################################################################################
// MIT Licence
// #########################################################################################
//
// * easylogging++ Copyright (c) 2017 muflihun.com
//   https://github.com/easylogging/easyloggingpp
//   https://easylogging.muflihun.com
//   https://muflihun.com
//
// Permission is hereby granted, free of charge, to any person obtaining a copy of
// this software and associated documentation files (the "Software"), to deal in
// the Software without restriction, including without limitation the rights to
// use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
// the Software, and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
// FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
// COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
// IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
// CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
/*
 * CEA2045DeviceUCM.cpp
 *
 *  Created on: Aug 25, 2015
 *      Author: dupes
 */

#include "CEA2045DeviceUCM.h"
#include "message/SetCapabilityBit.h"

namespace cea2045 {

CEA2045DeviceUCM::CEA2045DeviceUCM(std::unique_ptr<ILinkLayerComm> linkLayer, std::unique_ptr<IProcessMessage> processMessage) :
	CEA2045Device(std::move(linkLayer), std::move(processMessage))
{
}

CEA2045DeviceUCM::CEA2045DeviceUCM(ILinkLayerComm *linkLayer, IProcessMessage *processMessage) :
	CEA2045Device(linkLayer, processMessage)
{
}

CEA2045DeviceUCM::~CEA2045DeviceUCM()
{
}


//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateSetCapabilityBit(unsigned char capabilityBit, unsigned char setValue)
{
    return queueRequest(new SetCapabilityBit(capabilityBit, setValue));
}

// std::future<ResponseCodes> intermediateSetCapabilityBit(unsigned char capabilityBit, unsigned char setValue);

// std::future<ResponseCodes> CEA2045DeviceUCM::intermediateSetCapabilityBit(unsigned char capabilityBit, unsigned char setValue)
// {
	// return queueRequest(new Intermediate(MessageCode::SET_CAPABILITY_BIT_REQUEST, 0x01, 0x03, capabilityBit, setValue));

//     return queueRequest(new Intermediate(MessageCode::SET_CAPABILITY_BIT_REQUEST,
//             0x01,  // opCode1 for Device Information
//             0x03,  // opCode2 for SetCapabilityBit
//             capabilityBit,  // 0x06 for Advanced Load Up
//             setValue));     // 0x01 to set, 0x00 to unset --> Doc pages 49 and 50.
// }
//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateGetDeviceInformation()
{
	return queueRequest(new Intermediate(MessageCode::DEVICE_INFORMATION_REQUEST,
			INFO_REQ, INFO_REQ));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateGetCommodity()
{
	return queueRequest(new Intermediate(MessageCode::GET_COMMODITY_REQUEST,
			COMMODITY_READ, CLEAR_OP_CODE2));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateGetTemperatureOffset()
{
	return queueRequest(new Intermediate(MessageCode::GET_TEMPERATURE_OFFSET,
			GET_SET, TEMP_OFFSET));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateGetSetPoint()
{
	return queueRequest(new Intermediate(MessageCode::GET_SETPOINTS_REQUEST,
			GET_SET, TEMP_SETPOINT));

}

//======================================================================================

// std::future<ResponseCodes> CEA2045DeviceUCM::intermediateGetAdvancedLoadUp()
// {
// 	return queueRequest(new Intermediate(MessageCode::GET_ADVANCEDLOADUP_REQUEST,
// 			ADVANCED_LOADUP, CLEAR_OP_CODE2));
// }

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateGetPresentTemperature()
{
	return queueRequest(new Intermediate(MessageCode::GET_PRESENT_TEMPERATURE_REQUEST,
			GET_SET, PRESENT_TEMPERATURE));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateSetTemperatureOffset(unsigned char temperatureOffset, TemperatureUnits units)
{
	return queueRequest(new SetTemperatureOffset(temperatureOffset, units));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateSetSetpoints(unsigned short deviceType, TemperatureUnits units, unsigned short setpoint1, unsigned short setpoint2)
{
	return queueRequest(new SetSetpoints(deviceType, units, setpoint1, setpoint2));
}

//======================================================================================


// std::future<ResponseCodes> CEA2045DeviceUCM::intermediateSetAdvancedLoadUp(unsigned char eventDuration, unsigned short value, unsigned short unit)
// {
// 	return queueRequest(new SetAdvancedLoadUp(eventDuration, value, unit));
// }

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateSetEnergyPrice(unsigned short currentPrice, unsigned short currencyCode,
		unsigned char digitsAfterDecimalPoint, unsigned int expirationDatetimeUTC,
		unsigned short nextPrice)
{
	return queueRequest(new SetEnergyPrice(currentPrice, currencyCode, digitsAfterDecimalPoint, expirationDatetimeUTC,
			nextPrice));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateStartCycling(unsigned int eventID, unsigned int startTimeUTCSince2000, unsigned short durationInMinutes,
		unsigned char dutyCycle, unsigned char startRandomizationMinutes, unsigned char endRandomizationMintues,
		unsigned char criticality)
{
	return queueRequest(new StartCycling(eventID, startTimeUTCSince2000, durationInMinutes,
			dutyCycle, startRandomizationMinutes, endRandomizationMintues, criticality));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::intermediateTerminateCycling(unsigned int eventID, unsigned char endRandomizationInMinutes)
{
	return queueRequest(new TerminateCycling(eventID, endRandomizationInMinutes));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicCriticalPeakEvent(unsigned char eventDuration)
{
	return queueRequest(new Basic(MessageCode::BASIC_CRITICAL_PEAK_EVENT_REQUEST,
			CPP, eventDuration));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicEndShed(unsigned char durationToNextEvent)
{
	return queueRequest(new Basic(MessageCode::BASIC_END_SHED_REQUEST,
			END_SHED, durationToNextEvent));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicGridEmergency(unsigned char eventDuration)
{
	return queueRequest(new Basic(MessageCode::BASIC_GRID_EMERGENCY_REQUEST,
			GRID_EMERGENCY, eventDuration));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicLoadUp(unsigned char eventDuration)
{
	return queueRequest(new Basic(MessageCode::BASIC_LOAD_UP_REQUEST,
			LOADUP, eventDuration));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicOutsideCommConnectionStatus(OutsideCommuncatonStatusCode code)
{
	return queueRequest(new Basic(MessageCode::BASIC_OUTSIDE_COMM_CONNECTION_STATUS_MESSAGE,
			COMM_STATUS, (unsigned char)code));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicPresentRelativePrice(unsigned char relativePriceIndicator)
{
	return queueRequest(new Basic(MessageCode::BASIC_PRESENT_RELATIVE_PRICE_REQUEST,
			PRESENT_RELATIVE_PRICE, relativePriceIndicator));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicNextRelativePrice(unsigned char relativePriceIndicator)
{
	return queueRequest(new Basic(MessageCode::BASIC_NEXT_RELATIVE_PRICE_REQUEST,
			NEXT_RELATIVE_PRICE, relativePriceIndicator));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicQueryOperationalState()
{
	return queueRequest(new Basic(MessageCode::BASIC_QUERY_OPERATIONAL_STATE_REQUEST,
			OPER_STATE_REQ, CLEAR_OP_CODE2));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicShed(unsigned char eventDuration)
{
	return queueRequest(new Basic(MessageCode::BASIC_SHED_REQUEST,
			SHED, eventDuration));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::basicPowerLevel(unsigned char powerLevel)
{
	return queueRequest(new Basic(MessageCode::BASIC_POWER_LEVEL,
			POWER_LEVEL, powerLevel));
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::queryMaxPayload()
{
	return CEA2045Device::queryMaxPayload();
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::queryMessageTypeSupported(MessageCode messageCode, unsigned char messageType1, unsigned char messageType2)
{
	return CEA2045Device::queryMessageTypeSupported(messageCode, messageType1, messageType2);
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::querySuportDataLinkMessages()
{
	return CEA2045Device::querySuportDataLinkMessages();
}

//======================================================================================

std::future<ResponseCodes> CEA2045DeviceUCM::querySuportIntermediateMessages()
{
	return CEA2045Device::querySuportIntermediateMessages();
}

//======================================================================================

bool CEA2045DeviceUCM::start()
{
	return CEA2045Device::start();
}

//======================================================================================

void CEA2045DeviceUCM::shutDown()
{
	return CEA2045Device::shutDown();
}

} /* namespace cea2045 */

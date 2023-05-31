/*
 * ref: https://github.com/epri-dev/CTA-2045-UCM-CPP-Library.git
 * author: Midrar Adham
 */

#include "UCMImpl.h"

#include "easylogging++.h"

#include <cea2045/device/DeviceFactory.h>

#include <cea2045/communicationport/CEA2045SerialPort.h>

#include <unistd.h>

#include <thread>

//#include <QCoreApplication>
#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <wiringPi.h>

using namespace cea2045;

INITIALIZE_EASYLOGGINGPP

#include <cea2045/util/MSTimer.h>


void commodity_service_loop(shared_ptr<ICEA2045DeviceUCM> dev){
    //ICEA2045DeviceUCM* dev = device;
    while (1){
        dev->intermediateGetCommodity().get();
        dev->basicQueryOperationalState().get();
        sleep(60);
    }
}
int main()
{
	MSTimer timer;
	bool shutdown = false;

	CEA2045SerialPort sp("/dev/ttyUSB0");
	UCMImpl ucm;
	ResponseCodes responseCodes;

	if (!sp.open())
	{
		LOG(ERROR) << "failed to open serial port: " << strerror(errno);
		return 0;
	}

	//shared_ptr<ICEA2045DeviceUCM> device = make_shared<DeviceFactory::createUCM(&sp, &ucm)>();
    //auto device = mak
	//shared_ptr<ICEA2045DeviceUCM> device = make_shared<DeviceFactory::createUCM>(&sp,&ucm);
    shared_ptr<ICEA2045DeviceUCM> device(DeviceFactory::createUCM(&sp,&ucm));
    //device = make_shared<ICEA2045DeviceUCM>();
    //device = DeviceFactory::createUCM(&sp,&ucm);

	device->start();


	LOG(INFO) << "starting commodity service...";
    thread commodity(commodity_service_loop,device);
    commodity.detach();
    sleep(5);


	while (!shutdown)
	{
        cout<<"c- CriticalPeakEvent\n";
        cout<<"e- Endshed\n";
        cout<<"g- GridEmergency\n";
        cout<<"l- Loadup\n";
        cout<<"o- OutsideCommunication\n";
        cout<<"s- Shed\n";
        cout<<"q- Quit\n";
        cout<<"enter choice: ";
		char c = getchar();

		switch (c)
		{
			case 'c':
				device->basicCriticalPeakEvent(0).get();
				break;

			case 'e':
				device->basicEndShed(0).get();
				break;

			case 'g':
				device->basicGridEmergency(0).get();
				break;

			case 'l':
				device->basicLoadUp(0).get();
				break;

			case '\n':
				break;

			case 'o':
				device->basicOutsideCommConnectionStatus(OutsideCommuncatonStatusCode::Found);
				break;


			case 'q':
				shutdown = true;
				break;

			case 's':
				device->basicShed(0).get();
				break;

			default:
				LOG(WARNING) << "invalid command";
				break;
		}
	}

	device->shutDown();

	//delete (device);

	return 0;
}

#include <wiringPi.h>
#include <mcp3004.h>
#include "mcp3008.h"

mcp3008::mcp3008(int channel) : channel_(channel){
wiringPiSetupGpio();
mcp3004Setup(channel, 0);
};

mcp3008::~mcp3008(){};

float mcp3008::GetCurrent(){
	float voltage = float(analogRead(channel_)) / 1023 * 4.4; // 4.4 is Vref
	float current = voltage * 10; // factor dependent on CT setting
	return current;
};

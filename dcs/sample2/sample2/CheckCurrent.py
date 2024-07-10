#include <wiringPi.h>
#include <mcp3004.h>
#include "mcp3008.h"
#include <iostream>

mcp3008::mcp3008(int channel) : channel_(channel){
wiringPiSetupGpio();
mcp3004Setup(channel, 0);
};

mcp3008::~mcp3008(){};

using namespace std;

float mcp3008::GetCurrent(){
        float voltage = float(analogRead(channel_)) / 1023 * 4.4; // 4.4 is Vref
        float current = voltage * 10; // factor dependent on CT setting
        cout << "\nVoltage check: " << voltage << endl; // prints out voltage value from CT
        cout << "\nCurrent check: " << current << endl; // prints out current from CT
        return current;
};

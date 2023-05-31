#include <iostream>
#include <fstream>
#include <time.h>
#include <unistd.h>
using namespace std;

void perform_command(char cmd){
    switch (tolower(cmd)){
        case 's':
            cout<<"shedding"<<endl;
            break;
        case 'e':
            cout<<"endshedding"<<endl;
            break;
        case 'l':
            cout<<"loading up"<<endl;
            break;
        case 'g':
            cout<<"grid emergency"<<endl;
            break;
        case 'c':
            cout<<"critical peak event"<<endl;
            break;
        default:
            break;
    }
    return;
}

int main(){
    fstream file;
    file.open("schedule.csv", ofstream::in);
    int t;
    time_t now;
    string header,lines;
    char cmd,comma;
    // prime the buffer -- skip the header
    getline(file,header);
    cout<<"header: "<<header<<endl;
    lines = header+ "\n";
    while (file>>t>>comma>>cmd){
        // grab time
        time(&now);
        if (now >= t)
        {
            // passed & should act on it
            cout<<t<<comma<<cmd<<" (PASSED!)\n";
            perform_command(cmd);
        }
        else{
            // did not pass, leave it be for the future
            cout<<t<<cmd<<" (STILL!)\n";
            lines+= to_string(t) + comma + cmd + "\n";
        }
        sleep(1);
    }
    file.close();
    file.open("schedule.csv",ofstream::out);
    // rewrite the commands
    file << lines<<endl;
    file.close();
    return 0;
}

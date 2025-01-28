from gpiozero import MCP3008
import time
from datetime import datetime
import csv

class MCP3008Current:
    VREF = 5.0
    CURRENT_FACTOR = 7.5

    def __init__(self, channel):
        self.adc = MCP3008(channel=channel)

    def get_current(self):
        voltage = self.adc.value * self.VREF
        current = voltage * self.CURRENT_FACTOR
        return voltage, current

# Usage example
if __name__ == "__main__":
    sensor = MCP3008Current(channel=0)  # Assuming we're using channel 0
    
    csv_filename = "CTlog.csv"
    
    # Open the CSV file in write mode
    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write the header
        csvwriter.writerow(["Timestamp", "Voltage", "Current"])
        
        print(f"Logging data to {csv_filename}")
        print("Press Ctrl+C to stop logging")
        
        try:
            while True:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Millisecond precision
                voltage, current = sensor.get_current()
                
                # Write to CSV file
                csvwriter.writerow([timestamp, f"{voltage:.3f}", f"{current:.3f}"])
                
                # Also print to console
                print(f"{timestamp},{voltage:.3f},{current:.3f}")
                
                # Flush the CSV file to ensure data is written immediately
                csvfile.flush()
                
                time.sleep(1)
        except KeyboardInterrupt:
            print("Measurement stopped by user")

print(f"Data saved to {csv_filename}")

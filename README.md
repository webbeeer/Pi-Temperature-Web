### Raspberry Pi Temperature Web Monitor

This project uses a Raspberry Pi with a Sense HAT to monitor temperature and display the data on a self-refreshing web page. The system tracks changes between readings and provides visual feedback via the Sense HAT LED matrix.

![Preview](screenshot.png)

## Features
Temperature Monitoring: Retrieves temperature data directly from the Sense HAT's onboard sensors.

## Visual Indicators: 
The LED matrix changes color based on temperature trends:

Red: Temperature has increased.

Blue: Temperature has decreased.

Green: Temperature is stable or it is the first reading.

### Web Interface: 
A simple HTML dashboard displaying the current temperature, previous reading, and the calculated trend.

### Auto-Refresh: 
The webpage includes a meta-tag to automatically refresh every 5 seconds.

### Data Persistence: 
Saves the last recorded temperature to a local file (my_temp.txt) to allow comparisons between readings even after a refresh.

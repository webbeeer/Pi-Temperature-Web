#!/usr/bin/python

from sense_hat import SenseHat
import sys

sense = SenseHat()

GREEN = [0, 255, 0]
RED = [255, 0, 0]  
BLUE = [0, 0, 255]

HTML_START = """
<html>
<head>
    <meta http-equiv="refresh" content="5">
    <title>Current Temperature</title>
</head>
<body>
"""

HTML_END = """
</body>
</html>
"""

last_temp = None
file_name = "my_temp.txt"  

def write_temp(temp, file_name):
    with open(file_name, "w") as f:
        f.write(str(temp))

def read_temp(file_name):
    try:
        with open(file_name, "r") as f:
            temp = f.read()
        return float(temp)
    except:
        return None  

def change_color(current_temp, previous_temp):
    if previous_temp is None:
        sense.clear(GREEN)
    elif current_temp > previous_temp:
        sense.clear(RED)
    elif current_temp < previous_temp:
        sense.clear(BLUE)
    else:
        sense.clear(GREEN)

def temperature_change_message(current_temp, previous_temp):
    if previous_temp is None:
        return "No previous temperature data available."
    elif current_temp > previous_temp:
        return "The temperature has increased."
    elif current_temp < previous_temp:
        return "The temperature has decreased."
    else:
        return "The temperature is the same as before."

def application(environ, start_response):
    global last_temp  

    status = "200 OK"
    headers = [("Content-Type", "text/html; charset=utf-8")]
    start_response(status, headers)
   
    try:
        last_temp = read_temp(file_name)
       
        current_temp = round(sense.get_temperature(), 1)
       
        change_color(current_temp, last_temp)
       
        temp_change_message = temperature_change_message(current_temp, last_temp)
       
        write_temp(current_temp, file_name)
       
        body = (
            HTML_START +
            f"<p>It is currently <strong>{current_temp}&deg;C</strong>.</p>\n"
        )
       
        if last_temp is not None:
            body += f"<p>The last temperature was <strong>{last_temp}&deg;C</strong>.</p>\n"
       
        body += f"<p>{temp_change_message}</p>\n"
       
        body += HTML_END
       
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        body = (
            HTML_START +
            "<p><strong>Error reading temperature:</strong> " + str(e) + "</p>" +
            HTML_END
        )
   
    return [body.encode("utf-8")]

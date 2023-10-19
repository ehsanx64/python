# Write a string to a specific serial port
import serial
import time

# The target serial port and baud-rate setting
s = serial.Serial("/dev/ttyUSB0", 115200)

# Send the given string to the configured port
def send(str):
    # Wait for 1 second before sending anything
    time.sleep(1)
    s.write(bytes(str, 'utf-8'))

# The string is actually punyforth code that hopefully will be executed on device
code="""
: say-hello print: "Hello there!!!" cr ;
cr
say-hello
"""

# Print the code and then send it
print(code)
send(code)


# Before starting, make sure that pyfirmata is uploaded to the arduino via the arduino ide 
# In the arduino ide, go to file -> examples -> firmata -> standard firmata and upload 

import time # leave this as is, important statement importing code to make it runnable
from pyfirmata import Arduino, util

# Set up the board (replace 'port' with your actual port number)
# This can be seen after you have plugged in the usb, search for "device manager" in windows and look for "ports"
board = Arduino('port')

# Define LED pins
# 0 = port (it can have two values - a for analog(infinite) or d for digital(on or off))
# 0 = replace with the pin number that is connected to the LED with a wire
# 0 = i/o (it can have two values - i for input or o for output)
# question: should the port be written as an analog or digital value?
# question: should the i/o be written as input or output?
green_led = board.get_pin('0:0:0')  # replace the first '0' with a or d, second '0' with the actual pin number, third '0' with o or i
yellow_led = board.get_pin('0:0:0')  # same
red_led = board.get_pin('0:0:0')  # same
button = board.get_pin('0:0:0')     # same

# Start iterator for reading analog values (leave this as is)
it = util.Iterator(board)
it.start()

# Small delay for stability
time.sleep(0.1)

# Main loop (do this until we stop)
try:
    while True:
        # Read the button state
        switchstate = button.read()
        
        if switchstate is None:
            # Skip if switchstate is None, as pyfirmata may return None initially
            continue

        # If the button is not pressed (LOW), turn on the green LED and turn off the yellow and red LED
        
        if switchstate == 0:  # LOW
            green_led.write(1)   # Green LED on
            yellow_led.write(0)   # Yellow off
            red_led.write(0)   # Red off
            
        else:  # If the button is pressed (HIGH), blink both red LEDs together
            
            green_led.write(0)   # Green LED off
            yellow_led.write(0)   # Yellow off
            red_led.write(1)    # Red on 
            time.sleep(0.25)     # Wait 250 ms

            yellow_led.write(1)   # Yellow on
            red_led.write(0)    # Red off
            time.sleep(0.25)     # Wait 250 ms

# Try building your own sequence, by adding more LED's, and turning them on and off as you wish!

# Exit code, leave this as is
except KeyboardInterrupt:
    # Clean up by turning off all LEDs when the program is interrupted
    green_led.write(0)
    yellow_led.write(0)
    red_led.write(0)
    board.exit()

# answer: digital, output
# answer: digital, input
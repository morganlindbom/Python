# Before starting, make sure that pyfirmata is uploaded to the arduino via the arduino ide 
# In the arduino ide, go to file -> examples -> firmata -> standard firmata and upload 

import pyfirmata # leave this as is, important statement importing code to make it runnable
import time 

# Set up the board (replace 'port' with your actual port number)
# This can be seen after you have plugged in the usb, search for "device manager" in windows and look for "ports"
board = pyfirmata.Arduino('port')

# Define LED pins
# 0 = port (it can have two values - a for analog(infinite) or d for digital(on or off))
# 0 = replace with the pin number that is connected to the LED with a wire
# 0 = i/o (it can have two values - i for input or o for output)
# question: should the port be written as an analog or digital value?
# question: should the i/o be written as input or output?
green_led_pin = board.get_pin('0:0:0')  # replace the first '0' with a or d, second '0' with the actual pin number, third '0' with o or i
red_led_pin = board.get_pin('0:0:0')    # same
blue_led_pin = board.get_pin('0:0:0')   # same

# Define sensor pins
# 0 = port (it can have two values - a for analog(infinite) or d for digital(on or off))
# 0 = replace with the pin number that is connected to the LED with a wire
# 0 = i/o (it can have two values - i for input or o for output)
# question: should the port be written as an analog or digital value?
# question: should the i/o be written as input or output?
red_sensor_pin = board.get_pin('0:0:0')   # # replace the first '0' with a or d, second '0' with the actual pin number, third '0' with o or i
green_sensor_pin = board.get_pin('0:0:0') # same
blue_sensor_pin = board.get_pin('0:0:0')  # same

# Start iterator for reading analog values (leave this as is)
it = pyfirmata.util.Iterator(board)
it.start()

# Main loop (do this until we stop)
try:
    while True:
        # Read sensor values
        red_sensor_value = red_sensor_pin.read()  # Read from sensor
        green_sensor_value = green_sensor_pin.read()  # Read from sensor
        blue_sensor_value = blue_sensor_pin.read()  # Read from sensor

        # Debugging: print raw sensor values
        # print(f"Raw sensor values - Red: {red_sensor_value}, Green: {green_sensor_value}, Blue: {blue_sensor_value}")

        # Scale values to increase sensitivity
        scale_factor = 3.0  # Increase sensitivity of the lights by scaling. You can test different numbers here!
        # Leave these as is
        red_value = int((red_sensor_value * 255 * scale_factor) if red_sensor_value is not None else 0)
        green_value = int((green_sensor_value * 255 * scale_factor) if green_sensor_value is not None else 0)
        blue_value = int((blue_sensor_value * 255 * scale_factor) if blue_sensor_value is not None else 0)

        # Cap values to the maximum of 255
        # Question: Why 255?
        red_value = min(red_value, 255)
        green_value = min(green_value, 255)
        blue_value = min(blue_value, 255)

        # Debugging: print mapped sensor values
        # print(f"Mapped sensor values - Red: {red_value}, Green: {green_value}, Blue: {blue_value}")

        # Write values to the LEDs (normalize value for PWM)
        red_led_pin.write(red_value / 255)  
        green_led_pin.write(green_value / 255)  
        blue_led_pin.write(blue_value / 255)  

        # Debugging: print the values sent to LEDs
        # print(f"LED values - Red: {red_value / 255}, Green: {green_value / 255}, Blue: {blue_value / 255}")

        time.sleep(0.1)  # Small delay for stability

# Exit code, leave this as is
except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    # Turn off LEDs on exit
    red_led_pin.write(0)
    green_led_pin.write(0)
    blue_led_pin.write(0)
    board.exit()

# answer: digital, output
# answer: analog, input
# answer: The 0-255 range represents 8 bits, which is commonly used for color and brightness settings 
# in digital electronics. Since 2^8 = 256, you have 256 possible values (0 to 255) that represent 
# different levels of brightness or intensity. PWM : a digital signal rapidly switches between high (on) and low (off) states,
# creating a "pulsed" effect. By changing the ratio of on-time to off-time, called the duty cycle, 
# we can effectively control the amount of power that the component receives. A 50% duty cycle means 
# the signal is on half the time and off half the time, providing roughly half of the maximum power.
import pyfirmata
import time 

board = pyfirmata.Arduino('com4')
led_pin = board.get_pin('d:9:p')

it = pyfirmata.util.Iterator(board)
it.start()

try:
    while True:
        # Fade in: Increase the brightness
        for brightness in range(0, 255, 1):  # From 0 to 255, step by 5
            led_pin.write(brightness / 255.0)  # Scale brightness to [0, 2]
            time.sleep(0.010)  # Delay to make the fade smooth

        # Fade out: Decrease the brightness
        for brightness in range(255, 0, -1):  # From 255 to 0, step by 5
            led_pin.write(brightness / 255.0)  # Scale brightness to [0, -2]
            time.sleep(0.010)  # Delay to make the fade smooth

    
except KeyboardInterrupt:

    print("Program stopped by User")
    led_pin.write(0)
finally:
    led_pin.write(0)
    board.exit()

import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# Turn on the 6-volt pin to generate a beep
GPIO.output(17, GPIO.HIGH)

# Wait for half a second
time.sleep(0.5)

# Turn off the 6-volt pin to stop the beep
GPIO.output(17, GPIO.LOW)

# Clean up GPIO
GPIO.cleanup()

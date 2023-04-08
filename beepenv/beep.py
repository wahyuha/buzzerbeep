import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

# Define the length of each beep in seconds
beep_length = 0.5

# Define the number of beeps to generate
num_beeps = int(5 / beep_length)

# Generate the beeps
for i in range(num_beeps):
    # Turn on the 6-volt pin to generate a beep
    GPIO.output(17, GPIO.HIGH)
    
    # Wait for the length of the beep
    time.sleep(beep_length)
    
    # Turn off the 6-volt pin to stop the beep
    GPIO.output(17, GPIO.LOW)
    
    # Wait for a short pause between beeps
    time.sleep(beep_length / 2)

# Generate a longer last beep
GPIO.output(17, GPIO.HIGH)
time.sleep(beep_length * 2)
GPIO.output(17, GPIO.LOW)

# Clean up GPIO
GPIO.cleanup()

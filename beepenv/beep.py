import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
buzzer_pin = 21
GPIO.setup(buzzer_pin, GPIO.OUT)

# Beep every half second for 5 seconds
for i in range(10):
    if i == 9:
        # Last beep is 1 second
        duration = 1
    else:
        duration = 0.5
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(0.1)

# Clean up the GPIO pins
GPIO.cleanup()

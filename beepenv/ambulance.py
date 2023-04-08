import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
buzzer_pin = 21
GPIO.setup(buzzer_pin, GPIO.OUT)

# Define the beep pattern
beep_pattern = [0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05]

# Beep the buzzer pin in the defined pattern
for duration in beep_pattern:
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(duration)

# Clean up the GPIO pins
GPIO.cleanup()

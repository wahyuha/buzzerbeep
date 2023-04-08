import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
buzzer_pin = 21
GPIO.setup(buzzer_pin, GPIO.OUT)

# Define the beep pattern (original duration)
beep_pattern = [0.15, 0.15, 0.15, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.6, 0.3, 0.3, 0.3, 0.15, 0.15, 0.15]

# Repeat the beep pattern for 3 times (3 times longer)
beep_pattern *= 3

# Beep the buzzer pin in the defined pattern
for duration in beep_pattern:
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(duration)

# Clean up the GPIO pins
GPIO.cleanup()

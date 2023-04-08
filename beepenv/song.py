import RPi.GPIO as GPIO
import time

# set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

# set up the beep pattern
beep_pattern = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 1]

# generate the beep pattern
for duration in beep_pattern:
    GPIO.output(21, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(21, GPIO.LOW)
    time.sleep(0.05)

# clean up GPIO
GPIO.cleanup()

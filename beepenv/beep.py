import RPi.GPIO as GPIO
import time

# Set the GPIO pin number
BEEP_PIN = 18

# Set up the GPIO pin as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(BEEP_PIN, GPIO.OUT)

# Define the beep function
def beep(frequency, duration):
    # Calculate the period of the tone in microseconds
    period = 1000000 // frequency
    # Calculate the duration of each half-period in microseconds
    half_period = period // 2
    # Calculate the number of cycles to generate for the specified duration
    cycles = int(duration * frequency)
    # Generate the tone by toggling the beep pin on and off
    for i in range(cycles):
        GPIO.output(BEEP_PIN, GPIO.HIGH)
        time.sleep(half_period / 1000000.0)
        GPIO.output(BEEP_PIN, GPIO.LOW)
        time.sleep(half_period / 1000000.0)

# Define the notes for the simple song
notes = [262, 294, 330, 349, 392, 440, 494, 523]

# Play the simple song
for note in notes:
    beep(note, 0.5)
    time.sleep(0.1)

# Clean up the GPIO pin
GPIO.cleanup()

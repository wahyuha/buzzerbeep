import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
buzzer_pin = 21
GPIO.setup(buzzer_pin, GPIO.OUT)

# Define the notes for the tune
notes = ['C5', 'C5', 'G5', 'G5', 'A5', 'A5', 'G5']

# Define the durations for the notes
durations = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.4]

# Define the frequency mapping for each note
frequency_map = {
    'C5': 523,
    'D5': 587,
    'E5': 659,
    'F5': 698,
    'G5': 784,
    'A5': 880,
    'B5': 988
}

# Play the tune
for i in range(len(notes)):
    note = notes[i]
    duration = durations[i]
    frequency = frequency_map[note]
    if note == 'rest':
        time.sleep(duration)
    else:
        period = 1.0 / frequency
        half_period = period / 2
        cycles = int(duration / period)
        for j in range(cycles):
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(half_period)
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(half_period)

# Clean up the GPIO pins
GPIO.cleanup()

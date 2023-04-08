import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pin for buzzer
buzzer_pin = 21

# Define frequency of notes
G4 = 392
E5 = 659
C5 = 523
D5 = 587

# Define note lengths in seconds
quarter_note = 0.25
half_note = 0.5
whole_note = 1

# Define the melody
melody = [(G4, quarter_note), (E5, quarter_note), (C5, quarter_note), (D5, whole_note)]

# Set up the buzzer pin
GPIO.setup(buzzer_pin, GPIO.OUT)

# Play the melody
for note in melody:
    frequency = note[0]
    duration = note[1]
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(0.05)  # add a small pause between notes

# Play the last note for longer
GPIO.output(buzzer_pin, GPIO.HIGH)
time.sleep(whole_note * 1.5)
GPIO.output(buzzer_pin, GPIO.LOW)

# Clean up GPIO pins
GPIO.cleanup()

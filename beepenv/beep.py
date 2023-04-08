import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# Define the frequency of each note in Hz
note_freqs = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

# Define the length of each note in seconds
note_lengths = {
    'whole': 1.0,
    'half': 0.5,
    'quarter': 0.25,
    'eighth': 0.125,
    'sixteenth': 0.0625
}

# Define the notes of the song
song_notes = [
    ('E', 'quarter'),
    ('E', 'quarter'),
    ('F', 'quarter'),
    ('G', 'half'),
    ('G', 'quarter'),
    ('F', 'quarter'),
    ('E', 'quarter'),
    ('D', 'half'),
    ('C', 'quarter'),
    ('C', 'quarter'),
    ('D', 'quarter'),
    ('E', 'half'),
    ('E', 'quarter'),
    ('D', 'quarter'),
    ('D', 'half'),
    ('E', 'quarter'),
    ('E', 'quarter'),
    ('F', 'quarter'),
    ('G', 'half'),
    ('G', 'quarter'),
    ('F', 'quarter'),
    ('E', 'quarter'),
    ('D', 'half'),
    ('C', 'quarter'),
    ('C', 'quarter'),
    ('D', 'quarter'),
    ('E', 'half'),
    ('D', 'quarter'),
    ('C', 'quarter'),
    ('C', 'half')
]

# Play the song
for note, length in song_notes:
    # Calculate the duration of the note in seconds
    duration = note_lengths[length]
    
    # Calculate the frequency of the note in Hz
    frequency = note_freqs[note]
    
    # Generate the tone for the note
    tone = GPIO.PWM(17, frequency)
    tone.start(50)
    
    # Wait for the duration of the note
    time.sleep(duration)
    
    # Stop the tone
    tone.stop()
    
    # Wait for a short pause between notes
    time.sleep(duration / 4)

# Clean up GPIO
GPIO.cleanup()

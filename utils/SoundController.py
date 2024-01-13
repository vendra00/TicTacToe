# utils/SoundController.py

import pygame

# Initialize the mixer module
pygame.mixer.init()

# Create a dictionary to store sound objects
sounds = {}


# Load sounds from files
def load_sound(key, sound_file_path):
    """
    Loads a sound file and stores it in the sound dictionary with a unique key.

    Args:
        key (str): The unique identifier for the sound.
        sound_file_path (str): The file path to the sound file.
    """
    sounds[key] = pygame.mixer.Sound(sound_file_path)


# Play a sound
def play_sound(key):
    """
    Plays a sound corresponding to the given key.

    Args:
        key (str): The key of the sound to be played.
    """
    sound = sounds.get(key)
    if sound:
        sound.play()


# Stop a sound
def stop_sound(key):
    """
    Stops playing the sound corresponding to the given key.

    Args:
        key (str): The key of the sound to be stopped.
    """
    sound = sounds.get(key)
    if sound:
        sound.stop()


# Load sounds values
load_sound('valid_move', 'files/wav/valid_move.wav')
load_sound('invalid_move', 'files/wav/invalid_move.wav')
load_sound('victory', 'files/wav/victory2.wav')
load_sound('draw', 'files/wav/draw.wav')
load_sound('select', 'files/wav/selection.wav')
load_sound('hard', 'files/wav/hard.wav')


# Play a midi file
def play_midi_file(midi_file_path):
    """
    Plays a MIDI file.

    Args:
        midi_file_path (str): The file path to the MIDI file.
    """
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the midi file
    pygame.mixer.music.load(midi_file_path)
    # Play the midi file
    pygame.mixer.music.play()

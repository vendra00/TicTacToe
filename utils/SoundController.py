import pygame

# Initialize the mixer module
pygame.mixer.init()

# Create a dictionary to store sound objects
sounds = {}


def load_sound(key, sound_file_path):
    sounds[key] = pygame.mixer.Sound(sound_file_path)


def play_sound(key):
    sound = sounds.get(key)
    if sound:
        sound.play()


def stop_sound(key):
    sound = sounds.get(key)
    if sound:
        sound.stop()


# Load sounds2
load_sound('valid_move', 'files/wav/valid_move.wav')
load_sound('invalid_move', 'files/wav/invalid_move.wav')
load_sound('victory', 'files/wav/victory2.wav')
load_sound('draw', 'files/wav/draw.wav')
load_sound('select', 'files/wav/selection.wav')


def play_midi_file(midi_file_path):
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the midi file
    pygame.mixer.music.load(midi_file_path)
    # Play the midi file
    pygame.mixer.music.play()

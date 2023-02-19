import mido

# Get a list of all the MIDI devices connected to the computer
devices = mido.get_output_names()

# Print the names of the MIDI devices
print(devices)

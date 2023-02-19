import mido

# Get the name of the input port for your digital piano
input_port_name = "Midi Through:Midi Through Port-0 14:0"  # Replace with the name of your MIDI input port

# Open a connection to the input port
input_port = mido.open_input(input_port_name)

# Print a message to indicate that the program is ready to receive notes
print("Ready to receive notes...")

# Loop to continuously receive note messages
for message in input_port:
    # Check if the message is a note on or note off message
    if message.type in ["note_on", "note_off"]:
        # Extract the note number and velocity from the message
        note_number = message.note
        velocity = message.velocity

        # Print the note number and velocity to the console
        print("Note: {}, Velocity: {}".format(note_number, velocity))
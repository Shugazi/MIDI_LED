import mido

# Get the name of the input port for your digital piano
# port = mido.open_output('Midi Through:Midi Through Port-0 14:0')
# or
port = mido.open_output("CH345:CH345 MIDI 1 20:0")
file_name = 'Ramin_Djawadi_-_Westworld_Theme.mid'


# Define the callback function to print note_on and note_off messages
def print_message(message):
    if message.type == 'note_on':
        print('Note On: Note = {}, Velocity = {}'.format(message.note, message.velocity))
    elif message.type == 'note_off':
        print('Note Off: Note = {}, Velocity = {}'.format(message.note, message.velocity))


# Create a MIDI output port
output_port = mido.open_output(port)

# Load the MIDI file and play it while monitoring the messages
with mido.MidiFile(file_name) as mid:
    for message in mid.play():
        output_port.send(message)
        print_message(message)

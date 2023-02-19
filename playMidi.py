import mido

# Get the name of the input port for your digital piano
port = mido.open_output('Midi Through:Midi Through Port-0 14:0')
# or
#port = mido.open_output("CH345:CH345 MIDI 1 20:0")
mid = mido.MidiFile('Dr Dre.mid')
for msg in mid.play():
    port.send(msg)
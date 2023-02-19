from rpi_ws281x import PixelStrip, Color
import mido

# LED strip configuration
LED_COUNT = 10
LED_PIN = 13
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 100
LED_INVERT = False

# Initialize the LED strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Get the name of my piano
input_port_name = "CH345:CH345 MIDI 1 20:0"  # name returned

# Open a connection to the input port
input_port = mido.open_input(input_port_name)


# Creating fun for color based on note
def led_color(number):
    # Set the LED color based on the number
    if number == 1:
        color = Color(255, 0, 0)  # Red
    elif number == 2:
        color = Color(0, 255, 0)  # Green
    elif number == 3:
        color = Color(0, 0, 255)  # Blue
    elif number == 4:
        color = Color(255, 255, 0)  # Yellow
    elif number == 5:
        color = Color(255, 0, 255)  # Magenta
    elif number == 6:
        color = Color(0, 255, 255)  # Cyan
    elif number == 7:
        color = Color(255, 255, 255)  # White
    elif number == 8:
        color = Color(255, 127, 0)  # Orange
    elif number == 9:
        color = Color(127, 0, 255)  # Purple
    elif number == 0:
        color = Color(0, 127, 255)  # Teal
    else:
        color = Color(0, 0, 0)  # Off

    return color

# Creating the logic of the fun for note to led
def note_2_led(note_num):
    # Map the number to an LED index (0-9)
    led_index = note_num % 10

    # Set the LED color
    strip.setPixelColor(led_index, led_color(led_index))
    strip.show()


# Print a message to indicate that the program is ready to receive notes
print("Ready to receive notes...")
# Loop to continuously receive note messages
try:
    for message in input_port:
        # Check if the message is a note on or note off message
        if message.type in ["note_on"]:
            # Extract the note number and velocity from the message
            note_number = message.note
            velocity = message.velocity

            # Print the note number and velocity to the console
            print("Note: {}, Velocity: {}".format(note_number, velocity))
except KeyboardInterrupt:
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, led_color(10))
        strip.show()

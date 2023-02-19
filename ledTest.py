from rpi_ws281x import PixelStrip, Color

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

# Define a function to set the LED color based on a number
def set_led_color(number):
    # Map the number to an LED index (0-9)
    led_index = number - 1

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
    elif number == 10:
        color = Color(0, 127, 255)  # Teal
    else:
        color = Color(0, 0, 0)  # Off

    # Set the LED color
    strip.setPixelColor(led_index, color)
    strip.show()

# Set the LED colors for numbers 1-10
set_led_color(1)
set_led_color(2)
set_led_color(3)
set_led_color(4)
set_led_color(5)
set_led_color(6)
set_led_color(7)
set_led_color(8)
set_led_color(9)
set_led_color(10)

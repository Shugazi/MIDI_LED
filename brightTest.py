from rpi_ws281x import PixelStrip, Color
import time

# LED strip configuration
LED_COUNT = 10
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 50
LED_INVERT = False
decay_rate = 5

# Initialize the LED strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Set the LED color
strip.setPixelColor(0, 255 * LED_BRIGHTNESS, 0, 0)
strip.show()

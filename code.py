import board
import digitalio
import time
from adafruit_debouncer import Debouncer

# Setup button on GP15
print("button")
my_button = digitalio.DigitalInOut(board.GP9)
my_button.direction = digitalio.Direction.INPUT
my_button.pull = digitalio.Pull.UP
button = Debouncer(my_button)

print("led")
# Setup LEDs
redled = digitalio.DigitalInOut(board.GP13)
redled.direction = digitalio.Direction.OUTPUT

blueled = digitalio.DigitalInOut(board.GP14)
blueled.direction = digitalio.Direction.OUTPUT

while True:
    button.update()

    if button.value is True:
        print("not pressed")
        redled.value = False
        blueled.value = False
    if button.value is False:
        print("pressed")
        redled.value = True
        blueled.value = True

    time.sleep(0.1)  # Shorter delay for better responsiveness

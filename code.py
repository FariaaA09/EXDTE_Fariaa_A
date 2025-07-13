import board
import digitalio
import time
from adafruit_debouncer import Debouncer

# Setup button on GP15
print("button")
button_io = digitalio.DigitalInOut(board.GP15)
button_io.direction = digitalio.Direction.INPUT
button_io.pull = digitalio.Pull.UP
button = Debouncer(button_io)
print("led")
# Setup LEDs
led1 = digitalio.DigitalInOut(board.GP1)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP3)
led2.direction = digitalio.Direction.OUTPUT

print("Running...")

while True:
    button.update()

    if button.fell:
        print("Button pressed")
        led1.value = True
        led2.value = False
    elif button.rose:
        print("Button released")
        led1.value = False
        led2.value = True
    elif not button.value:  # Held down
        print("Button held")
        led1.value = True
        led2.value = True
    else:  # Idle
        print("Button idle")
        led1.value = False
        led2.value = False

    time.sleep(0.1)

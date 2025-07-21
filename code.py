import board
import digitalio
import time
import random
from adafruit_debouncer import Debouncer

# Setup button on GP9
my_button = digitalio.DigitalInOut(board.GP9)
my_button.direction = digitalio.Direction.INPUT
my_button.pull = digitalio.Pull.UP
button = Debouncer(my_button)

# Setup blue LED on GP14
blueled = digitalio.DigitalInOut(board.GP14)
blueled.direction = digitalio.Direction.OUTPUT
#So it dosent keep looping I added this
print("Press the button to start the game.")

while True:
    # Put BlueLed on Standby Mode
    print("Waiting for press Blue LED on")
    blueled.value = True

# Wait for button to be pressed and released
# The user will press a button that will utilise debounce code
    while True:
        button.update()
        if button.fell:
            print("Button Pressed, Waiting to be released")
# The LED will turn off once they release the button
        if button.rose:
            print("Button released")
            blueled.value = False
            break
        time.sleep(0.01)

# Wait for a random delay between 2 and 5
    delay = random.uniform(2, 5)
    time.sleep(delay)

# Turn on LED and start timer for reaction time
# After an amount of time the LED will turn back on
    blueled.value = True
    start_time = time.monotonic()
# Once the LED comes on the user needs to press the button again as quickly as possible
    print("Press the button")

# Wait for user to press button again
    while True:
        button.update()
        if button.fell:
            reaction_time = time.monotonic() - start_time
# Print The users Reaction time
# It should print their time to the console
            print(f"Reaction time: {reaction_time:.3f} seconds")
            blueled.value = False
            time.sleep(1)
            break
        time.sleep(0.001)

# Wait for user to press the button again to start the next round if they want
    print("Press the button if you want to play again")
    while True:
        button.update()
        if button.fell:
#Breaking the loop
            break
        time.sleep(0.01)

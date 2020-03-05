# Import modules that this game depends on
from microbit import * # for utilising micro:bit's power
import random # for utilising randomness

# This is a function that shows a flashing dash
def flashDash():
    display.show("_")
    sleep(200)
    display.clear()
    sleep(200)

options = ["P","R","S"] # define options

while True:
    flashDash() # show a flashing... dash
    # Because the shake-detection is not always working,
    # the micro:bit also monitors simultaneous pressing of A and B
    if accelerometer.was_gesture("shake") or (button_a.is_pressed() and button_b.is_pressed()):
        # If one of the above happened, clear the display...
        display.clear()
        # ... and randomly show P(aper), R(ock) or S(cissors)
        display.show(random.choice(options))
        # wait for two seconds and then restart
        sleep(2000)
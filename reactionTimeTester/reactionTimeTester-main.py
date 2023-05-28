# Imports go at the top
from microbit import *
import random
SCORE = None

# Code in a 'while True:' loop repeats forever
while True:   

    # Wait for user to start the game
    while button_a.was_pressed() == False:
        # Scroll previous score if availeable
        if SCORE is not None:
            display.scroll(SCORE, wait=True)
        pass

    # At the start, light up the entire display
    display.show(Image('99999:'
                       '99999:'
                       '99999:'
                       '99999:'
                       '99999:'))

    # Wait for a random amount of time
    # from 2 seconds to 3 seconds
    waitFor = 2000 + random.randint(0, 1000)

    # Save current time to compare
    currentTime = running_time()

    # Has player pressed B too early
    tooEarly = False

    # While waiting
    while running_time() - currentTime < waitFor:
        # If player presses button
        if button_b.was_pressed():
            # Too early is true
            tooEarly = True
            # Break loop
            break

    # If button was pressed too early
    if tooEarly:
        # Put message in score
        SCORE = 'TOO EARLY'
        # Return to beginning of loop
        continue

    # Clear display after wait
    display.clear()

    # Save current time
    startTime = running_time()

    # Wait for user to press button
    while button_b.is_pressed() == False:
        # Break after 10 seconds if no input
        if (running_time() - startTime >= 10000):
            break
        pass

    # Save current time
    endTime = running_time()

    # Save reaction time in string
    SCORE = str(endTime - startTime) + " ms"

    # return to beginning of loop
    # start scrolling score
    # wait for new game


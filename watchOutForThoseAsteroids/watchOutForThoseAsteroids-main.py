'''
Juha Rainto
2023
'''
# Imports go at the top
from microbit import *
import random

'''
At the moment the player can move to the left and to the right
the player will cross from one side to the other if they go too dar in one direction

The obstacles spawn endlessly one at a time
Since there is no game over mechanic the player can hit the obstacles

If the player occupies the same LED as the obstacle when the obstacle is despwned
the player's dot will also despawn and the player becomes invisible until they move'''

# TO DO
# Startup logic
# some kind of screen in the beginning to let the player decide when to begin the game

# Collision detection and game over logic
# check for collisions between the player and obstacle
# add a game over screen and the possibility to start over


# FUTURE IMPROVEMENTS
# increasing the gameplay speed
# multiple obstacles at the same time

class Player:
    # Player position
    x = 2
    y = 4 #constant

    
    def __init__(self):
        # Draw player when initialized
        display.set_pixel(self.x, self.y ,9)

    def move(self, movement):
        # Extinguish LED at current player position
        display.set_pixel(self.x, self.y, 0)

        # Move player
        # If player position is out of bounds, reset position
        # otherwise move player normally
        if self.x + movement > 4:
            self.x = 0
        elif self.x + movement < 0:
            self.x = 4
        else:
            self.x += movement

        # Light up LED at new player position
        display.set_pixel(self.x, self.y, 9)

        

class Obstacle:
    # Obstacle position
    x = 0
    y = 0

    def __init__(self):
        # Select a random column for obstacle
        self.x = random.randint(0, 4)
        # Draw obstacle when initialized
        display.set_pixel(self.x, self.y, 9)

    def move(self):
        # Extinguish LED at current position
        display.set_pixel(self.x, self.y, 0)

        # If the obstacle has not reached the bottom row
        if self.y < 4:
            # Move down by one
            self.y += 1
        else:
            # If the obstacle is at the bottom, return False
            return False

        # Light up LED at new position
        display.set_pixel(self.x, self.y, 9)
        # Obstacle could and has moved, return True
        return True

        
# Code in a 'while True:' loop repeats forever

def main():
    # Initialize player and Obstacle objects
    player = Player()
    obstacle = Obstacle()

    # Count of loop cycles
    cycle = 0

    score = 0

    # Main gameplay loop
    while True:
        # Move player if button was pressed
        # -1 move to the left
        # +1 move to the right
        if button_a.was_pressed():
            player.move(-1)
        if button_b.was_pressed():
            player.move(+1)

        # When loop has executed 50 times, move obstacle
        if cycle >= 50:
            # If obstacle can't move, initialize new obstacle
            if obstacle.move() == False:
                obstacle = Obstacle()
                score += 1
            cycle = 0
        else:
            cycle += 1

        if collision(player, obstacle):
            gameOver(score)

        # Sleep for 10ms
        sleep(10)


# Clear entire display
def clearDisplay():
    display.show(Image('00000:'
                       '00000:'
                       '00000:'
                       '00000:'
                       '00000:'))

def collision(player, obstacle):
    if player.x == obstacle.x and player.y == obstacle.y:
        return True
    else:
        return False

def gameOver(score):
    display.scroll('Score: ' + str(score), delay=100, loop=True)


main()
    
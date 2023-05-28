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
    x = 2
    y = 4

    def __init__(self):
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

        # Light LED at new player position
        display.set_pixel(self.x, self.y, 9)

        

class Obstacle:
    x = 0
    y = 0

    def __init__(self):
        self.x = random.randint(0, 4)
        display.set_pixel(self.x, self.y, 9)

    def move(self):
        display.set_pixel(self.x, self.y, 0)
        
        if self.y < 4:
            self.y += 1
        else:
            return False

        display.set_pixel(self.x, self.y, 9)
        return True

        
# Code in a 'while True:' loop repeats forever

def main():
    player = Player()
    obstacle = Obstacle()
    cycle = 0
    
    while True:
        
        if button_a.was_pressed():
            player.move(-1)
        if button_b.was_pressed():
            player.move(+1)

        if cycle >= 50:
            if obstacle.move() == False:
                obstacle = Obstacle()
            cycle = 0
        else:
            cycle += 1


        sleep(10)

    
def draw(obstacle):
    clearDisplay()
    # Draw obstacle
    display.set_pixel(obstacle.x, obstacle.y, 9)


# Clear entire display
def clearDisplay():
    display.show(Image('00000:'
                       '00000:'
                       '00000:'
                       '00000:'
                       '00000:'))


main()
    
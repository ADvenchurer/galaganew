import pygame
import pgzrun
import random

#Screen Dimensions
WIDTH = 1200
HEIGHT = 600

#defining colours
WHITE = (255,255,255)
BLUE = (0,0,255)

#create a ship
ship = Actor('ship')
alien = Actor('alien')

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 5

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

enemies.append(Actor('alien'))
#now the enimies will be in a straight line

enemies[-1].x = 10
#starting off the screen thats why putting it at 100,
#slowly the enemy will come down
enemies[-1].y = -100

score = 0

#for updating the score
def displayScore():
    sceren.draw.text(str(score),(50,30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        #the last bullet added , set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

def update():
    global score
    #move the ship left or right with arrow keys
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0

    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH
    #to fire bullets
    #it should now be while you on hold space key event
    #rather it shoutld be on space key down event

    for bullet in bullets:
        #if the bullet reaches the top of the screen it should get removed
        #else the list will become huge
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10


def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    ship.draw()
    displayScore()


pgzrun.go()
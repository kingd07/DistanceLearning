import pygame as py
import time
import random
py.init()


score = 0
lives = 3
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay = py.display.set_mode((display_width, display_height))
#the set_caption titles the window
py.display.set_caption('This is the window title just so ya know')
#this clock here is like the fps for everything basically, keep that in mind for later
clock = py.time.Clock()

killed_enemy = pass
ship_width = 110

game_exit = False
ship_img = py.image.load('ship.png')
life_img = py.image.load('smaller_ship.png')
tip = py.image.load('tip.png')
blank = py.image.load('blank.png')
enemy = py.image.load('enemy.png')
enemy2 = py.image.load('enemy.png')
enemy3 = py.image.load('enemy.png')
enemy4 = py.image.load('enemy.png')
enemy5 = py.image.load('enemy.png')
enemy6 = py.image.load('enemy.png')
enemy7 = py.image.load('enemy.png')
enemy8 = py.image.load('enemy.png')
enemy9 = py.image.load('enemy.png')
enemy10 = py.image.load('enemy.png')
explosion = py.image.load('explode.png')

def enemy_spawn():
    gameDisplay.blit(enemy, (random.randint(-10, 700), -10))
    py.display.update()
    time.sleep(2)
    gameDisplay.blit(enemy2, (random.randint(-10, 700), -10))
def enemy_kill():
    pass
def ship(x,y):
    gameDisplay.blit(ship_img, (x,y))
    gameDisplay.blit(tip, (x+9, y-22))
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    message = py.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, message)
    TextRect.center = ((display_width*0.1), (display_height*0.04))
    gameDisplay.blit(TextSurf, TextRect)
    py.display.update()
def scoreboard():
    global score
    message_display('Score: '+str(score))

def life_counter():
    global lives
    if lives == 3:
        gameDisplay.blit(life_img, (40, 550))
        gameDisplay.blit(life_img, (10, 550))
        gameDisplay.blit(life_img, (70, 550))
    if lives == 2:
        gameDisplay.blit(blank, (10, 550))
    if lives == 1:
        gameDisplay.blit(blank, (40, 550))


def game_over():
    pass

def game_loop():
    global lives
    global game_exit
    x = (display_width*0.45)
    y = (display_height*0.65)

    x_change = 0
    while not game_exit:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    x_change = -8
                    
                elif event.key == py.K_RIGHT:
                    x_change = 8
                if event.key == py.K_q:
                    py.quit()
                    quit()
                
            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                    x_change = 0     
        x += x_change


        gameDisplay.fill(black)
        ship(x,y)
        scoreboard()
        life_counter()


        if x > display_width - ship_width or x < -30:
            x_change = 0
            enemy_spawn()
        if lives == 0:
            game_over()
            
        #pygame.update.flip changes the whole screen, and so does update unless you put parameners in the parenthesis
        py.display.update()
        #clock.tick actually handles the fps
        clock.tick(60)
 

game_loop()
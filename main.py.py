# cheat codes and home screen
import random
import pygame
import os

pygame.mixer.init()

pygame.init()

# colors
white= (225,225,225)
red= (225,0,0)
black = (0,0,0)
green = "#54a832"

#creating a window
screen_height= 400
screen_width= 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#background image
bgimg=pygame.image.load("backimg.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game by Rishita")

clock = pygame.time.Clock()

font=pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,(x,y))

def plot_snake(gameWindow,color,snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game= False
    while not exit_game:
        gameWindow.fill((233,210,233))
        snkimg = pygame.image.load("snakedead.jpg")
        snkimg = pygame.transform.scale(snkimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(snkimg,(0,0))
        text_screen("Welcome to Snakes",red,120,130)
        text_screen("Press space key to play",red, 100, 180)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('backgrnd.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()         #mandatory to update
        clock.tick(60)


# Game loop
def gameloop():
    #local var so that replay the game
    # Game specific variables
    exit_game = False
    game_over =  False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snake_size = 10
    score = 0
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    fps = 30  # loop ek frame usko kitni baar update
    snk_list = []
    snk_length = 1
    # check if file exist or not
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore=f.read()

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            overimg = pygame.image.load("snakeimg.jpg")
            overimg = pygame.transform.scale(overimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(overimg, (0, 0))
            # s3 = pygame.Surface((80, 40))
            # pygame.Surface.set_colorkey(s3, (0, 0, 0))
            text_screen("Game over:press enter to replay",black,10,150)
            text_screen("Your score:"+str(score),black,200,190)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('backgrnd.mp3')
                        pygame.mixer.music.play()
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key== pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key== pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key== pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    #cheat code:
                    if event.key == pygame.K_q:
                        score+=10
            snake_x= snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                food_x = random.randint(20, screen_width /2)
                food_y = random.randint(20, screen_height /2)
                snk_length+=5
                if int(highscore)<score:
                    with open("highscore.txt","w") as f:
                        highscore=score
                        f.write(str(score))

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: "+str(score)+" Highscore:"+str(highscore),red,5,5)       # remember this after white bg
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            #for collision and handling walls
            if head in snk_list[:-1]:
                game_over= True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x>screen_width or snake_x<0 or snake_y>screen_height or snake_y<0:
                game_over= True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()               #doesn't really matter
    quit()
welcome()
import pygame
import time
import random
import math
from sys import exit
# wheat=(245,222,179)
# wheat active=(244,164,96)

pygame.init()
gamedisplay=pygame.display.set_mode((800,700))
pygame.display.set_caption('Car Race')
#main page image
main_image=pygame.image.load('main.png')
#intro main image
intro_image=pygame.image.load('instruction.png')
#car image
car_image=pygame.image.load('car.png')
carX=352
carY=565
#enemy car
E_car=pygame.image.load('enemycar.png')
E_carY_change=0.5
E_car_state='on_way'
#text
font=pygame.font.Font('freesansbold.ttf',30)
textX=180
textY=300

#car_image function
def car(x,y):
    gamedisplay.blit(car_image,(x,y))
#text_function
def text_function(x,y):
    text_screen=font.render("YOU CRASHED !!!",True,(255,255,255))
    t_s2=font.render("SCORE :"+str(score),True,(255,255,255))
    gamedisplay.blit(text_screen,(x,y))
    gamedisplay.blit(t_s2,(x,y+100))
    pygame.display.update()
    time.sleep(3)
    Game_loop()
def score_text(x,y,score):
    score_text=font.render("SCORE :"+str(score),True,(255,255,255))
    gamedisplay.blit(score_text,(x,y))
#enemy car function
def enemy_car_function(x,y):
    global E_car_state
    if E_car_state == 'on_way':
        gamedisplay.blit(E_car,(x,y))
#crashed
def collision(x,y,a,b):
    distance=math.sqrt((math.pow(x-a,2))+(math.pow(y-b,2)))
    if distance<115:
        return True
    else:
        return False
#main image function
def main_function(x,y):
    gamedisplay.blit(main_image,(x,y))
#intro image function
def intro_function(x,y):
    gamedisplay.blit(intro_image,(x,y))
clock=pygame.time.Clock()
#main page
def main():
    
    run=True
    while run:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                run=False
        gamedisplay.fill((118,215,234))
        main_function(144,94)
        button('Start',532,128,40,100,'start')
        button('Instruction',532,228,40,180,'intro')
        button('Quit',532,328,40,100,'quit')
        pygame.display.update()
def button(msg,x,y,h,w,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplay,(244,164,96),(x,y,w,h))
        if click[0]==1 and action !=None:
            if action =='quit':
                
                pygame.quit()
                
                exit()
            elif action =='start':
                Game_loop()
                
            elif action =='intro':
                intro()
    else:

        pygame.draw.rect(gamedisplay,(245,222,179),(x,y,w,h))
    text_1=font.render(msg,True,(255,255,255))
    gamedisplay.blit(text_1,(x+5,y+5))
    pygame.display.update()
#intro loop
def intro():
    intro=True
    while intro:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                intro=False
        gamedisplay.fill((255,255,255))
        intro_function(144,94)
        pygame.display.update()



#game loop
def Game_loop():
    global score
    carX=352
    carY=565
    carX_change=0
    carY_change=0
    E_carX=random.randint(110,590)
    E_carY=0
    scoreX=100
    scoreY=100
    bumped=True
    score=0
    while bumped:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                bumped=False
            # if event.key==pygame.K_LEFT():
            #     carX_change=0.5
            # if event.key==pygame.K_LEFT:
            #     carX_change=-0.5
        gamedisplay.fill((0,0,0))
        pygame.draw.rect(gamedisplay,(86,125,70),(0,0,100,700))
        pygame.draw.rect(gamedisplay,(255,255,255),(410,0,10,700))
        pygame.draw.rect(gamedisplay,(86,125,70),(700,0,100,700))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            carX_change=-1
        if keys[pygame.K_RIGHT]:
            carX_change=1
        if keys[pygame.K_DOWN]:
            
            carX_change=0
        if keys[pygame.K_SPACE]:
            bumped=False
        #Enemy function calling
        
        for i in range(2):
            E_carY+=E_carY_change
            
            if E_carY <700:
                
                enemy_car_function(E_carX,E_carY)
            if E_carY>700:
                E_carX=random.randint(110,590)
                E_carY=0
                score+=1
                
        #car function call
        carX+=carX_change
        if carX>580:
            
            text_function(textX,textY)
            break
            
        if carX<90:
            
            text_function(textX,textY)
            break
     
        car(carX,carY)
        #collision
        status=collision(E_carX,E_carY,carX,carY)
        if status :
            text_function(textX,textY)
            break
        #score game
        score_text(scoreX,scoreY,score)
        pygame.display.update()
    # clock.tick(60)
# Game_loop()
main()





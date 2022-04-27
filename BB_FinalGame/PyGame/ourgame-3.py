
#Import library
import pygame
from pygame.locals import *
import math
import random
import sys



pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))


def button(screen, position, text):
    font = pygame.font.SysFont("Bailey", 30)
    text_render = font.render(text, 1,(255,255,0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150,150,150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150,150,150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def start():
    #Initialize the game
    keys = [False, False, False, False]
    playerpos=[100,100]
    acc=[0,0]
    arrows=[]
    badtimer=100
    badtimer1=0
    badguys=[[640,100]]
    healthvalue=194
    pygame.mixer.init()

    #images
    player = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\pikachu.png")
    player = pygame.transform.smoothscale(player,(50,70))
    bg = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\bg.jpg")
    bg = pygame.transform.smoothscale(bg,(width,height))
    f1 = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\f1pokemon.png")
    f1 = pygame.transform.smoothscale(f1,(70,70))
    f2 = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\f2may.png")
    f2 = pygame.transform.smoothscale(f2,(70,70))
    f3 = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\f3misty.png")
    f3 = pygame.transform.smoothscale(f3,(70,70))
    f4 = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\f4brock.png")
    f4 = pygame.transform.smoothscale(f4,(70,70))
    arrow = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\shoot.png")
    arrow = pygame.transform.smoothscale(arrow,(100,30))
    badguyimg1 = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\antagonist.png")
    badguyimg1 = pygame.transform.smoothscale(badguyimg1,(50,50))
    badguyimg=badguyimg1
    healthbar = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\healthbar.png")
    health = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\health.png")
    gameover = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\gameover.png")
    youwin = pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\youwin.png")


    #audios
    hit = pygame.mixer.Sound(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\audio\explode.wav")
    enemy = pygame.mixer.Sound(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\audio\enemy.wav")
    shoot = pygame.mixer.Sound(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\audio\shoot.wav")
    hit.set_volume(0.05)
    enemy.set_volume(0.05)
    shoot.set_volume(0.05)
    pygame.mixer.music.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\audio\moonlight.wav")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    running = 1
    exitcode = 0
    #game loop
    while running:
        badtimer-=1
        screen.fill(0)
        for x in range(640):
         for y in range(480):
            screen.blit(bg,(x*640,y*480))
        screen.blit(f1,(0,30))
        screen.blit(f2,(0,135))
        screen.blit(f3,(0,240))
        screen.blit(f4,(0,345 ))
        #player position and rotation
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
        playerrot = pygame.transform.rotate(player, 360-angle*57.29)
        playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
        screen.blit(playerrot, playerpos1)
        
        #arrows
        for bullet in arrows:
            index=0
            velx=math.cos(bullet[0])*10
            vely=math.sin(bullet[0])*10
            bullet[1]+=velx
            bullet[2]+=vely
            if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                arrows.pop(index)
            index+=1
            for projectile in arrows:
                arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
                screen.blit(arrow1, (projectile[1], projectile[2]))
         #antagonist
        if badtimer==0:
             badguys.append([640, random.randint(50,410)])
             badguys.append([640, random.randint(50,410)])
             badtimer=100-(badtimer1*2)
             if badtimer1>=35:
                 badtimer1=35
             else:
                 badtimer1+=5
        index=0
        for badguy in badguys:
            if badguy[0]<-64:
                badguys.pop(index)
            badguy[0]-=7
            
            badrect=pygame.Rect(badguyimg.get_rect())
            badrect.top=badguy[1]
            badrect.left=badguy[0]
            if badrect.left<64:
                 hit.play()
                 healthvalue -= random.randint(5,20)
                 badguys.pop(index)
             #collisions
            index1=0
            for bullet in arrows:
                 bullrect=pygame.Rect(arrow.get_rect())
                 bullrect.left=bullet[1]
                 bullrect.top=bullet[2]
                 if badrect.colliderect(bullrect):
                     enemy.play()
                     acc[0]+=1
                     badguys.pop(index)
                     arrows.pop(index1)
                 index1+=1
             #Next bad guy
            index+=1
        for badguy in badguys:
            screen.blit(badguyimg, badguy)
        screen.blit(healthbar, (5,5))
        for health1 in range(healthvalue):
             screen.blit(health, (health1+8,8))
             #update the screen
        pygame.display.flip()
        
        for event in pygame.event.get(): 
             if event.type==pygame.QUIT:
                 # if it is quit the game
                 pygame.quit()
                 exit(0)
             if event.type == pygame.KEYDOWN:
                 if event.key==K_w:
                     keys[0]=True
                 elif event.key==K_a:
                     keys[1]=True
                 elif event.key==K_s:
                     keys[2]=True
                 elif event.key==K_d:
                     keys[3]=True
             if event.type == pygame.KEYUP:
                 if event.key==pygame.K_w:
                     keys[0]=False
                 elif event.key==pygame.K_a:
                     keys[1]=False
                 elif event.key==pygame.K_s:
                     keys[2]=False
                 elif event.key==pygame.K_d:
                     keys[3]=False
             if event.type==pygame.MOUSEBUTTONDOWN:
                 shoot.play()
                 position=pygame.mouse.get_pos()
                 acc[1]+=1
                 arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
        #Movement of player
        if keys[0]:
            playerpos[1]-=5
        elif keys[2]:
            playerpos[1]+=5
        if keys[1]:
            playerpos[0]-=5
        elif keys[3]:
            playerpos[0]+=5
        #Win/Lose check
        if pygame.time.get_ticks()>=120000:
            running=0
            exitcode=1
        if healthvalue<=0:
            running=0
            exitcode=0
        if acc[1]!=0:
            accuracy=acc[0]*1.0/acc[1]*100
            acc_float="{:.2f}".format(accuracy)
        else:
            accuracy=0
    #Win/lose display        
    if exitcode==0:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("BETTER LUCK NEXT TIME !",True, (240,255,255))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(gameover, (0,0))
        screen.blit(text, textRect)
        
    
    else:
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        screen.blit(youwin, (0,0))
        with open("accuracy_data.txt","a") as data:
            data.write(str(acc_float)+'\n')
        with open("accuracy_data.txt","r") as data:
            content2=[str(x) for x in data.readlines()]
        best_acc=max(content2)
        text = font.render("Accuracy: "+str(acc_float)+"% "+"Best Accuracy: "+str(best_acc)+"%",True, (240,255,255))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(text, textRect)
            

def frontend():
    frontend=pygame.image.load(r"C:\Users\Welcome\Desktop\Pikachu-PaRa\BB_FinalGame\PyGame\resources\images\frontend.jpeg")
    frontend = pygame.transform.smoothscale(frontend,(width,height))
    for x in range(640):
         for y in range(480):
            screen.blit(frontend,(x*640,y*480))
    b1 = button(screen, (400, 300), "  Quit  ")
    b2 = button(screen, (500, 300), "  Play  ")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
        pygame.display.update()
    pygame.quit()

frontend()



                    
    

    


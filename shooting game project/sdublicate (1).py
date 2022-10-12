
rename=input("Enter Name : ")
def select_level():
    print("1.Easy Level","2.Medium Level","3.Difficult Level",sep="\n")
    global level
    level=input("Select level : ")
    if(int(level) not in range(1,4)):
        print("\nWrong key entered")
        select_level()
select_level()
import pygame
pygame.init()
pygame.mixer.init()

#Color Names with codes
black=(0,0,0)
blue=(0,0,255)
white=(255,255,255)
lime=(0,255,0)
yellow=(255,255,0)
aqua=(0,255,255)
dark_pink=(255,0,255)
silver=(192,192,192)
gray=(128,128,128)
maroon=(128,0,0)
olive=(128,128,0)
green=(0,128,0)
purple=(128,0,128)
teal=(0,128,128)
navy=(0,0,128)
red=(255,0,0)

screen_width=900
screen_height=600
dis=pygame.display.set_mode((screen_width,screen_height))

bgimg=pygame.image.load("gg2.webp")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption("Shooting Game")
dis.blit(bgimg,(0,0))
pygame.display.update()

#Gun distance from left and up side(l,b)
l=100
b=500    
def gun1(l,b):
    pygame.draw.rect(dis,maroon,[l,b,25,60],width=13)
    pygame.draw.rect(dis,maroon,[l+15,b,50,20],width=8)
    pygame.display.update()

def gun2(l,b):
    pygame.draw.rect(dis,maroon,[l,b,15,40],width=10)
    pygame.draw.rect(dis,maroon,[l+15,b,30,10],width=3)
    pygame.display.update()

def gun3(l,b):
    pygame.draw.rect(dis,maroon,[l,b,18,45],width=10)
    pygame.draw.rect(dis,maroon,[l+15,b,20,14],width=5)
    pygame.draw.rect(dis,maroon,[l+35,b+3,15,8],width=2)
    pygame.display.update()

def text(score,hit,miss,life):
    Font=pygame.font.SysFont("arial",20,True,True)

    name=Font.render("Name : "+ rename,True,black,yellow)
    dis.blit(name,pygame.draw.rect(dis,navy,[20,30,100,25],width=1))

    score=Font.render(("Score : "+str(score)),True,black,yellow)
    dis.blit(score,pygame.draw.rect(dis,navy,[20,70,100,25],width=1))

    hit=Font.render(("Hit : "+str(hit)),True,black,yellow)
    dis.blit(hit,pygame.draw.rect(dis,navy,[150,70,100,25],width=1))

    miss=Font.render(("Miss : "+str(miss)),True,black,yellow)
    dis.blit(miss,pygame.draw.rect(dis,navy,[300,70,100,25],width=1))

    Quit=Font.render("Q: Quit",True,black,yellow)
    dis.blit(Quit,pygame.draw.rect(dis,navy,[20,110,100,25],width=1))

    Continue=Font.render("C: Continue",True,black,yellow)
    dis.blit(Continue,pygame.draw.rect(dis,navy,[150,110,100,25],width=1))

    life=Font.render("Life:"+str(life),True,black,yellow)
    dis.blit(life,pygame.draw.rect(dis,navy,[600,70,100,25],width=1))
    
    pygame.display.update()

#Object distance from left and upside(ol,ob)
ol=700
ob=300
def Object1(ol,ob):
    pygame.draw.circle(dis,red,[ol,ob],40,width=10)
    pygame.draw.circle(dis,yellow,[ol,ob],30,width=10)
    pygame.draw.circle(dis,navy,[ol,ob],20,width=10)
    pygame.draw.circle(dis,lime,[ol,ob],10,width=10)
    pygame.display.update()

def Object2(ol,ob):
    pygame.draw.circle(dis,red,[ol,ob],28,width=8)
    pygame.draw.circle(dis,yellow,[ol,ob],20,width=7)
    pygame.draw.circle(dis,navy,[ol,ob],13,width=7)
    pygame.draw.circle(dis,lime,[ol,ob],6,width=6)
    pygame.display.update()

def Object3(ol,ob):
    pygame.draw.circle(dis,red,[ol,ob],23,width=7)
    pygame.draw.circle(dis,yellow,[ol,ob],17,width=6)
    pygame.draw.circle(dis,navy,[ol,ob],11,width=6)
    pygame.draw.circle(dis,lime,[ol,ob],5,width=5)
    pygame.display.update()

#bullet start point and distance from up side(bullet_start,b)
def bullet1(bullet_start,b):
    pygame.draw.circle(dis,aqua,[bullet_start,b+9],radius=9,width=6)
    pygame.display.update()

def bullet2(bullet_start,b):
    pygame.draw.circle(dis,aqua,[bullet_start,b+5],radius=5,width=3)
    pygame.display.update()

def bullet3(bullet_start,b):
    pygame.draw.circle(dis,aqua,[bullet_start,b+5],radius=3,width=2)
    pygame.display.update()

def over():
    Font=pygame.font.SysFont("arial",80,True,True)
    over=Font.render(("Game Over"),True,black,yellow)
    dis.blit(over,pygame.draw.rect(dis,navy,[300,250,100,25],width=1))
    pygame.display.update()

def hit1():
    Font=pygame.font.SysFont("arial",70,True,True)
    hit=Font.render("HIT",True,black,aqua)
    dis.blit(hit,pygame.draw.rect(dis,navy,[400,250,100,25],width=1))
    pygame.display.update()

def miss1():
    Font=pygame.font.SysFont("arial",70,True,True)
    miss=Font.render("MISS",True,white,red)
    dis.blit(miss,pygame.draw.rect(dis,navy,[400,250,100,25],width=1))
    pygame.display.update()
    
run=True
def Run(ol,ob,l,b,run):
    score=0
    miss=0
    hit=0
    life=3
    run1=True
    
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.quit()
    
        keys=pygame.key.get_pressed()
        if(keys[pygame.K_c]):
            run1=True
            b-=0.1
            dis.blit(bgimg,(0,0))
            Run(ol,ob,l,b,run)
        if(keys[pygame.K_q]):
            run=False
            pygame.quit()
            
        while run1:
            import random
            bullet_start=130
            pygame.time.delay(15)
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.quit()
            
            keys=pygame.key.get_pressed()
            if(life == 0):
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                over()
                run1=False
                        
            if((keys[pygame.K_UP]) and b>150):
                b-=2
                dis.blit(bgimg,(0,0))
                pygame.time.delay(30)
                b-=2
                dis.blit(bgimg,(0,0))
            if(keys[pygame.K_DOWN] and b<540):
                b+=2
                dis.blit(bgimg,(0,0))
                pygame.time.delay(30)
                b+=2
                dis.blit(bgimg,(0,0))

            if(keys[pygame.K_RIGHT]):
                while(bullet_start<ol):
                    bullet_start+=12
                    pygame.mixer.music.load('gun.mp3')
                    pygame.mixer.music.play()
                    if(level=='1'):
                        bullet1(bullet_start,b)
                    elif(level=='2'):
                        bullet2(bullet_start,b)
                    elif(level=='3'):
                        bullet3(bullet_start,b)
                pygame.time.delay(60)
                dis.blit(bgimg,(0,0))

                if(level=='1'):
                    if(bullet_start in range(ol-50,ol+50) and b in range(ob-50,ob+38)):
                        score+=1
                        hit+=1
                        ol=random.randint(450,650)
                        ob=random.randint(200,550)
                        hit1()
                    else:
                        miss+=1
                        life-=1
                        miss1()
                        
                elif(level=='2'):
                    if(bullet_start in range(ol-50,ol+50) and b in range(ob-25,ob+25)):
                        score+=1
                        hit+=1
                        ol=random.randint(450,650)
                        ob=random.randint(200,550)
                        hit1()
                    else:
                        miss+=1
                        life-=1
                        miss1()

                if(level=='3'):
                    if(bullet_start in range(ol-50,ol+50) and b in range(ob-20,ob+20)):
                        score+=1
                        hit+=1
                        ol=random.randint(450,650)
                        ob=random.randint(200,550)
                        hit1()
                    else:
                        miss+=1
                        life-=1
                        miss1()
                        
            if(keys[pygame.K_q]):
                run=False
                pygame.quit()

            if(level=='1'):
                gun1(l,b)
                Object1(ol,ob)
                
            if(level=='2'):
                gun2(l,b)
                Object2(ol,ob)

            if(level=='3'):
                gun3(l,b)
                Object3(ol,ob)
            text(score,hit,miss,life)
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play()
Run(ol,ob,l,b,run)

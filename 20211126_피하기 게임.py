

import pygame as p
import random

p.init()

size = [500,900]
sc = p.display.set_mode(size)

p.display.set_caption("피하기 게임")

font1 = p.font.SysFont('malgungothic',25)
font2 = p.font.SysFont('malgungothic',85)
score = 0
hp = 3
playing = True

image2 = p.image.load("city.png")
image = p.image.load("car.png")
image1 = p.image.load("img.png")
image_rect = image.get_rect(left = 200 , top = 850)
image_rect1 = image1.get_rect(left = 200, top = 1)  #left =x좌표 top = y좌표 

while playing:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit() #파이게임 창 끄기
            quit()  #shell창 끄는 명령어
            playing = False
    
    if event.type == p.KEYDOWN:
        if event.key == p.K_RIGHT:
            image_rect.left +=10
        if event.key == p.K_LEFT:
            image_rect.left -=10

    sc.fill([255,255,255])
    sc.blit(image2,[0,0])

    sc.blit(image,image_rect)
    if image_rect.left == 450:
        image_rect.left -=10
    if image_rect.left == 0:
        image_rect.left +=10
        
    sc.blit(image1,image_rect1)
    if image_rect1.top >= 800:
        image_rect1.top = 0
        image_rect1.left = random.randint(1,450)
        score +=1
    image_rect1.top +=10
    if image_rect.colliderect(image_rect1):
        hp -=1
        image_rect1.top = 0
        image_rect1.left = random.randint(1,450)
    if hp == 0:
        text3 = font2.render("GMAE OVER",True,(255,0,0))
        sc.blit(text3,[0,450])
        playing = False
    text1 = font1.render("점수:{}".format(score),True,(0,0,255))
    text2 = font1.render("목숨:{}".format(hp),True,(0,0,255))
    if score == 10:
        text4 = font2.render("Clear",True,(0,255,0))
        sc.blit(text4,[0,450])
        playing = False
    sc.blit(text1,[30,30])
    sc.blit(text2,[400,30])
    p.display.flip() #업데이트

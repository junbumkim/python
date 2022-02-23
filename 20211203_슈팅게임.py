#미사일을 쏘아 운석을 피하면 된다

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
#미사일
m_list = []
playing = True
m_count = 0

image2 = p.image.load("s.png") #배경
image = p.image.load("n.png")#전투기
image3 = p.image.load("m.png")#미사일
image1 = p.image.load("img.png")
image_rect = image.get_rect(left = 200 , top = 850)
image_rect2 = image3.get_rect(left = 200, top = 1)#left =x좌표 top = y좌표 
#적군 복제
e_list = []
for x in range(5):
    image_rect1 = image1.get_rect(left =x*100, top = 1)
    e_list.append(image_rect1)

while playing:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit() #파이게임 창 끄기
            quit()  #shell창 끄는 명령어
            playing = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_SPACE:
                m_count +=1
                if m_count <= 5:
                    mis = image3.get_rect(left = image_rect.left+30, top = image_rect.top)
                    m_list.append(mis)
    if event.type == p.KEYDOWN:
        if event.key == p.K_RIGHT:
            image_rect.left +=10
        if event.key == p.K_LEFT:
            image_rect.left -=10
       
                
            
            
    sc.fill([255,255,255])
    sc.blit(image2,[0,0]) #배경                   

    sc.blit(image,image_rect)
    if image_rect.left == 450:
        image_rect.left -=10
    if image_rect.left == 0:
        image_rect.left +=10
        
    

    
    text1 = font1.render("점수:{}".format(score),True,(0,0,255))
    if score == 5:
        text4 = font2.render("Clear",True,(0,255,0))
        sc.blit(text4,[0,450])
        playing = False
    sc.blit(text1,[30,30])
        
    for mis in m_list:   #미사일이 복제되었을때
        sc.blit(image3,mis)
        mis.top-=10
        for f in e_list:
            if mis.colliderect(f): #미사일과 적군이 충돌하는가?
                m_list.remove(mis)
                e_list.remove(f)
                score +=1
                
    for e in e_list: #적군이 복제되었을때
        sc.blit(image1,e)
        e.top +=1
    p.display.flip() #업데이트

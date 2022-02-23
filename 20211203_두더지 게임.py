#제한시간 내에 두더지를 많이 잡는 게임

import pygame as p
import random as r
import time as t
p.init()

size = [1000,500]
sc = p.display.set_mode(size)

p.display.set_caption("두더지게임")

font1 = p.font.SysFont('malgungothic',20)
font2 = p.font.SysFont('malgungothic',40)

score = 0
start = t.time()
playing = True
image = p.image.load("mmm.png")
image_rect = image.get_rect(left = 300 , top = 200)
#효과음 넣기
p.mixer.init()
hit1 = p.mixer.Sound("123.wav")
#두더지 복제
a_list = []
for x in range(10):
    do = image.get_rect(left = r.randint(0,900), top = r.randint(0,400))
    a_list.append(do)
    
while playing:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit() #파이게임 창 끄기
            quit()  #shell창 끄는 명령어
            playing = False
        if event.type == p.MOUSEBUTTONDOWN:
            for do in a_list:
                if do.collidepoint(event.pos):#두더지를 클릭한다면
                    a_list.remove(do)
                    do = image.get_rect(left = r.randint(0,900), top = r.randint(0,400))
                    a_list.append(do)
                    hit1.play()
                    score += 1
        sc.fill([255,255,255])
        text1 = font1.render("점수:{}".format(score),True,(0,0,255))
        for do in a_list:
            sc.blit(image,do)
            sc.blit(text1,[10,10])
        end = t.time()
        time =60 - (end - start)
        text2 = font2.render("시간:{}".format(int(time)),True,(0,0,255))
        sc.blit(text2,[400,10])            
        if time <= 0:
            text3 = font2.render("게임 종료".format(score),True,(0,0,255))
            sc.blit(text3,[400,250])
            if score >= 200:
                text4 = font2.render("등급:A".format(int(time)),True,(0,0,255))
                sc.blit(text4,[400,300])
            elif score >= 100:
                text5 = font2.render("등급:B".format(int(time)),True,(0,0,255))
                sc.blit(text5,[400,300])
            elif score >= 50:
                text6 = font2.render("등급:C".format(int(time)),True,(0,0,255))
                sc.blit(text6,[400,300])
            playing = False
    p.display.flip()  #업데이트

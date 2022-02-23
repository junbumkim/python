#빨간 색깔을 먹으면 크기가 늘어난다. 점수를 많이내면 승리


import pygame as p
import random
p.init()

size = [600,600]
sc = p.display.set_mode(size)

p.display.set_caption("지렁이게임")

font1 = p.font.SysFont('malgungothic',25)
font2 = p.font.SysFont('malgungothic',50)
score = 0
playing = True
#지렁이생성
snake = [(200,200),(210,200),(220,200)]
snake_skin = p.Surface((10,10))#지렁이 객체 생성
snake_skin.fill((0,255,0))
#아이템 생성
item_locate = (300,300)
item = p.Surface((10,10))
item.fill((255,0,0))
#지렁이 움직이기
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
my_direction = LEFT #나의 현재 방향
#프레임 설정
clock = p.time.Clock()
while playing:
    clock.tick(10) 
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit() #파이게임 창 끄기
            quit()  #shell창 끄는 명령어
            playing = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_w:
                my_direction = UP
            if event.key == p.K_a:
                my_direction = LEFT
            if event.key == p.K_d:
                my_direction = RIGHT
            if event.key == p.K_s:
                my_direction = DOWN
    if my_direction == UP:
        snake[0] = (snake[0][0],snake[0][1]-10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1]+10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0]-10,snake[0][1])
    if my_direction == RIGHT:
        snake[0] = (snake[0][0]+10,snake[0][1])
    #지렁이 꼬리 같이 움직이게하기
    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0],snake[i-1][1])
    text2 = font2.render("GAME OVER".format(score),True,(255,0,0))               
    sc.fill([0,0,0])
    #가로 세로선 귿기
    for x in range(0,600,10): #세로선
        p.draw.line(sc,(70,70,70),(x,0),(x,600))
        p.draw.line(sc,(70,70,70),(0,x),(600,x))
    
    #지렁이 화면 배치
    for s in snake:
        sc.blit(snake_skin,s)
    
    if snake[0] == item_locate:
        score +=1
        item_locate = (random.randint(0,59)*10,random.randint(0,59)*10)
        snake.append((0,0))
        
    if snake[0][0] == 600 or snake[0][0] == 0 or snake[0][1] == 600 or snake[0][1] == 0:
        sc.blit(text2,[180,250])
        playing = False

    text1 = font1.render("점수:{}".format(score),True,(255,255,0))
    sc.blit(text1,[500,10])
    #아이템 업로드
    sc.blit(item,item_locate)
    p.display.flip() #업데이트

#공을 안떨어트리고 끝까지 가면 승리 


import pygame as p

p.init()

size = [1000,500]
sc = p.display.set_mode(size)

p.display.set_caption("바운스볼")

playing = True
j = 0
image = p.image.load("pp.png")
image2 = p.image.load("bb.png")
image3 = p.image.load("bb.png")
image4 = p.image.load("bb.png")
image_rect = image.get_rect(left = 0 , top = 250)
image_rect2 = image2.get_rect(left = 0 , top = 450)
image_rect3 = image3.get_rect(left = 400 , top = 450)
image_rect4 = image4.get_rect(left = 550 , top = 450)


clock = p.time.Clock() #FPS

while playing:
    clock.tick(50) #초당프레임 100
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
    sc.blit(image,image_rect)
    image_rect.top +=j
    j+=1
    if image_rect.top >= 450:
        playing = False
    if image_rect.left == 0:
        image_rect.left +=10
    if image_rect.left == 950:
        image_rect.left -=10
    sc.blit(image2,image_rect2)
    if image_rect.colliderect(image_rect2):
        j = -17
        
    sc.blit(image3,image_rect3)
    if image_rect.colliderect(image_rect3):
        j = -17
    sc.blit(image4,image_rect4)
    if image_rect.colliderect(image_rect4):
        j = -17
    if image_rect4.left >= 920:
        image_rect4.left -= 1
   
    p.display.flip() #업데이트

import pygame
import pygame.tests
from pygame import mixer

pygame.init()
# bullet_sound = mixer.Sound("./sound.wav") it will burst ur eardrum while training
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()


score_p1 = 0
score_p2 = 0

font = pygame.font.Font("./fonts.ttf", 32)
rect_1_posi_y = 300
rect_2_posi_y =  300

ball_posi = [640,360]





velo_x = -9
velo_y = -2

running = True
while running:
        # Quit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

    keys = pygame.key.get_pressed()

    

# Ball MOvemetn \
    ball_posi[0] += velo_x
    ball_posi[1] += velo_y
  
    if ball_posi[1] + 15 == 15:
     
        velo_y = -velo_y
    if ball_posi[1] + 15 == 705:
     
        velo_y = -velo_y
    

# Collision for rect_1_x 
    if ball_posi[0] + 15  <= 79:
        
        if ball_posi[1]+15  >= rect_1_posi_y and ball_posi[1]+15 <= rect_1_posi_y + 100:
            velo_x = -velo_x
            # bullet_sound.play()
            # print("ballls",ball_posi)
            print(rect_1_posi_y-ball_posi[1])
        if rect_1_posi_y >=0 and rect_1_posi_y <=50:
            velo_y = -velo_y
            # bullet_sound.play()
        if rect_1_posi_y >= 50 and rect_1_posi_y <=100:
            velo_y = -velo_y
            # bullet_sound.play()
        if velo_x <0:
            velo_x -= 0.7
        if velo_x > 0:
            velo_x += 0.7

    # print("ball",ball_posi)
# Collisiong for rect_2
    if ball_posi[0]+15  >= 1200:
        if ball_posi[1]+15  >= rect_2_posi_y and ball_posi[1]+15 <= rect_2_posi_y + 100:
            velo_x = -velo_x
            # bullet_sound.play() 
            
        if rect_1_posi_y >=0 and rect_1_posi_y <=50 :
            # bullet_sound.play()
            velo_y = -velo_y
        if rect_1_posi_y >= 50 and rect_1_posi_y <=100:
            # bullet_sound.play()
            velo_y = -velo_y
        if ball_posi[1] + 15 >= 1280:
            # bullet_sound.play()
            velo_y = -velo_y
        if velo_x <0:
            velo_x -= 0.1
        if velo_x > 0:
            velo_x += 0.1
        
     

# Movement of rect-1 
    if keys[pygame.K_w] and rect_1_posi_y > 5 :
         rect_1_posi_y -= 10

    
    if keys[pygame.K_s] and rect_1_posi_y < 611 :
        rect_1_posi_y += 10

# Movement of rect-2 
    
    if keys[pygame.K_i] and rect_2_posi_y > 5 :
        rect_2_posi_y -= 10

    
    if keys[pygame.K_j] and rect_2_posi_y < 611 :
        rect_2_posi_y += 10

# Game End -- > 
    if ball_posi[0] + 15 <= 10 :
        ball_posi[0] = 640
        score_p2 +=1
        velo_x = +9

    
    if ball_posi[0] + 15 >= 1260:
        ball_posi[0] = 640
        score_p1 +=1
        velo_x = -9

# Auto movement player 2 
    if ball_posi[0] >=640:
        if ball_posi[1] >= rect_2_posi_y + 50 :
            rect_2_posi_y+=6
    
        if ball_posi[1] <= rect_2_posi_y + 50:
            rect_2_posi_y -=6
#Auto Movement player 1     
    # if ball_posi[1] >= rect_1_posi_y + 50 :
    #     rect_1_posi_y+=6
    
    # if ball_posi[1] <= rect_1_posi_y + 50:
    #     rect_1_posi_y -=6


    print(rect_1_posi_y)
















    screen.fill("black")
    pygame.draw.rect(screen,"white", (30,rect_1_posi_y, 25, 100))
    pygame.draw.rect(screen,"white", (1200, rect_2_posi_y ,25, 100))
    pygame.draw.rect(screen,"white", (640,0, 2, 1200))
    pygame.draw.circle(screen,'green',ball_posi,15)
    score = font.render("Socre :" + str(score_p1) , True, (255, 255, 255))
    screen.blit(score, (180, 18))
    score = font.render("Socre :" + str(score_p2) , True, (255, 255, 255))
    screen.blit(score, (960, 18))







    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
pygame.quit()


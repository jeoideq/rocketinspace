import pygame

pygame.init()

WIDTH =600
HEIGHT=600
TITLE="SPACE_SHIP"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)  

spaceship_x = 300
spaceship_y = 300




background = pygame.image.load("space.png")


spaceship=pygame.image.load("spaceship.png")
spaceship=pygame.transform.scale(spaceship,(100,200))
spaceship=pygame.transform.rotate(spaceship, 90)






run = True
while run:
    screen.blit(background,(0, 0))
    screen.blit(spaceship,(spaceship_x,spaceship_y))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        spaceship_y -= 5
    if keys[pygame.K_s]:
        spaceship_y += 5
    if keys[pygame.K_a]:
        spaceship_x -= 5
    if keys[pygame.K_d]:
        spaceship_x += 5

    
    
    for event in pygame.event.get():
        
       
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()


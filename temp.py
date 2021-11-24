import pygame

pygame.init()
window=pygame.display.set_mode((600,500))
pygame.display.set_caption("its working")
blue=(0,0,255)
red=(0,245,0)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    
    square=pygame.Rect(40,50,60,60)
    pygame.draw.rect(window,blue,square)
    
    recta=pygame.Rect(100,300,50,60)
    pygame.draw.rect(window,red,recta)
    pygame.display.update()

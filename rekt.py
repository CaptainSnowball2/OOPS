import pygame
pygame.init()
HEIGHT=500
WIDTH=500
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("Green")

class rex():
    def __init__(self,h,w,x,y,color,t):
        self.h=h
        self.w=w
        self.x=x
        self.y=y
        self.color=color
        self.t=t
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h),self.t)
rect1=rex(10,10,300,68,(67,67,67),1)
rect2=rex(200,100,50,200,"red",20)
rect1.draw()
rect2.draw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    
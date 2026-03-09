import pygame
pygame.init()
HEIGHT=500
WIDTH=500
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("green")

class circle():
    def __init__(self,x,y,r,color,t):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
        self.t=t
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,self.t)
    def big(self):
        self.r+=1
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,self.t)
    def UP(self):
        self.y+=-10
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r,self.t)
    def Down(self):
        pass
circle1=circle(250,250,10,"red",0)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.draw()
        if event.type == pygame.MOUSEBUTTONUP:
            circle1.big()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("green")
                circle1.UP()

    pygame.display.update()
    
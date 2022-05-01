import pygame
    
class Player:
    def __init__(self, ecran):
        self.x = 10
        self.y = 10
        self.vit = 200
        self.ecran = ecran
        self.canjump = True
        self.sautForce = 0
        self.maxSautForce = 500

    def Draw(self):
        pygame.draw.circle(self.ecran, ( 0, 0, 255), (self.x,self.y), 20)
    def Update(self, deltaTime):
        if pygame.key.get_pressed()[pygame.K_d]:
                self.x += deltaTime * self.vit
        if pygame.key.get_pressed()[pygame.K_q]:
                self.x += -deltaTime * self.vit
        self.y += deltaTime*200
        self.jump(deltaTime)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.x += deltaTime * self.vit
        if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.x += -deltaTime * self.vit
        self.y += deltaTime*200
        self.jump(deltaTime)

    def jump(self, deltatime):
        self.y -= deltatime* self.sautForce
        self.sautForce -= deltatime* 500
        if self.sautForce<0 : self.sautForce = 0
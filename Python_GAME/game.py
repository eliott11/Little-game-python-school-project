# import pygame
# from player import Perso

# pygame.init()

# ecran = pygame.display.set_mode((1000, 1000))
# p = Perso(ecran)
# loop = True
# getTicksLastFrame = 0
# while loop:

#     t = pygame.time.get_ticks()
#     deltaTime = (t - getTicksLastFrame) / 1000.0
#     getTicksLastFrame = t
#     p.Upgrade(deltaTime)
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN/
#             if event.key == pygame.K_LEFT:
#                 p.x += 10
#             if event.type == pygame.QUIT:
#                 loop = False
#     ecran.fill((0,0,0))
#     p.Draw()
#     pygame.display.flip()

# pygame.quit()


# def Collision(self, player):
#         if self.y <= player.y +20 and player.x +20 >= self.x:
#             if player.x <= self.x+self.width and player.y-20<=self.y+self.height:

#                 x = self.x + self.width/2
#                 y = self.y + self.height/2
#                 if player.y>self.y and player.y<self.y+self.height:
#                     if player.x < x:
#                         player.x = self.x - 20
#                     if player.x > x:
#                         player.x = self.x+self.width+20
#                 if player.x>self.x and player.x<self.x+self.width:
#                     if player.y < y:
#                         player.y = self.y - 20
#                     if player.y > y:
#                         player.y = self.y + 20
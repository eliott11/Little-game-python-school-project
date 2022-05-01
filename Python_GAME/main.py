import random
import pygame
from player import Player
from sol import Sol
from enemie import Enemie
pygame.init()

ecran = pygame.display.set_mode((700,700))
pygame.display.set_caption("oklm")
p = Player(ecran)
solList = []
enemies=[]
solList.append(Sol(ecran,5,600,700,50))
solList.append(Sol(ecran,600,540,50,60))
solList.append(Sol(ecran,5,570,50,60))
enemies.append(Enemie(ecran, 300,200, "right"))
enemies.append(Enemie(ecran, 320, 250, "right"))
enemies.append(Enemie(ecran, 280, 300, "right"))
timerEnemy = 1
for i in range(0):
    solList.append(Sol(ecran, random.randint(0,1000), random.randint(40,20), random))
for i in range(0):
    enemies.append(Enemie(ecran, random.randint(0,1000), random.randint(0,500), "right"))
loop = True
getTicksLastFrame = 0
while loop:
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    timerEnemy -= deltaTime
    if timerEnemy<=0:
        timerEnemy = 0.5
        enemies.append(Enemie(ecran, random.randint(0,1000), random.randint(0, 500), "right"))

    p.Update(deltaTime)
    for sol in solList:
        sol.Collision(p)
        for en in enemies:
            sol.Collision(en)
    for en in enemies:
        en.Collision(p)
        en.Update(deltaTime)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if p.canjump:
                    p.canjump = False
                    p.sautForce = p.maxSautForce
        if event.type == pygame.QUIT:
            loop = False
    ecran.fill((0,0,0))

    for sol in solList:
        sol.Draw()
    p.Draw()

    for en in enemies:
        en.Draw()

    pygame.display.flip()

pygame.quit()
import pygame
from Ship import *
from Asteroid import *

pygame.init() 

screen_info = pygame.display.Info() 
print(screen_info)

size = (width, height) = (screen_info.current_w, screen_info.current_h) 
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)

NumsLevels = 4
Levle = 1
AsteroidCount = 3
Player = Ship((28, 288))
Asteroids = pygame.sprite.Group()
# Asteroids = ast((50, 280))

def init():
  global AsteroidCount
  Player.reset((20, 200))
  Asteroids.empty()
  AsteroidCount += 3
  for i in range(AsteroidCount):
    Asteroids.add(ast((400, 300))

def main():
  init()
  while Level <= NumLevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 10
        if event.key == pygame.K_LEFT:
          Player.speed[0] = -10
        if event.key == pygame.K_UP:
          Player.speed[1] = 10
    Player.update()
    screen.fill(color)
    Asteroids.update() 
    Asteroids.draw(screen)
    screen.blit(Player.image, Player.rect)
    pygame.display.flip()

    if Player.checkReset(width):
      init()

if __name__ == '__main__':
  main()
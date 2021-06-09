import pygame
import skeleton
background_colour = (128,100,255)
(width, height) = (500, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Platformer')
screen.fill(background_colour)
skeleton1=skeleton.skeleton()
skeleton1.walkLeft()
pygame.display.flip()
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(background_colour)
  skeleton1.draw(screen)
  pygame.display.flip()
  skeleton1.nextFrame()
  clock.tick(1)

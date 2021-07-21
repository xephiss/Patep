import pygame
import player

background_colour = (128, 100, 255)
(width, height) = (700, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Platformer')
screen.fill(background_colour)
skeleton1 = player.Player()
skeleton1.set_position(480, 300)
# skeleton1.walk_left()
skeleton1.walk_right()
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
    skeleton1.next_frame()
    clock.tick(4)

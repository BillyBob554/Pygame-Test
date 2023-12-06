import pygame
#Variables
Res = (300, 300)
running = True


pygame.init()

screen = pygame.display.set_mode((Res))
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False

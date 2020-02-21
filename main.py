import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 20, 20)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
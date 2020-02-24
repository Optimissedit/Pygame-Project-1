import pygame

pygame.init()

##  COLORS  ##
WHITE = (255, 255, 255)
RED = (255, 20, 20)
BLUE = (0, 0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window")

drawList = []

running = True
clock = pygame.time.Clock()

block = pygame.Rect(300, 200, 20, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     circ = pygame.mouse.get_pos()
        #     pygame.draw.circle(screen, BLUE, circ, 30, 1)
    clock.tick(60)
    screen.fill(WHITE)
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        block.x -= 3
    if keys[pygame.K_d]:
        block.x += 3
    if keys[pygame.K_w]:
        block.y -= 3
    if keys[pygame.K_s]:
        block.y += 3
    if keys[pygame.K_SPACE]:
        temp = [block.x + 5, block.y + 5]
        tempBlock = pygame.Rect(temp, (10, 10))
        drawList.append(tempBlock)


    for obj in drawList:
        pygame.draw.rect(screen, RED, obj)

    pygame.draw.rect(screen, (150, 200, 20), block)
    pygame.display.flip()

pygame.quit()
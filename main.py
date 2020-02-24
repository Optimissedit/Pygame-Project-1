import pygame

pygame.init()

##  COLORS  ##
WHITE = (255, 255, 255)
RED = (255, 20, 20)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):

    def __init__(self, left, top, width, height):
        super().__init__()

        self.image = pygame.image.load("man.png").convert_alpha()
        self.x = left
        self.y = top

        pygame.draw.rect(self.image, WHITE, [left, top, width, height])

        self.rect = self.image.get_rect()

    def handle_keys(self):

        key = pygame.key.get_pressed()
        dist = 3
        if key[pygame.K_a]:
            block.x -= dist
        if key[pygame.K_d]:
            block.x += dist
        if key[pygame.K_w]:
            block.y -= dist
        if key[pygame.K_s]:
            block.y += dist
        if key[pygame.K_SPACE]:
            temp = [block.x + 5, block.y + 5]
            tempBlock = pygame.Rect(temp, (10, 10))
            drawList.append(tempBlock)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window")

drawList = []

running = True
clock = pygame.time.Clock()

block = Player(200, 300, 20, 20)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(block)


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

    block.handle_keys()

    for obj in drawList:
        pygame.draw.rect(screen, RED, obj)

    block.draw(screen)

    pygame.display.flip()

pygame.quit()
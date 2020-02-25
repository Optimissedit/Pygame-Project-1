import pygame

# COLORS
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, left, top, width, height):
        super().__init__()

        # Sets image to man and sets starting position
        self.image = pygame.image.load("sprites/man.png").convert_alpha()
        self.x = left
        self.y = top

        pygame.draw.rect(self.image, WHITE, [left, top, width, height])

        self.rect = self.image.get_rect()

    def handle_keys(self):

        key = pygame.key.get_pressed()
        dist = 3
        if key[pygame.K_a]:
            self.x -= dist
        if key[pygame.K_d]:
            self.x += dist
        if key[pygame.K_w]:
            self.y -= dist
        if key[pygame.K_s]:
            self.y += dist
        if key[pygame.K_SPACE]:
            temp = [self.x + 5, self.y + 5]
            temp_block = pygame.Rect(temp, (10, 10))
            return temp_block

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


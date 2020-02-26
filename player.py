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

        self.move_dist = 3;

        pygame.draw.rect(self.image, WHITE, [left, top, width, height])

        self.rect = self.image.get_rect()

    # Handles logic input from keys for moving and interacting
    def handle_keys(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.x -= self.move_dist
        if key[pygame.K_d]:
            self.x += self.move_dist
        if key[pygame.K_w]:
            self.y -= self.move_dist
        if key[pygame.K_s]:
            self.y += self.move_dist
        if key[pygame.K_SPACE]:
            temp = [self.x + 5, self.y + 5]
            temp_block = pygame.Rect(temp, (10, 10))
            return temp_block

    # draws self onto surface at current location
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    # Set the move speed attribute for the player
    def setMove(self, move):
        self.move_dist = move;


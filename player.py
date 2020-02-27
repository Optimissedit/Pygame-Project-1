import pygame

# COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Player(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, left, top, width, height, move=3, supply=5):
        super().__init__()

        # Sets image to man and sets starting position
        self.image = pygame.image.load("sprites/man.png").convert_alpha()
        self.x = left
        self.y = top

        # Variables relating to spawning objects.
        self.rect_supply = supply
        self.last_spawn = pygame.time.get_ticks()
        self.cool_down = 300

        # Display for player supply
        self.font = pygame.font.Font('arial.ttf', 20)
        self.supply_display = self.font.render(str(self.get_supply()), True, RED, WHITE)
        self.display_rect = self.supply_display.get_rect()

        # Pixels moved per tick, 3 by default
        self.move_dist = move

        pygame.draw.rect(self.image, WHITE, [left, top, width, height])

        self.rect = self.image.get_rect()

    # Handles logic input from keys for moving and interacting
    def handle_keys(self):

        # Receives key input from tick
        key = pygame.key.get_pressed()

        # Movement keys
        if key[pygame.K_a]:
            self.x -= self.move_dist
        if key[pygame.K_d]:
            self.x += self.move_dist
        if key[pygame.K_w]:
            self.y -= self.move_dist
        if key[pygame.K_s]:
            self.y += self.move_dist
        # Creates a block at center of player if space is held and the player has the supply
        if key[pygame.K_SPACE]:
            # Gets current time
            now = pygame.time.get_ticks()
            # creates an object to pass along to render list
            temp = [self.x + 5, self.y + 5]
            temp_block = pygame.Rect(temp, (10, 10))

            # Check for sufficient supply and cooldown before passing object to calling variable
            if self.rect_supply > 0 and now - self.last_spawn >= self.cool_down:
                self.last_spawn = now
                self.rect_supply -= 1
                # print("spawning...")
                return temp_block
            # Case for insufficient supply
            elif self.rect_supply <= 0:
                # print("none left bruh")
                return None

    # draws self onto surface at current location
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.supply_display = self.font.render(str(self.get_supply()), True, RED, WHITE)
        surface.blit(self.supply_display, (20, 20))

    # Set the move speed attribute for the player
    def set_move(self, move):
        self.move_dist = move

    # Returns value of self.rect_supply
    def get_supply(self):
        return self.rect_supply


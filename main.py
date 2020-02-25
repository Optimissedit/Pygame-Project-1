import pygame
from player import Player

pygame.init()

# COLORS
WHITE = (255, 255, 255)
RED = (255, 20, 20)
BLUE = (0, 0, 255)

# set up screen
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window")

# Initialize some variables
drawList = []
running = True
clock = pygame.time.Clock()
block = Player(200, 300, 20, 20)

# Main game loop
def main(running):
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

        # Block returns objs spawned by block
        drawn = block.handle_keys()

        # if Block created an object this tick, add to the drawlist
        if drawn is not None:
            drawList.append(drawn)

        # Iterate through draw list and draw objects to screen
        for obj in drawList:
            pygame.draw.rect(screen, RED, obj)

        # Player draws self onto screen
        block.draw(screen)

        # Update display
        pygame.display.flip()


# Main function
main(1)

# End of file, exit program
pygame.quit()

import sys
import pygame


def makelevel(level):
    collidelist = []
    for y, line in enumerate(level):
        for x, character in enumerate(line):
            if character == "#":
                block = pygame.Rect(x*64, y*64, 64, 64)
                collidelist.append(block)
    return collidelist


def move(xvel, yvel, player_rect, collideList):
    # Move the rect along the x-axis first.
    player_rect.x += xvel
    # Check if it collides with a block.
    for block in collidelist:
        if player_rect.colliderect(block):
            if xvel < 0:  # We're moving to the left.
                # Move the player out of the block.
                player_rect.left = block.right
            elif xvel > 0:  # We're moving to the right.
                player_rect.right = block.left
            break

    # Now do the same for the y-axis.
    player_rect.y += yvel
    for block in collidelist:
        if player_rect.colliderect(block):
            if yvel < 0:
                player_rect.top = block.bottom
            elif yvel > 0:
                player_rect.bottom = block.top
            break


pygame.init()
screen = pygame.display.set_mode((800, 600))
BLOCK_COLOR = (50, 50, 255)
BG_COLOR = (0, 0, 0)

level = ["#=======##=========================",
         "#=======#==========================",
         "#==###############=========###=====",
         "#===============#####==============",
         "#==================================",
         "###################################",]

collidelist = makelevel(level)
player_rect = pygame.Rect((64*3, 0, 64, 64))
# A clock to limit the frame rate.
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        move(5, 0, player_rect, collidelist)
    if pressed[pygame.K_LEFT]:
        move(-5, 0, player_rect, collidelist)
    if pressed[pygame.K_UP]:
        move(0, -5, player_rect, collidelist)
    if pressed[pygame.K_DOWN]:
        move(0, 5, player_rect, collidelist)

    # Draw everything.
    screen.fill(BG_COLOR)

    for rect in collidelist:
        pygame.draw.rect(screen, BLOCK_COLOR, rect)

    pygame.draw.rect(screen, (255, 255, 255), player_rect)

    pygame.display.update()
    clock.tick(30)  # Limit frame rate to 30 fps.



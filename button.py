import pygame

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Button Example")

# Define the button
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
button_rect = pygame.Rect(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
button_color = WHITE
button_hover_color = (200, 200, 200)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is over the button
    if button_rect.collidepoint(mouse_pos):
        button_color = button_hover_color
    else:
        button_color = WHITE

    # Draw the button
    pygame.draw.rect(screen, button_color, button_rect)

    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()

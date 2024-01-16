import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Pac-Man properties
pacman_radius = 30
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5
pacman_angle = 0
pacman_direction = 0  # 0: Right, 1: Up, 2: Left, 3: Down

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    pacman_angle += pacman_direction * 90  # Change direction based on user input

    # Update Pac-Man's position
    pacman_x += pacman_speed * round(math.cos(math.radians(pacman_angle)))
    pacman_y -= pacman_speed * round(math.sin(math.radians(pacman_angle)))

    # Wrap Pac-Man around the screen
    pacman_x %= WIDTH
    pacman_y %= HEIGHT

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

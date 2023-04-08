import pygame
import random
import sys
# Define map dimensions and tile size
MAP_WIDTH = 100
MAP_HEIGHT = 100
TILE_SIZE = 8

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define random map generation algorithm
def generate_map():
    # Create an empty map
    map_data = []
    for row in range(MAP_HEIGHT):
        map_data.append([])
        for column in range(MAP_WIDTH):
            map_data[row].append(0)
    
    # Randomly set tiles on the map
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            if random.randint(0, 100) < 20:
                map_data[row][column] = 1
    
    return map_data

# Define function for rendering the map
def draw_map(map_data):
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            if map_data[row][column] == 1:
                pygame.draw.rect(screen, GREEN, (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Generate and render the map
map_data = generate_map()
draw_map(map_data)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()

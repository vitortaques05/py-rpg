import pygame
import random
import noise

# Carregar texturas
grass_texture = pygame.image.load('assets/images/grass.jpg')
water_texture = pygame.image.load('assets/images/water.jpg')
tree_texture = pygame.image.load('assets/images/tree.png')

def generate_world(screen, width, height):
    cell_width = screen.get_width() // width
    cell_height = screen.get_height() // height
    world_surface = pygame.Surface((screen.get_width(), screen.get_height()))

    height_map = generate_height_map(width, height)

    for y in range(height):
        for x in range(width):
            altitude = height_map[y][x]
            if altitude < 0.3:
                texture = water_texture
            elif altitude < 0.6:
                texture = grass_texture
            else:
                texture = tree_texture

            draw_texture(world_surface, texture, x, y, cell_width, cell_height)
    
    return world_surface

def generate_height_map(width, height):
    height_map = []
    scale = 10.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    # Usando random.seed() para garantir variação
    random.seed()  # Semente aleatória baseada no tempo atual

    for y in range(height):
        row = []
        for x in range(width):
            amplitude = 1.0
            frequency = 1.0
            noise_value = 0.0

            for _ in range(octaves):
                noise_value += noise.pnoise2(x / scale * frequency, y / scale * frequency) * amplitude
                amplitude *= persistence
                frequency *= lacunarity

            noise_value = (noise_value + 1) / 2.0
            row.append(noise_value)
        height_map.append(row)

    return height_map

def draw_texture(screen, texture, x, y, cell_width, cell_height):
    scaled_texture = pygame.transform.scale(texture, (cell_width, cell_height))
    screen.blit(scaled_texture, (x * cell_width, y * cell_height))

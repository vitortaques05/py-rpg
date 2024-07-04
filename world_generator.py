import pygame
import random
import noise  # Certifique-se de que o pacote `noise` esteja instalado corretamente

# Carregar texturas
grass_texture = pygame.image.load('assets/grass.jpg')
water_texture = pygame.image.load('assets/water.jpg')

def generate_world(tela, largura, altura):
    tamanho_celula_x = tela.get_width() // largura
    tamanho_celula_y = tela.get_height() // altura
    world_surface = pygame.Surface((tela.get_width(), tela.get_height()))

    mapa_alturas = generate_height_map(largura, altura)

    for y in range(altura):
        for x in range(largura):
            altura = mapa_alturas[y][x]
            if altura < 0.4:
                texture = water_texture
            else:
                texture = grass_texture
            draw_texture(world_surface, texture, x, y, tamanho_celula_x, tamanho_celula_y)
    
    return world_surface

def generate_height_map(largura, altura):
    mapa_alturas = []
    frequencia = 16.0 / largura
    for y in range(altura):
        linha = []
        for x in range(largura):
            altura = noise.pnoise2(x * frequencia, y * frequencia)
            altura = (altura + 1) / 2.0
            linha.append(altura)
        mapa_alturas.append(linha)
    return mapa_alturas

def draw_texture(tela, texture, x, y, tamanho_celula_x, tamanho_celula_y):
    textura_redimensionada = pygame.transform.scale(texture, (tamanho_celula_x, tamanho_celula_y))
    tela.blit(textura_redimensionada, (x * tamanho_celula_x, y * tamanho_celula_y))

import pygame

def carregar_imagem(caminho, largura, altura):
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transform.scale(imagem, (largura, altura))


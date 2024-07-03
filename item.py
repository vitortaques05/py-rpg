import pygame
import random
from util import carregar_imagem

class Item:
    def __init__(self, tela_largura, tela_altura, tipo):
        self.largura = 20
        self.altura = 20
        self.x = random.randint(0, tela_largura - self.largura)
        self.y = random.randint(0, tela_altura - self.altura)
        self.tipo = tipo
        if tipo == 'vida':
            self.imagem = carregar_imagem('item_vida.png', self.largura, self.altura)
        elif tipo == 'forca':
            self.imagem = carregar_imagem('item_forca.png', self.largura, self.altura)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)

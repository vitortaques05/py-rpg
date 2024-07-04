import pygame
from utils.ui_helpers import carregar_imagem

class Personagem:
    def __init__(self, tela_largura, tela_altura):
        self.largura = 50
        self.altura = 50
        self.x = tela_largura / 2 - self.largura / 2
        self.y = tela_altura / 2 - self.altura / 2
        self.velocidade = 5
        self.vida = 100
        self.forca = 10
        self.level = 1
        self.experiencia = 0
        self.inventario = []
        self.imagem = carregar_imagem('assets\images\personagem.png', self.largura, self.altura)
        self.imagem_original = self.imagem  # Guardar a imagem original
        self.direcao = 'right'  # Direção inicial
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover(self, teclas, tela_largura, tela_altura):
        if teclas[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.y < tela_altura - self.altura:
            self.y += self.velocidade
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidade
            if self.direcao != 'left':
                self.direcao = 'left'
                self.imagem = pygame.transform.flip(self.imagem_original, True, False)  # Inverte a imagem
        if teclas[pygame.K_RIGHT] and self.x < tela_largura - self.largura:
            self.x += self.velocidade
            if self.direcao != 'right':
                self.direcao = 'right'
                self.imagem = self.imagem_original  # Restaura a imagem original
        self.rect.topleft = (self.x, self.y)

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)

    def usar_item(self, item):
        if item == 'vida':
            self.vida += 20
        elif item == 'forca':
            self.forca += 5
        self.inventario.remove(item)

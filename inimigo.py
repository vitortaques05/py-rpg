import pygame
import random
from util import carregar_imagem

class Inimigo:
    def __init__(self, tela_largura, tela_altura):
        self.largura = 30
        self.altura = 30
        self.x = random.randint(0, tela_largura - self.largura)
        self.y = random.randint(0, tela_altura - self.altura)
        self.vida = 20
        self.forca = 5
        self.velocidade = random.randint(1, 3)  # Velocidade variável entre 1 e 3
        self.distancia_detecao = 200  # Distância a partir da qual o inimigo começa a seguir o jogador
        self.imagem = carregar_imagem('inimigo.png', self.largura, self.altura)
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def mover(self, personagem_x, personagem_y):
        # Calcular distância entre o inimigo e o jogador
        distancia = ((personagem_x - self.x) ** 2 + (personagem_y - self.y) ** 2) ** 0.5

        # Seguir o jogador apenas se estiver dentro da distância de detecção
        if distancia < self.distancia_detecao:
            # Movimento na direção do jogador com velocidade variável
            if personagem_x > self.x:
                self.x += self.velocidade
            elif personagem_x < self.x:
                self.x -= self.velocidade

            if personagem_y > self.y:
                self.y += self.velocidade
            elif personagem_y < self.y:
                self.y -= self.velocidade

            self.rect.topleft = (self.x, self.y)

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)

import pygame
import random
from utils.ui_helpers import carregar_imagem

class Inimigo:
    def __init__(self, tela_largura, tela_altura):
        self.largura = 80
        self.altura = 80
        self.x = random.randint(0, tela_largura - self.largura)
        self.y = random.randint(0, tela_altura - self.altura)
        self.vida = 200
        self.forca = 5
        self.velocidade = random.randint(1, 2)  # Velocidade variável entre 1 e 2
        self.distancia_detecao = 200  # Distância a partir da qual o inimigo começa a seguir o jogador
        self.imagem_padrao = carregar_imagem('assets/images/inimigo.png', self.largura, self.altura)
        self.imagem_ataque = carregar_imagem('assets/images/inimigo_atacando.png', self.largura, self.altura)  # Imagem durante o ataque
        self.imagem_atual = self.imagem_padrao  # Inicia com a imagem padrão
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.ultimo_ataque = 0
        self.cooldown_ataque = 1000  # Cooldown de 1 segundo entre ataques
        self.atacando = False

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

    def atacar(self, personagem):
        # Verifica se o inimigo pode atacar o jogador (dentro da distância e cooldown)
        agora = pygame.time.get_ticks()
        if self.rect.colliderect(personagem.rect) and (agora - self.ultimo_ataque > self.cooldown_ataque):
            personagem.vida -= self.forca
            self.ultimo_ataque = agora
            self.atacando = True
            # Troca para a imagem de ataque durante um curto período
            self.imagem_atual = self.imagem_ataque
            pygame.time.set_timer(pygame.USEREVENT + 1, 300)  # Timer para voltar à imagem padrão após 300 ms

    def desenhar(self, tela):
        tela.blit(self.imagem_atual, self.rect.topleft)

    def atualizar(self):
        # Função chamada para atualizar o estado do inimigo
        pass  # Aqui você pode adicionar lógicas de atualização adicionais, se necessário

    def resetar_imagem(self):
        self.imagem_atual = self.imagem_padrao
        self.atacando = False

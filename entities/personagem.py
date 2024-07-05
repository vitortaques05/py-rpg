import pygame
from utils.ui_helpers import carregar_imagem

class Personagem:
    def __init__(self, tela_largura, tela_altura):
        self.largura = 80
        self.altura = 80
        self.x = tela_largura / 2 - self.largura / 2
        self.y = tela_altura / 2 - self.altura / 2
        self.velocidade = 5
        self.vida = 100  # Atributo vida é suficiente para a barra de vida
        self.forca = 10
        self.level = 1
        self.experiencia = 0
        self.inventario = []
        self.imagem = carregar_imagem('assets/images/personagem.png', self.largura, self.altura)
        self.imagem_original = self.imagem  # Guardar a imagem original
        self.direcao = 'right'  # Direção inicial
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.atacando = False
        self.tempo_ataque = 0
        
        # Dimensões da espada
        self.largura_da_espada = 60
        self.altura_da_espada = 20
        
        # Imagem da espada para o ataque
        self.imagem_espada = carregar_imagem('assets/images/espada.png', self.largura_da_espada, self.altura_da_espada)  # Substitua com as dimensões corretas da espada

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

    def atacar(self):
        if not self.atacando:
            self.atacando = True
            self.tempo_ataque = pygame.time.get_ticks()

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)
        if self.atacando:
            # Desenhe a espada com base na direção
            if self.direcao == 'right':
                pos_espada = (self.rect.right, self.rect.centery - self.altura_da_espada // 2)
            elif self.direcao == 'left':
                pos_espada = (self.rect.left - self.largura_da_espada, self.rect.centery - self.altura_da_espada // 2)
            elif self.direcao == 'up':
                pos_espada = (self.rect.centerx - self.largura_da_espada // 2, self.rect.top - self.altura_da_espada)
            elif self.direcao == 'down':
                pos_espada = (self.rect.centerx - self.largura_da_espada // 2, self.rect.bottom)
            
            tela.blit(self.imagem_espada, pos_espada)
            
            # Reseta o estado de ataque após um curto período
            if pygame.time.get_ticks() - self.tempo_ataque > 200:  # 200 milissegundos de duração do ataque
                self.atacando = False

    def usar_item(self, item):
        if item in self.inventario:
            if item == 'vida':
                self.vida += 20
            elif item == 'forca':
                self.forca += 5
            self.inventario.remove(item)

    def get_espada_rect(self):
        # Implemente conforme a lógica do seu jogo
        # Por exemplo, crie um retângulo para representar a espada
        if self.direcao == 'right':
            return pygame.Rect(self.rect.right, self.rect.centery - self.altura_da_espada // 2, self.largura_da_espada, self.altura_da_espada)
        elif self.direcao == 'left':
            return pygame.Rect(self.rect.left - self.largura_da_espada, self.rect.centery - self.altura_da_espada // 2, self.largura_da_espada, self.altura_da_espada)
        elif self.direcao == 'up':
            return pygame.Rect(self.rect.centerx - self.largura_da_espada // 2, self.rect.top - self.altura_da_espada, self.largura_da_espada, self.altura_da_espada)
        elif self.direcao == 'down':
            return pygame.Rect(self.rect.centerx - self.largura_da_espada // 2, self.rect.bottom, self.largura_da_espada, self.altura_da_espada)

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
            espada_largura = 20
            espada_altura = 10
            if self.direcao == 'right':
                espada_rect = pygame.Rect(self.rect.right, self.rect.centery - espada_altura // 2, espada_largura, espada_altura)
            elif self.direcao == 'left':
                espada_rect = pygame.Rect(self.rect.left - espada_largura, self.rect.centery - espada_altura // 2, espada_largura, espada_altura)
            elif self.direcao == 'up':
                espada_rect = pygame.Rect(self.rect.centerx - espada_largura // 2, self.rect.top - espada_altura, espada_largura, espada_altura)
            elif self.direcao == 'down':
                espada_rect = pygame.Rect(self.rect.centerx - espada_largura // 2, self.rect.bottom, espada_largura, espada_altura)
            
            pygame.draw.rect(tela, (255, 0, 0), espada_rect)
            
            # Reseta o estado de ataque após um curto período
            if pygame.time.get_ticks() - self.tempo_ataque > 200:  # 200 milissegundos de duração do ataque
                self.atacando = False

    def usar_item(self, item):
        if item == 'vida':
            self.vida += 20
        elif item == 'forca':
            self.forca += 5
        self.inventario.remove(item)

    def get_espada_rect(self):
        # Implemente conforme a lógica do seu jogo
        # Por exemplo, crie um retângulo para representar a espada
        largura_da_espada = 30
        altura_da_espada = 20
        if self.direcao == 'right':
            return pygame.Rect(self.rect.right, self.rect.centery - altura_da_espada // 2, largura_da_espada, altura_da_espada)
        elif self.direcao == 'left':
            return pygame.Rect(self.rect.left - largura_da_espada, self.rect.centery - altura_da_espada // 2, largura_da_espada, altura_da_espada)
        elif self.direcao == 'up':
            return pygame.Rect(self.rect.centerx - largura_da_espada // 2, self.rect.top - altura_da_espada, largura_da_espada, altura_da_espada)
        elif self.direcao == 'down':
            return pygame.Rect(self.rect.centerx - largura_da_espada // 2, self.rect.bottom, largura_da_espada, altura_da_espada)

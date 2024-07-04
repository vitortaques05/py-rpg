import pygame
import sys
import random
from config.settings import tela, tela_largura, tela_altura, som_colisao, som_item, fonte, clock, nivel_dificuldade, pontuacao
from utils.ui_helpers import texto_na_tela, confirmar_saida, menu_principal, tela_game_over
from core.world_generator import generate_world
from entities.personagem import Personagem
from entities.inimigo import Inimigo
from entities.item import Item
from entities.barravida import BarraVida

class Game:
    def __init__(self):
        self.personagem = Personagem(tela_largura, tela_altura)
        self.inimigos = [Inimigo(tela_largura, tela_altura) for _ in range(5)]
        self.itens = [Item(tela_largura, tela_altura, random.choice(['vida', 'forca'])) for _ in range(5)]
        self.fonte = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.nivel_dificuldade = 1
        self.pontuacao = 0
        self.barra_vida = BarraVida(10, 10, 200, 20, (0, 255, 0), (255, 0, 0), self.personagem.vida)

    def run(self):
        world_surface = generate_world(tela, tela_largura // 50, tela_altura // 50)
        menu_principal(tela, tela_largura, tela_altura)

        while True:
            self.barra_vida.atualizar_vida(self.personagem.vida)

            tela.blit(world_surface, (0, 0))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        confirmar_saida(tela, tela_largura, tela_altura)
                    if evento.key == pygame.K_SPACE:
                        self.personagem.atacar()

            teclas = pygame.key.get_pressed()
            self.personagem.mover(teclas, tela_largura, tela_altura)

            for inimigo in self.inimigos[:]:
                inimigo.mover(self.personagem.x, self.personagem.y)
                inimigo.atacar(self.personagem)

                if self.personagem.atacando:
                    espada_rect = self.personagem.get_espada_rect()
                    if espada_rect.colliderect(inimigo.rect):
                        # Aplica um dano fixo ao inimigo
                        dano = max(1, self.personagem.forca // 2)  # Exemplo de cálculo de dano
                        inimigo.vida -= dano

                        # Verifica se o inimigo foi derrotado
                        if inimigo.vida <= 0:
                            self.inimigos.remove(inimigo)
                            self.personagem.experiencia += 10
                            self.pontuacao += 10
                            if self.personagem.experiencia >= 100 * self.nivel_dificuldade:
                                self.nivel_dificuldade += 1
                                self.inimigos.append(Inimigo(tela_largura, tela_altura))
                                self.personagem.experiencia -= 100 * self.nivel_dificuldade

            for item in self.itens[:]:
                if self.personagem.rect.colliderect(item.rect):
                    if item.tipo == 'vida':
                        self.personagem.vida += 20
                    elif item.tipo == 'forca':
                        self.personagem.forca += 5
                    self.itens.remove(item)
                    som_item.play()

            self.barra_vida.desenhar(tela)

            self.personagem.desenhar(tela)
            for inimigo in self.inimigos:
                inimigo.desenhar(tela)
            for item in self.itens:
                item.desenhar(tela)

            texto_na_tela(tela, f"Vida: {self.personagem.vida}", self.fonte, (255, 255, 255), 10, 10)
            texto_na_tela(tela, f"Força: {self.personagem.forca}", self.fonte, (255, 255, 255), 10, 40)
            texto_na_tela(tela, f"Level: {self.personagem.level}", self.fonte, (255, 255, 255), 10, 70)
            texto_na_tela(tela, f"Experiência: {self.personagem.experiencia}", self.fonte, (255, 255, 255), 10, 100)
            texto_na_tela(tela, f"Pontuação: {self.pontuacao}", self.fonte, (255, 255, 255), 10, 130)

            if self.personagem.vida <= 0:
                tela_game_over(tela, tela_largura, tela_altura)
                return

            pygame.display.flip()
            self.clock.tick(60)

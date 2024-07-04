import pygame
import sys
import random
from config.settings import tela, tela_largura, tela_altura, som_colisao, som_item, fonte, clock, nivel_dificuldade
from utils.ui_helpers import texto_na_tela, confirmar_saida, menu_principal, tela_game_over
from core.world_generator import generate_world
from entities.personagem import Personagem
from entities.inimigo import Inimigo
from entities.item import Item
from entities.barravida import BarraVida

class Game:
    def __init__(self):
        self.pontuacao = 0  # Adicionando o atributo pontuacao
        self.init_game()

    def init_game(self):
        """Inicializa o jogo configurando o Pygame, objetos principais e display."""
        self.init_pygame()
        self.init_objects()
        self.init_display()

    def init_pygame(self):
        """Inicializa o Pygame."""
        pygame.init()

    def init_objects(self):
        """Inicializa os objetos principais do jogo."""
        self.personagem = Personagem(tela_largura, tela_altura)
        self.inimigos = [Inimigo(tela_largura, tela_altura) for _ in range(5)]
        self.itens = [Item(tela_largura, tela_altura, random.choice(['vida', 'forca'])) for _ in range(5)]
        self.barra_vida = BarraVida(10, 10, 200, 20, (0, 255, 0), (255, 0, 0), self.personagem.vida)
        self.world_surface = generate_world(tela, tela_largura // 50, tela_altura // 50)

    def init_display(self):
        """Inicializa o display e elementos visuais."""
        self.fonte = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

    def run(self):
        """Loop principal do jogo."""
        world_surface = generate_world(tela, tela_largura // 50, tela_altura // 50)
        menu_principal(tela, tela_largura, tela_altura)

        while True:
            self.handle_events()
            self.update_game()
            self.render()

    def handle_events(self):
        """Trata eventos do Pygame."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.quit_game()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    confirmar_saida(tela, tela_largura, tela_altura)
                if evento.key == pygame.K_SPACE:
                    self.personagem.atacar()

    def update_game(self):
        """Atualiza o estado do jogo."""
        teclas = pygame.key.get_pressed()
        self.personagem.mover(teclas, tela_largura, tela_altura)

        self.update_enemies()
        self.check_collisions()
        self.check_player_health()

        # Atualiza a barra de vida com a vida atual do personagem
        self.barra_vida.atualizar_vida(self.personagem.vida)

    def update_enemies(self):
        """Atualiza os inimigos."""
        for inimigo in self.inimigos[:]:
            inimigo.mover(self.personagem.x, self.personagem.y)
            inimigo.atacar(self.personagem)

            if self.personagem.atacando:
                espada_rect = self.personagem.get_espada_rect()
                if espada_rect.colliderect(inimigo.rect):
                    dano = max(1, self.personagem.forca // 2)  # Calcula o dano ao inimigo
                    inimigo.vida -= dano

                    if inimigo.vida <= 0:
                        self.defeat_enemy(inimigo)

    def defeat_enemy(self, inimigo):
        """Lida com a derrota de um inimigo."""
        self.inimigos.remove(inimigo)
        self.personagem.experiencia += 10
        self.pontuacao += 10
        if self.personagem.experiencia >= 100 * nivel_dificuldade:  # Corrigido para acessar nivel_dificuldade diretamente
            self.nivel_dificuldade += 1
            self.inimigos.append(Inimigo(tela_largura, tela_altura))
            self.personagem.experiencia -= 100 * nivel_dificuldade  # Corrigido para acessar nivel_dificuldade diretamente

    def check_collisions(self):
        """Verifica colisões entre o jogador e itens."""
        for item in self.itens[:]:
            if self.personagem.rect.colliderect(item.rect):
                self.collect_item(item)

    def collect_item(self, item):
        """Lida com a coleta de um item pelo jogador."""
        if item.tipo == 'vida':
            self.personagem.vida += 20
        elif item.tipo == 'forca':
            self.personagem.forca += 5
        self.itens.remove(item)
        som_item.play()

        # Atualiza a barra de vida após a coleta do item
        self.barra_vida.atualizar_vida(self.personagem.vida)

    def check_player_health(self):
        """Verifica a saúde do jogador."""
        if self.personagem.vida <= 0:
            self.game_over()

    def game_over(self):
        """Finaliza o jogo."""
        tela_game_over(tela, tela_largura, tela_altura)
        self.quit_game()

    def quit_game(self):
        """Encerra o jogo."""
        pygame.quit()
        sys.exit()

    def render(self):
        """Renderiza o jogo na tela."""
        tela.blit(self.world_surface, (0, 0))

        self.draw_objects()
        self.draw_ui()

        pygame.display.flip()
        self.clock.tick(60)

    def draw_objects(self):
        """Desenha os objetos do jogo na tela."""
        self.personagem.desenhar(tela)
        for inimigo in self.inimigos:
            inimigo.desenhar(tela)
        for item in self.itens:
            item.desenhar(tela)

        # Desenha a barra de vida após os objetos do jogo
        self.barra_vida.desenhar(tela)

    def draw_ui(self):
        """Desenha a interface do usuário na tela."""
        texto_na_tela(tela, f"Vida: {self.personagem.vida}", self.fonte, (255, 255, 255), 10, 10)
        texto_na_tela(tela, f"Força: {self.personagem.forca}", self.fonte, (255, 255, 255), 10, 40)
        texto_na_tela(tela, f"Level: {self.personagem.level}", self.fonte, (255, 255, 255), 10, 70)
        texto_na_tela(tela, f"Experiência: {self.personagem.experiencia}", self.fonte, (255, 255, 255), 10, 100)
        texto_na_tela(tela, f"Pontuação: {self.pontuacao}", self.fonte, (255, 255, 255), 10, 130)

    def run_game(self):
        """Executa o jogo."""
        self.init_game()
        self.run()

if __name__ == "__main__":
    jogo = Game()
    jogo.run_game()

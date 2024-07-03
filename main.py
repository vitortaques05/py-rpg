import pygame
import sys
import random
from personagem import Personagem
from inimigo import Inimigo
from item import Item
from config import tela, tela_largura, tela_altura, som_colisao, som_item
from util import texto_na_tela, confirmar_saida, menu_principal, tela_game_over

# Inicialização do jogo
personagem = Personagem(tela_largura, tela_altura)
inimigos = [Inimigo(tela_largura, tela_altura) for _ in range(5)]
itens = [Item(tela_largura, tela_altura, random.choice(['vida', 'forca'])) for _ in range(5)]
fonte = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
nivel_dificuldade = 1
pontuacao = 0

# Função principal do jogo
def main():
    global pontuacao, nivel_dificuldade, inimigos, itens
    menu_principal(tela, tela_largura, tela_altura)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                confirmar_saida(tela, tela_largura, tela_altura)

        teclas = pygame.key.get_pressed()
        personagem.mover(teclas, tela_largura, tela_altura)

        for inimigo in inimigos[:]:
            inimigo.mover(personagem.x, personagem.y)
            if personagem.rect.colliderect(inimigo.rect):
                personagem.vida -= inimigo.forca
                inimigo.vida -= personagem.forca
                som_colisao.play()
                if inimigo.vida <= 0:
                    inimigos.remove(inimigo)
                    personagem.experiencia += 10
                    pontuacao += 10
                    if personagem.experiencia >= 100 * nivel_dificuldade:
                        nivel_dificuldade += 1
                        inimigos.append(Inimigo(tela_largura, tela_altura))
                        personagem.experiencia -= 100 * nivel_dificuldade

        for item in itens[:]:
            if personagem.rect.colliderect(item.rect):
                if item.tipo == 'vida':
                    personagem.vida += 20
                elif item.tipo == 'forca':
                    personagem.forca += 5
                itens.remove(item)
                som_item.play()

        tela.fill((0, 0, 0))
        personagem.desenhar(tela)
        for inimigo in inimigos:
            inimigo.desenhar(tela)
        for item in itens:
            item.desenhar(tela)

        texto_na_tela(tela, f"Vida: {personagem.vida}", fonte, (255, 255, 255), 10, 10)
        texto_na_tela(tela, f"Força: {personagem.forca}", fonte, (255, 255, 255), 10, 40)
        texto_na_tela(tela, f"Level: {personagem.level}", fonte, (255, 255, 255), 10, 70)
        texto_na_tela(tela, f"Experiência: {personagem.experiencia}", fonte, (255, 255, 255), 10, 100)
        texto_na_tela(tela, f"Pontuação: {pontuacao}", fonte, (255, 255, 255), 10, 130)

        if personagem.vida <= 0:
            tela_game_over(tela, tela_largura, tela_altura)
            return

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

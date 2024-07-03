import pygame
import sys
import random
from personagem import Personagem
from inimigo import Inimigo
from item import Item


# Inicializa o pygame
pygame.init()

# Definições de tela
tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
tela_largura, tela_altura = tela.get_size()

mundo_largura = 2000
mundo_altura = 2000


# Funções auxiliares
def texto_na_tela(tela, texto, fonte, cor, x, y):
    imagem_texto = fonte.render(texto, True, cor)
    tela.blit(imagem_texto, (x, y))

# Função de confirmação de saída
def confirmar_saida(tela):
    fonte = pygame.font.Font(None, 72)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_y:
                    pygame.quit()
                    sys.exit()
                elif evento.key == pygame.K_n:
                    return
        
        tela.fill((0, 0, 0))
        texto_na_tela(tela, "Você quer sair? (Y/N)", fonte, (255, 255, 255), tela_largura / 2 - 200, tela_altura / 2 - 50)
        pygame.display.flip()

# Função do menu principal
def menu_principal(tela):
    fonte = pygame.font.Font(None, 72)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        tela.fill((0, 0, 0))
        texto_na_tela(tela, "Pressione ENTER para começar", fonte, (255, 255, 255), tela_largura / 2 - 250, tela_altura / 2 - 50)
        pygame.display.flip()

# Função de tela de Game Over
def tela_game_over(tela):
    fonte = pygame.font.Font(None, 72)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return

        tela.fill((0, 0, 0))
        texto_na_tela(tela, "Game Over! Pressione ENTER para reiniciar", fonte, (255, 255, 255), tela_largura / 2 - 350, tela_altura / 2 - 50)
        pygame.display.flip()

# Inicialização do jogo
personagem = Personagem(tela_largura, tela_altura)
inimigos = [Inimigo(tela_largura, tela_altura) for _ in range(5)]
itens = [Item(tela_largura, tela_altura, random.choice(['vida', 'forca'])) for _ in range(5)]
fonte = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
nivel_dificuldade = 1
pontuacao = 0

# Carregar música de fundo e efeitos sonoros
pygame.mixer.music.load('musica_de_fundo.mp3')
som_colisao = pygame.mixer.Sound('colisao.wav')
som_item = pygame.mixer.Sound('item.wav')
pygame.mixer.music.pause()  # Pausa a música
pygame.mixer.music.unpause()  # Retoma a música pausada

# Função principal do jogo
def main():
    global pontuacao, nivel_dificuldade, inimigos, itens
    menu_principal(tela)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                confirmar_saida(tela)

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
            tela_game_over(tela)
            return

        pygame.display.flip()
        clock.tick(60)

        

if __name__ == "__main__":
    main()

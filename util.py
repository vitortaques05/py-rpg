import pygame
import sys

def texto_na_tela(tela, texto, fonte, cor, x, y):
    imagem_texto = fonte.render(texto, True, cor)
    tela.blit(imagem_texto, (x, y))

def confirmar_saida(tela, tela_largura, tela_altura):
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

def menu_principal(tela, tela_largura, tela_altura):
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

def tela_game_over(tela, tela_largura, tela_altura):
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


def carregar_imagem(caminho, largura, altura):
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transform.scale(imagem, (largura, altura))


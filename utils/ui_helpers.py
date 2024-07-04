import pygame
import sys

# Fontes
fonte_grande = pygame.font.Font(None, 72)
fonte_pequena = pygame.font.Font(None, 36)

# Relógio
clock = pygame.time.Clock()

def texto_na_tela(tela, texto, fonte, cor, x, y, centralizar=False):
    """Exibe texto na tela, com opção de centralizar."""
    imagem_texto = fonte.render(texto, True, cor)
    if centralizar:
        texto_rect = imagem_texto.get_rect(center=(x, y))
    else:
        texto_rect = imagem_texto.get_rect(topleft=(x, y))
    tela.blit(imagem_texto, texto_rect)

def confirmar_saida(tela, tela_largura, tela_altura):
    """Exibe uma mensagem de confirmação de saída e aguarda a resposta."""
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
        texto_na_tela(tela, "Você quer sair? (Y/N)", fonte, (255, 255, 255), tela_largura // 2, tela_altura // 2)
        pygame.display.flip()

def menu_principal(tela, tela_largura, tela_altura):
    """Exibe o menu principal e aguarda a seleção do jogador."""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    # Feedback visual ao pressionar ENTER
                    texto_na_tela(tela, "Meu Jogo", fonte_grande, (255, 0, 0), tela_largura // 2, tela_altura // 4, centralizar=True)
                    pygame.display.flip()
                    pygame.time.wait(2000)  # Aguarda 200 milissegundos
                    return
                elif evento.key == pygame.K_ESCAPE:
                    confirmar_saida(tela, tela_largura, tela_altura)

        tela.fill((0, 0, 0))
        texto_na_tela(tela, "Meu Jogo", fonte_grande, (255, 255, 255), tela_largura // 2, tela_altura // 4, centralizar=True)
        texto_na_tela(tela, "Pressione ENTER para começar", fonte_pequena, (255, 255, 255), tela_largura // 2, tela_altura // 2, centralizar=True)
        texto_na_tela(tela, "Pressione ESC para sair", fonte_pequena, (255, 255, 255), tela_largura // 2, tela_altura // 1.5, centralizar=True)
        pygame.display.flip()

def tela_game_over(tela, tela_largura, tela_altura):
    """Exibe a tela de Game Over e aguarda o reinício do jogo."""
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
        texto_na_tela(tela, "Game Over! Pressione ENTER para reiniciar", fonte, (255, 255, 255), tela_largura // 2, tela_altura // 2)
        pygame.display.flip()

def carregar_imagem(caminho, largura, altura):
    """Carrega uma imagem do arquivo e a redimensiona para a largura e altura especificadas."""
    imagem = pygame.image.load(caminho).convert_alpha()
    return pygame.transform.scale(imagem, (largura, altura))

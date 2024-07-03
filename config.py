import pygame

# Inicializa o pygame
pygame.init()

# Definições de tela
tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
tela_largura, tela_altura = tela.get_size()

# Carregar música de fundo e efeitos sonoros
pygame.mixer.music.load('musica_de_fundo.mp3')
som_colisao = pygame.mixer.Sound('colisao.wav')
som_item = pygame.mixer.Sound('item.wav')
pygame.mixer.music.pause()  # Pausa a música
pygame.mixer.music.unpause()  # Retoma a música pausada

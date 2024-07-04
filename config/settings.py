import pygame
import os

# Inicialização do Pygame
pygame.init()

# Configurações da tela
tela_info = pygame.display.Info()  # Informações sobre o monitor
tela_largura = tela_info.current_w  # Largura do monitor
tela_altura = tela_info.current_h  # Altura do monitor
tela = pygame.display.set_mode((tela_largura, tela_altura), pygame.FULLSCREEN)  # Modo de tela cheia

# Títulos e ícones
pygame.display.set_caption("Meu Jogo")

# Certifique-se de que o caminho para o ícone está correto
icone_path = os.path.join('assets', 'images', 'icon.png')  # Caminho para o ícone
icone = pygame.image.load(icone_path).convert_alpha()
pygame.display.set_icon(icone)

# Sons
som_colisao = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'colisao.wav'))
som_item = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'item.wav'))

# Fonte
fonte = pygame.font.Font(None, 36)

# Relógio
clock = pygame.time.Clock()

# Variáveis globais
nivel_dificuldade = 1
pontuacao = 0

# Inicializa o mixer com um buffer maior
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

# Carregar música de fundo e efeitos sonoros
try:
    pygame.mixer.music.load('assets/sounds/musica_de_fundo.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Erro ao carregar a música de fundo: {e}")



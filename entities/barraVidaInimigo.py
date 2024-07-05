import pygame

class BarraVidaInimigo:
    def __init__(self, x, y, largura, altura, cor_cheia, cor_vazia, vida_maxima):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor_cheia = cor_cheia
        self.cor_vazia = cor_vazia
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima  # Inicializa a vida atual com o máximo


    def atualizar_vida(self, vida_atual):
        self.vida_atual = vida_atual

    def desenhar(self, tela):
        # Calcula a largura da barra cheia baseada na vida atual
        largura_cheia = int(self.largura * (self.vida_atual / 100))
        
        # Calcula a posição para desenhar a barra de vida acima do inimigo
        pos_x = self.x - self.largura // 2
        pos_y = self.y - self.altura
        
        # Desenha a barra vazia
        pygame.draw.rect(tela, self.cor_vazia, (pos_x, pos_y, self.largura, self.altura))
        
        # Desenha a barra cheia
        pygame.draw.rect(tela, self.cor_cheia, (pos_x, pos_y, largura_cheia, self.altura))

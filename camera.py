import pygame

class Camera:
    def __init__(self, largura, altura):
        self.camera = pygame.Rect(0, 0, largura, altura)
        self.largura = largura
        self.altura = altura

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.largura / 2)
        y = -target.rect.centery + int(self.altura / 2)

        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.camera.width - self.largura), x)  # right
        y = max(-(self.camera.height - self.altura), y)  # bottom

        self.camera = pygame.Rect(x, y, self.largura, self.altura)

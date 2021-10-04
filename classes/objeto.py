import pygame
from random import randint, choice

pygame.mixer.init()

class Carro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('ima/objeto/CARRO01.png'))
        self.sprites.append(pygame.image.load('ima/objeto/CARRO02.png'))

        self.primera = 0
        self.image = self.sprites[self.primera]
        self.largura = 800
        self.altura = 280
        self.x = [280, 310]
        self.velocidade = 1

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = self.largura, self.altura
        self.velo = False

    def correr(self):
        self.velo = True
        if self.velo == True:
            self.largura -= self.velocidade
        if self.largura < -250:
            self.largura = randint(900, 1900)
            self.altura = choice(self.x)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.largura, self.altura
        self.vrum = pygame.mixer.Sound('ima/SONS/carrovindo.wav')
        if self.largura <= 750:
            self.vrum.play()

    def buzina(self):
        self.pompon = pygame.mixer.Sound('ima/SONS/buzina.wav')
        if self.largura > 600:
            self.pompon.play()

    def update_car(self):
        if self.velo == True:
            self.primera = self.primera + 0.25
            if self.primera >= len(self.sprites):
                self.primera = 0

            self.image = self.sprites[int(self.primera)]

    def colocar_car(self, superficie):
        superficie.blit(self.image, self.rect)

carro = Carro()

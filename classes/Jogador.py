import pygame

class Jogador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.sprites = []
		self.sprites.append(pygame.image.load('ima/TON/TON_01.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_02.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_03.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_04.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_05.png'))
		self.sprites.append(pygame.image.load('ima/TON/TON_06.png'))
		self.primera = 0
		self.image = self.sprites[self.primera]
		self.ataca = []
		self.ataca.append(pygame.image.load('ima/TON_ATACA/STON01.png'))
		self.ataca.append(pygame.image.load('ima/TON_ATACA/STON02.png'))
		self.ataca.append(pygame.image.load('ima/TON_ATACA/STON03.png'))
		self.ataca.append(pygame.image.load('ima/TON_ATACA/STON04.png'))
		self.ataca.append(pygame.image.load('ima/TON_ATACA/STON05.png'))
		self.largura = 100
		self.altura = 270

		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect.topleft = self.largura, self.altura
		self.passo = False
		self.soco = False
		self.pulo = False
	def atacar(self):
		self.soco = True
		self.primeiro_soco = 0
		if self.soco == True:
			self.image = self.ataca[self.primeiro_soco]
			self.rect = self.image.get_rect()
			self.rect.topleft = self.largura, self.altura
		self.son_soco = pygame.mixer.Sound('ima/SONS/soco.flac')
		self.son_soco.play()
	def andar(self):
		self.passo = True
		self.largura += 2
		if self.largura > 200:
			self.largura = 200
		self.rect = self.image.get_rect()
		self.rect.topleft = self.largura, self.altura
	def voltar(self):
		self.passo = True
		self.largura -= 2
		if self.largura <= 10:
			self.largura = 10
		self.rect = self.image.get_rect()
		self.rect.topleft = self.largura, self.altura
	def pra_baixo(self):
		self.passo = True
		self.altura += 2
		if self.altura > 307:
			self.altura = 307
		self.rect = self.image.get_rect()
		self.rect.topleft = self.largura, self.altura
	def pra_cima(self):
		self.passo = True
		self.altura -= 2
		if self.altura <= 256:
			self.altura = 256
		self.rect = self.image.get_rect()
		self.rect.topleft = self.largura, self.altura

	def salto(self):
		self.pulo = True

	def update(self):
		if self.pulo == True:
			if self.rect.y <= 165:
				self.pulo = False
			self.rect.y -= 20
			self.rect.x += 10

		else:
			if self.rect.y < self.altura:
				self.rect.y += 30
			else:
				self.rect.y = self.altura

		if self.passo == True:
			self.primera = self.primera + 0.25
			if self.primera >= len(self.sprites):
				self.primera = 0
				self.passo = False
			self.image = self.sprites[int(self.primera)]
		if self.soco == True:
			self.passo = False
			self.primeiro_soco = self.primeiro_soco + 0.5
			if self.primeiro_soco >= len(self.ataca):
				self.primeiro_soco = 0
				self.soco = False
			self.image = self.ataca[int(self.primeiro_soco)]
	def colocar(self, superficie):
		superficie.blit(self.image, self.rect)

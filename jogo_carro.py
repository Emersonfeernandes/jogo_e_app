import pygame
from time import sleep
from classes.Jogador import Jogador
from classes.objeto import Carro
from PIL import ImageColor

vermelho = ImageColor.getrgb("red")
preto = ImageColor.getrgb("black")

def jogo():
	pygame.init()
	pygame.font.init()

	largura = 600
	altura = 400

	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption('Cuidado com o Carro')

	relogio = pygame.time.Clock()
	message = lambda m, c, pos : tela.blit(
	                         pygame.font.SysFont(
	                                            "segol UI"
	                                            , 25
	                                            ).render(m,True,c)
	                                , pos
	                        )

	grupo_sprites = pygame.sprite.Group()
	grupo_inimigos = pygame.sprite.Group()
	jogador = Jogador()
	carro = Carro()
	grupo_sprites.add(jogador)
	grupo_sprites.add(carro)

	grupo_inimigos.add(carro)

	cenario_01 = pygame.image.load('ima/CENARIO_01.png').convert_alpha()
	cenario_02 = pygame.image.load('ima/CENARIO_02.png').convert_alpha()
	fim_de_jogo = pygame.image.load('ima/tela_fim_de_jogo.png').convert_alpha()
	velo = 2
	pos = 0
	posf = 0
	posc2 = 600
	jog = 100
	jog_alt = 270
	janela = True
	while janela:
		relogio.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if jogador.rect.y != jogador.altura:
						pass
					else:
					    jogador.salto()


		comandos = pygame.key.get_pressed()
		if comandos[pygame.K_RIGHT]:
			sleep(0.03)
			if posf == -600:
				posf = 600
			if posc2 == -600:
				posc2 = 600
			if jog == 200:
			   posf -= velo
			   posc2 -= velo
			jog += velo
			if jog > 200:
				jog = 200
		tela.blit(cenario_01, (posf, pos))
		tela.blit(cenario_02, (posc2, pos))
		if comandos[pygame.K_RIGHT]:
			jogador.andar()
		if comandos[pygame.K_LEFT]:
			jogador.voltar()
		if comandos[pygame.K_DOWN]:
			jogador.pra_baixo()
			jog_alt += velo
			if jog_alt > 307:
				jog_alt = 307
		if comandos[pygame.K_UP]:
			jogador.pra_cima()


		colisoe = pygame.sprite.spritecollide(jogador, grupo_inimigos, False, pygame.sprite.collide_mask)

		carro.correr()
		carro.buzina()
		grupo_sprites.draw(tela)
		if colisoe:
			fimdejogo = False
			while not fimdejogo:
				if fimdejogo == False:
					tela.fill(preto)
					message('Você perdeu!', vermelho, [200,100])
					message('Aperte S para sair ou J para jogar!', vermelho, [100,120])
					pygame.display.update()

				for e in pygame.event.get():
					if e.type == pygame.KEYDOWN:
						if e.type == pygame.QUIT:
							fimdejogo = True
							janela = False
						if e.key == pygame.K_s:
							fimdejogo = True
							janela = False
						if e.key == pygame.K_j:
							jogo()
		else:
			carro.velocidade += 0.5
			grupo_sprites.update()



		pygame.display.update()

	pygame.quit()

jogo()

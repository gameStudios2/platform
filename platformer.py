import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Тест игры на пайтоне")

bg = pygame.image.load("bg.jpg")
player = pygame.image.load("player.png")

x = 50
y = 425
speed = 5
height = 60

isJump = False
jumpCount = 1

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super.__init__()
		self.image = pygame.image.load('player.png')
		self.rect = self.image.get_rect()

		self.change_x = 0
		self.change_y = 0

		self.level = None

	def update(self):
		self.calc_gravity()

		self.rect.y += self.change.x


class Level(object):
	def __init__(self):
		self.platforms = pygame.sprite.Group()
		self.player = player
		
		self.background = None

clock = pygame.time.Clock()
run = True
while(run):
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x -= speed
	if keys[pygame.K_RIGHT]:
		x += speed
	if keys[pygame.K_DOWN] and y < 500 - height - 5:
		y += speed
	if not(isJump):
		if keys[pygame.K_SPACE]:
			isJump = True	
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount ** 2) / 2
			else:	
				y -= (jumpCount ** 2) / 2
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10			

	win.blit(bg, (0, 0))
	win.blit(player, (x, y))
	pygame.display.update()

pygame.quit()
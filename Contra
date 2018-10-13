# -*- coding: utf-8 -*-
'''
@Project Name(Game Name):Contra
@Author:DuckQuick
@Email: m18834164553@163.com
@Construction Time:2018-10-13
@Github ID:DuckQuick
@Editing Software: Sublime Text 3(Python 3.X)
@Introduction:Rewriting Contra with Python
'''
'''
website:https://www.cnblogs.com/hhh5460/p/7029217.html
'''
import pygame
from sys import exit

class Hero(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
	pass

class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
	pass

class Map(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
	pass

class Sound(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
	pass

class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
	pass

class Screen(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.size = self.width, self.height = 960, 640
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Contra")

class Game():
	def __init__(self):
		#游戏(pygame)初始化
		pygame.init()
		Screen()

	def run(self):
		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit(0)
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						exit(0)
		
			pygame.display.flip()

if __name__ == '__main__':
	Game().run()

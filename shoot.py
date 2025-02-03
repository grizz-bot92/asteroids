from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
	def __init__(self, position, velocity):
		super().__init__(position.x, position.y, SHOT_RADIUS)
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.position = position
		self.velocity = velocity


	def draw(self, screen):
		pygame.draw.circle(screen, 'white', (self.position.x, self.position.y), self.radius, 2)	
	
	def update(self, dt):
		self.position += self.velocity * dt

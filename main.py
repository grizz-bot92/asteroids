from constants import *
from players import *
from asteroidfield import *
from shoot import *
import pygame

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")



	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable,)
	asteroidfield = AsteroidField()

	shots = pygame.sprite.Group()
	Shot.groups = (shots, updatable, drawable)

	Player.containers = (updatable, drawable)
	player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)




	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game Over!")
				screen.exit()

		for obj in drawable:
			obj.draw(screen)

		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.kill()
					shot.kill()

		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()

from constants import *
from players import *
import pygame

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")



	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()

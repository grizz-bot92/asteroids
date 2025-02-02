from constants import *
import pygame

def main():
	pygame.init()
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen_on = True

	while screen_on:
		screen.fill("black")
		pygame.display.flip()




	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return


	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
	main()


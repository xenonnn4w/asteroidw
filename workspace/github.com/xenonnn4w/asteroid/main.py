import pygame
from constants import *
import sys

def main():
    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    print("Initializing pygame...")
    pygame.init()
    
    # Add these debug lines
    print("Available pygame video drivers:", pygame.display.get_driver())
    
    print("Creating display...")
    try:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Display created successfully")
    except pygame.error as e:
        print(f"Failed to create display: {e}")
        return

    print("Starting game loop...")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event received")
                pygame.quit()
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")
        pygame.quit()
        sys.exit(1)
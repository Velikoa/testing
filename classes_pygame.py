import pygame
import random

Starting_Blue_Blobs = 10
Starting_Red_Blobs = 3

Width = 800
Height = 600

White = (255, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)

game_display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()



class Blob:

    def __init__(self, colour):
        self.x = random.randrange(0, Width)
        self.y = random.randrange(0, Height)
        self.size = random.randrange(4, 8)
        self.colour = colour

    def move(self):
        self.move_x = random.randrange(-1, 2)
        self.move_y = random.randrange(-1, 2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > Width:
            self.x = Width

        if self.y < 0:
            self.y = 0
        elif self.y > Height:
            self.y = Height

def draw_environment(blobs):
    game_display.fill(White)
    for blob_id in blobs:
        blob = blobs[blob_id]    # Also have individual ID's for each blob now.
        pygame.draw.circle(game_display, blob.colour, (blob.x, blob.y), blob.size)
        blob.move()
    pygame.display.update()

def main():
    blue_blobs = dict(enumerate([Blob(Blue) for i in range(Starting_Blue_Blobs)]))
    print blue_blobs
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(blue_blobs)
        clock.tick(60)

if __name__ == "__main__":
    main()
import pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (2000, 100)
pygame.font.init()

WIDTH, HEIGHT = 750, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Light in the Space")


Player_Ship = pygame.image.load(os.path.join(f"dti_game/Images/spr_playerShip.png"))

img_file_dir = 'dti_game/Images'

def loadImage(spr):
    return pygame.image.load(os.path.join(f"{img_file_dir}/{spr}"))

# Load images
#Ships
Player_Ship = loadImage("spr_playerShip.png")

#Background
BG = pygame.transform.scale((loadImage("spr_background.png")), (WIDTH, HEIGHT))#scale the bg

class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = Player_Ship
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_healt = health
    
    def draw(self, window):
        super().draw(window)

def main():
    run = True  
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    player = Player(300, 650)
    player_vel = 5

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))

        # draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))

        WIN.blit(level_label, (10, 10))
        WIN.blit(lives_label, (WIDTH - lives_label.get_width() - 10, 10))

        player.draw(WIN)

        pygame.display.update()

    while run:
        redraw_window()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + 80 < WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > HEIGHT/2:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + 100 < HEIGHT:
            player.y += player_vel

if __name__ == "__main__":
    main()
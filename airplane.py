# import pygame,random,time
#
# WIDTH = 360
# HEIGHT = 480
# FPS = 30
#
# WHTIE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
#
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("My Game")
# clock = pygame.time.Clock()
#
# myfont = pygame.font.Font(None,60)
# textImage = myfont.render("pygame",True,WHTIE)
#
# running = True
# count = 0
# start = time.time()
#
# while running:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     count += 1
#     now = time.time()
#     fps = count/(now-start)
#     fpsImage = myfont.render(str(),True,WHTIE)
#
#     screen.fill(GREEN)
#     screen.blit(fpsImage,(100,100))
#     pygame.display.flip()
#
# pygame.quit()
#
# import pygame,random,os
#
#
# WIDTH = 800
# HEIGHT = 600
# FPS = 30
#
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
#
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder,"img")
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load("img/p1_jump.png").convert()
#         self.image.set_colorkey(BLUE)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH/2, HEIGHT/2)
#
#     def update(self, *args):
#         self.rect.x += 5
#         if self.rect.left > WIDTH:
#             self.rect.right = 0
#
#
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("Sprite Example")
# clock = pygame.time.Clock()
#
#
# all_sprites = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)
# running = True
# while running:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     all_sprites.update()
#     screen.fill(BLACK)
#     all_sprites.draw(screen)
#     pygame.display.flip()
#
# pygame.quit()
# import pygame,random,os
#
# WIDTH = 800
# HEIGHT = 600
# FPS = 30
#
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
#
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder,"img")
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH/2,HEIGHT/2)
#         self.image.set_colorkey(BLACK)
#         self.y_speed = 5
#
#     def update(self, *args):
#         self.rect.x += 5
#         self.rect.y += self.y_speed
#         if self.rect.bottom > HEIGHT - 200:
#             self.y_speed = -5
#         if self.rect.top < 200:
#             self.y_speed = 5
#         if self.rect.left > WIDTH:
#             self.rect.right = 0
#
#
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("My Game")
# clock = pygame.time.Clock()
#
# all_sprites = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)
# running = True
# while running:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     all_sprites.update()
#     screen.fill(BLUE)
#     all_sprites.draw(screen)
#     pygame.display.flip()
#
# pygame.quit()
# import pygame
#
# WIDTH = 480
# HEIGHT = 600
# FPS = 60
#
# Black = (0,0,0)
# White = (255,255,255)
# Blue = (0,0,255)
# Red = (255,0,0)
# Green = (0,255,0)
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50,40))
#         self.image.fill(Green)
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH/2
#         self.rect.bottom = HEIGHT-10
#
#     def update(self, *args):
#         self.speedx = 0
#         keystate = pygame.key.get_pressed()
#         if keystate[pygame.K_LEFT]:
#             self.speedx = -8
#         if keystate[pygame.K_RIGHT]:
#             self.speedx = 8
#         self.rect.x += self.speedx
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.left < 0:
#             self.rect.left = 0
#
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("My Game")
# clock = pygame.time.Clock()
#
# all_sprite = pygame.sprite.Group()
# player = Player()
# all_sprite.add(player)
#
# running = True
# while running:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     all_sprite.update()
#     screen.fill(Black)
#     all_sprite.draw(screen)
#     pygame.display.flip()
# pygame.quit()
#
import pygame, random

WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

# define colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

font_name = pygame.font.match_font("arial")


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, White)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def newmob():
    m = Mob()
    all_sprite.add(m)
    mobs.add(m)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, Green, fill_rect)
    pygame.draw.rect(surf, White, outline_rect, 2)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 40))
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .70 / 2)
        # pygame.draw.circle(self.image,Red,self.rect.center,self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self, *args):
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if keystate[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprite.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprite.add(bullet1)
                all_sprite.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()
            if self.power > 2:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprite.add(bullet1)
                all_sprite.add(bullet2)
                all_sprite.add(bullet)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(bullet)
                shoot_sound.play()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(Black)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        # pygame.draw.circle(self.image,Red,self.rect.center,self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 4)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self, *args):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/laserRed16.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -20

    def update(self, *args):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self, *args):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["shield", "gun"])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self, *args):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()


def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys move, Space to fire", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# Load all game graphics
background = pygame.image.load("img/starfield.png").convert()
background_rect = background.get_rect()
player_img = pygame.image.load("img/playerShip1_orange.png").convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(Black)
meteor_images = []
meteor_list = ["meteorBrown_big1.png", "meteorBrown_big2.png", "meteorBrown_med1.png",
               "meteorBrown_med3.png", "meteorBrown_small1.png", "meteorBrown_small2.png",
               "meteorBrown_tiny1.png"]
for img in meteor_list:
    meteor_images.append(pygame.image.load("img/" + img).convert())
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
explosion_anim["player"] = []
for i in range(9):
    filename = f"regularExplosion0{i}.png"
    img = pygame.image.load("img/" + filename).convert()
    img.set_colorkey(Black)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim["sm"].append(img_sm)
    filename = f"sonicExplosion0{i}.png"
    img = pygame.image.load("img/" + filename).convert()
    img.set_colorkey(Black)
    explosion_anim["player"].append(img)

powerup_images = {}
powerup_images["shield"] = pygame.image.load("img/shield_gold.png").convert()
powerup_images["gun"] = pygame.image.load("img/bolt_gold.png").convert()

# Load all game sounds
shoot_sound = pygame.mixer.Sound("snd/pew.wav")

expl_sounds = []
for snd in ["expl3.wav", "expl6.wav"]:
    expl_sounds.append(pygame.mixer.Sound("snd/" + snd))
player_die_sound = pygame.mixer.Sound("snd/rumble1.ogg")
pygame.mixer.music.load("snd/tgfcoder-FrozenJam-SeamlessLoop.ogg")

pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play(loops=-1)
# Game loop
gameover = True
running = True
all_sprite = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
for i in range(8):
    newmob()
score = 0
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    if gameover:
        show_go_screen()
        gameover = False
    # Process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprite.update()
    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, "lg")
        all_sprite.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprite.add(pow)
            powerups.add(pow)
        newmob()

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, "sm")
        all_sprite.add(expl)
        newmob()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, "player")
            all_sprite.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == "shield":
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == "gun":
            player.powerup()
            shoot_sound.play()

    if player.lives <= 0 and not death_explosion.alive():
        gameover = True
    # Draw / render
    screen.fill(Black)
    screen.blit(background, background_rect)
    all_sprite.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    # *after* drawing everything,flip the display
    pygame.display.flip()
pygame.quit()

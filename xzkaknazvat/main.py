import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (500, 500))
window.blit(background, (0, 0))
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play()

kick = pygame.mixer.Sound('kick.ogg')
kick.set_volume(0.3)
# kick.play()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            hero.rect.y += self.speed
        if keys[pygame.K_w]:
            hero.rect.y -= self.speed

        if keys[pygame.K_a]:
            hero.rect.x -= self.speed
        if keys[pygame.K_d]:
            hero.rect.x += self.speed



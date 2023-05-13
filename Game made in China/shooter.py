#Создай собственный Шутер!

from pygame import *
from random import randint
# from pydub import AudioSegment

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.width = w
        self.high = h
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.shoot = False
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 800:
            self.rect.y = 0
            self.rect.x = randint(0,800)


mixer.init()
mixer.music.load('dio.mp3')
# AudioSegment.from_mp3("dio.mp3").export('dio.ogg', format='ogg')
mixer.music.play()

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 1000-self.width:
            self.rect.x += self.speed
#         if keys[K_w] and self.rect.y > 5:
#             self.rect.y -= self.speed
#         if keys[K_s] and self.rect.y < 800-self.high:
#             self.rect.y -= self.speed
        
class Bullet(GameSprite):
    def update(self):
        self.rect.x = player.rect.x
        keys = key.get_pressed()
        if keys[K_r]:
            self.shoot = True
        if self.shoot == True and self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.rect.y = player.rect.y
            self.shoot = False


# #создай окно игры
window = display.set_mode((1000,800))
display.set_caption(('STAND POWER GAME AMOGUS VS ROAD SIGNS'))
# #задай фон сцены
background=transform.scale(image.load('galaxy.jpg'),(1000,800))

player = Player('This would be The world.png', 500, 600, 24, 132, 200)

enemy1 = Enemy('STOP.png', randint(0,1000), 300, 5, 100, 100)
enemy2 = Enemy('STOP.png', randint(0,1000), 300, 9, 100, 100)
enemy3 = Enemy('STOP.png', randint(0,1000), 300, 16, 100, 100)
enemy4 = Enemy('STOP.png', randint(0,1000), 300, 20, 100, 100)
enemy5 = Enemy('STOP.png', randint(0,1000), 300, 22, 100, 100)

bullet = Bullet('UNO card.png', 500+132/2, 600, 55, 50, 100 )

# # sprite1 = transform.scale(image.load('JOTARO.png'),(190,190))
# # sprite2 = transform.scale(image.load('sprite1.png'),(250,250))

game = True
while game:
    window.blit(background,(0,0))
    player.update()
    player.reset()
    enemy1.update()
    enemy1.reset()
    enemy2.update()
    enemy2.reset()
    enemy3.update()
    enemy3.reset()
    enemy4.update()
    enemy4.reset()
    enemy5.update()
    enemy5.reset()
    bullet.reset()
    bullet.update()
    # window.blit(sprite1, (300,200))
    # window.blit(sprite2, (300,300))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
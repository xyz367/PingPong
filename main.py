from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,speed,rect_x,rect_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (70, 70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class PlayerSprite(sprite.Sprite):
    def __init__(self,player_image,speed,rect_x,rect_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (15, 150))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(PlayerSprite):
    def __init__(self,player_image,speed,rect_x,rect_y):
        super().__init__(player_image,speed,rect_x,rect_y)
    def update1(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

window = display.set_mode((700,500))

back = (210, 190, 200)

player1 = Player('platform.png',2,10,245)
player2 = Player('platform.png',2,675,245)

ball = GameSprite('ball.png',4,350,250)

speed_x = 3
speed_y = 3

FPS = 60
clock = time.Clock()

game = True
while game:
    window.fill(back)

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
        speed_y *= 1

    for i in event.get():
        if i.type == QUIT:
            game = False

    player1.update1()
    player2.update2()

    player1.reset()
    player2.reset()
    ball.reset()


    clock.tick(FPS)
    display.update()
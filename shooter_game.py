
from pygame import *
from random import randint
from time import time as timer 

#фоновая музыка



# нам нужны такие картинки:
img_back = "1gg.jpg" 
img_hero1 = "gg1.png" 
img_hero2 = "gg2.png" 
img_ball = "gg3.jpg"

font.init()
font1 = font.Font(None, 80)
win_gg1 = font1.render('blue is win', True, (0, 0, 0))
win_gg2 = font1.render('red is win', True, (255, 255, 255))


# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < win_height - 80:
            self.rect.y += self.speed


# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
player1 = Player(img_hero1, 0,0, 10, 70, 20)
player2 = Player(img_hero2, 690,0, 10, 70, 20)
ball = GameSprite(img_ball, 15, 0, 40, 40, 10)
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
speed_x = 10
speed_y = 10
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
finish = False
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
       
        # производим движения спрайтов
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <0 or ball.rect.y >500-40:
            speed_y *=-1 
    
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2): 
            speed_x *=-1
        
        


        window.blit(background, (0,0))
        if ball.rect.x > 700-40:
            window.blit(win_gg2, (200,100))
            finish = True
        if ball.rect.x <0:
            window.blit(win_gg1, (200,100))
            finish = True
        player1.update1()
        player2.update()
        player1.reset()
        player2.reset()
        ball.reset()
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
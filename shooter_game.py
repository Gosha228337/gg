
from pygame import *
from random import randint
from time import time as timer 

#фоновая музыка



# нам нужны такие картинки:
img_back = "1gg.jpg" 
img_hero1 = "gg1.png" 
img_hero2 = "gg2.png" 



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
  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
   
# класс спрайта-врага   
#class Enemy(GameSprite):
#     движение врага
#    def update(self):
#        self.rect.y += self.speed
#        global lost
#         исчезает, если дойдет до края экрана
#        if self.rect.y > win_height:
#            self.rect.x = randint(80, win_width - 80)
#            self.rect.y = 0
#            lost = lost + 1

# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
player1 = Player(img_hero1, 0,0, 10, 70, 10)
player2 = Player(img_hero2, 690,0, 10, 70, 10)
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты

# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
       
        # производим движения спрайтов
    
    window.blit(background, (0,0))
    player1.update1()
    player2.update()
    player2.reset()
    player1.reset()
    display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
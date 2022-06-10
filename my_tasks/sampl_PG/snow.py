from random import randint
import pygame as pg
import sys
from os import path

# Инициализация
sc = pg.display.set_mode()
infoObject = pg.display.Info()  # Информационный объект
# Разрешение экрана
W = infoObject.current_w
H = infoObject.current_h

# Загрузка мелодий игры
pg.mixer.init()
pg.mixer.music.load("Merry-Christmas-Jingle-Bells.mp3")
pg.mixer.music.play(-1, 0.0)

pg.time.set_timer(pg.USEREVENT, 60)

SNOW = ('snow1.png', 'snow2.png', 'snow3.png')
# для хранения готовых снежинок-поверхностей
SNOW_SURF = []

for i in range(len(SNOW)):
    SNOW_SURF.append(
        pg.image.load(SNOW[i]).convert_alpha())


class Snowflake(pg.sprite.Sprite):
    def __init__(self, x, size, surf, group):
        super(Snowflake, self).__init__()
        pg.sprite.Sprite.__init__(self)
        self.surf = pg.transform.scale(surf, (size, size))
        self.image = self.surf
        self.rect = self.image.get_rect(
            center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у снежинок будет разная скорость
        self.speed = randint(1, 7)
        self.angle = 0
        self.change_angle = randint(-1, 1)

    def update(self, wind):
        if self.rect.y < H:
            self.rect.y += self.speed
            self.rect.x += wind
            self.image = pg.transform.rotate(self.surf, self.angle)
            self.angle += self.change_angle
            self.angle = self.angle % 360
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()


snow = pg.sprite.Group()

# добавляем первую снежинку,
# которая появляется сразу
Snowflake(randint(1, W), randint(10, 101),
    SNOW_SURF[randint(0, 2)], snow)

wind = 0 # Ветер

while 1:

    if randint(0, 1000) < 20:
        wind += randint(-1, 1)
        if wind < -5:
            wind = -5
        if wind > 5:
            wind = 5

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Snowflake(randint(-400, W+400), randint(10, 101),
                SNOW_SURF[randint(0, 2)], snow)
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_ESCAPE:
                sys.exit()

    sc.fill((0, 0, 30))

    snow.draw(sc)

    pg.display.update()
    pg.time.delay(20)

    snow.update(wind)

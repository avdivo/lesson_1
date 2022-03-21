from random import randint
import time


class Hero():
    # Класс описывающий героя
    def __init__(self, name, life, armor):
        self.name = name
        self.life = life
        self.armor = armor

    def attack(self, hero, power):
        # аргументы hero - на кого атака, power - сила атаки
        print('Атакует ' + self.name + ' c силой ' + str(power))
        hero.life -= power - hero.armor
        return hero.life

    def __str__(self):
        # Печать состояния героя
        return self.name + ' имеет ' + str(self.life) + ' жизней'


class Good(Hero):
    # Класс описывающий доброго героя
    def __init__(self, name, life, armor):
        name = 'Добрый молодец ' + name
        super().__init__(name, life, armor)


class Evil(Hero):
    # Класс описывающий доброго героя
    def __init__(self, name, life, armor):
        name = 'Злой молодец ' + name
        super().__init__(name, life, armor)


good_hero = Good('Илья Муромец', 200, 20)
eval_hero = Evil('Соловей разбойник', 200, 20)

if 1 == randint(1, 2):
    hero1 = good_hero
    hero2 = eval_hero
else:
    hero2 = good_hero
    hero1 = eval_hero

one = two = 0
end = 1
while end > 0:
    one = hero1.attack(hero2, randint(0, 100))
    time.sleep(1)
    two = hero2.attack(hero1, randint(0, 100))
    time.sleep(1)
    print('----------------------------------------')
    print(hero1)
    print(hero2)
    print()
    end = -1 if one <= 0 or two <= 0 else 1

if good_hero.life > 0 and eval_hero.life < 0:
    print('Победило добро! ')
    print(good_hero)
elif eval_hero.life > 0 and good_hero.life < 0:
    print('Победило зло! ')
    print(eval_hero)
else:
    print('Победил мир, воевать больше некому')

# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    _species = 'Дракон'
        
class Troll(Enemy):
    _species = 'Тролль'        


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'
        self._experience_for_kill = 3

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(str(x + y))
        return self.__quest
        
        
class RedDragon(Dragon):
    def __init__(self):
        self._health = 150
        self._attack = 13
        self._color = 'красный'
        self._experience_for_kill = 2
        
    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(str(x - y))
        return self.__quest            


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 51
        self._color = 'черный'
        self._experience_for_kill = 6
        
    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(str(x * y))
        return self.__quest
        
class RandomTroll(Troll):
    def __init__(self):
        self._health = 140
        self._attack = 34
        self._color = 'оранжевый'
        self._experience_for_kill = 7
        
    def question(self):
        x = randint(1, 3)
        self.__quest = 'Угадай число от 1 до 3'
        self.set_answer(str(x))
        return self.__quest
        
        
class SimpleTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 25
        self._color = 'фиолетовый'
        self._experience_for_kill = 10
        
    def question(self):
        x = randint(1, 200)
        self.__quest = 'Число ' + str(x) + ' простое? (0 или 1)'
        def isprime(x):
            if x == 1:
                return '0'
            for i in range(2, x//2):
                if x % i == 0:
                    return '0'
                else:
                    return '1'        
        self.set_answer(isprime(x))
        return self.__quest
        

                          
#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon, RandomTroll, SimpleTroll]

# coding: utf-8
# license: GPLv3
from gameunit import *


class Hero(Attacker):
    def __init__(self, name):
        self._health = 100000
        self._attack = 10000000
        self._experience = 0
        self._name = name
        
    def plusxp(self, target):
        self._experience += target._experience_for_kill    






#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""

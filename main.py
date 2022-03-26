from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod
import random


class Character(ABC):
    """Абстрактный класс игрового объекта."""
    @abstractmethod
    def create(self) -> dict:
        pass


class Hero(Character):
    """Абстрактный класс игрока."""
    @abstractmethod
    def create(self) -> dict:
        pass


class Swordsman(Character):
    """Мечник."""
    def create(self) -> dict:
        return {'HP': 30, 'profession': 'sword', 'inventory':[('sword', 5)], 'monster_counter': 0}


class Ranger(Character):
    """Рейнджер."""
    def create(self) -> dict:
        return {'HP': 30, 'profession': 'bow', 'inventory': [('sword', 5)], 'monster_counter': 0}


class Mage(Character):
    """Маг."""
    def create(self) -> dict:
        return {'HP': 30, 'profession': 'book', 'inventory': [('sword', 5)], 'monster_counter': 0}


class Enemy(Character):
    """Абстрактный класс игрового противника."""
    @abstractmethod
    def create(self) -> dict:
        """Метод, наличие которого обязательно у всех."""
        pass


class Ork(Enemy):
    def create(self) -> dict:
        return {'HP': random.randint(10, 20), 'profession': 'Ork', 'inventory': [('sword', random.randint(2, 4))]}


class Skeleton(Enemy):
    def create(self) -> dict:
        return {'HP': random.randint(2, 10), 'profession': 'Skeleton', 'inventory': [('book', random.randint(5, 7))]}


class Goblin(Enemy):
    def create(self) -> dict:
        return {'HP': random.randint(7, 12), 'profession': 'Goblin', 'inventory': [('bow', random.randint(4, 7))]}


def enemy_spawner() -> dict:
    """спавнер врагов."""
    spawner_to_factory_mapping = {
        "ork" : Ork,
        "skeleton" : Skeleton,
        "goblin" : Goblin
    }
    enemy_type_list = ["ork", "skeleton", "goblin"]
    spawner_type = random.choice(enemy_type_list)
    spawner = spawner_to_factory_mapping[spawner_type]()
    return spawner.create()


def hero_spawner() -> dict:
    """спавнер героев."""
    spawner_to_factory_mapping = {
        1: Swordsman,
        2: Ranger,
        3: Mage
    }
    while True:
        hero_choice = input("Введите Героя от 1 до 3: ")
        if hero_choice.isdigit() is True:
            if 1 <= int(hero_choice) <= 3:
                spawner = spawner_to_factory_mapping[int(hero_choice)]()
                return spawner.create()
        print("Ошибка. Такого героя пока нет, ждите обновлений")


def apple() -> int:
    """Apple generator."""
    some_apple = random.randint(2, 5)
    print('Герой нашел яблоко. И стал здоровее на', some_apple)
    return some_apple


def treasure_chest(hero_dict: dict) -> tuple:          # Todo не соответствует принципам Solid
    """Сундук с рандомными сокровищами."""
    passive = hero_dict['profession']
    all_items = ('sword', 'bow', 'book', 'arrows', 'totem')
    item = random.choice(all_items)
    if item == passive:
        stat = random.randint(10, 15)
        print("Благодаря вашему классу вы находите усиленный", item, "с силой в", stat)
        return item, stat
    elif item == 'totem':
        print("Тотем! С его помощью текущее состояние персонажа будет сохранено и, после гибели в бою,"
              "можно воскреснуть")
        return item, hero_dict
    elif item == 'arrows':
        stat = 50
        print("Стрелы. Без них невозможно стрелять.")
        return item, stat
    else:
        stat = random.randint(5, 10)
        print("Вы находите", item, "с силой", stat)
        return item, stat


def choice() -> Any:
    """Функция для выбора из инпута "Да-Нет"."""
    while True:
        yes_or_no = (input("Введите 1 или 2: "))
        if yes_or_no.isdigit() is True:
            if 1 <= int(yes_or_no) <= 2:
                return int(yes_or_no)
        print("то не 1 или 2")


def on_fight(hero_dict: dict) -> list:
    """Функция, собирающая из инвентаря вооружение. Если к луку нет стрел, то и использоваться он не будет"""
    m = hero_dict['inventory']
    action_list = list()
    totem_info = list(filter(lambda x: 'arrows' in x, hero_dict['inventory']))
    if len(totem_info) != 0:
        for i_inv, val_inv in enumerate(m):
            if val_inv[0] in ('sword', 'bow', 'book'):
                action_list.append(val_inv)
    else:
        for i_inv, val_inv in enumerate(m):
            if val_inv[0] in ('sword', 'book'):
                action_list.append(val_inv)
    return action_list


def mass_choice(action_list: list) -> list:
    """Функция выбора в зависимости от длинны подаваемого списка."""
    print(action_list)   # todo Нужен красивый вывод инфы
    while True:
        weapon_for_fight = input(f"Введите число от 1 до {len(action_list)}: ")
        if weapon_for_fight.isdigit() is True:
            if 1 <= int(weapon_for_fight) < len(action_list) + 1:
                print(action_list[int(weapon_for_fight) - 1])
                return action_list[int(weapon_for_fight) - 1]
        print("Ошибка. Такого предмента в инвентаре нет. Попробуйте ещё раз")


def observer(item: str) -> Any:
    """Класс, помогающий с выбором приоритета атаки."""
    # В классе обработчике, который имеет слушателя событий - переменная, которая хранит ключ каждого объекта
    # для события и факт срабатывания события.  Потом если сработало первое - ок, делаем и записываем, если второе
    # - не делаем, но записываем, и потом делаем оба, когда триггер на первое сраьотал
    if item == "bow":
        return 1
    elif item == "book":
        return 3
    elif item == "sword":
        return 5
    else:
        return "что то пошло не так"


def game() -> Any:
    """Main game function."""
    hero = hero_spawner()  # вызываем Героя
    while hero['monster_counter'] < 10:
        accidental = random.randint(1, 3)  # рандом один из трех вариантов энкаунтеров
        if accidental == 1:
            # Яблоки
            hero.update({'HP': hero['HP'] + apple()})
            print("Теперь у героя", hero['HP'], "здоровья")
        elif accidental == 2:
            # Сундук
            print("Вы нашли сундук!")
            treasure = treasure_chest(hero)
            print("Будем брать? 1 - да, 2 - нет")
            if choice() == 1:   # Проверяем на кол-во предметов в инвенторе, не больше 4
                if len(hero['inventory']) >= 4:  # Проверяем на заполненность инвентарь
                    print(hero['inventory'])
                    if treasure[0] == 'totem':  # Проверяем, есть ли тотем, предлагаем переписать сохраниение, если есть
                        for i_inv, val_inv in enumerate(hero['inventory']):
                            if val_inv[0] == 'totem':
                                print("У вас есть тотем. Больше одного в инвентаре храниться не может. Будем\
                                     переписывать данные сейва? 1 - да, 2 - нет")
                                if choice() == 1:
                                    hero['inventory'].pop(i_inv)
                                    hero['inventory'].append(('totem', hero))
                                    print("Вы подобрали", treasure, "теперь у вас есть", hero['inventory'])
                    print("У вас заполнен инвентарь! Будем что-то выкидывать? 1 - да, 2 - нет")
                    if choice() == 1:
                        print("Ок! Выберите номер предмета, который будем выкидывать")
                        for_del = mass_choice(hero['inventory'])
                        hero['inventory'].remove(for_del)
                        hero['inventory'].append(treasure)
                        print("Вы подобрали", treasure, "теперь у вас есть", hero['inventory'])
                else:  # Автоматически закидываем в инвентарь предмет, если это возможно
                    print(hero['inventory'])
                    hero['inventory'].append(treasure)
                    print("Вы подобрали", treasure, "теперь у вас есть", hero['inventory'])
        else:
            # сражение
            monster = enemy_spawner()
            print(f"Прибыл {monster['profession']} {monster['HP']} ХП {monster['inventory'][0][1]} "
                  f"атаки {monster['inventory'][0][0]}")
            for_fight = on_fight(hero)  # Проверяем, сколько предметов из инвентаря герой может использовать как оружие
            action_list = list(range(1, len(for_fight) + 1))  # строю список из предметов, которыми можно атаковать
            action_list.append(0)  # Ноль для бегства
            while True:
                select = input(f"Введите 0 что бы сбежать или цифру, соответствующую оружию из "
                               f"инвентаря {for_fight} для атаки: ")
                if select.isdigit() is True:
                    if int(select) in action_list:
                        if int(select) == 0:
                            print("Убегаем")
                            break
                        else:
                            while monster['HP'] > 0 and hero['HP'] > 0:               # todo НЕ СДЕЛАНА очередь
                                passive_effect = 1  # Пассивка героя
                                if hero['profession'] == monster['inventory'][0][0]:
                                    passive_effect = 0
                                effect = random.randint(passive_effect, 1)
                                monster['HP'] = monster['HP'] - for_fight[int(select) - 1][1]
                                hero['HP'] = hero['HP'] - int(monster['inventory'][0][1]) * effect
                                if effect == 0:
                                    print("Пассивное умение героя заблокировало урон")
                                print(monster['HP'], hero['HP'])
                            if hero['HP'] <= 0:
                                # Проверяем на наличие тотема
                                totem_info = list(filter(lambda x: 'totem' in x, hero['inventory']))
                                if len(totem_info) != 0:
                                    print("Вы можете воскресить героя с помощбю тотема, 1 - да, 2 - нет")
                                    if choice() == 1:
                                        hero = totem_info[0][1]
                                        print("Вы снова в бою. У вас ", hero['HP'], "здоровья, но только ",
                                              hero['monster_counter'], "уничтоженных монстров")
                                        break
                                print("Вы погибли!", 'Поверженых врагов', hero['monster_counter'], ". Конец игры")
                                quit()
                            if monster['HP'] <= 0:
                                print("Великая победа!")
                                hero.update({'monster_counter': hero['monster_counter'] + 1})
                                print('Поверженых врагов', hero['monster_counter'])
                                break
                    else:
                        print("Неверное число")
                else:
                    print("Неверный ввод")
    return print("ПОБЕДА, вы убили их всех. Добро пожаловать на пенсию")

# print(treasure_chest({'HP': 30, 'profession': 'book', 'inventory': [('sword', 5)], 'monster_counter': 0}))
# print((enemy_spawner()['inventory']))
# game()

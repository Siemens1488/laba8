import random


num_doors = 3
num_gift = 1


def generate_door(num_doors, num_gift):
    door = ['пусто'] * num_doors
    for i in range(num_gift):
        gift_index = random.randint(0, num_doors - 1)
        door[gift_index] = 'приз'
    return door

def game(num_doors, num_gift):
    door = generate_door(num_doors, num_gift)
    player1 = int(input("Игрок 1 - Выбери дверь: "))
    player2 = int(input("Игрок 2 - Ввыбери дверь: "))
    if player1 == 1 and player2 == 2:
        last_door = (door[2])
        if last_door == 'пусто':
            print('За 1 или 2 дверью приз')
            print("Игрок 1 изменил свой выбор")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
        else:
            print("Игрок 1 изменил свой выбор и победил")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
    elif player1 == 1 and player2 == 3:
        last_door = (door[1])
        if last_door == 'пусто':
            print('За 1 или 3 дверью приз')
            print("Игрок 1 изменил свой выбор")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
        else:
            print("Игрок 1 изменил свой выбор и победил")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
    elif player1 == 2 and player2 == 1:
        last_door = (door[2])
        if last_door == 'пусто':
            print('За 2 или 1 дверью приз')
            print("Игрок 1 изменил свой выбор")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
        else:
            print("Игрок 1 изменил свой выбор и победил")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
    elif player1 == 2 and player2 == 3:
        last_door = (door[0])
        if last_door == 'пусто':
            print('За 2 или 3 дверью приз')
            print("Игрок 1 изменил свой выбор")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
        else:
            print("Игрок 1 изменил свой выбор и победил")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
    elif player1 == 3 and player2 == 1:
        last_door = (door[1])
        if last_door == 'пусто':
            print('За 3 или 1 дверью приз')
            print("Игрок 1 изменил свой выбор")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
        else:
            print("Игрок 1 изменил свой выбор и победил")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
    elif player1 == 3 and player2 == 2:
        last_door = (door[0])
        if last_door == 'пусто':
            print('За 3 или 2 дверью приз')
            print("Игрок 1 изменил свой выбор")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")
        else:
            print("Игрок 1 изменил свой выбор и победил")
            print("Шанс выиграша 1 игрока: 0.6667")
            print("шанс выйграша 2 игрока: 0.3333")



generate_door(num_doors, num_gift)
game(num_doors, num_gift)

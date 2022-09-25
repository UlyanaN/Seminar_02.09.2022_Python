# игра против бота с "интеллектом"

from random import randint, randrange

print('Начало игры')
print('На столе лежат 2021 конфета')

def whos_first ():
    a = randint(0,2)
    if a == 0:
        return False
    else:
        return True

def rand_sweets(n):
    c = randint (1, n+1)
    return c

def check_nums_of_sweets(q, su):
    while q < 1 or q > su:
        print ('Неверно введено количество конфет')
        q = int(input())
    return q


def player_moves (total_sweet):
    if total_sweet > 28:
        print('Сколько конфет возьмет первый игрок (от 1 до 28)')
        player = check_nums_of_sweets (int(input()), 29)
    if total_sweet < 28:
        print(f'Сколько конфет возьмет первый игрок (от 1 до {total_sweet})')
        player = check_nums_of_sweets (int(input()), total_sweet)
    total_sweet -= player
    print(f'Игрок взял {player} конфет, осталось {total_sweet} конфет')
    return total_sweet

def bot_moves(ts):
    if ts > 56:
        int_bot = randrange(1, 29)
    elif 28 < ts <= 56:
        int_bot = 29
    else:
        int_bot = ts
    ts-=int_bot
    print(f'Компьютер взял {int_bot} конфет, осталось {ts} конфет')
    return ts

total_sweets = 60
int_bot = 0
player_turn = whos_first()

while total_sweets != 0:
    if player_turn == True:
        total_sweets = player_moves (total_sweets)
        player_turn = False   
    else:   
        total_sweets = bot_moves(total_sweets)
        player_turn = True
            
def print_text(b):
    if b == True:
        print(f'Победил первый игрок!')
        print(f'Осталось {total_sweets} конет')
    else:
        print(f'Победил бот!')
        print(f'Осталось {total_sweets} конет')

print_text(player_turn)
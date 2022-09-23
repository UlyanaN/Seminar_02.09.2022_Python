from random import randint, randrange

print('Начало игры')
print('На столе лежат 2021 конфета')

# игра против бота

total_sweets = 2021

int_bot = 0
player_turn = True

while total_sweets >= 28:
    if player_turn == True:
        print('Сколько конфет возьмет первый игрок (от 1 до 28)')
        player = int(input())
        while player < 1 or player > 28:
            print ('Неверно введено количество конфет')
            player = int(input())
        total_sweets -= player
        print(f'Игрок взял {player} конфет, осталось {total_sweets} конфет')
        player_turn = False
        
    else:
        int_bot = randrange(1, 29)
        total_sweets-=int_bot
        print(f'Компьютер взял {int_bot} конфет, осталось {total_sweets} конфет')
        player_turn = True
            

if player_turn == True:
    print(f'Победил первый игрок!')
    print(f'Осталось {total_sweets} конет')
else:
    print(f'Победил бот!')
    print(f'Осталось {total_sweets} конет')
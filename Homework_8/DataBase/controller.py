# 1 вывод запроса (если это поиск по фио или id)
# вывод базы данных (json)
# прием запросов от пользователя, обработка запросов из меню view

from view import menu
import add_new_data as ad
import find_data as fd
import show_data as sd
import change_phone as cp
import delete_data as dd


def user_choice():
    choice_num = input (menu())
    if choice_num == '1':
        ad.create_json()
    elif choice_num == '2':
        ad.add_to_json()
    elif choice_num == '3':
        fd.find_person()
    elif choice_num == '4':
        sd.all_db()
    elif choice_num == '5':
        cp.change_phone_number()
    elif choice_num == '6':
        dd.delete_person()
    elif choice_num == 'x':
        print('\nБлагодарим за визит!\n\nДо новых встреч!')
        exit()
    else:
        print('Некорректный ввод! Введите значение из меню\n')
from user_interface import get_info as gi

list_info = gi()
def writing_csv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{list_info}\n')

def writing_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {list_info[0]}\n\nИмя: {list_info[1]}\n\nОтчество: {list_info[2]}\n\nНомер телефона: {list_info[3]}\n\nОписание: {list_info[4]}\n\n\n')
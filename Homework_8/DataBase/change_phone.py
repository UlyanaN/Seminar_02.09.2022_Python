import json
import controller
from data_provider import input_name, input_number

path_to_db = 'db.json'

def change_phone_number():  
    name = input_name()
    count = 0
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in name:
            if i in data['Name']:
                count+=1
        if count == 3:
            print('Работник найден\n')
            print('Новый номер:\n')
            data['Phone number'] = input_number()
        else:
            print('Имя работника не найдено\n')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nНомер успешно изменён!\n')
    controller.user_choice()
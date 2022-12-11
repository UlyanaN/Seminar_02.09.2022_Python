import json
import controller
from data_provider import input_name as inm

path_to_db = 'db.json'

def find_person():
    
    name = inm ()
    count = 0
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in name:
            if i in data['Name']:
                count+=1
        if count == 3:
            print(f'\nРаботник найден!:\n{data}\n')
        else:
            print('Данные отсутствуют\n')
    controller.user_choice()
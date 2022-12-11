import json
import controller

path_to_db = 'db.json'

def all_db():

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in data:
            print (' '.join(data[i]))
    controller.user_choice()
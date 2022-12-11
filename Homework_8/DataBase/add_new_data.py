import json
from data_provider import input_name, input_comment, input_job_info, input_number
import controller

def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_choice()

def add_to_json():
    name = input_name ()
    phone = input_number ()
    jinfo = input_job_info ()
    comment = input_comment ()
    json_data = {
        "Name": name,
        "Phone number": phone,
        "Job info": jinfo,
        "Comment": comment,
    }
    with open("db.json", "w") as file:
        json.dump(json_data, file, indent=2, ensure_ascii=False)
    print('\n Новый сотрудник успешно добавлен!\n')
    controller.user_choice()

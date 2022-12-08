from os.path import exists
from csv_creator import creating
from data_provider import writing_csv
from data_provider import writing_txt

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_csv()
writing_txt()
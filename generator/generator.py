import random
from faker import Faker

from data.data import Person

faker_en = Faker('en')


def generated_file():
    path = rf'C:\Users\user\PycharmProjects\pythonProject2\testfile{random.randint(1, 100)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 100)}')
    file.close()
    return file.name, path


def generated_person():
    yield Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        e_mail=faker_en.email(),
        password=faker_en.password()
    )

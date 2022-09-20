from random import randint
from data.data import Person
from faker import Faker

rand = randint(1, 11)
faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        # full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        full_name=faker_ru.name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=randint(16, 42),
        salary=randint(1500, 5100),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


# def test_generated_file():
#     # path = '/home/srghei/PycharmProjects/test_framework_UI/generator/test_file.txt'
#     with open('test_file.txt', 'w') as f:
#         f.write(f'test_content\n')
#         # return f
#         print(f.name)

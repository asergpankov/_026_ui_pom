from random import randint
from data.data import Person
from faker import Faker

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


def generated_file(tmp_path):
    p = tmp_path.join("test_hello.txt")
    p.write("test_content")

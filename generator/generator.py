from random import randint

import faker.generator

from data.data import Person
from faker import Faker

rand = randint(1, 11)
faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=randint(16, 42),
        salary=randint(1500, 5100),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
        date_of_birth=faker_ru.date(),
        # subject=faker_ru.
    )



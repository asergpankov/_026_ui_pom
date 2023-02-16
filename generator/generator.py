from itertools import product
from random import randint, choice
from data.data import Person, Color, Date_and_Time, Group_Option
from faker import Faker

fake = Faker("ru_RU")
fake_eng = Faker("en_US")


# Faker.seed(0)


def person_data_generator():
    yield Person(
        full_name=fake.name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=randint(16, 66),
        salary=randint(1500, 5100),
        department=fake.job(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address(),
        mobile=fake.msisdn(),
        date_of_birth=fake.date(),
        mac_address=fake.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^', upper=True),  # 'MAC Address: CD:18:FC:9F:B6:49'
        product_number=fake.bothify(text='Product Number: ????-########', letters='ABCDE'),
        # 'Product Number: DCEB-66048764'
        # unique_int=fake.unique.random_int(min=1, max=5),
        # ipv4_private=fake.ipv4_private(), # '166.186.169.69'
        # ipv4_public=fake.ipv4_public(),
        sentence=fake.sentence(nb_words=10)
    )


def color_generator():
    yield Color(
        colors_list=["red", "Blue", "Green", "yellow", "Purple", "black", "White", "voilet", "Indigo", "Magenta",
                     "aqua"]
    )


time_15min_step = [f"{h:02d}:{m:02d}" for h, m in product(range(24), range(0, 60, 15))]


def date_and_time_generator():
    yield Date_and_Time(
        year=fake_eng.year(),
        month=fake_eng.month_name(),
        day=fake_eng.day_of_month(),
        time=choice(time_15min_step)
    )


def group_option_generator():
    yield Group_Option(
        options_list=["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2",
                      "A root option", "Another root option"]
    )

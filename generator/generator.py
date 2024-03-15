from itertools import product
from random import randint, choice
from data.data import UserData, Color, Date_and_Time, Group_Option
from faker import Faker

fake = Faker("ru_RU")
fake_eng = Faker("en_US")


# Faker.seed(0)

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

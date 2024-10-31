import string
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from itertools import product
from random import choice, sample
from typing import Any

from faker import Faker

fake = Faker("ru_RU")
fake_eng = Faker("en_US")


# Faker.seed(0)

def rand_value(): return str().join(sample(string.ascii_uppercase + string.digits, k=11))


def rand_uuid(): return str(uuid.uuid4())


def rand_hex(): return str(uuid.uuid4().hex)


@dataclass
class Color:
    colors_list: list

    @staticmethod
    def generate_data():
        yield Color(
            colors_list=["red", "Blue", "Green", "yellow", "Purple", "black", "White", "voilet", "Indigo", "Magenta",
                         "aqua"]
        )


time_15min_step = [f"{h:02d}:{m:02d}" for h, m in product(range(24), range(0, 60, 15))]


@dataclass
class Date_and_Time:
    year: str
    month: str
    day: str
    time: str

    @staticmethod
    def generate_date_and_time():
        yield Date_and_Time(
            year=fake_eng.year(),
            month=fake_eng.month_name(),
            day=fake_eng.day_of_month(),
            time=choice(time_15min_step)
        )


@dataclass
class Group_Option:
    options_list: list

    @staticmethod
    def generate_group_option():
        yield Group_Option(
            options_list=["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2",
                          "A root option", "Another root option"]
        )


@dataclass
class Some_Option:
    current_id = 0

    id: int = field(init=False)
    # id: int
    name: Any = None

    def __post_init__(self):
        print('Some_Options: post_init')
        Some_Option.current_id += 1
        self.id = Some_Option.current_id


some1 = Some_Option('some1')
some2 = Some_Option('some2')


@dataclass
class DateTime:
    hour_ago: str
    day_ago: str
    week_ago: str
    now: str
    hour_ahead: str
    day_ahead: str
    week_ahead: str

    @staticmethod
    def generate_data():
        date_repr = "%Y-%m-%dT%H:%M:%S"
        return DateTime(
            hour_ago=(datetime.now() - timedelta(hours=1)).strftime(date_repr),
            day_ago=(datetime.now() - timedelta(days=1)).strftime(date_repr),
            week_ago=(datetime.now() - timedelta(weeks=1)).strftime(date_repr),
            now=(datetime.now()).strftime(date_repr),
            hour_ahead=(datetime.now() + timedelta(hours=1)).strftime(date_repr),
            day_ahead=(datetime.now() + timedelta(days=1)).strftime(date_repr),
            week_ahead=(datetime.now() + timedelta(weeks=1)).strftime(date_repr)
        )
        # cooldown_time = datetime.now() - timedelta(hours=1)
        # print(cooldown_time.strftime("%Y-%m-%dT%H:%M:%S"))
        # fake_eng = Faker("ru_RU")

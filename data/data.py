from dataclasses import dataclass
from random import randint

from faker import Faker

fake_eng = Faker("en_US")


@dataclass
class UserData:
    full_name: str
    first_name: str
    last_name: str
    age: int
    salary: int
    department: str
    email: str
    current_address: str
    permanent_address: str
    mobile: str
    date_of_birth: str
    mac_address: str
    password: str
    product_number: str
    sentence: str

    @staticmethod
    def generate_data():
        return UserData(
            full_name=fake_eng.name(),
            first_name=fake_eng.first_name(),
            last_name=fake_eng.last_name(),
            age=randint(16, 66),
            salary=randint(1500, 5100),
            department=fake_eng.job(),
            email=fake_eng.email(),
            current_address=fake_eng.address(),
            permanent_address=fake_eng.address(),
            mobile=fake_eng.msisdn(),
            date_of_birth=fake_eng.date(),
            mac_address=fake_eng.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^', upper=True),
            # 'MAC Address: CD:18:FC:9F:B6:49'
            product_number=fake_eng.bothify(text='Product Number: ????-########', letters='ABCDE'),
            # 'Product Number: DCEB-66048764'
            password=fake_eng.bothify(text='?????##?##?##', letters='ABCDE!@#$%^&zxc'),
            # unique_int=fake_eng.unique.random_int(min=1, max=5),
            # ipv4_private=fake_eng.ipv4_private(), # '166.186.169.69'
            # ipv4_public=fake_eng.ipv4_public(),
            sentence=fake_eng.sentence(nb_words=10)
        )


@dataclass()
class Color:
    colors_list: list


@dataclass
class Date_and_Time:
    year: str
    month: str
    day: str
    time: str


@dataclass
class Group_Option:
    options_list: list

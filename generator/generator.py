from random import randint
from data.data import Person
from faker import Faker

fake = Faker("ru_RU")
Faker.seed(4)


def generate_person_data():
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
        mac_address=fake.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^', upper=True), # 'MAC Address: CD:18:FC:9F:B6:49'
        product_number=fake.bothify(text='Product Number: ????-########', letters='ABCDE'), # 'Product Number: DCEB-66048764'
        # unique_int=fake.unique.random_int(min=1, max=5),
        # ipv4_private=fake.ipv4_private(), # '166.186.169.69'
        # ipv4_public=fake.ipv4_public(),
        # subject=faker_ru.
    )



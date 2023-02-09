from dataclasses import dataclass


@dataclass
class Person:
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
    product_number: str
    sentence: str

@dataclass()
class Color:
    colors_list: list

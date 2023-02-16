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


@dataclass
class Date_and_Time:
    year: str
    month: str
    day: str
    time: str


@dataclass
class Group_Option:
    options_list: list

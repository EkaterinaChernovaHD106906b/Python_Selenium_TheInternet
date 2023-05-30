from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    e_mail: str = None
    password: str = None

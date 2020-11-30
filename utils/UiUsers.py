from dataclasses import Field, dataclass
from datetime import datetime
from random import random


@dataclass
class UiUsers(object):
    name: str
    surname: str
    gender: str
    email: str
    passwords: str
    street_address: str
    zip_code: str
    city: str
    phone_number: str
    date_of_birth: str

    @property
    def day_of_birth(self):
        return self.date_of_birth[:2]

    @property
    def month_of_birth(self):
        return self.date_of_birth[3:4]

    @property
    def year_of_birth(self):
        return self.date_of_birth[4::]

    @property
    def generate_email(self):
        return self.name + '.' + self.surname + str(datetime.now().strftime("%H:%M:%S")).replace(':','.') + '@gmail.com'

Male_user = UiUsers('Mark', 'Whalberg', 'male', 'mark.whalberg@gmail.com', '123456', '66th Street', '65301','Humphreys', '735456773', '10081979')
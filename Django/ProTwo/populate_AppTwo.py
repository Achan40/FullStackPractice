import os

# configures settings for project
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# Fake population script
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for i in range(N):

        # Create fake data for that entry
        # This uses the faker module
        fake_name = fakegen.name().split()
        fake_first = fake_name[0]
        fake_last = fake_name[1]
        fake_email = fakegen.email()

        # Create new entry
        user = User.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)[0]

if __name__ == "__main__":
    print("Populating Script")
    populate(20)
    print("Populating Complete")
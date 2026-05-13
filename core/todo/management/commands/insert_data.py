from faker import Faker
from django.core.management.base import BaseCommand
import random
from datetime import datetime

from accounts.models import User, Profile
from todo.models import TaskModel, Priority

priority_list = [('Low', 1), ('Medium', 2), ('High', 3)]

class Command(BaseCommand):
    help = 'inserting dummy data'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),password="a/@1234567")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for key, value in priority_list:
            Priority.objects.get_or_create(title=key, level=value)

        for _ in range(5):
            TaskModel.objects.create(
                author = profile,
                title = self.fake.paragraph(nb_sentences=1),
                description = self.fake.paragraph(nb_sentences=10),
                completed = random.choice([True,False]),
                priority = Priority.objects.get(title=random.choice(['Low','Medium','High'])),
                created_date = datetime.now()
            )
from django.core.management.base import BaseCommand
from mainapp.models import *
from authapp.models import Person

JSON_PATH = 'mainapp/json'


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        # Create superuser
        super_user = Person.objects.create_superuser('skilldiary', 'root@localhost.local', '')

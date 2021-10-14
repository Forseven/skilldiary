from django.core.management.base import BaseCommand

from authapp.models import *
from skilldiary.settings import BASE_DIR

JSON_PATH = 'mainapp/json'


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        # Create superuser
        print(f'{BASE_DIR}/mainapp/data/city.txt')
        with open(f'{BASE_DIR}/mainapp/data/city.txt',"r")as file:
            citys = file.readlines()
            for city in citys:
                City.objects.get_or_create(name=city)

            file.close()

       # super_user = Person.objects.create_superuser('skilldiary', 'root@localhost.local', '')

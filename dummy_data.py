import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker

import random 

from product.models import Brand,Product



def seed_brand(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brands/{images[random.randint(0,11)]}'
        )
    print(f'Seed {n} brands')
       
    





def seed_product(n):
    pass



seed_brand(5)
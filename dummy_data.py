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
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg']
    flags = ['New','Sale','Feature']

    for _ in range(n):
        Product.objects.create(
            name = fake.name() ,
            image = f'brands/{images[random.randint(0,11)]}' ,
            flag = flags[random.randint(0,1)] ,
            price = round(random.uniform(20.99,99.99),2),
            sku = random.randint(1000,1000000),
            subtitle = fake.text(max_nb_chars=250),
            description = fake.text(max_nb_chars=2500),
            quantity = random.randint(0,30) ,
            brand = Brand.objects.get(id=random.randint(1,105))
           )
        
        
        
    print(f'Seed {n} products')
  

seed_product(1000)
# seed_brand(100)
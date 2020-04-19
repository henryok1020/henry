# Your next car
import random

colors = ['Red', 'Blue', 'Black', 'Pink', 'Yellow', 'Green']
cars = ['lambo', 'ferrari', 'maserati', 'porsche', 'bently']
color = random.choices(colors, k=1)
brand = random.choices(cars, k=1)
print(color, brand)

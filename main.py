from car import Car as Vehicle, CarWithOdometer
from console_input import test_console_input

#
# Lists
#

family = ['martin', 'patti']
print(f"Last family member: {family[-1].lower()}")
family.append('alan')
print(f"Appended a member to family: {family[-1].upper()}")
print(f"First family member: {family[0].title()}")
family.reverse()
print(f"Reversed family: {family}")
family.sort()
print(f"Sorted family: {family}")
family.sort(reverse=True)
print(f"Reverse sorted family: {family}")
for member in family:
    print(f"Hello, {member.title()}!")

print(f"Odd numbers: {list(range(2, 21, 2))}")
numbers = [v for v in range(1, 1_000_001)]
print(f"Sum of a million: {sum(numbers)}")
print(f"Cubes: {[f"{v}**3 = {v**3}" for v in range(1, 11)]}")
cities = ["Dresden", "Berlin", "Hamburg", "Frankfurt", "Dortmund"]
print(f"Städte: {cities[:2]} {cities[1:3]} {cities[2:]} {cities[-2:]}")
copy_of_cities = cities[:]
new_city = "Köln"
cities.append(new_city)
print(f"Die letzten beiden Städte: {cities[-2:]}")
print(f"Original Städte: {copy_of_cities}")

#
# Ii statements
#

if new_city not in copy_of_cities:
    print(f"Die Original-Städte wurden erfolgreich gesichert!")

empty_list = []
for v in empty_list:
    print("Hallo!")
if not empty_list:
    print("Liste ist leer")

#
# Dictionaries
#

alien_0 = {'color': 'grün', 'speed': 2, 'points': 100}
alien_1 = {}
print(f"Das erste Alien ist {alien_0['color']}")
alien_1['speed'] = 5
print(f"Das zweite Alien ist {alien_1.get('color', 'von unbekannter Farbe')}")
glossary = {
    'list': 'Stores a dynamic number of values.',
    'if statement': 'Conditional execution of a code block.',
    'for loop': 'Calls a block of code for each value in a range.',
    'dictionary': 'Stores a dynamic number of key-value pairs.',
    'tupel': 'Stores a fixed set of values.'
}
print('Glossary:')
for key, value in sorted(glossary.items()):
    print(f"  {key.title()}:\n    {value}")

print('Glossary keys:', end='')
for key in glossary:
    print(f' "{key}"', end='')

test_console_input(False)


class ElectricCar(CarWithOdometer):
    def __init__(self, vendor, brand, capacity):
        super().__init__(vendor, brand)
        self.capacity = capacity

    def print_label(self):
        super().print_label()
        print(f"  Capacity: {self.capacity}, Odometer reading: {self.odometer_reading}")


my_cars = [ElectricCar("VW", "Golf", "2000KW"), Vehicle("Audi", "A4")]
my_cars[0].raise_odometer(139)
my_cars[0].print_label()
my_cars[1].print_label()

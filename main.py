import random


class Person:
    def __init__(self, name):
        self.name = name
        self.age = random.randint(0, 100)


# people = [
#     Person("Nikita"),
#     Person("Daniil"),
#     Person("Marry"),
#     Person("Sonya"),
#     Person("Ekaterina"),
#     Person("Artem")
# ]
# 
# old = []
# young = []
# 
# for person in people:
#     if person.age > 50:
#         old.append(person)
#     else:
#         young.append(person)
# 
# for person in old:
#     print(person.name, person.age)
# 
# print()
# 
# for person in young:
#     print(person.name, person.age)

people = [
    "Nikita", "Daniil", "Marry",
    "Sonya", "Ekaterina", "Artem"
]

old = []
young = []

number = int(input("Enter number of people: "))

for num in range(number):
    person = Person(people[random.randint(0, 5)])

    if person.age > 50:
        old.append(person)
    else:
        young.append(person)

for person in old:
    print(person.name, person.age)

print()

for person in young:
    print(person.name, person.age)

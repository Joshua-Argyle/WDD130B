youngest = 100
youngest_name = ""
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
for person in people:
    person = person.split(" ")
    age = int(person[1])
    name = person[0]
    if age < youngest:
        youngest = age
        youngest_name = name
print(youngest_name)

    
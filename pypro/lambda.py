people = [
    {"name":"Harry","House":"Gryffindor"},
    {"name":"Cho","House":"Ravenclaw"},
    {"name":"Draco","House":"Slytherin"},
    {"name":"Daenerys","House":"Targaryen"},
]

'''def f(person):
    return person["name"]'''


people.sort(key=lambda person: person["name"])
print(people)
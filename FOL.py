humans = ["Socrates", "Plato", "Aristotle"]

male = ["Socrates", "Plato"]
female = ["Hypatia"]

parents = {
    "Socrates": "Plato",
    "Plato": "Aristotle"
}

def is_human(x):
    return x in humans

def is_mortal(x):
    if is_human(x):
        return True
    return False

print("First Order Logic Facts\n")

for person in humans:
    print(person, "is Human:", is_human(person))
    print(person, "is Mortal:", is_mortal(person))
    print()

print("Parent Relationships\n")

for child,parent in parents.items():
    print(parent, "is parent of", child)

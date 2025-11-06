class Grandfather:
    eye_color = "Blue"
    hair_color = "Black"
    favorite_food = "Pizza"
    musician = "None"

    def __init__(self):
        self.skin_color = None   # Default / Not Defined


class Child(Grandfather):
    hair_color = "Light Grey"
    favorite_food = "Pizza"
    musician = "Atif Aslam"

    def __init__(self):
        self.skin_color = "Fair"   # Child chooses independently


class Grandchild(Child):
    favorite_food = "Burger"
    musician = "Kawish"

    def __init__(self):
        self.skin_color = "Fair"   # Same as child


grandfather = Grandfather()
child = Child()
grandchild = Grandchild()


print("\n Grandfather:")
print("Eye:", grandfather.eye_color)
print("Skin:", grandfather.skin_color)
print("Hair:", grandfather.hair_color)
print("Food:", grandfather.favorite_food)
print("Musician:", grandfather.musician)

print("\n Child: ")
print("Eye:", child.eye_color)
print("Skin:", child.skin_color)   # independently choose
print("Hair:", child.hair_color)
print("Food:", child.favorite_food)
print("Musician:", child.musician)

print("\n Grandchild: ")
print("Eye:", grandchild.eye_color)
print("Skin:", grandchild.skin_color) # same as child
print("Hair:", grandchild.hair_color)
print("Food:", grandchild.favorite_food)
print("Musician:", grandchild.musician)
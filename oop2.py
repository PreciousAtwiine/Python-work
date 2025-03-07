class Animal():
    name = ""
    type = ""
    age = 0
    gender = ""
    color = ""
    sound = ""
    speed = ""
    
dog = Animal()
dog.name = "Dog"
dog.type = "Domestic"
dog.age = 10
dog.gender = "Female"
dog.color = "Brown"
dog.sound = "Bark"
dog.speed = "moderate"

cat = Animal()
cat.name = "Cat"
cat.type = "Domestic"
cat.age = 3
cat.gender = "Male"
cat.color = "Grey"
cat.sound = "Meow"
cat.speed = "moderate"

cow = Animal()
cow.name = "Cow"
cow.type = "Domestic"
cow.age = 5
cow.gender = "Female"
cow.color = "Black and white"
cow.sound = "Moo"
cow.speed = "moderate"

lion = Animal()
lion.name = "Lion"
lion.type = "Wild"
lion.age = 11
lion.gender = "Male"
lion.color = "Brown"
lion.sound = "Roar"
lion.speed = "Fast"

#The dot operator is used to access the properties,characteristics of the object
print(lion.name)
print(f"cow: {cow.name}-{cow.sound}")

    
    
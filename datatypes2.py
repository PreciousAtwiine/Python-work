#sequence
num1, num2, num3, = 100,300,500
numbers = [100, 300, 500]
numbers1 = [num1, num2, num3]
numbers2 = []
my_things = [100, "hello", 3.14, True, [1,2,3]] #
print(type(my_things))
print(type(num1))
print(my_things[1])
print(my_things[4][2])
trouble= [20,[20,[100,20,[500]]]]
print(trouble[1][1][2][0])

trouble.append(40)

print(trouble)
trouble.pop()
print(trouble)
#tuples are read only sequences
mytuple = (100, 300, 500)

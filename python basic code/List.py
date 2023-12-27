fruits = ['Apples','Banana','Mango','Grapes','Strabery','Apples']
years = [3,"1984",203,63,"1982"]
print(fruits,years)
print("Apples" in fruits)
print("Apple" in fruits)
print(fruits.count("Apples"))
print(fruits.count("Mango"))
print(fruits.index("Apples"))
print(fruits.index("Banana"
                   ""))

"""
fruits.append("Pineapple")
print(fruits)


fruits.extend(years)
print(fruits)

fruits.remove("Mango")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

numbers = [5,96,4,1,6,36,96]
numbers.sort()
print(numbers)
"""


numbers = [20,30,35,45,90,95]
numbers.append(12)
print(numbers)

numbers = [20,30,35,45,90,95]
numbers.insert(0,23)
print(numbers)

numbers = [20,30,35,45,90]
numbers.remove(30)
print(numbers)

numbers = [20,30,35,45,90]
numbers.clear()
print(numbers)

numbers = [20,30,35,45]
numbers.pop()
print(numbers)

numbers = [20,30,35,45,90]
print(numbers.index(30))

numbers = [20,30,35,45,90]
print(50 in numbers)

numbers = [20,30,35,45,90,20,30,20]
print(numbers.count(20))
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [20,30,35,45]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)


fruits = {'Apple':14,'Banana':12,'straberry':6}
print(fruits.get('Apple'))
print(fruits.items())
print(fruits.keys())

print(fruits.popitem())

print(fruits.setdefault("hanugalu"))
print(fruits)
print(fruits.setdefault("Avacardo",20))
print(fruits)
print(fruits)

new_item = {"chair":12,"Table":5}
fruits.update(new_item)
print(fruits)
print(fruits)

up_new = {'biscate5050':10 , 'Darkfantacy':23}
fruits.update(up_new)
print(fruits)

fruits.update(biscate5050 = 23)
print(fruits)

customer = {
            "name": "Mosh",
            "age": 16,
            "Address": 20.
           }
print(customer.get("Birthdaty","Jan 1 1986"))

phone = input("Phone:")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
print()

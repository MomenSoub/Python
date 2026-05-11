fruits = [
    "Orange", 
    "Apple",
    "Banana",
    "Grape",
    "Orange",
    "Banana",
    "Orange"
    ]

def removeDuplicate():
    return list(set(fruits))

new_list = removeDuplicate()
print(new_list)
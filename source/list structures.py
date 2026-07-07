my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[9])
my_list[9] = 10
print(my_list[9]) 

my_tuple=(0,1,2,3,4,5,6,7,8,9)
print(my_tuple[2])
my_dictionary={
    "key1": 1,
    "key2": "my value",
    "key3": True,
    "key4": [1,2,3,4,5],
}
print(my_dictionary["key1"])
print(my_dictionary)

#$ SETs
cars={"audi","bmw","mercedes"}
print(cars)
cars.add("toyota")
print(cars)
cars.add("audi")
print(cars)

for values in my_dictionary.values():
    print("dic: " + str(values))

for index, value in enumerate(my_dictionary.values()):
    print("index: " + str(index) + " value: " + str(value))

    

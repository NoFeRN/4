my_dict={"Alina": 20,"Misha":22,"Oskar":19}
print(my_dict)
print(my_dict["Alina"])
print(my_dict.get("Katya"))
my_dict.update({"Roman": 21,
                "Artem": 27})
print(my_dict)
bag=my_dict.pop("Misha")
print(bag)
print(my_dict)
my_set={1,2,2,3,4,5,4,6,3,4,2,1,1,2,3,5,6,5,6}
print(my_set)
my_set.update([8,17])
my_set.discard(2)
print(my_set)
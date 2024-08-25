# Работа со словарями:

my_dict = {"Andrey": 1999, "Roma": 2001, "Valeriya": 2003}
print(my_dict)
print(my_dict.get("Andrey"))
print(my_dict.get("Maxim"))
my_dict.update({"Konstatin": 1980, "Alena": 1995})
a = my_dict.pop("Roma")
print(a)
print(my_dict)

#Работа с множествами:

my_set = {1,2,2,2,4,4,"Andrey",5,"Andrey", 6.5}
print(my_set)
my_set.add((7,8,9))
my_set.add("Anastasiya")
my_set.remove("Andrey")
print(my_set)
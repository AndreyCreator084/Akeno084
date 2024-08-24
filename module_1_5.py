# Задайте переменные разных типов данных:
#immutable_var = 1, 2, 3.5, "Привет", False
#print(immutable_var)
#immutable_var[3] = "Пока" # 'tuple' object does not support item assignment - ошибка потому что кортеж не поддерживает обращение по элементам
#print(immutable_var)

#Создание изменяемых структур данных:
mutable_list = [1, 2, 3.5, "Hello", False]
mutable_list.append("Urban")
mutable_list[5] = "university"
mutable_list[2] = 3
print(mutable_list)


# print() вывододит данные на экран
print("hello world!") # двойные кавычки
print("hello world") # одинарная кавычка
print(2026)
# короткий комментарий
''' длинный коментарий '''
# переменные
name = " Олег"
print("воин", name)
print(f"Воин {name}")
num1= 5
num2 = 10
total = num1 + num2
print(total)

num = 7
print(num)
num = 10
print(num)

# Правила наименования переменных
# только латинкские символы a-z A-Z
# цифры можно использовать, но не на первой позиции
# разрешон символ _
client1 =1
client2 = 2
# 1car = 5 ошибка
#нельзя использовать зарезервирование слова
# print = 10 нельзя


# snake_case - рекомендован
client_name ='Иван'
ticket_price = 250

#camelCase
clientName = 'иван'
ticketPrice = 200

# Типы данных - у каждого своё предназначение
# integer / int / целое число
my_int = 10
print(my_int, type(my_int))

#float / float / дробное число
my_float = 3.14
print(my_float, type(my_float))

# string / str / строка
my_str_1 = 'hello1'
my_str_2 = "hello2"
print(my_str_1, type(my_str_1))
my_str_3 = "Иван сказал: '...'"
print(my_str_3, type(my_str_3))

#boolean / bool / логический тип
my_bool_1= True
print(my_bool_1, type(my_bool_1))
my_bool_2= False
print(my_bool_2, type(my_bool_2))

# list / list / список - хранит упорядочные значения
my_list = ["Иван", "Алан"]
print(my_list, type(my_list))

# tuple / tuple / кортеж - после создания нельзя изменить
my_tuple = (19,'hello', 3.9)
print(my_tuple, type(my_tuple))

# set/ set/ множества - хранит только уникальные значения
my_set = {"иван"," 25"}
print(my_set, type(my_set))

#dictionary / dict / словарь
my_dict = {'name': 'егор', 'age': 25}
print(my_dict, type(my_dict))

# input()- считывает введеные значения
name = input('Введите имя:')
print(name, type(name))
# проблема с типами данных
num1 = int(input('введите первое число:'))
num2 = input('введите второе число:')
num2 = int(num2)
print(num1 + num2)
# множество присваивание
num1, num2 = 5, 6

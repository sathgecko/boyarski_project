import itertools

numbers = [num for num in range(1, 10)]
for item in itertools.combinations(numbers, 4):
    print(item)

# import requests
# from lxml import html
#
# """получает список всех подзаголовков сайта (теги h3)"""
#
# url = 'http://www.columbia.edu/~fdc/sample.html'
# response = requests.get(url).text
# h3 = html.fromstring(response).xpath('//h3')
# print('Список тегов h3 на данном сайте:\n')
# if h3:
#     for element in h3:
#         print(element.text)
# else:
#     print('Тегов h3 на данном сайте нет')

# import itertools
# """переберёт все возможные коды в диапазоне 0-9 """
# pin_code = itertools.product(range(10), repeat=4)
# print('Результат работы программы:')
# for number in pin_code:
#     print(*number)

# import re
# phones_list = ['8999999999', '999999-999', '99999x9999']
# """
#     Проверяет каждый номер из списка на соответствие критериям и выводит на экран
#     Длина номера — ровно 10 знаков.
#     Номер начинается с цифры 8 или с цифры 9.
#     Остальные знаки — только цифры.
#     """
# for index, phone in enumerate(phones_list):
#     phone_check = re.findall(r'[8-9]\d{9}', phone)
#     if phone_check:
#         print(f'C номером {index + 1} все в порядке: {phone_check}')
#     else:
#         print(f'Номер {index + 1} не подходит')

# import requests
# import json
# from typing import Callable, List, Dict
#
# def home(home_url: str) -> Callable:
#     """по URL домашней планеты возвращает название планеты из ключа name"""
#     # print(home_url)
#     home_planet = requests.get(home_url)
#     if home_planet.status_code == 200:
#         home_read = json.loads(home_planet.text)
#         for key, value in home_read.items():
#             # print(value)
#             if key == 'name':
#                 return value
#     else:
#         print(f'Возвращен код: {home_planet.status_code}')
#
# def get_pilots(pilots_url_list: str) -> Callable:
#     """Проходит циклом по списку URL пилотов и добавляет в список pilots_list словари
#         с заданными ключами"""
#     # print(pilots_url_list)
#     pilots_list: List = list()
#     for url in pilots_url_list:
#         # print(url)
#         pilot_num = requests.get(url)
#         if pilot_num.status_code == 200:
#             pilot_read = json.loads(pilot_num.text)
#             pilots_dict: Dict = {}
#             for key, value in pilot_read.items():
#                 # print(value)
#                 if key == 'name' or key == 'height' or key == 'mass':
#                     pilots_dict[key] = value
#                 elif key == 'homeworld':
#                     # print(value)
#                     pilots_dict['homeworld_url'] = value
#                     """возвращаем из функции название планеты"""
#                     pilots_dict['homeworld'] = home(value)
#                     # count += 1
#             pilots_list.append(pilots_dict)
#         else:
#             print(f'Возвращен код: {home_planet.status_code}')
#     return pilots_list
#
# def get_ship(url: str) -> Callable:
#     """Парсит URL с кораблем, формирует словарь с заданными параметрами
#         записывает в файл и выводит на экран"""
#     falcon_dict: Dict = dict()
#     falcon = requests.get(url)
#     if falcon.status_code == 200:
#         falcon_read = json.loads(falcon.text)
#         for key, val in falcon_read.items():
#             if key == 'name' or key == 'max_atmosphering_speed' or key == 'starship_class':
#                 falcon_dict[key] = val
#             elif key == 'pilots':
#                 # get_pilots(val)
#                 falcon_dict[key] = get_pilots(val)
#         print(json.dumps(falcon_dict, indent=4, sort_keys=True))
#     else:
#         print(f'Возвращен код: {falcon.status_code}')
#     with open("falcon_pilots.json", "w") as file:
#         json.dump(falcon_dict, file, indent=4)
#
# get_ship("https://swapi.dev/api/starships/10/")



import re
auto_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

# # result_private = re.findall('\D\d+\D{2}\d+\s+', auto_numbers)
# # result_taxi = re.findall('\D{2}\d{3}\d+\s+', auto_numbers)
# result_private = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', auto_numbers)
# result_taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', auto_numbers)
#
# """в перечне номеров находит номера частных автомобилей и номера такси
#     У частных легковых автомобилей номера — это буква, три цифры, две буквы,
#     затем две или три цифры с кодом региона.
#     У такси — две буквы, три цифры, затем две или три цифры с кодом региона."""
#
# print(f'Список номеров частных автомобилей: {result_private}')
# print(f'Список номеров такси: {result_taxi}')

# import re
# text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
# Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
# nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
# Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate
# """
# result = re.findall(r"\b[a-zA-Z]{4}\b", text)
# """обрабатывает этот текст и выводит список слов, состоящих ровно из четырёх букв"""
# print(result)

# import requests
# import json
#
#
# result = requests.get("https://swapi.dev/api/people/3/") # https://swapi.dev/api/planets/8/
# """ программа, которая парсит данные об этом человеке,
#     изменяет его имя на ваше собственное и сохраняет результат в виде JSON-файла."""
#
# if result.status_code == 200:
#     json_dict = json.loads(result.text)
#     json_dict['name'] = input("Введите имя: ")
#     with open("swap.json", "w") as file:
#         json_text = json.dump(json_dict, file, indent=4)
#
#
# # Доп:
# result_homeworld = requests.get(json_dict['homeworld'])
# print(result_homeworld.text)

# lambda x: x % 2 возвращает результат остатка от деления - ноль или единица. Ноль это всегда False, а единица True
#
# Допустим строчка abbcba
# 1) Counter(string) создаст словарик {'b': 3, 'a': 2, 'c': 1}
# 2) Counter(string).values() вернет [3, 2, 1]
# 3) При использовании filter выборка происходит согласно условию в lambda  функции. Если результат остатка от деления будет True или единица, то число будет взято.
# 3 % 2 = 1 - число будет взято
# 2 % 2 = 0 - число будет пропущено
# 1 % 2 = 1 - число будет взято
# 4) В результате от list(filter(lambda x: x % 2, Counter(string).values() )) получим список [3, 1]
# 5) Нужно сделать сравнение длины списка, но сравнивать нужно с единицей. Потому что из строк вроде "abbcba" палиндром получить нельзя.

# import re
#
# # найти список всех дат, которые встречаются в строке
# text5 = "Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"
#
# result = re.findall(r"\d{2}-\d{2}-\d{4}", text5) # \d Любая цифра [0-9] (\D — все, кроме цифры)
# # дата состоит из цифр: 2-2-4
# print(result)

# text4 = 'Even if they are djinns, I will get djinns that can outdjinn them.'
# result_1 = re.findall(r'\b[aeiouAEIOU]\w*', text4) # найти все слова на гласные знак * все буквы
# print("Слова на гласную:", result_1)
# result_2 = re.findall(r"\b[^aAeEiIoOuUyY\W]\w*", text4) # найти все слова кроме гласных \W — все, кроме буквы или цифры
# print("Слова на любой символ, кроме гласной:", result_2)

# nemo_pattren = r'[Nn]em\w{0, 2}'# паттерн слово начинается на большую или маленькую букву и заканчивается до 2 символов
# transparent = re.sub(r'[Oo]\w{4}\s+', '', deep_ocean) # найти и заменитб на пробелы все слова на Оо и 4 символа после них
# если нужно удалить пробелы, поставить символ \s+

# text3 = 'AV simple AV'
# result = re.findall(r'.', text3) # найти все символы включая пробелы
# print(result)
# result = re.findall(r'\w', text3) # найти все символы без пробелов
# print(result)
# result = re.findall(r'\w+', text3) # найти все слова
# print(result)
#
# result = re.findall(r'\b[aeiouAEIOU]\w+', text3) # найти все слова, кооторые начинаются на гласные символ \b указывает на начало подстроки
# print(result)

# text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
# result = re.match(r'wo', text) # поиск в начале строки
# print(result)
#
# pattern = re.compile(r'wo') # присвоить искомое знаение (паттерн)
# print(pattern.search(text)) # поиск первого упоминания в тексте
#
# result = re.search(r'wo', text)
# print(result.group(0)) # вывести содержимое поиска
# print(result.start()) # начало искомого
# print(result.end()) # конец искомого
# result = re.findall(r'wo', text) # найти все упоминания в тексте
# print(result)
# result = re.sub(r'wo', 'ЗАМЕНА', text) # заменить шаблон на другой
# print(result)
#
# text2 = r'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
# result = re.findall(r'\\wwood\+\?,', text2) # если найти спец символы, поставить слэш перед ними
# print(result)





# from collections import Counter # возвращает словарь ключ-символ, значение - количество
#
# def can_be_poly(string: str) -> bool:
#     """ функция can_be_poly, которая принимает на вход строку
#         и проверяет, можно ли получить из неё палиндром """
#     # return len(string) % 2 == sum(x % 2 for x in Counter(string).values())
#     return len(list(filter(lambda x: x % 2, Counter(string).values()))) <= 2
#     # return list(filter(lambda x: x % 2, Counter(string).values()))
#
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))

# # функция генератор простых чисел
# def get_prime_numbers(n):
#     """ функция генератор простых чисел"""
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
# print(*get_prime_numbers(1000))
#
# """генератор простых чисел в одну строку"""
# print(*[n for n in range(1000) if n >= 2 and (n == 2 or n % 2 and all(n % i for i in range(3, int(n ** 0.5) + 1, 2)))])


# from typing import List
# from functools import reduce
# 
# floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
# 
# """ Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой"""
# result = map(lambda x: round(x ** 3, 3), floats)
# print(list(result))
# 
# """Из списка names берутся только те имена, в которых есть минимум пять букв """
# 
# result = filter(lambda elem: len(elem) >= 5, names)
# print(list(result))
# 
# """ Из списка numbers берётся произведение всех чисел """
# def my_add(a: int, b: int) -> int:
#     return a * b
# result = reduce(my_add, numbers)
# print(result)
#
# 
# # # содержимое испортируемого файла
# # def test():
# #     print('тут что-то происходит')
# #
# # if __name__ == '__main__':
# #     test()
# #     print('Основной код')
# # else:
# #     print(f'Импортирован модуль{test.__name__}')
# # # содержимыое основного файла
# # import test_module
# # test_module.test()
# 
# # from functools import reduce
# # from typing import List
# #
# # def my_add(a: int, b: int) -> int:
# #     result = a + b
# #     print(f"{a} + {b} = {result}")
# #     return result
# #
# # numbers: List[int] = [0, 1, 2, 3, 4]
# #
# # print(reduce(my_add, numbers))
# #
# # # Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке
# # sentences = ["Nory was a Catholic", "because her mother was a Catholic",
# #              "and Nory’s mother was a Catholic", "because her father was a Catholic",
# #              "and her father was a Catholic", "because his mother was a Catholic", "or had been"]
# #
# # def check_was(a, b):
# #     if isinstance(a, str):  # обработаем первый элемент отдельно
# #         a = int(a.count('was'))
# #     result = a + int(b.count('was'))
# #     return result  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка
# #
# # print(f'Слово was встречается в тексте, раз: {reduce(check_was, sentences)}')
# 
# # # map сортирует строку из цифр
# # nums = '5 8 4 1 0 3'
# # result = sorted(map(int, nums.split(' ')))
# # print(result)
# # # фильтр убирает из строки большие буквы и цифры
# # text = 'qWe456rtY'
# # result2 = filter(lambda x: not (x.isupper() or x.isdigit()), text)
# # print(list(result2))
# 
# ## функции map filter
# # import random
# #
# # def from_string(date: str) -> 'Date':
# #     day, month, year = map(int, date.split('-'))
# #     print(day, month, year)
# #
# # from_string('10-12-2077')
# #
# # list1 = [random.randint(0, 10) for i in range(10)]
# # list2 = [random.randint(0, 10) for i in range(10)]
# # print(list1)
# # print(list2)
# #
# # result = list(map(lambda x, y: x + y, list1, list2))
# #
# # result_even = filter(lambda x: x % 2 == 0, result)
# # print(max(result_even))
# 
# 
# # # список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.
# # class Person:
# #     def __init__(self, name, age):
# #         self._name = name
# #         self._age = age
# #
# #     @property
# #     def name(self):
# #         return self._name
# #
# #     @property
# #     def age(self):
# #         return self._age
# #
# #     @age.setter
# #     def age(self, value):
# #         self._age = value
# #
# #     @name.setter
# #     def name(self, word):
# #         self._name = word
# #
# #     def __repr__(self):
# #         return f"({self.name}, {self.age})"
# #
# #
# # first = Person("Max", 29)
# # second = Person("Christine", 21)
# # third = Person("Anthony", 35)
# # humans = [first, second, third]
# # print(humans)
# # humans.sort(key=lambda x: x.age)
# # print(humans)
# # humans.sort(key=lambda x: -x.age)
# # print(humans)
# 
# 
# ## вывод значений через lambda
# # grades = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
# # {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
# # {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
# # {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
# # {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
# # {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
# # {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
# # {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
# # ]
# 
# # print(sorted(grades, key=lambda dict: int(dict['score'])))
# # # Решение через key
# # print(max(grades, key=lambda x: x["score"]))
# # print(min(grades, key=lambda x: x["score"]))
# # # Вывод исключительно очков:
# # print(max(grades, key=lambda x: x["score"])['score'])
# # print(min(grades, key=lambda x: x["score"])['score'])
# # 
# # # Решение через map, который будет изучен в следующем модуле
# # print(list(map(lambda x: x['score'], grades)))  # для наглядности
# # print(max(map(lambda x: x['score'], grades)))
# # print(min(map(lambda x: x['score'], grades)))
# 
# # test = 1
# # def f1():
# #     print(test)
# #     test = 7
# #     print(test)
# # f1()
# 
# # def f2():
# #     test = 2
# #     print(test)
# #     if test not in globals():
# #         raise Exception
# #     if test not in locals():
# #         raise Exception
# # f2()
# 
# # def func():
# #     var = 1
# #     def f3():
# #         par = 2
# #         if 'var' not in locals():
# #             raise Exception
# #         print('var' in locals())
# #
# #     f3()
# #
# #
# #     def f4():
# #         par = 3
# #         print(var)
# #         if 'var' not in locals():
# #             raise Exception
# #     f4()
# #
# #     def f5():
# #         var = 4
# #         par = 4
# #         print(var)
# #         if 'var' not in globals():
# #             raise Exception
# #     f5()
# 
# 
# 
# 
# # from typing import Callable, Any
# # import functools
# #
# # global_count = {}
# # global_count_list = []
# # count = 0
# #
# # def counter(func: Callable) -> Callable:
# #     """
# #     :param func: Декоратор
# #     :return: считающий и выводящий количество вызовов декорируемой функции в глобальную область видимости
# #     """
# #
# #     @functools.wraps(func)
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         # wrapped_func.count += 1
# #         global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
# #         global_count_list.append(1)
# #         global count
# #         count += 1
# #         return func(*args, **kwargs)
# #
# #     # wrapped_func.count = 0
# #     return wrapped_func
# #
# # @counter
# # def test():
# #     print('<Тут что-то происходит...>')
# # test()
# # test()
# # test()
# # test()
# #
# # print(f'Количество вызовов функции (словарь): {global_count}')
# # print(f'Количество вызовов функции (счетчик): {count}')
# # print(f'Количество вызовов функции (список): {len(global_count_list)}')
# # print('*' * 100)
# # print(dir('.')) # перечисляет все функции и методы,
# # # находящиеся во встроенном пространстве имён в Python
# 
# # import functools
# # from typing import Callable
# # 
# # def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable)-> Callable:
# #     """ Декоратор. Даёт возможность другому декоратору принимать произвольные аргументы """
# #
# #     def decorator_maker(*args, **kwargs) -> Callable:
# #         def decorator_wrapper(func: Callable) -> Callable:
# #             return decorator_to_enhance(func, *args, **kwargs)
# #         return decorator_wrapper
# #     return decorator_maker
# #
# # @decorator_with_args_for_any_decorator
# # def decorated_decorator(func: Callable, *args, **kwargs):
# #     """Декаротор. Шаблон"""
# #
# #     @functools.wraps(func)
# #     def wrapper(*func_args, **func_kwargs) -> Callable:
# #         print("Переданные арги и кварги в декоратор:", args, kwargs)
# #         return func(*func_args, **func_kwargs)
# #
# #     return wrapper
# #
# # @decorated_decorator(100, 'рублей', 200, 'друзей')
# # def decorated_function(text: str, num: int) -> None:
# #     print("Привет", text, num)
# #
# #
# # decorated_function("Юзер", 101)
# 
# # import functools
# # def singleton(cls):
# #     """ декоратор singleton, который превращает класс в одноэлементный"""
# #     @functools.wraps(cls)
# #     def wrapper_singleton(*args, **kwargs):
# #         if not wrapper_singleton.instance:
# #             wrapper_singleton.instance = cls(*args, **kwargs)
# #
# #     wrapper_singleton.instance = None
# #     return wrapper_singleton
# #
# # @singleton
# # class Example:
# #     pass
# #
# # my_obj = Example()
# # my_another_obj = Example()
# #
# # print(id(my_obj))
# # print(id(my_another_obj))
# #
# # print(my_obj is my_another_obj)
# 
# 
# # from typing import Callable, Any, Optional
# # import time
# # from datetime import datetime
# #
# # def timer(cls, func, date_format):
# #
# #     def wrapped(*args, **kwargs):
# #         format = date_format
# #         for sym in format:
# #             if sym.isalpha():
# #                 format = format.replace(sym, '%' + sym) # return %b %d %Y - %H:%M:%S
# #                 # print(format)
# #
# #         print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")
# #         start = time.time()
# #         result = func(*args, **kwargs)
# #         end = time.time()
# #         print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
# #         return result
# #
# #     return wrapped
# #
# #
# # def log_methods(date_format):
# #     """
# #     Декоратор, который будет логировать все методы декорируемого класса (кроме магических методов)
# #             и в который можно передавать формат вывода даты и времени логирования
# #     """
# #     def decorate(cls):
# #         for method in dir(cls):
# #             if not method.startswith('__'):
# #                 current_method = getattr(cls, method)
# #                 decorated_method = timer(cls, current_method, date_format)
# #                 setattr(cls, method, decorated_method)
# #         return cls
# #
# #     return decorate
# #
# #
# # @log_methods("b d Y - H:M:S")
# # class A:
# #     def test_sum_1(self) -> int:
# #         print('test sum 1')
# #         number = 100
# #         result = 0
# #         for _ in range(number + 1):
# #             result += sum([i_num ** 2 for i_num in range(10000)])
# #
# #         return result
# #
# # @log_methods("b d Y - H:M:S")
# # class B(A):
# #     def test_sum_1(self):
# #         super().test_sum_1()
# #         print("Наследник test sum 1")
# #
# #     def test_sum_2(self):
# #         print("test sum 2")
# #         number = 200
# #         result = 0
# #         for _ in range(number + 1):
# #             result += sum([i_num ** 2 for i_num in range(10000)])
# #
# #         return result
# #
# # my_obj = B()
# # my_obj.test_sum_1()
# # my_obj.test_sum_2()
# 
# # # понимаю, как работает, но не понимаю, почему в словарь мы добавляем параметр внутри декоратора,
# # # где ключом является параметр, а значением функция
# # # предполагаю, что уже есть какой-то словарь, с которым сравнивается параметр и выдается значение
# # # но в условии задачи не дается никакого словаря
# #
# # import functools
# # from typing import Callable, Any, Optional
# # def callback(route: str) -> Callable:
# #     """Декоратор. выполняется после определённого события"""
# #     def inner_decorator(func: Callable) -> Callable:
# #         app[route] = func # это событие о котором идет речь??
# #         @functools.wraps(func)
# #         def wrapped() -> Any:
# #             return func()
# #         return wrapped
# #     return inner_decorator
# #
# # app = {}
# # @callback('//')
# # def example():
# #     print('Пример функции, которая возвращает ответ сервера')
# #     return 'OK'
# # route = app.get('//')
# # if route:
# #     response = route()
# #     print('Ответ:', response)
# # else:
# #     print('Такого пути нет')
# #
# # print(f'Словарь: {app}')
# 
# # import functools
# # from typing import Callable, Any, Optional
# # def check_permission(user: str) -> Callable:
# #     """Декоратор, проверяет права доступа для выполнения функции"""
# #     def inner_decorator(func: Callable) -> Callable:
# #         @functools.wraps(func)
# #         def wrapped() -> Any:
# #
# #             if user in user_permissions:
# #                 return func()
# #             print(f'PermissionError: У пользователя {user} недостаточно прав, '
# #                   f'чтобы выполнить функцию {func.__name__}')
# #         return wrapped
# #     return inner_decorator
# #
# # user_permissions = ['admin']
# # @check_permission('admin')
# # def delete_site():
# #     print('Удаляем сайт')
# #
# # @check_permission('user_1')
# # def add_comment():
# #     print('Добавляем комментарий')
# #
# # delete_site()
# # add_comment()
# 
# 
# # from typing import Callable
# # import functools
# #
# # class CountCalls:
# #     """Класс декоратор. Считает количество вызовов функции
# #         метод num_calls для базовой функции для счета вызовов
# #     """
# #     def __init__(self, func: Callable) -> None:
# #
# #         functools.update_wrapper(self, func)
# #         self.func = func
# #         self.num_calls = 0
# #
# #     def __call__(self, *args, **kwargs) -> Callable:
# #         self.num_calls += 1
# #         print(f'Вызов номер {self.num_calls} функции: {self.func.__name__}')
# #         return self.func(*args, **kwargs)
# #
# #
# # @CountCalls
# # def say_hello():
# #     print('Hello')
# #
# # say_hello()
# # say_hello()
# # say_hello()
# # print(say_hello.num_calls)
# 
# # import functools
# # from datetime import datetime
# # import time
# # from typing import Callable, Any
# #
# # def timer(func: Callable) -> Callable:
# #     """Декоратор, выводящий время работы функции"""
# #
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         start = time.time()
# #         result = func(*args, **kwargs)
# #         end = time.time()
# #         run_time = round(end - start, 4)
# #         print(f'Функция работала {run_time} секунд(ы)')
# #
# #         return result
# #     return wrapped_func
# #
# # def create_time(cls):
# #     """Декоратор выводит время создания инстанса класса и список методов класса"""
# #     @functools.wraps(cls)
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         cls(*args, **kwargs)
# #         print(f'Время создания инстанса класса: {datetime.utcnow()}')
# #         print(f'Список методов класса:\n {dir(cls)}')
# #         for i_method in dir(cls):
# #             if i_method.startswith('__') is False:
# #                 print(i_method)
# #         return cls(*args, **kwargs)
# #     return wrapped_func
# #
# # def for_all_methods(decorator: Callable) -> Callable:
# #     """Декоратор, принимает другой декоратор для применения к методоам класса"""
# #
# #     @functools.wraps(decorator)
# #     def wrapped(cls):
# #         for i_method in dir(cls):
# #             if i_method.startswith('__') is False:
# #                 cur_method = getattr(cls, i_method)
# #                 decorated_method = decorator(cur_method)
# #                 setattr(cls, i_method, decorated_method)
# #         return cls
# #     return wrapped
# #
# # @create_time
# # @for_all_methods(timer)
# # class A:
# #
# #     def test_sum_1(self) -> int:
# #         print('Тут метод test_sum_1')
# #         number = 100
# #         result = 0
# #         for _ in range(number + 1):
# #             result += sum([i_num ** 2 for i_num in range(10000)])
# #
# #         return result
# #
# #
# # A().test_sum_1()
# 
# # class CanFly:
# #
# #     def __init__(self, *args, **kwargs):
# #         self.altitude = 0  # метров
# #         self.velocity = 0  # км/ч
# #
# #     def take_off(self):
# #         self.altitude = 100
# #         self.velocity = 300
# #
# #     def fly(self):
# #         self.altitude = 5000
# #
# #     def land_on(self):
# #         self.altitude = 0
# #         self.velocity = 0
# #
# #     def operate(self):
# #         super().operate()
# #         print('летим')
# #
# #     def __str__(self):
# #         res = super().__str__()
# #         return res + ' {} высота {} скорость {}'.format(
# #             self.__class__.__name__, self.altitude, self.velocity,
# #         )
# #
# # CanFly()
# 
# 
# # # Декоратор с параметром, перед выполнением декорируемой функции ждёт несколько секунд (замедление кода)
# # import time
# # from typing import Callable, Any
# # import functools
# # from typing import Optional
# #
# #
# # def time_sleep_value(_func: Optional[Callable]=None, *, value: int = 1) -> Callable:
# #     def time_sleep(func: Callable) -> Callable:
# #         """
# #         Декоратор, перед выполнением декорируемой функции ждёт несколько секунд (с определением времени ожидания)
# #         """
# #
# #         @functools.wraps(func)
# #         def wrapped_func(*args, **kwargs) -> Any:
# #             time.sleep(value)
# #             result = func(*args, **kwargs)
# #             return result
# #         return wrapped_func
# #     if _func is None:
# #         return time_sleep
# #     else:
# #         return time_sleep(_func)
# #
# # @time_sleep_value(value=2)
# # def test():
# #     print('<Тут что-то происходит...>')
# #
# # test()
# 
# # # временно меняет текущую рабочую директорию на новую
# # from contextlib import contextmanager
# # import os
# #
# # @contextmanager
# # def in_dir(path):
# #     cur_path = os.getcwd()
# #     os.chdir(path)
# #     try:
# #         yield
# #     finally:
# #         os.chdir(cur_path)
# #
# #
# # with in_dir('C:\\'):
# #     print(os.listdir())
# 
# 
# # # библиотека контекст менеджер - добавляет автоматически строки enter exit
# # import time
# # from contextlib import contextmanager
# # from collections.abc import Iterator
# #
# # @contextmanager
# # def timer() -> Iterator:
# #     start = time.time()
# #     try:
# #         yield
# #     except Exception as exc:
# #         print(exc)
# #     finally:
# #         print(time.time() - start)
# #
# #
# # with timer() as t1:
# #     val_1 = 100 * 100 ** 10000
# 
# # 28.8 Практическая работа
# 
# # import os
# # class File:
# #     """
# #     класс File — контекстный менеджер для работы с файлами
# #     """
# #
# #     def __init__(self, filename, mode):
# #         self.filename = filename
# #         self.mode = mode
# #         self.file = None
# #
# #     def __enter__(self):
# #         """
# #         Если файл не существует, создает файл в режиме записи
# #         и закрывает его для дальнейшей работы
# #         :return: os.path.exists(self.filename) = True
# #         """
# #         if not os.path.exists(self.filename):
# #             open(self.filename, 'w', encoding='utf8').close()
# #         self.file = open(self.filename, self.mode, encoding='utf8')
# #         return self.file
# #
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.file.close()
# #         """
# #         При выходе из контекстного менеджера подавляет все ошибки
# #         """
# #         # if exc_type and issubclass(exc_type, IOError):
# #         #     return True
# #         return True
# #
# #
# # with File("example.txt", "r") as file:
# #     file.write("Всем привет!")
# 
# # class MyMath:
# #     """
# #     Класс для работы с фигурами: мат вычисления
# #     вычисление длины окружности P=2πR
# #     вычисление площади окружности S=πR²
# #     вычисление объёма куба V=a³
# #     вычисление площади поверхности сферы S = 4 π R 2
# #     """
# #     def __init__(self) -> None:
# #         pass
# #         # self.radius = 0
# #         # self.cube_side = 0
# #     def circle_len(radius) -> int:
# #         # self.radius = radius
# #         return 2 * 3.1415926535 * radius
# #     def circle_sq(radius) -> int:
# #         # self.radius = radius
# #         return 3.1415926535 * radius ** 2
# #     def cube_volume(cube_side) -> int:
# #         return cube_side ** 3
# #     def s_surf_sph(radius) -> int:
# #         return 4 * 3.1415926535 * radius * 2
# #
# #
# # res_1 = MyMath.circle_len(radius=5)
# # res_2 = MyMath.circle_sq(radius=6)
# # res_3 = MyMath.cube_volume(cube_side=3)
# # res_4 = MyMath.s_surf_sph(radius=6)
# # print(res_1)
# # print(res_2)
# # print(res_3)
# # print(res_4)
# 
# # import math
# # class Square:
# #     """
# #     Классы квадрат, треугольник, куб, пирамида.
# #     Вычисляются функции по 2-D классам, затем передаются в 3D классы куб и пирамида
# #     для вычисления аналогичных параметров
# #
# #     """
# #     def __init__(self, side: int):
# #         self._side = side
# #         self._figure_name = "Квадрат"
# #
# #     @property
# #     def square(self) -> int:
# #         return self._side ** 2
# #
# #     @property
# #     def perimeter(self) -> int:
# #         return self._side * 4
# #
# # class Triangle:
# #     """
# #     Класс треугольник
# #     """
# #     def __init__(self, base: int, h: int):
# #         self._base = base
# #         self._h = h
# #         self._figure_name = "Треугольник"
# #
# #     @property
# #     def square(self) -> int:
# #         return 0.5 * self._base * self._h
# #
# #     @property
# #     def perimeter(self) -> int:
# #         return 2 * math.sqrt(self._h**2 + (self._base / 2)**2) + self._base
# #
# #
# # class Cube(Square):
# #     """
# #     Класс куб
# #     """
# #     def __init__(self, side: int):
# #         super().__init__(side)
# #         self.figure_name = 'Куб'
# #
# #     @property
# #     def square(self) -> int:
# #         return 6 * super().square
# #
# #     @property
# #     def perimeter(self) -> int:
# #         return 3 * super().perimeter
# #
# #
# # class Pyramid(Triangle, Square):
# #     """
# #     Класс пирамида
# #     """
# #     def __init__(self, base: int, h: int):
# #         super().__init__(base, h)
# #         self.figure_name = 'Пирамида'
# #
# #     @property
# #     def square(self) -> int:
# #         side_square = 4 * super().square
# #         base_square = self._base ** 2
# #         return side_square + base_square
# #
# #     @property
# #     def perimeter(self) -> int:
# #         return 2 * super().perimeter + 2 * self._base
# #
# #
# # p = Pyramid(6, 4)
# # print(f'Площадь фигуры {p.figure_name}: {p.square}')
# # print(f'Периметр фигуры {p.figure_name}: {p.perimeter}')
# # print()
# #
# # p = Cube(5)
# # print(f'Площадь фигуры {p.figure_name}: {p.square}')
# # print(f'Периметр фигуры {p.figure_name}: {p.perimeter}')
# 
# # class Date:
# #     def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
# #         self.day = day
# #         self.month = month
# #         self.year = year
# #     def __str__(self):
# #         return f'День: {self.day} Месяц: {self.month} Год: {self.year}'
# #
# #     """
# #     Класс ДАТА - проверять числа даты на корректность;
# #     конвертировать строку даты в объект класса Date,
# #     состоящий из соответствующих числовых значений дня, месяца и года.
# #     методы класса получают на вход строку вида ‘dd-mm-yyyy’
# #
# #     """
# #     @classmethod
# #     def is_date_valid(cls, date: str) ->bool:
# #         # dmy_list = date.split('-')
# #         # day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
# #         day, month, year = map(int, date.split('-'))
# #         return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999
# #
# #     @classmethod
# #     def from_string(cls, date: str) -> 'Date':
# #         # dmy_list = date.split('-')
# #         # day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
# #         day, month, year = map(int, date.split('-'))
# #         date_obj = cls(day, month, year) # передаем через cls параметры в класс для присвоения self.
# #         print(date_obj) # выводим на экран класс Date через строку __str__
# #
# # date = Date.from_string('10-12-2077')
# # print(date)
# # print(Date.is_date_valid('10-12-2077'))
# # print(Date.is_date_valid('40-12-2077'))
# 
# 
# # # парк транспорта (автомобили, лодки и амфибии). У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал
# # from abc import ABC, abstractmethod
# #
# # class MusicMixin:
# #
# #     def play_music(self):
# #         print("""
# #         I see trees of green
# #         Red roses too
# #         I see them bloom
# #         For me and for you
# #         And I think to myself
# #         What a wonderful world
# #         """)
# #
# #
# # class Transport(ABC):
# #
# #     def __init__(self, color, speed):
# #         self._color = color
# #         self._speed = speed
# #
# #     @property
# #     def color(self):
# #         return self._color
# #
# #     @color.setter
# #     def color(self, value):
# #         self._color = value
# #
# #     @property
# #     def speed(self):
# #         return self._speed
# #
# #     @speed.setter
# #     def speed(self, value):
# #         self._speed = value
# #
# #     @abstractmethod
# #     def ride_on_earth(self):
# #         pass
# #
# #     @abstractmethod
# #     def ride_on_water(self):
# #         pass
# #
# #     def signal(self):
# #         print("Сигнал")
# #
# #
# # class Car(Transport):
# #
# #     def ride_on_earth(self):
# #         print("Едем по земле")
# #
# #
# # class Boat(Transport):
# #
# #     def ride_on_water(self):
# #         print("Ходим по воде")
# #
# #
# # class Amphibian(Car, Boat, MusicMixin):
# #    pass
# #
# #
# # amph_transport = Amphibian('blue', 123)
# # amph_transport.ride_on_earth()
# # amph_transport.ride_on_water()
# # amph_transport.play_music()
# # print(amph_transport.color)
# # amph_transport.color = 'white'
# # print(amph_transport.color)
# 
# # # класс «Контекст-менеджер», который будет выдавать такой же результат
# # class Example:
# #
# #     def __init__(self):
# #         print("Вызов __init__")
# #
# #     def __enter__(self):
# #         print("Вызов __enter__")
# #         return True
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         print("Вызов __exit__")
# #         if exc_type:
# #             print(f'Тип ошибки: {exc_type}\nЗначение ошибки: {exc_val}\n"След" ошибки:{exc_tb}')
# #         return True  # первый вариант без этой строки, второй с этой строкой
# #
# #
# # my_obj = Example()
# #
# # with my_obj as obj:
# #     print('Код внутри первого вызова контекст менеджера')
# #
# # with my_obj as obj2:
# #     raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
# #
# # print('Я обязательно выведусь...')
# 
# # class File:
# #     """
# #     класс File — контекстный менеджер для работы с файлами
# #     """
# #
# #     def __init__(self, filename, mode):
# #         self.filename = filename
# #         self.mode = mode
# #         self.file = None
# #
# #     def __enter__(self):
# #         self.file = open(self.filename, self.mode, encoding='utf8')
# #         return self.file
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.file.close()
# #         return True
# #
# #
# # with File("example.txt", "w") as file:
# #     file.write("Всем привет!")
# 
# # # парк транспорта (автомобили, лодки и амфибии). У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал
# # from abc import ABC, abstractmethod
# #
# #
# # class MusicMixin:
# #
# #     def play_music(self):
# #         print("""
# #         I see trees of green
# #         Red roses too
# #         I see them bloom
# #         For me and for you
# #         And I think to myself
# #         What a wonderful world
# #         """)
# #
# #
# # class Transport(ABC):
# #     """
# #     Родительский класс транспорт
# #     """
# #
# #     @abstractmethod
# #     def ride_on_earth(self):
# #         pass
# #
# #     @abstractmethod
# #     def ride_on_water(self):
# #         pass
# #
# #
# # class Car(Transport):
# #
# #     def ride_on_earth(self):
# #         print("Едем по земле")
# #
# #
# # class Boat(Transport):
# #
# #     def ride_on_water(self):
# #         print("Ходим по воде")
# #
# # class Amphibian(Car, Boat, MusicMixin):
# #     pass
# #
# # amph_transport = Amphibian()
# # amph_transport.ride_on_earth()
# # amph_transport.ride_on_water()
# # amph_transport.play_music()
# #
# #
# # from abc import ABC, abstractmethod
# #
# # class Figure(ABC):
# #     """
# #      Абстрактный базовый класс фигура
# #      args and attr:
# #      pos_x (int): координата X
# #      pos_y (int): координата Y
# #      lenght (int): длина фигуры
# #      width (int): ширина фигуры
# #     """
# #
# #     def __init__(self, pos_x:int, pos_y:int, length:int, width:int) -> None:
# #         self.pos_x = pos_x
# #         self.pos_y = pos_y
# #         self.length = length
# #         self.width = width
# #
# #     @abstractmethod
# #     def move(self, pos_x:int, pos_y:int) -> None:
# #         self.pos_x = pos_x
# #         self.pos_y = pos_y
# #
# #     def resize(self, width, length):
# #         pass
# #
# #     def __str__(self):
# #         return f'Фигура: {self.__class__}\nДлина: {self.length}\nШирина: {self.width}\n'
# #
# # # class ResizableMixin:
# # #     """
# # #     класс изменения размеров ResizableMixin
# # #     """
# # #     def resize(self, lenght:int, width:int) -> None:
# # #         self.lenght = lenght
# # #         self.width = width
# #
# # class Rectangle(Figure):
# #     """
# #     Прямоугольник, родительский класс фигура
# #     """
# #
# #     def resize(self, width, length):
# #         self.width = width
# #         self.length = length
# #     def move(self, pos_x:int, pos_y:int) -> None:
# #         self.pos_x = pos_x
# #         self.pos_y = pos_y
# #
# #
# # class Square(Figure):
# #     """
# #     Квадрат, родительский класс фигура
# #     """
# #
# #     def __init__(self, pos_x, pos_y, size):
# #         super().__init__(pos_x, pos_y, size, size)
# #
# #     def resize(self, width, length):
# #         if width == length:
# #             self.width = width
# #             self.length = length
# #         else:
# #             print("У квадрата стороны равны!")
# #     def move(self, pos_x:int, pos_y:int) -> None:
# #         self.pos_x = pos_x
# #         self.pos_y = pos_y
# #
# # rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
# # rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
# # square_1 = Square(pos_x=30, pos_y=40, size=7)
# #
# # for figure in [rect_1, rect_2, square_1]:
# #     print(figure)
# #     new_size_x = figure.length * 2
# #     new_size_y = figure.width * 2
# #     figure.resize(new_size_x, new_size_y)
# #     print(figure)
# 
# 
# # # Снова роботы
# # class Robot:
# #
# #     def __init__(self, model, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.model = model
# #
# #     def __str__(self):
# #         res = super().__str__()
# #         return res + ' {} model {}'.format(self.__class__.__name__, self.model)
# #
# #     def operate(self):
# #         print('Я - Робот!')
# #
# # class CanFly:
# #
# #     def __init__(self, *args, **kwargs):
# #         self.altitude = 0  # метров
# #         self.velocity = 0  # км/ч
# #
# #     def take_off(self):
# #         self.altitude = 100
# #         self.velocity = 300
# #
# #     def fly(self):
# #         self.altitude = 5000
# #
# #     def land_on(self):
# #         self.altitude = 0
# #         self.velocity = 0
# #
# #     def operate(self):
# #         super().operate()
# #         print('летим')
# #
# #     def __str__(self):
# #         res = super().__str__()
# #         return res + ' {} высота {} скорость {}'.format(
# #             self.__class__.__name__, self.altitude, self.velocity,
# #         )
# #
# # class ScoutDrone(CanFly, Robot):
# #
# #     def __init__(self, model):
# #         super().__init__(model=model)
# #
# #     def operate(self):
# #         super().operate()
# #         print('Робот ведет разведку с воздуха')
# #
# #
# # class WarDrone(CanFly, Robot):
# #
# #     def __init__(self, model, gun):
# #         super().__init__(model=model)
# #         self.gun = gun
# #
# #     def operate(self):
# #         super().operate()
# #         print(f'Робот защищает объект при помощи {self.gun}')
# #
# #
# # print()
# # ScoutDrone('a1').operate()
# # print()
# # WarDrone('r2-d2', 'intellect').operate()
# 
# 
# # from typing import Callable, Any
# # import functools
# #
# # def counter(func: Callable) -> Callable:
# #     """
# #     :param func: Декоратор
# #     :return: считающий и выводящий количество вызовов декорируемой функции
# #     """
# #
# #     @functools.wraps(func)
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         wrapped_func.count += 1
# #         result = func(*args, **kwargs)
# #         print(f'Функция {func.__name__} была вызвана {wrapped_func.count} раз(а)')
# #         return result
# #     wrapped_func.count = 0
# #     return wrapped_func
# #
# # @counter
# # def test():
# #     print('<Тут что-то происходит...>')
# # test()
# # test()
# # test()
# # test()
# 
# # from typing import Callable, Any
# # import functools
# #
# # def debug(func: Callable) -> Callable:
# #     """ декоратор debug, который при каждом вызове декорируемой функции выводит её имя
# #     (вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает.
# #     После этого выводится результат её выполнения.
# #
# #     """
# #     @functools.wraps(func)
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         print(f'Имя функции: {func.__name__}\n'
# #               f'Переданы аргументы: {args}\n'
# #               f'Переданы именованные аргументы: {kwargs}')
# #         if kwargs:
# #               print(f'Возвращает значение: {"Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!"}')
# #         else:
# #             print(f'Возвращает значение: {"Привет, {name}!"}')
# #         result = func(*args, **kwargs)
# #         print('Функция успешно завершена\n')
# #         return result
# #     return wrapped_func
# # @debug
# # def greeting(name, age=None):
# #     if age:
# #         return print("Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age))
# #     else:
# #         return print("Привет, {name}!".format(name=name))
# #
# # greeting("Том")
# # greeting("Миша", age=100)
# # greeting(name="Катя", age=16)
# 
# 
# # import datetime
# # import time
# # from typing import Callable, Any
# # import functools
# #
# # def logging(func: Callable) -> Callable:
# #     """декоратор logging, логирование функций в файл errors_dec.log"""
# #
# #     @functools.wraps(func)
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         try:
# #             return func(*args, **kwargs)
# #         except Exception as error:
# #             if error:
# #                 with open("errors_dec.log", "a", encoding="utf8") as file:
# #                     today = datetime.date.today().strftime("%c")
# #                     file.write(f'В функции {func.__name__} выявлена {today} ошибка: {str(type(error))}\n')
# #
# #     return wrapped_func
# #
# # @logging
# # def test():
# #     print('<Тут что-то происходит...>')
# #     x = 1 / 0
# #
# # test()
# 
# # # Декоратор, перед выполнением декорируемой функции ждёт несколько секунд (замедление кода)
# # import time
# # from typing import Callable, Any
# # import functools
# # def time_sleep(func: Callable) -> Callable:
# #     """
# #     Декоратор, перед выполнением декорируемой функции ждёт несколько секунд
# #     """
# #
# #     @functools.wraps(func)
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         time.sleep(10)
# #         result = func(*args, **kwargs)
# #         return result
# #     return wrapped_func
# #
# # @time_sleep
# # def test():
# #     print('<Тут что-то происходит...>')
# #
# # test()
# 
# # # Декоратор. Вставляет принт перед\после выполнением функции
# # from typing import Callable
# # import functools
# #
# # def how_are_you(func: Callable) -> Callable:
# #     """ Декоратор. Вставляет принт перед/после выполнением функции"""
# #     @functools.wraps(func)
# #     def wrapped_func(*args, **kwargs) -> str:
# #         print("Как дела?")
# #         func(*args, **kwargs)
# #         print("А у меня не очень!")
# #     return wrapped_func
# #
# #
# # @how_are_you
# # def test():
# #     print('<Тут что-то происходит...>')
# #
# # test()
# 
# 
# 
# # # декортатор печатает текст сверху и снизу от функции
# # def get_some_salad(func):
# #     def wrap_that_salad(*args, **kwargs):
# #         print("#помидоры#")
# #         func(*args, **kwargs)
# #         print("~салат~")
# #
# #     return wrap_that_salad
# #
# #
# # def get_some_buns(func):
# #     def wrap_that_buns(*args, **kwargs):
# #         print("</----------\>")
# #         func(*args, **kwargs)
# #         print("<\______/>")
# #
# #     return wrap_that_buns
# #
# #
# # @get_some_buns
# # @get_some_salad
# # def filling_burger(filler):
# #     print(filler)
# #
# #
# # filling_burger("ветчина")
# 
# # # декоратор, регистрирует функцию как плагин
# # from typing import Callable
# # import functools
# # plugings = dict()
# #
# # def register(func: Callable) -> Callable:
# #     """декоратор, регистрирует функцию как плагин"""
# #
# #     plugings[func.__name__] = func
# #     return func
# #
# # @register
# # def hello(name):
# #     return f"Привет, {name}!"
# #
# # print(hello('Вася'))
# # print(plugings)
# # print(hello.__name__)
# 
# 
# 
# # # декоратор do_twice, который дважды вызывает декорируемую функцию
# # from typing import Callable, Any
# # import functools
# #
# # def do_twice(func: Callable) -> Callable:
# #     """декоратор do_twice, который дважды вызывает декорируемую функцию"""
# #     @functools.wraps(func)
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         func(*args, **kwargs)
# #         return func(*args, **kwargs)
# #
# #     return wrapped_func
# #
# # @do_twice
# # def greeting(name: str) -> None:
# #     print('Привет, {name}!'.format(name=name))
# #
# #
# # greeting("Ваня!")
# 
# ## Функция таймер. Выводит время работы функции и возвращает ее результат
# # def timer(func, *args, **kwargs):
# #     """Функция таймер. Выводит время работы функции и возвращает ее результат"""
# #     import time
# #     start = time.time()
# #     result = func(*args, **kwargs)
# #     end = time.time()
# #     run_time = round(end - start, 4)
# #     print(f'Функция работала {run_time} секунд(ы)')
# #
# #     return result
# 
# # # Декоратор, выводящий время работы функции
# # import time
# # from typing import Callable, Any
# # def timer(func: Callable) -> Callable:
# #         """Декоратор, выводящий время работы функции"""
# #     def wrapped_func(*args, **kwargs) -> Any:
# #         start = time.time()
# #         result = func(*args, **kwargs)
# #         end = time.time()
# #         run_time = round(end - start, 4)
# #         print(f'Функция работала {run_time} секунд(ы)')
# #
# #         return result
# #     return wrapped_func
# 
# 
# # # Односвязный список
# # from typing import Any, Optional
# # class Node:
# #     def __init__(self, value: Optional[Any], next: Optional['Node'] = None) -> None:
# #         self.value = value
# #         self.next = next
# #     def __str__(self) -> str:
# #         return f'Node [{str(self.value)}]'
# #
# # class LinkedList:
# #     def __init__(self) -> None:
# #         self.head: Optional[Node] = None
# #         self.lengh = 0
# #
# #     def __str__(self) -> str:
# #         if self.head is not None:
# #             current = self.head
# #             values = [str(current.value)]
# #             while current.next is not None:
# #                 current = current.next
# #                 values.append(str(current.value))
# #             return '[{values}]'.format(values=' '.join(values))
# #         return 'LinkedList []'
# #
# #     def append(self, elem: Any) -> None:
# #         new_node = Node(elem)
# #         if self.head is None:
# #             self.head = new_node
# #             return
# #
# #         last = self.head
# #         while last.next:
# #             last = last.next
# #         last.next = new_node
# #         self.lengh += 1
# #     def get(self, index):
# #         pass
# #     def remove(self, index) -> None:
# #         cur_node = self.head
# #         cur_index = 0
# #         if self.lengh == 0 or self.lengh <= index:
# #             raise IndexError
# #
# #         if cur_node is not None:
# #             if index == 0:
# #                 self.head = cur_node.next
# #                 self.lengh += 1
# #                 return
# #
# #         while cur_node is not None:
# #             if cur_index == index:
# #                 break
# #             prev = cur_node
# #             cur_node = cur_node.next
# #             cur_index += 1
# #
# #         prev.next = cur_node.next
# #         self.lengh -= 1
# 
# 
# 
# # my_list = LinkedList()
# # my_list.append(10)
# # my_list.append(20)
# # my_list.append(30)
# # print(my_list)
# # print()
# # my_list.remove(1)
# # print(my_list)
# 
# 
# 
# 
# 
# # # берёт все питоновские файлы в директории
# # # и вычисляет общее количество строк кода, игнорируя пустые строки и строчки комментариев
# # import os.path
# #
# # def count_py_lines(path_search):
# #     count = 0
# #     for root, dirs, files in os.walk(path_search):
# #         for file in files:
# #             if file.endswith('.py'):
# #                 path = os.path.join(root, file)
# #                 with open(path, 'r', encoding='utf-8') as file:
# #                     for i_line in file:
# #                         if '#' not in i_line:
# #                             i_line.rstrip()
# #                             count += 1
# #                             # yield count
# #     return count
# #
# # code_lines_count = count_py_lines("O:\Python")
# # print(f'Общее количество строк кода: {code_lines_count}\n')
# 
# # # генерация последовательности Q Хофштадтера итератором
# # class Hofstadter:
# #     def __init__(self, s):
# #         self.s = s[:]
# #
# #     def __iter__(self):
# #         return self
# #
# #     def next(self):
# #         try:
# #             q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
# #             self.s.append(q)
# #             return q
# #         except IndexError:
# #             raise StopIteration()
# #
# #     def current_state(self):
# #         return self.s
# #
# # hofstadter = Hofstadter([1, 1])
# # print([hofstadter.next() for __ in range(10)])
# 
# # # рекурсивно проходит по всем каталогам указанной директории,
# # # находит указанный пользователем каталог и генерирует пути всех встреченных файлов.
# # import os.path
# #
# # def gen_file_path(path_search, folder_search):
# #     for root, dirs, files in os.walk(path_search):
# #         if folder_search in dirs:
# #             for file in files:
# #                 path = os.path.join(root, file)
# #                 yield path
# #
# # path_search = input("Введите путь для поиска: ") # r"C:\Users\Вика\Desktop"
# # folder_search = input("Какой каталог будем искать? ") # "Python"
# # print("\nПути всех встречающихся файлов\n")
# # print(*gen_file_path(path_search, folder_search), end='\n')
# 
# # # рефакторинг
# # # выход через генератор yield
# # list_1 = [2, 5, 7, 10]
# # list_2 = [3, 8, 4, 9]
# # to_find = 56
# # def refact(num: int) -> int:
# #     for x in list_1:
# #         for y in list_2:
# #             result = x * y
# #             print(x, y, result)
# #             if result == num:
# #                 print('Found!!!')
# #                 yield result
# #                 return
# # print(*refact(to_find))
# #
# # # исходный код
# # list_1 = [2, 5, 7, 10]
# # list_2 = [3, 8, 4, 9]
# # to_find = 56
# # can_continue = True
# # for x in list_1:
# #     for y in list_2:
# #         result = x * y
# #         print(x, y, result)
# #         if result == to_find:
# #             print('Found!!!')
# #             can_continue = False
# #             break
# #     if not can_continue:
# #         break
# 
# # # генерирует последовательность из квадратов чисел от 1 до N тремя способами
# # print('Выражение - генератор')
# # n = 10
# # square_num = (num ** 2 for num in range(1, n+1))
# # print(*square_num)
# #
# # print('Функция - генератор')
# # def square_number(num):
# #     for number in range(1, num + 1):
# #         yield number ** 2
# #
# # n = 10
# # for i in square_number(n):
# #     print(i, end=' ')
# #
# # print('\nКласс - итератор')
# # class Square_gen:
# #     def __init__(self, number):
# #         self.n = number
# #         self.i = 1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         while self.i < self.n:
# #             self.i += 1
# #             return self.i ** 2
# #         raise StopIteration
# # n = 10
# # square = Square_gen(n)
# # print(*square)
# 
# # def numbers_from_text(text):
# #     return [int(number) for number in text.rstrip().split()]
# #
# #
# # def file_parser(path_to_file):
# #     with open(path_to_file) as file:
# #         for line in file:
# #             clear_line_sum = sum(numbers_from_text(line))
# #             # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
# #             yield clear_line_sum
# #
# #
# # all_sum = 0
# # for number in file_parser("numbers.txt"):
# #     all_sum += number
# #
# # print("Вариант №1", all_sum)
# #
# #
# # # Ещё один вариант решения с функцией map()
# # def file_parser(path_to_file):
# #     with open(path_to_file) as file:
# #         for line in file:
# #             clear_line_sum = sum(map(int, line.rstrip().split()))
# #             # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
# #             yield clear_line_sum
# #
# #
# # all_sum = 0
# # for number in file_parser("numbers.txt"):
# #     all_sum += number
# #
# # print("Вариант №2", all_sum)
# 
# # # генератор бесконечные цифры функция
# # # def counter():
# # #     n = 0
# # #     while True:
# # #         n += 1
# # #         yield n
# # # for i in counter():
# # #     print(i)
# #
# # # функция генератор простых чисел
# # def get_prime_numbers(n):
# #     prime_numbers = []
# #     for number in range(2, n + 1):
# #         for prime in prime_numbers:
# #             if number % prime == 0:
# #                 break
# #         else:
# #             prime_numbers.append(number)
# #             yield number
# #
# #
# # for i in get_prime_numbers(50):
# #     print(i, end='\t')
# # print()
# 
# # ## генератор фибоначи функция через yield
# # def fibonacci(number):
# #     cur_val = 0
# #     next_val = 1
# #     for _ in range(number):
# #         yield cur_val
# #         cur_val, next_val = next_val, cur_val + next_val
# #         if cur_val > 10 ** 6:
# #             return
# # def square(num):
# #     for num in num:
# #         yield num ** 2
# #
# # fib_seq = fibonacci(number=1000000)
# # # for i in fib_seq:
# # #     print(i)
# # print()
# #
# # # генератор от генератора
# # print(sum(square(fibonacci(number=5000))))
# #
# # # генераторные выражения
# # cubes_gen = (num ** 3 for num in range(10))
# # print(*cubes_gen)
# 
# # # класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
# # class Primes:
# #
# #     def __init__(self, n):
# #         self.n = n
# #         self.i = 1
# #         self.prime_number = []
# #
# #     def __iter__(self):
# #         self.i = 1
# #         return self
# #
# #     def __next__(self):
# #         while self.i <= self.n:
# #             self.i += 1
# #             for prime in self.prime_number:
# #                 if self.i % prime == 0:
# #                     break
# #             else:
# #                 self.prime_number.append(self.i)
# #                 return self.i
# #         raise StopIteration
# #
# #
# # prime_nums = Primes(50)
# #
# # for i_elem in prime_nums:
# #     print(i_elem, end=' ')
# 
# 
# # # Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента (первый элемент —
# # # # просто случайное вещественное число от 0 до 1)
# # import random
# # class SumsOfLastTwo:
# #
# #     def __init__(self, count):
# #         self.last = 0
# #         self.end = count
# #         self.start = 0
# #
# #     def __iter__(self):
# #         self.last = 0
# #         self.start = 0
# #         return self
# #
# #     def __next__(self):
# #         self.start += 1
# #         if self.start > self.end:
# #             raise StopIteration
# #         self.last += random.random()
# #         return self.last
# #
# #
# # counter = SumsOfLastTwo(5)
# # for i in counter:
# #     print(round(i, 2))
# 
# 
# # # Итератор увеличивает счётчик и возвращает предыдущее значение
# # class СountIterator:
# #     counter = 0
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         self.counter += 1
# #         return self.counter - 1
# # my_iter = СountIterator()
# # for i_elem in my_iter:
# #     print(i_elem)
# 
# #  Итератор последовательности Фибоначчи из N элементов поиск числа в ряде
# # class Fibonacci:
# #     """ Итератор последовательности Фибоначчи из N элементов"""
# #     def __init__(self, number):
# #         self.counter = 0
# #         self.cur_val = 0
# #         self.next_val = 1
# #         self.number = number
# #
# #     def __iter__(self):
# #         self.counter = 0
# #         self.cur_val = 0
# #         self.next_val = 1
# #         return self
# #
# #     def __next__(self):
# #         self.counter += 1
# #         if self.counter > 1:
# #             if self.counter > self.number:
# #                 raise StopIteration()
# #             self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
# #         return self.cur_val
# #
# #
# # fib_iterator = Fibonacci(10000000000000000000000000000000)
# # if 8 in fib_iterator:
# #     print(f'Число {8} есть в ряде')
# 
# ## итератор выдает указанное количество случайных чисел в диапазаоне, прописанном в классе
# # import random
# #
# # class RamdomNumber:
# #     def __init__(self, limit):
# #         self.__limit = limit
# #         self.__counter = 0
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         if self.__counter < self.__limit:
# #             self.__counter += 1
# #             return random.randint(0, 999)
# #         else:
# #             raise StopIteration
# #
# # my_iter = RamdomNumber(limit=10)
# # # print(next(my_iter))
# # # print(next(my_iter))
# # # print(next(my_iter))
# # for num in my_iter:
# #     print(num)
# 
# 
# # while True:
# #     try:
# #         print(next(buffer_iter))
# #     except StopIteration:
# #         print("Конец!")
# #         break
# 
# # # класс, который реализует стек и его возможности
# # class Stack:
# #     def __init__(self):
# #         self.__st = []
# #     def __str__(self):
# #         return '; '.join(self.__st)
# #         # return str(self.__st)
# #     def push(self, elem):
# #         self.__st.append(elem)
# #
# #     def pop(self):
# #         if len(self.__st) == 0:
# #             return None
# #         return self.__st.pop()
# #
# # # my_st = Stack()
# # # for i in range(5):
# # #     my_st.push(i)
# # # print(my_st)
# # # for _ in range(3):
# # #     my_st.pop()
# # # print(my_st)
# #
# # class TaskManager:
# #     def __init__(self):
# #         self.task = dict()
# #     def __str__(self):
# #         display = []
# #         if self.task:
# #             for i_priority in sorted(self.task.keys()):
# #                 display.append(f'{str(i_priority)} : {self.task[i_priority]}\n')
# #         return ''.join(display)
# #     def new_task(self, task, priotity):
# #         if priotity not in self.task:
# #             self.task[priotity] = Stack()
# #         self.task[priotity].push(task)
# #
# #
# # manager = TaskManager()
# # manager.new_task("сделать уборку", 4)
# # manager.new_task("помыть посуду", 4)
# # manager.new_task("отдохнуть", 1)
# # manager.new_task("поесть", 2)
# # manager.new_task("сдать дз", 2)
# # print(manager)
# 
# # # Совместное проживание - 2
# #
# # class People:
# #     def __init__(self, name, hungry, happy):
# #         self.name = name
# #         self.hungry = hungry
# #         self.happy = happy
# #
# # class Man(People):
# #     count_money = 0
# #     def __init__(self, name, hungry, happy):
# #        super().__init__(name, hungry, happy)
# #     def eat(self):
# #         self.hungry += 30
# #         House.food -= 30
# #         House.count_food += 30
# #     def work(self):
# #         self.hungry -= 10
# #         House.money += 150
# #         self.count_money += 150
# #     def play(self):
# #         self.hungry -= 10
# #         self.happy += 20
# #     def iron_pet(self):
# #         self.happy += 5
# #
# # class Woman(Man):
# #     count_coat = 0
# #     def __init__(self, name, hungry, happy):
# #         super().__init__(name, hungry, happy)
# #
# #     def eat(self):
# #         self.hungry += 30
# #         House.food -= 30
# #         House.count_food += 30
# #     def buy_eat(self):
# #         self.hungry -= 10
# #         House.food += 10
# #         House.cat_food += 10
# #         House.money -= 20
# #
# #     def buy_coat(self):
# #         self.hungry -= 10
# #         self.happy += 60
# #         House.money -= 350
# #         self.count_coat += 1
# #
# #     def clean_house(self):
# #         self.hungry -= 10
# #         House.durty -= 100
# #
# # class Cat:
# #     def __init__(self, name, hungry):
# #         self.nane = name
# #         self.hungry = hungry
# #     def eat(self):
# #         House.cat_food -= 10
# #         self.hungry += 20
# #         House.count_food += 10
# #     def break_wall(self):
# #         self.hungry -= 10
# #         House.durty += 5
# #
# # class House:
# #     food = 50
# #     money = 100
# #     cat_food = 30
# #     durty = 0
# #     count_food = 0
# #     def __init__(self, man, woman, cat):
# #         self.man = man
# #         self.woman = woman
# #         self.cat = cat
# #
# #     def info(self):
# #         health1 = self.man.hungry
# #         health2 = self.woman.hungry
# #         health3 = self.cat.hungry
# #
# #         print(f'Количество еды: {self.food}'
# #               f'\nДенег: {self.money}'
# #               f'\nМуж {self.man.name} питание: {health1}'
# #               f'\nЖена {self.woman.name} питание: {health2}'
# #               f'\nКот {self.cat.nane} питание: {health3}')
# #         print('\nСтатистика за прожитый период:')
# #         print(f'Заработано денег: {man.count_money}'
# #               f'\nСъедено еды: {House.count_food}'
# #               f'\nКуплено шуб: {woman.count_coat}')
# #
# #
# # man = Man('Иван', hungry=30, happy=100)
# # woman = Woman('Марья', hungry=30, happy=100)
# # cat_1 = Cat('Федор', hungry=30)
# # house_1 = House(man, woman, cat_1)
# # count = 0
# #
# # for i in range(365):
# #     if man.hungry > 20 and woman.hungry > 20 and house_1.food >= 40 and house_1.cat_food >= 10:
# #         man.eat()
# #         woman.eat()
# #         cat_1.eat()
# #         count += 1
# #         house_1.durty += 5
# #     elif house_1.food < 40 or house_1.cat_food < 10:
# #         woman.buy_eat()
# #         count += 1
# #         house_1.durty += 5
# #     elif house_1.money < 100:
# #         man.work()
# #         woman.iron_pet()
# #         woman.clean_house()
# #         woman.eat()
# #         count += 1
# #         house_1.durty += 5
# #     elif House.durty >= 90:
# #         man.happy -= 10
# #         woman.happy -= 10
# #         woman.buy_coat()
# #         count += 1
# #     else:
# #         man.play()
# #         woman.play()
# #         man.eat()
# #         woman.eat()
# #         count += 1
# #         house_1.durty += 5
# #
# # house_1.info()
# # print(f'Прожито дней: {count}')
# # if man.hungry <= 0:
# #     print(f'\nМуж {man.name} умер от голода')
# # elif man.happy <=10:
# #     print(f'\nМуж {man.name} умер от депрессии')
# #
# # if woman.hungry <= 0:
# #     print(f'\nЖена {woman.name} умерла от голода')
# # elif woman.happy <= 10:
# #     print(f'\nЖена {woman.name} умерла от депрессии')
# #
# # if cat_1.hungry <= 0:
# #         print(f'\nКот {cat_1.name} умер от голода')
# 
# 
# # # автомобиль и автобус движение
# # from math import cos, sin
# #
# # class Auto:
# #     def __init__(self, x, y, coal):
# #         self.x = x
# #         self.y = y
# #         self.coal = coal
# #
# #     def move(self, dist):
# #         self.x = self.x + dist * cos(self.coal)
# #         self.y = self.y + dist * sin(self.coal)
# #
# # class Bus(Auto):
# #     m_count = 51
# #
# #     def __init__(self, x, y, coal):
# #         super().__init__(x, y, coal)
# #         self.count = 0
# #         self.summ = 0
# #
# #     def passengers(self):
# #         return self.count
# #
# #     def money(self, money):
# #         self.summ += money
# #
# #     def enter(self, passengers):
# #         if self.count < self.m_count and passengers < self.m_count:
# #             self.count += passengers
# #         else:
# #             return print('Слишком много пассажиров!')
# #
# #     def exit(self, money, passengers):
# #         self.count -= passengers
# #
# #     def move(self, dist):
# #         self.summ += self.count * dist
# #
# # bus = Bus(1,1,15)
# # bus.enter(10)
# # bus.move(50)
# # bus.money(50)
# # # bus.enter(100)
# # print(bus.summ)
# 
# # # иерархия классов - показывает зарплату, но понимаю, что не то
# # # как определить в классе Employee(Person): параметр self.salary, так, чтобы он суммировал зарплату
# # # из всех подклассов и сотрудников, инициированных в этих подклассах
# # import random
# # class Person:
# #     def __init__(self, name, surname, age):
# #         self.__name = name
# #         self.__surname = surname
# #         self.__age = age
# #
# # class Employee(Person):
# #     def __init__(self, name, surname, age, salary):
# #         super().__init__(name, surname, age)
# #         self.salary = salary
# #
# #     def get_salary(self):
# #         self.salary = Manager.get_salary() + Agent.get_salary() + Worker.get_salary()
# #         return self.salary
# #
# # class Manager(Employee):
# #     def __init__(self, name, surname, age):
# #         super().__init__(name, surname, age, salary=0)
# #
# #     def get_salary(self):
# #         self.salary = 13000
# #         return self.salary
# #
# # class Agent(Employee):
# #
# #     def __init__(self, name, surname, age, salary, volume=0):
# #         super().__init__(name, surname, age, salary)
# #         self.volume = 100000
# #
# #     def get_salary(self):
# #         self.salary = 5000 + (self.volume * 5 / 100)
# #         return self.salary
# #
# # class Worker(Employee):
# #
# #     def __init__(self, name, surname, age, salary, hours=0):
# #         super().__init__(name, surname, age, salary)
# #         self.hours = 160
# #
# #     def get_salary(self):
# #         self.salary = 100 * self.hours
# #         return self.salary
# #
# # names = ['Иван', 'Петр', 'Сергей', 'Алексей']
# # surnames = ['Грозный', 'Босой', 'Кривой', 'Козлов']
# #
# # manager_1 = Manager(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50))
# # manager_2 = Manager(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50))
# # manager_3 = Manager(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50))
# #
# # agent_1 = Agent(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50), salary=10)
# # agent_2 = Agent(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50), salary=10)
# # agent_3 = Agent(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50), salary=10)
# #
# # worker_1 = Worker(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50), salary=10)
# # worker_2 = Worker(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50), salary=10)
# # worker_3 = Worker(name=random.choice(names), surname=random.choice(surnames), age=random.randint(20, 50), salary=10)
# #
# # salary_sum = manager_1.get_salary() + manager_2.get_salary() + manager_3.get_salary() + agent_1.get_salary() + agent_2.get_salary() + agent_3.get_salary() + worker_1.get_salary() + worker_2.get_salary() + worker_3.get_salary()
# #
# # # salary_sum = Employee.get_salary() # как тут вызвать родительский класс, чтобы собрать все данные с дочерних в один?
# # print(f'Суммарная заработная плата всех сотрудников: {salary_sum}')
# 
# 
# 
# 
# # # если такого ключа в словаре нет, возвращает 0
# # class MyDict(dict):
# #     def get(self, key, default_value=0):
# #             return super().get(key, default_value)
# # #        if key in self:
# # #           return self[key]
# # #        else:
# # #            return default_value
# #
# #
# # new_dict = MyDict()
# # new_dict['Иван'] = 1
# # new_dict['Петр'] = 2
# # new_dict['Сергей'] = 3
# # print(new_dict)
# # print(new_dict.get('Стол'))
# 
# # # # функция one_day() возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений
# # import random
# #
# # class KillError(Exception):
# #     pass
# # class DrunkError(Exception):
# #     pass
# # class CarCrashError(Exception):
# #     pass
# # class GluttonyError(Exception):
# #     pass
# # class DepressionError(Exception):
# #     pass
# #
# #
# # def one_day():
# #
# #     if random.randint(1, 10) == 5:
# #         try:
# #             my_exception = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
# #             raise my_exception
# #         except my_exception as error:
# #             # print(str(error))
# #             with open("karma.log", "a", encoding="utf8") as file:
# #                 file.write(f'{str(type(error))}\n')
# #             return 0
# #     else:
# #         return random.randint(1, 7)
# #
# #
# # karma_count = 0
# # karma_end = 500
# # while karma_count <= karma_end:
# #     if one_day():
# #         karma_count += int(one_day())
# #         print(f'Ваш уровень кармы: {karma_count}')
# #
# # print(f'Вы достигли просветления! Уровень кармы: {karma_count}')
# 
# # # иерархия классов, описывающих имущество налогоплательщиков
# # # Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор
# # # Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.
# #
# # # не понял, что имеется в виду под конструктором?
# # # и если мы у пользователя запрашиваем отельно по каждой категории worth, где взять базовый worth?
# #
# # class Property:
# #     def __init__(self, worth):
# #         self.worth = worth
# #         self.tax = 0
# #
# #     def tax_property(self):
# #         pass
# #
# # class Apartment(Property):
# #     # def __init__(self, worth):
# #     #     super().__init__(worth)
# #     #     self.tax = 0
# #
# #     def tax_apart(self):
# #         self.tax = self.worth / 1000
# #         return self.tax
# #
# # class Car(Property):
# #     # def __init__(self, worth):
# #     #     super().__init__(worth)
# #     #     self.tax = 0
# #
# #     def tax_car(self):
# #         self.tax = self.worth / 200
# #         return self.tax
# #
# # class CountryHouse(Property):
# #     # def __init__(self, worth):
# #     #     super().__init__(worth)
# #     #     self.tax = 0
# #
# #     def tax_house(self):
# #         self.tax = self.worth / 500
# #         return self.tax
# #
# #
# # money = int(input('Сколько у вас денег? '))
# # car_price = int(input('Сколько стоит машина? '))
# # car = Car(car_price)
# # apart_price = int(input('Сколько стоит квартира? '))
# # apart = Apartment(apart_price)
# # house_price = int(input('Сколько стоит дача? '))
# # house = CountryHouse(house_price)
# #
# # print(f'Налог на квартиру: {round(apart.tax_apart(), 2)}')
# # print(f'Налог на машину: {round(car.tax_car(), 2)}')
# # print(f'Налог на дом: {round(house.tax_house(), 2)}')
# # full_tax = car.tax + apart.tax + house.tax
# #
# # # property = Property(car_price + apart_price + house_price)
# #
# # if money < full_tax:
# #     print(f'Вам не хватает денег для оплаты налогов: {round(full_tax - money, 2)} рублей')
# # else:
# #     print('Вам хватит заплатить налоги')
# 
# 
# 
# # ## задача Полет реализация ракеты и бабочки разные функции
# #
# # class CanFly:
# #     def __init__(self):
# #         self.altitude = 0  # метров
# #         self.velocity = 0  # км/ч
# #     def take_off(self):
# #         pass
# #     def fly(self):
# #         pass
# #     def land_on(self):
# #         self.altitude = 0
# #         self.velocity = 0
# #     def __str__(self):
# #         return '{} высота {} скорость {}'.format(
# #             self.__class__.__name__, self.altitude, self.velocity,
# #         )
# #
# # class Butterfly(CanFly):
# #     def take_off(self):
# #         self.altitude = 1
# #     def fly(self):
# #         self.velocity = 0.1
# #
# # class Aircraft(CanFly):
# #     def take_off(self):
# #         self.velocity = 300
# #         self.altitude = 1000
# #     def fly(self):
# #         self.velocity = 800
# #
# # class Missile(CanFly):
# #
# #     def take_off(self):
# #         self.velocity = 1000
# #         self.altitude = 10000
# #     def land_on(self):
# #         self.altitude = 0
# #         self.destroy_enemy_base()
# #
# #     def destroy_enemy_base(self):
# #         print('Ракета показала себя великолепно. Только упала не на ту планету (C) Вернер фон Браун')
# #
# # mis = Missile()
# # but = Butterfly()
# # air = Aircraft()
# # mis.destroy_enemy_base()
# # print(mis)
# # print(but)
# # print(air)
# 
# ## класс Юнит и классы солдат и гражданский взять значение из юнита и передать в дочерний
# # class Unit:
# #     def __init__(self, hp):
# #         self.__hp = hp
# #     def set_hp(self, amount):
# #         self.__hp = amount
# #     def get_hp(self):
# #         return self.__hp
# #     def get_damage(self, amount):
# #         self.set_hp(self.get_hp() - 0)  # -0 написан для наглядности, в теории  мы могли бы этого и не писать
# #
# # class Soldier(Unit):
# #     def get_damage(self, amount):
# #         self.set_hp(self.get_hp() - amount)
# #
# # class Citizen(Unit):
# #     def get_damage(self, amount):
# #         self.set_hp(self.get_hp() - amount * 2)
# #
# #
# # soldier = Soldier(hp=200)
# # citizen = Citizen(hp=100)
# # print(citizen.get_hp())
# # print(citizen.get_damage(5))
# 
# ## свое исключение сделать исключение
# # class DivisionError(Exception):
# #     pass
# #
# #
# # with open("numbers.txt", "r", encoding="utf8") as file:
# #
# #     for line in file:
# #         try:
# #             clear_line = line.rstrip()
# #             first, second = clear_line.split()
# #             if int(first) < int(second):
# #                 raise DivisionError("нельзя делить большее на меньшее")
# #         except (ValueError, DivisionError) as exc:
# #             print(exc, type(exc), first, second)
# 
# # # класс роботы и подклассы роботов из роботы и робот из роботв
# # class Robot:
# #
# #     def __init__(self, model):
# #         self.model = model
# #
# #     def __str__(self):
# #         return '{} model {}'.format(self.__class__.__name__, self.model)
# #
# #     def operate(self):
# #         print('Робот ездит по кругу')
# #
# #
# # class WarRobot(Robot):
# #
# #     def __init__(self, gun, model):
# #         super().__init__(model)
# #         self.gun = gun
# #
# #     def operate(self):
# #         print(f'Робот охраняет военный обьект при помощи {self.gun}')
# #
# #
# # class VacuumCleaningRobot(Robot):
# #
# #     def __init__(self, model):
# #         super().__init__(model)
# #         self.garbage_bag = 0
# #
# #     def operate(self):
# #         print('Робот пылесосит пол')
# #
# #
# # class SubmarineRobot(WarRobot):
# #
# #     def __init__(self, gun, model, depth):
# #         super().__init__(gun, model)
# #         self.depth = depth
# #
# #     def operate(self):
# #         super().operate()
# #         print('Охрана ведется под водой на глубине', self.depth)
# #
# # vc = VacuumCleaningRobot('пылесос')
# # vc.operate()
# # war_r = WarRobot('Ракета', 'военный')
# # war_r.operate()
# #
# # sr = SubmarineRobot('Ракета', 'военный', 5)
# # sr.operate()
# 
# ## корабли классы супер классы
# # class Ship:
# #
# #     def __init__(self, model="корабль"):
# #         self.model = model
# #
# #     def __str__(self):
# #         return self.model
# #
# #     def sail(self):
# #         print(f"{self.model} идёт по воде!")
# #
# #
# # class WarShip(Ship):
# #
# #     def __init__(self, weapon, model="военный корабль"):
# #         super().__init__(model)
# #         self.weapon = weapon
# #
# #     def attack(self):
# #         print(f"{self} делает пиу-пиу!")
# #
# #
# # class CargoShip(Ship):
# #
# #     def __init__(self, model="грузовой корабль"):
# #         super().__init__(model)
# #         self.fullness = 0
# #
# #     def loading(self, value):
# #         self.fullness += value
# #
# #     def unloading(self, value):
# #         self.fullness -= value
# 
# 
# # class Human:
# #     count = 0
# #
# #     def __init__(self, name, age):
# #         self.__name = ''
# #         self.__age = 0
# #         self.set_age(age)
# #         self.set_name(name)
# #
# #         Human.count += 1
# #
# #     def set_age(self, value):
# #         if isinstance(value, (int, float)) and 0 <= value <= 100:
# #             self.__age = value
# #         else:
# #             raise ValueError("Возраст от 0 до 100")
# #
# #     def set_name(self, value):
# #         if isinstance(value, str) and value.isalpha():
# #             self.__name = value
# #         else:
# #             raise Exception("Имя должно состоять только из букв")
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def get_age(self):
# #         return self.__age
# #
# #     def __str__(self):
# #         return f'Имя: {self.__name}\nВозраст: {self.__age}'
# #
# # try:
# #     human = Human('helo', 100)  # значения передадутся в сеттер
# #     human._Human__age = 99  # «крайне не рекомендуемый» метод
# #     print(human)
# # except (ValueError, Exception) as error:
# #     print(error)
# 
# 
# 
# # # # класс координаты точки c геттером и сеттером
# # class Point:
# #     count = 0
# #
# #     def __init__(self, x=0, y=0):
# #         self.set_x(x)
# #         self.set_y(y)
# #         Point.count += 1
# #
# #     def __str__(self):
# #         return f"({self.__x}, {self.__y})"
# #     def get_x(self):
# #         return self.__x
# #     def check_value(self, value):
# #         if isinstance(value, str) and value.isdigit():
# #             value = float(value)
# #         if isinstance(value, (int, float)):
# #             return value
# #         return Exception('введите число')
# #
# #     def set_x(self, value):
# #         checker_value = self.check_value(value)
# #         if checker_value:
# #             self.__x = checker_value
# #
# #     def set_y(self, value):
# #         checker_value = self.check_value(value)
# #         if checker_value:
# #             self.__y = checker_value
# #
# #
# #
# # new = Point(5,6)
# # new2 = Point(3,4)
# # print(new2, new)
# #
# # print(f'Количество точек в классе: {new.count}')
# 
# # ## реализует игру «Крестики-нолики»
# ## разберусь потом
# #
# # class Player(object):
# #     def __init__(self, name, symbol, initial_score=0):
# #         self.name= name
# #         self.symbol= symbol
# #         self.score= initial_score
# #
# #     def won_match(self):
# #         self.score+= 100
# #
# #     def lost_match(self):
# #         self.score-= 50
# #
# #     def show_score(self):
# #         print('Player {}: {} points'.format(self.name, self.score))
# #
# # class PlayingField(object):
# #     def __init__(self):
# #         self.field= [
# #                      [None, None, None],
# #                      [None, None, None],
# #                      [None, None, None]
# #                     ]
# #
# #     def show_field(self):
# #         for row in self.field:
# #             for player in row:
# #                 print('_' if player is None else player.symbol,end=' ')
# #             print()
# #
# #     def set_player(self, x, y, player):
# #         if self.field[y][x] is not None:
# #             return False
# #
# #         self.field[y][x]= player
# #
# #         return True
# #
# #     def full_board(self):
# #         for row in self.field:
# #             for col in row:
# #                 if col is None:
# #                     return False
# #         return True
# #
# #     def check_won(self, x, y, player):
# #         if self.field[0][x] == player and self.field[1][x] == player and self.field[2][x] == player:
# #             return True
# #         elif self.field[y][0] == player and self.field[y][1] == player and self.field[y][2] == player:
# #             return True
# #         elif self.field[0][0] == player and  self.field[1][1] == player and self.field[2][2] == player:
# #             return True
# #         elif self.field[0][2] == player and  self.field[1][1] == player and  self.field[2][0] == player:
# #             return True
# #         else:
# #             return False
# #
# #
# # def main():
# #     name_1= input('Name of Player 1: ')
# #     name_2= input('Name of Player 2: ')
# #
# #     players= [
# #               Player(name_1, 'X'),
# #               Player(name_2, 'O')
# #               ]
# #
# #     field= PlayingField()
# #
# #     while True:
# #         for player in players:
# #             field.show_field()
# #
# #             x= int(input('Player {} choose your column: '.format(player.name))) - 1
# #
# #             y= int(input('Player {} choose your row: '.format(player.name))) - 1
# #
# #             if not field.set_player(x, y, player):
# #                 print('That field is already occupied.')
# #
# #             elif field.full_board():
# #                 field.show_field()
# #                 print('full board')
# #                 for player in players:
# #                     print('{}: {}'.format(player.name, player.score))
# #                     field= PlayingField()
# #
# #             elif field.check_won(x, y, player):
# #                 field.show_field()
# #                 print('Player {} won the game.'.format(player.name))
# #                 print('Score')
# #                 for player in players:
# #                     if field.check_won(player) == True:
# #                         player.won_match()
# #                     elif field.check_won(player) == False:
# #                         player.lost_match()
# #                     print('{}: {}'.format(player.name, player.score))
# #                 field= PlayingField()
# #
# # if __name__ == '__main__':
# #     main()
# 
# 
# # # # блэк джэк
# ## разберусь потом
# # import random
# #
# # random.seed()
# #
# #
# # class BlackJack:
# #     def __init__(self):
# #         self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4
# #         self.score = 0
# #         self.bot_score = 0
# #
# #     def print_card(self, current, score, bot):
# #         if not bot:
# #             print(f'Вам попалась карта {current}. У вас {score} очков.')
# #         else:
# #             print(f'Крупье попалась карта {current}. У крупье {score} очков')
# #
# #     def random_card(self, score, bot):
# #         current = self.deck.pop()
# #         if type(current) is int:
# #             score += current
# #         elif current == 'Туз':
# #             if score <= 10:
# #                 score += 11
# #             else:
# #                 score += 1
# #         else:
# #             score += 10
# #         self.print_card(current, score, bot)
# #         return score
# #
# #     def choice(self):
# #         score = self.random_card(self.score, False)
# #         bot_score = self.random_card(self.bot_score, True)
# #         while True:
# #             choice = input('Будете брать карту? y/n\n')
# #             if choice == 'y':
# #                 score = self.random_card(score, False)
# #                 if bot_score < 19 and score <= 21:
# #                     bot_score = self.random_card(bot_score, True)
# #                 if score > 21 or bot_score == 21:
# #                     print('Извините, но вы проиграли')
# #                     break
# #                 elif score == 21 and bot_score == 21:
# #                     print('ничья')
# #                 elif score == 21 or bot_score > 21:
# #                     print('Поздравляю, вы победили!')
# #                     break
# #             elif choice == 'n':
# #                 if score > bot_score and bot_score < 19:
# #                     while bot_score < 19:
# #                         bot_score = self.random_card(bot_score, True)
# #                 if score < bot_score <= 21:
# #                     print(f'Вы проиграли, у вас {score} очков, у крупье {bot_score} очков')
# #                 else:
# #                     print(f'Вы победили, у вас {score} очков, у крупье {bot_score} очков')
# #
# #                 break
# #
# #     def start(self):
# #         random.shuffle(self.deck)
# #         print('Игра в BlackJack началась')
# #         print('В блэкджеке десятки, валеты, дамы и короли стоят по 10 очков.\nТуз может стоить 1 или 11 очков')
# #         print('----------------------------------')
# #         self.choice()
# #
# #         print('До новых встреч!')
# #
# #
# # game = BlackJack()
# # game.start()
# 
# # # Совместное проживание
# # # по логике, надо бы еще прописать, если человек умер, то сколько дней он прожил и второй человек живет дольше
# # # в условиях задачи этого нет, но если у вас есть код, поделитесь пжл)
# # # Есть (+ сытость, − еда).
# # # Работать (− сытость, + деньги).
# # # Играть (− сытость).
# # # Ходить в магазин за едой (+ еда, − деньги).
# # # Если сытость человека становится меньше нуля, то человек умирает.
# #
# # class Man:
# #     house = True
# #     def __init__(self, name, hungry):
# #         self.name = name
# #         self.hungry = hungry
# #     def eat(self):
# #         self.hungry += 10
# #         House.food -= 10
# #     def work(self):
# #         self.hungry -= 10
# #         House.money += 10
# #     def play(self):
# #         self.hungry -= 10
# #     def buy_eat(self):
# #         House.food += 10
# #         House.money -= 10
# #
# # class House:
# #     food = 50
# #     money = 0
# #     def __init__(self, man1, man2):
# #         self.man1 = man1
# #         self.man2 = man2
# #
# #     def info(self):
# #         health1 = self.man1.hungry
# #         health2 = self.man2.hungry
# #         print(f'Количество еды: {self.food}'
# #               f'\nДенег: {self.money}'
# #               f'\nЖитель {self.man1.name} питание: {health1}'
# #               f'\nЖитель {self.man2.name} питание: {health2}')
# #
# # import random
# # cube = random.randint(1, 6)
# # man_1 = Man('Иван', 50)
# # man_2 = Man('Марья', 50)
# # house_1 = House(man_1, man_2)
# # count = 0
# #
# # for i in range(365):
# #     if man_1.hungry > 0 and man_2.hungry > 0:
# #         if man_1.hungry < 20 and man_2.hungry < 20:
# #             man_1.eat()
# #             man_2.eat()
# #             count += 1
# #         elif house_1.food < 10:
# #             man_1.buy_eat()
# #             # man_1.work() # тут прописал специально, чтобы житель умер первым для проверки условия
# #             man_2.buy_eat()
# #             count += 1
# #         elif house_1.money < 50:
# #             man_1.work()
# #             man_2.work()
# #             count += 1
# #         elif cube == 1:
# #             man_1.work()
# #             man_2.work()
# #             count += 1
# #         elif cube == 2:
# #             man_1.eat()
# #             man_2.eat()
# #             count += 1
# #         else:
# #             man_1.play()
# #             man_2.play()
# #             count += 1
# #
# # house_1.info()
# # print(f'Прожито дней: {count}')
# # if man_1.hungry <= 0:
# #         print(f'Житель {man_1.name} умер')
# # if man_2.hungry <= 0:
# #         print(f'Житель {man_2.name} умер')
# 
# # # Магия - соединение двух элементов в новый, взаимодействие между элементами
# # class Water:
# #     def __str__(self):
# #         return 'Вода'
# #     def __add__(self, other):
# #         if isinstance(other, Air):
# #             return Storm()
# #         elif isinstance(other, Fire):
# #             return Vapor()
# #         elif isinstance(other, Earth):
# #             return Dirt()
# #         else:
# #             return None
# #
# # class Air:
# #     def __str__(self):
# #         return 'Воздух'
# #     def __add__(self, other):
# #         if isinstance(other, Water):
# #             return Storm()
# #         elif isinstance(other, Fire):
# #             return Lightning()
# #         elif isinstance(other, Earth):
# #             return Dust()
# #         else:
# #             return None
# # class Fire:
# #     def __str__(self):
# #         return 'Огонь'
# #
# #     def __add__(self, other):
# #         if isinstance(other, Earth):
# #             return Lava()
# #
# # class Earth:
# #     def __str__(self):
# #         return 'Земля'
# #     pass
# #
# # class Storm:
# #     def __str__(self):
# #         return 'Шторм'
# #
# # class Vapor:
# #     def __str__(self):
# #         return 'Пар'
# #
# # class Dirt:
# #     def __str__(self):
# #         return 'Грязь'
# #
# # class Lightning:
# #     def __str__(self):
# #         return 'Молния'
# #
# # class Dust:
# #     def __str__(self):
# #         return 'Пыль'
# #
# # class Lava:
# #     def __str__(self):
# #         return 'Лава'
# #
# # water = Water()
# # air = Air()
# # fire = Fire()
# # earth = Earth()
# # lava = Lava()
# # dust = Dust()
# # lightning = Lightning()
# # dirt = Dirt()
# # vapor = Vapor()
# # storm = Storm()
# #
# # print(f'{water} + {air} = {water + air}')
# # print(f'{water} + {fire} = {water + fire}')
# # print(f'{water} + {earth} = {water + earth}')
# # print(f'{air} + {fire} = {air + fire}')
# # print(f'{air} + {earth} = {air + earth}')
# # print(f'{fire} + {earth} = {fire + earth}')
# 
# 
# # # Весёлая ферма 2 - садовник ухаживает за грядкой и собирает урожай, когда картошка созрела
# # class Potato:
# #     states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая' }
# #
# #     def __init__(self, index):
# #         self.index = index
# #         self.state = 0
# #
# #     def grow(self):
# #         if self.state < 3:
# #             self.state += 1
# #         self.print_state()
# #
# #     def is_ripe(self):
# #         if self.state == 3:
# #             return True
# #         return False
# #
# #     def print_state(self):
# #         print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')
# #
# # class PotatoGarden:
# #     def __init__(self, count):
# #         self.potatoes = [Potato(index) for index in range(1, count + 1)]
# #     def grow_all(self):
# #         print('Картошка прорастает!')
# #         for i_potato in self.potatoes:
# #             i_potato.grow()
# #     def are_all_ripe(self):
# #         if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
# #         # for i_potato in self.potatoes:
# #         #     if not i_potato.is_ripe():
# #             print('Картошка еще не созрела!')
# #             print([i_potato.state for i_potato in self.potatoes])
# #             print()
# #                 # break
# #         else:
# #             print('Вся картошка созрела, можно собирать!\n')
# #             print([i_potato.state for i_potato in self.potatoes])
# # class Gardener:
# #     def __init__(self, name, garden):
# #         self.name = name
# #         self.garden_bed = garden
# #
# #     def care_garden(self):
# #         if not all([i_potato.is_ripe() for i_potato in self.garden_bed.potatoes]):
# #             print(f'Садовник {self.name} ухаживает за грядкой')
# #
# #     def harvest(self):
# #         if all([i_potato.is_ripe() for i_potato in self.garden_bed.potatoes]):
# #             print(f'Садовник {self.name} собрал картошку!')
# #             # print([i_potato.state for i_potato in self.garden_bed.potatoes if i_potato != 3])
# #
# # my_garden = PotatoGarden(5)
# # gardener_1 = Gardener('Иван', my_garden)
# # my_garden.are_all_ripe()
# # for _ in range(3):
# #     my_garden.grow_all()
# #
# #     gardener_1.care_garden()
# #     gardener_1.harvest()
# 
# 
# 
# # # Отцы, матери и дети выводит инфо о родителях и детях, функции накормить и успокоить ребенка
# # class Child:
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         self.calm_state = 0
# #         self.hungry_state = 0
# #
# #     def info(self):
# #         print(f'\nИнформация о ребенке:'
# #               f'\nИмя: {self.name}'
# #               f'\nВозраст: {self.age}'
# #               )
# #     def print_state(self):
# #         calm_state = {0: 'Спокоен', 1: 'Плачет'}
# #         hungry_state = {0: 'Сыт', 1: 'Голоден'}
# #         print(f'Ребенок {self.name} сейчас '
# #               f'{calm_state[self.calm_state]} и '
# #               f'{hungry_state[self.hungry_state]}')
# #
# # class Parent:
# #
# #     def __init__(self, name, age, childrens):
# #         self.name = name
# #         self.age = age
# #         self.childrens = childrens
# #
# #     def info(self):
# #         print(f'Информация о родителе:'
# #               f'\nИмя: {self.name}'
# #               f'\nВозраст: {self.age}'
# #               f'\nДети:\n'
# #               )
# #         for i_child in self.childrens:
# #             i_child.info()
# #
# #     def calm_child(self, child):
# #         if child.calm_state == 1:
# #             print(f'{self.name} спешит утешить {child.name}! ')
# #             child.calm_state = 0
# #         else:
# #             print(f'{self.name} рад, что {child.name} спокоен! ')
# #
# #     def feed_child(self, child):
# #         if child.hungry_state == 1:
# #             print(f'{self.name} спешит накормить ребенка! ')
# #             child.hungry_state = 0
# #         else:
# #             print(f'{self.name} рад, что {child.name} сыт! ')
# #
# # import random
# #
# # names = ['Иван', 'Петр', 'Сергей', 'Алексей']
# #
# # parent_1 = Parent(random.choice(names), 32, childrens=[])
# # child_1 = Child(random.choice(names), 15)
# # if child_1.age < parent_1.age - 16:
# #     parent_1.childrens.append(child_1)
# # else:
# #     print(f'Возможно ошибка! Возраст ребенка - {child_1.age}, '
# #           f'должен быть меньше возраста родителя хотя бы на 16 лет '
# #           f'(сейчас разница: {parent_1.age - child_1.age} лет)\n'
# #           )
# # child_2 = Child(random.choice(names), 10)
# # parent_1.childrens.append(child_2)
# #
# # parent_1.info()
# #
# # for i_child in parent_1.childrens:
# #     i_child.calm_state = random.randint(0, 1)
# #     i_child.hungry_state = random.randint(0, 1)
# #     print()
# #     i_child.print_state()
# #     parent_1.calm_child(i_child)
# #     parent_1.feed_child(i_child)
# 
# 
# 
# # # вывод инфо о кругах - параметры, площадь, периметр, пересечение и функция увеличения
# 
# # import math
# # class Circle:
# #
# #     def __init__(self, radius, *args):
# #         self.center = args
# #         self.radius = radius
# #
# #     def check_info(self):
# #         print(f'Координаты x,y={self.center}, R={self.radius}')
# #
# #     def square(self):
# #         print(f'Площадь круга: {round(math.pi * self.radius ** 2, 2)}')
# #
# #     def perimeter(self):
# #         print(f'Периметр: {round(2 * math.pi * self.radius, 2)}')
# #
# #     def increase(self, k):
# #         self.radius *= k
# #
# #     def intersection(self, other):
# #         dist = ((self.center[0] - other.center[0]) ** 2 + (self.center[1] - other.center[1]) ** 2) ** 0.5
# #         return abs(self.radius - other.radius) <= dist <= self.radius + other.radius
# #
# # new = Circle(5, 0, 0)
# # print('Первый круг:')
# # new.check_info()
# # new.square()
# # new.perimeter()
# #
# # print('\nУвеличенный круг:')
# # new.increase(5)
# # new.check_info()
# #
# # print('\nВторой круг:')
# # new2 = Circle(5, 0, 0)
# # new2.check_info()
# # if new.intersection(new2):
# #     print('Круги не пересекаются')
# # else:
# #     print('Круги пересекаются')
# 
# # # # список студентов
# #
# # import random
# # class Student:
# #
# #     def __init__(self, name, surname, group_number, grade):
# #         self.name = name
# #         self.surname = surname
# #         self.group_number = group_number
# #         self.grade = grade
# #     def info(self):
# #         info = [self.name, self.surname, self.group_number, self.grade]
# #         return info
# #
# # names = ['Иван', 'Петр', 'Сергей', 'Алексей']
# # surnames = ['Грозный', 'Босой', 'Кривой', 'Козлов']
# #
# #
# #
# # student_list = []
# # for i_student in range(1, 11):
# #     group_number = random.randint(1, 5)
# #     grade = random.randint(30, 100)
# #     student_1 = Student(random.choice(names), random.choice(surnames), group_number, grade)
# #     student_list.append(student_1.info())
# #     # print(student_list)
# #
# # stunent_sort_grade = sorted(student_list, key=lambda i: i[3])
# # # print(stunent_sort_grade)
# # for student in stunent_sort_grade:
# #     print(student)
# 
# # # воин 1 нападает на воина 2 в случайном порядке, проигрывает со здоровьтем == 0
# # import random
# #
# # class Warrior:
# #
# #     def __init__(self, health, hit):
# #         self.health = health
# #         self.hit = hit
# #
# #     def health_info(self):
# #         print(f'остаток здоровья воина: {self.health}')
# #
# # def fight(warrior_1, warrior_2):
# #     while warrior_1.health > 0 and warrior_2.health > 0:
# #         choice = random.randint(1, 2)
# #         if choice == 1:
# #             warrior_2.health -= warrior_1.hit
# #             print(f'Атаковал воин 1, у воина 2 осталось здоровья: {warrior_2.health}')
# #         elif choice == 2:
# #             warrior_1.health -= warrior_2.hit
# #             print(f'Атаковал воин 2, у воина 1 осталось здоровья: {warrior_2.health}')
# #     if warrior_1.health > warrior_2.health:
# #         print(f'Одержал победу воин 1, остакток здоровья: {warrior_1.health}')
# #
# #
# # warrior_1 = Warrior(100, 20)
# # warrior_2 = Warrior(100, 20)
# #
# # fight(warrior_1, warrior_2)
# 
# 
# #     def __init__(self, health, hit):
# #         self.health = health
# #         self.hit = hit
# #     def health_info(self):
# #         print(f'остаток здоровья воина: {self.health}')
# #
# # warrior_1 = Warrior(100, 20)
# # warrior_2 = Warrior(100, 20)
# #
# # while warrior_1.health > 0 and warrior_2.health > 0:
# #     choice = random.randint(1, 2)
# #     if choice == 1:
# #         warrior_2.health -= warrior_1.hit
# #         print(f'Атаковал воин 1, у воина 2 осталось здоровья: {warrior_2.health}')
# #     elif choice == 2:
# #         warrior_1.health -= warrior_2.hit
# #         print(f'Атаковал воин 2, у воина 1 осталось здоровья: {warrior_2.health}')
# #
# # if warrior_1.health > warrior_2.health:
# #     print(f'Одержал победу воин 1, остакток здоровья: {warrior_1.health}')
# # else:
# #     print(f'Одержал победу воин 2, остакток здоровья: {warrior_2.health}')
# 
# 
# 
# 
# 
# # # класс координаты точки
# # class Point:
# #     count = 0
# #
# #     def __init__(self, x=0, y=0):
# #         self.x = x
# #         self.y = y
# #         Point.count += 1
# #
# #     def check_info(self):
# #         print(self.x, self.y)
# # new = Point(5,6)
# # new.check_info()
# # print(new.count)
# 
# # # инициализация класса через init
# # class Toyota:
# #
# #     def __init__(self, color='red', price=1e6, max_speed=200, current_speed=0):
# #         self.color = color
# #         self.price = price
# #         self.max_speed = max_speed
# #         self.current_speed = current_speed
# #
# #     def check_info(self):
# #         print(self.color, self.price, self.max_speed, self.current_speed)
# #
# #     def change_speed(self, new_speed):
# #         self.current_speed = new_speed
# #
# # # картошка сад из картошки взаимодействие между классами
# # class Potato:
# #     states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая' }
# #
# #     def __init__(self, index):
# #         self.index = index
# #         self.state = 0
# #
# #     def grow(self):
# #         if self.state < 3:
# #             self.state += 1
# #         self.print_state()
# #
# #     def is_ripe(self):
# #         if self.state == 3:
# #             return True
# #         return False
# #
# #     def print_state(self):
# #         print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')
# #
# # class PotatoGarden:
# #     def __init__(self, count):
# #         self.potatoes = [Potato(index) for index in range(1, count + 1)]
# #     def grow_all(self):
# #         print('Картошка прорастает!')
# #         for i_potato in self.potatoes:
# #             i_potato.grow()
# #     def are_all_ripe(self):
# #         if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
# #         # for i_potato in self.potatoes:
# #         #     if not i_potato.is_ripe():
# #             print('Картошка еще не созрела!\n')
# #                 # break
# #         else:
# #             print('Вся картошка созрела, можно собирать!\n')
# #
# # my_garden = PotatoGarden(5)
# # my_garden.are_all_ripe()
# # for _ in range(3):
# #     my_garden.grow_all()
# #     my_garden.are_all_ripe()
# 
# 
# # # Отобразить информацию о себе.
# # # Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# # # Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# # # Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# #
# # class Family:
# #     name = "Common family"
# #     money = 100000
# #     house = False
# #
# #     def print_info(self):
# #         print(
# #             "Family name: " + self.name,
# #             "Family funds: " + str(self.money),
# #             "Having a house: " + str(self.house),
# #             sep='\n')
# #     def earn_money(self, amount):
# #         self.money += amount
# #         print(f'Заработал денег: {amount}\nТекущий бюджет: {self.money}')
# #     def buy_house(self, house_price, discount=0):
# #         house_price -= house_price * discount / 100
# #         if self.money >= house_price:
# #             self.money -= house_price
# #             self.house = True
# #             print(f'Дом приобретен!\nТекущий бюджет: {self.money}')
# #         else:
# #             print('Не хватает денег!\n')
# #
# # my_family = Family()
# # my_family.print_info()
# # print('\nTry ro buy a house:')
# # my_family.buy_house(10 ** 6)
# # if not my_family.house:
# #     my_family.earn_money(800000)
# #     print('\nTry ro buy a house again:')
# #     my_family.buy_house(10 ** 6, 10)
# #
# # my_family.print_info()
# 
# # # формирует список из мониторов (из класса мониторы) и присваивает каждому монитору в списке значение частоты из спсика
# # class Monitor:
# #     name = "Samsung"
# #     matrix = "VA"
# #     resolution = "WQHD"
# #     frequency = 0
# #
# #     def info(self):
# #         print(self.name, self.matrix, self.resolution, self.frequency)
# #
# #
# # class Headphones:
# #     name = "Sony"
# #     sensitivity = 108
# #     micro = True
# #
# #
# # monitors = [Monitor() for _ in range(4)]
# #
# # headphones = [Headphones() for _ in range(3)]
# #
# # for index, number in enumerate([60, 144, 70, 60]):
# #     monitors[index].frequency = number
# # for i in monitors:
# #     print(i.info())
# #
# #
# # headphones[0].micro = False
# 
# 
# ## печатает информацию о машинах из класса и функция определения (прописывает) скорости
# # import random
# #
# # class Toyota:
# #     color = 'red'
# #     price = 1e6
# #     max_speed = 200
# #     current_speed = 0
# #
# #     def print_data(self):
# #         print(f'Цвет: {self.color}\nЦена:{self.price}\nМакс скорость: {self.max_speed}\nТекущая скорость: {self.current_speed}\n')
# #
# #     def set_speed(self, speed):
# #         self.current_speed = speed
# #
# # car_1 = Toyota()
# # car_2 = Toyota()
# # car_3 = Toyota()
# #
# # car_1.set_speed(random.randint(0, 200))
# # car_2.set_speed(random.randint(0, 200))
# # car_3.set_speed(random.randint(0, 200))
# #
# # car_1.print_data()
# # car_2.print_data()
# # car_3.print_data()
# 
# 
# 
# # # чат
# # # 1. Посмотреть текущий текст чата.
# # # 2. Отправить сообщение.
# # # Действия запрашиваются бесконечно.
# #
# # user_name = input('Как Вас звоут? ')
# # while True:
# #     print('Чтобы увидеть текущий текст чата, нажмите 1, чтобы написать сообщение введите 2:')
# #     response = input('Введите 1 или 2: ')
# #     if response == '1':
# #         try:
# #             with open('chat.txt', 'r', encoding='utf-8') as file:
# #                 messages = file.readlines()
# #                 print(''.join(messages))
# #         except FileNotFoundError:
# #             print('Служебное сообщение: пока ничего нет\n')
# #     elif response == '2':
# #         new_message = input('Введите сообщение: ')
# #         with open('chat.txt', 'a', encoding='utf-8') as file:
# #             file.write(f'{user_name}: {new_message}\n')
# #     else:
# #         print('Неизвестная команда\n')
# #
# # # Текстовый калькулятор
# # import pathlib
# # count = 0
# # count_errros = 0
# # with open('calc.txt', 'r', encoding='utf-8') as file:
# #     for line in file:
# #         if len(line.rsplit()[1]) > 1:
# #             change = input(f'Обнаружена ошибка в строке: {line} Хотите исправить? ').lower()
# #             if change == 'да':
# #                 new_line = input('Введите исправленную строку: ')
# #                 with open('calc.txt', 'a', encoding='utf-8') as file:
# #                     path = pathlib.Path('calc.txt')
# #                     path.write_text(path.read_text().replace(line, new_line + '\n'))
# #
# #     with open('calc.txt', 'r', encoding='utf-8') as file:
# #         for line in file:
# #             try:
# #                 # print(eval(line))
# #                 count += eval(line)
# #             except SyntaxError:
# #                 count_errros += 1
# #
# # print(f'Сумма результатов: {round(count, 2)}')
# # print(f'Количество ошибок: {count_errros}')
# 
# 
# # # выводит два лога с правильными данными и с ошибками
# # # не могу сделать вывод как в примере см строка 24
# # def answer(file_str):
# #     name, mail, age = file_str.split()
# #     age = int(age)
# #     if not name.isalpha():
# #         raise NameError("Поле «Имя» содержит НЕ только буквы")
# #     elif age not in range(10, 100):
# #         raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")
# #     elif '@' and '.' not in mail:
# #         raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
# #     elif not name and not mail and not age:
# #         raise IndexError('НЕ присутствуют все три поля')
# #     return file_str
# #
# #
# # with open("registrations.txt", "r", encoding="utf-8") as file, \
# #         open('registration_bad.log', 'a', encoding='utf-8') as error, \
# #         open('registrations_good.log', 'a', encoding='utf-8') as good:
# #     for line in file:
# #         try:
# #             str_file = answer(line)
# #         except (NameError, ValueError, SyntaxError, IndexError) as exc:
# #             error.write(line + str(exc) + '  -  ') # как местами не меняй, line не ставит первым
# #         else:
# #             good.write(line)
# 
# # # спрашивает число, записывает его в файл, пока сумма чисел меньше 777 и случайное число не 13
# # import random
# #
# # work = True
# # sum = 0
# # while work:
# #     number = int(input("Введите число: "))
# #     n = random.randint(1, 13)
# #     with open('out_file.txt', 'a', encoding='utf-8') as file:
# #         file.write(str(number) + '\n')
# #     if n == 13:
# #         print('Вы потерпели неудачу')
# #         work = False
# #     else:
# #         with open('out_file.txt', 'r', encoding='utf-8') as file:
# #             for line in file:
# #                 clear_line = line.rstrip()
# #                 sum += int(clear_line)
# #                 if (sum >= 777):
# #                     print('Вы успешно выполнили условие для выхода из порочного цикла!')
# #                     work = False
# 
# 
# # # берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму
# # # ошибку вывел не через raise, так как программа прерывается и не верно считает символы
# #
# # result = 0
# # line_count = 0
# # try:
# #     with open('people.txt', 'r', encoding='utf8') as peoples:
# #         for line in peoples:
# #             clear_line_len = len(line.rstrip())
# #             line_count += 1
# #             result += clear_line_len
# #             if clear_line_len < 3:
# #                 print(f'Ошибка: менее трёх символов в строке {line_count}')
# # except FileNotFoundError as exc:
# #     print('При выполнении возникла ошибка, см. errors.log')
# #     with open('errors.log', 'a', encoding='utf-8') as log_file:
# #         log_file.write(str(exc))
# # else:
# #     print('Вычисления прошли успешно')
# # finally:
# #     print(f'Общее количество символов: {result}')
# 
# # # Если в строке встречается число, то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log
# # import os
# # def check_palindrome(word):
# #     return word == word[::-1]
# #
# # # оператор with из 23.5
# # with open('people.txt', 'r', encoding='utf8') as file, open('errors.log', 'w', encoding='utf8') as log_file:
# #     count = 0
# #
# #     for line in file:
# #         try:
# #             clear_line = line.rstrip()
# #             if clear_line.isalpha():
# #                 count += check_palindrome(clear_line)
# #             else:
# #                 raise ValueError("строка не полностью состоит из букв!")
# #         except ValueError as exc:
# #             log_file.write(str(exc))
# #
# #     print(count)
# 
# 
# 
# # # функция создать новый файл в рабочей директории
# # def new_file(name, string=''):
# #     new_file = open(f"{name}", "w", encoding="utf8")
# #     new_file.write(string)
# #     new_file.close()
# 
# 
# # считает количество симоволов в строке файла без литерала и выводит сумму
# # если строка меньше 3 символов, выдает свою ошибку
# # new_file = open("people.txt", "w", encoding="utf8")
# # string = '80\n80\n92\n98\n78'
# # new_file.write(string)
# # new_file.close()
# 
# # sym_sum = 0
# # line_count = 0
# # try:
# #     people_file = open('people.txt', 'r', encoding='utf-8')
# #     for i_line in people_file:
# #         lenght = len(i_line)
# #         line_count += 1
# #         if i_line.endswith('\n'):
# #             lenght -= 1
# #         if lenght < 3:
# #             raise BaseException(f'Длина строки {line_count} меньше 3 символов')
# #         sym_sum += lenght
# #     people_file.close()
# # except FileNotFoundError:
# #     print('Файл не найден')
# # finally:
# #     print(f'Найденная сумма символов: {sym_sum}')
# 
# # это тот же код из ответов
# # peoples = open('people.txt', 'r', encoding='utf8')
# # result = 0
# # try:
# #     for line in peoples:
# #         clear_line_len = len(line.rstrip())
# #         result += clear_line_len
# #         if clear_line_len < 3:
# #             raise Exception
# # finally:
# #     print(result)
# 
# 
# 
# ## try exept блоки else finally
# ## Проблема при открытии файла. FileNotFoundError, PermissionError
# ## Нельзя преобразовать данные в целое. ValueError
# ## Неожиданная ошибка. Exception
# 
# # import os
# #
# # file = None
# # try:
# #     file = open("23.3.txt", "w", encoding="utf8")
# #     number = int(input("Введите текст: "))
# #     file.write(str(number))
# # except (FileNotFoundError, PermissionError) as exc:
# #     print(type(exc), exc)
# # except ValueError as exc:
# #     print(type(exc), exc)
# # except Exception as exc:
# #     print(type(exc), exc)
# # else:
# #     print("Запись прошла без ошибок")
# # finally:
# #     if file and not file.closed:
# #         file.close()
# 
# ## try exept
# ## TypeError, PermissionError
# 
# # def find_file(cur_path, file_name):
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         if file_name == i_elem:
# #             print(os.path.abspath(path))
# #         elif os.path.isdir(path):
# #             result = find_file(path, file_name)
# #             if result:
# #                 break
# #     else:
# #         result = None
# #
# #     return result
# #
# #
# # try:
# #     find_file('c:\\', 'hel')
# # except (TypeError, PermissionError) as exc:
# #     print(exc, type(exc))
# 
# # # считывает файл, даёт имя для каждого возраста и выводит результат в новый файл result.txt в формате «имя — возраст».
# # # Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:
# # #
# # # Попытка создания файла, который уже существует.
# # # На чтение ожидался файл, но это оказалась директория.
# # # Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# #
# # file_ages = None
# # file_result = None
# #
# # new_file = open("ages.txt", "w", encoding="utf8")
# # string = '80\n80\n92\n98\n78'
# # new_file.write(string)
# # new_file.close()
# #
# # try:
# #     file_ages = open("ages.txt", "r", encoding="utf8")
# #     file_result = open("result.txt", "x", encoding="utf8")
# #     # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
# # except (FileExistsError, PermissionError) as exc:  # названия исключений можно группировать в кортежи
# #     print("Поймано исключение: ", exc, type(exc))
# #
# # if file_result and file_ages:
# #     names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# #     count = 0
# #     for line in file_ages:
# #         try:
# #             clear_line = line.rstrip()
# #             int(clear_line)  # на всякий случай пытаемся преобразить данные в int, но не сохраняем это в переменную, т.к. записывать нам
# #             # в файл придётся именно строку
# #             file_result.write(names[count] + " - " + clear_line)
# #             count += 1
# #         except (ValueError, TypeError) as exc:
# #             print("Поймано исключение: ", exc, type(exc))
# 
# 
# # # печать исключений и запись исключения в переменную
# # input_data = input('Введите строку: ')
# # try:
# #     leeloo = int(input_data[4])
# #     result = BRUCE_WILLIS * leeloo
# #     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# #
# # except ValueError as exc:  # as - этот оператор запишет пойманное исключение в переменную exc (название может быть любым)
# #     print(type(exc), "— невозможно преобразовать к числу")
# # except IndexError as exc:
# #     print(type(exc), "— выход за границы списка")
# # except Exception as exc:
# #     print(type(exc), "поймано исключение")
# 
# 
# # # Толстой частота символов в тексте (из видеоурока результат лучше, чем из инета)
# # import collections
# # import zipfile
# #
# # # функция распаковки архива в режиме чтения
# # def unzip(archive):
# #     zfile = zipfile.ZipFile(archive, 'r')
# #     for i_file_name in zfile.namelist():
# #         zfile.extract(i_file_name)
# #     zfile.close()
# #
# # # функция формирования словаря с указанием частоты символов в тексте
# # def collect_stats(file_name):
# #     reult = {}
# #     if file_name.endswith('.zip'):
# #         unzip(file_name)
# #         file_name = ''.join((file_name[:-3], 'txt')) # берем срез от файла минус расширение и присоединяем расширение
# #         print(file_name)
# #     text_file = open(file_name, 'r', encoding='utf-8')
# #     for i_line in text_file:
# #         for j_char in i_line:
# #             if j_char.isalpha(): # проверяет есть ли буква в словаре
# #                 if j_char not in reult:
# #                     reult[j_char] = 0
# #                 reult[j_char] += 1
# #     text_file.close()
# #     return reult
# #
# # # функция печати словаря в таблице
# # def print_stats(stats):
# #     print('+{:-^19}+'.format('+'))
# #     print('|{: ^9}|{: ^9}|'.format('Буква', 'Частота'))
# #     print('+{:-^19}+'.format('+'))
# #     for char, count in stats.items():
# #         print('|{: ^9}|{: ^9}|'.format(char, count))
# #     print('+{:-^19}+'.format('+'))
# #
# # # функция сортировки словаря по возрастанию и убыванию
# # def sort_by_freqency(stats_dict):
# #     sorted_values = sorted(stats_dict.values())#, reverse=True)
# #     sorted_dict = collections.OrderedDict() # присваиваем упорядочееный словарь из библиотеки collections
# #     for i_value in sorted_values:
# #         for j_key in stats_dict.keys():
# #             if stats_dict[j_key] == i_value:
# #                 sorted_dict[j_key] = stats_dict[j_key]
# #     return sorted_dict
# #
# # file_name = r'C:\Users\Вика\Desktop\Python\voyna-i-mir.zip'
# # stats = collect_stats(file_name)
# # stats = sort_by_freqency(stats)
# # print_stats(stats)
# 
# # # распаковывает архив из текущей директории и проводит частотный анализ
# # # почти ничего не понял, но разберусь надеюсь потом))
# # import zipfile
# # alfabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# #
# # archive = "voyna-i-mir.zip"  # Путь к архиву.
# # directory_to_extract_to = r"C:\Users\Вика\Desktop\Python"  # Путь, куда будет распакован архив.
# # with zipfile.ZipFile(archive, 'r') as zip_file:
# #     zip_file.extractall(directory_to_extract_to)
# #
# # new_file = open(r"C:\Users\Вика\Desktop\Python\voyna-i-mir.txt", 'r', encoding='utf-8').read().lower()
# # dict_letter = {}
# # count = 0
# # for i_letter in new_file:
# #     if i_letter in alfabet:
# #         x = dict_letter.get(i_letter, 0)
# #         dict_letter[i_letter] = x + 1
# #         count += 1
# #
# # sort_dict = sorted(dict_letter)
# #
# # analysis = [[i_elem, round((dict_letter[i_elem] / count),3)] for i_elem in sort_dict]
# # result_list = [i_elem[0] + ' ' + str(i_elem[1]) for i_elem in analysis]
# # result = '\n'.join(result_list)
# #
# # output = open('analysis.txt', 'w')
# # output.write(result)
# # output = open('analysis.txt', 'r')
# # print(output.read())
# # output.close()
# 
# # # выполняет частотный анализ файла и записывает результат в другой файл
# # alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# # new_file = open('input.txt', 'w')
# # string = 'Mama myla ramu.'
# # new_file.write(string)
# # new_file.close()
# #
# # new_file = open('input.txt', 'r').read().lower()
# # dict_letter = {}
# # count = 0
# # for i_letter in new_file:
# #     if i_letter in alfabet:
# #         x = dict_letter.get(i_letter, 0)
# #         dict_letter[i_letter] = x + 1
# #         count += 1
# #
# # sort_dict = sorted(dict_letter)
# #
# # analysis = [[i_elem, round((dict_letter[i_elem] / count),3)] for i_elem in sort_dict]
# # result_list = [i_elem[0] + ' ' + str(i_elem[1]) for i_elem in analysis]
# # result = '\n'.join(result_list)
# #
# # output = open('analysis.txt', 'w')
# # output.write(result)
# # output = open('analysis.txt', 'r')
# # print(output.read())
# # output.close()
# 
# # # выводит в файл `second_tour.txt` данные всех участников, прошедших во второй тур, с нумерацией
# # new_file = open("first_tour.txt", "w", encoding="utf8")
# # string = '80\nIvanov Serg 80\nSergeev Petr 92\nPetrov Vasiliy 98\nVasiliev Maxim 78'
# # new_file.write(string)
# #
# # new_file = open("first_tour.txt", "r", encoding="utf8")
# # k = int(new_file.readline())
# # new_list = []
# # for line in new_file:
# #     new_line = line.split()
# #     if new_line != [] and int(new_line[-1]) > k:
# #         new_list.append(new_line)
# # new_file.close()
# # # print(f'Список: {new_list}')
# #
# # new_list.sort(key=lambda a: int(a[-1]))
# # new_list.reverse()
# # for list in new_list:
# #     list.reverse()
# # # print(f'Перевернутый список: {new_list}')
# #
# # count = str(len(new_list))
# # out_lst = []
# # n = 1
# # for i in new_list:
# #     name_sim = str(i[1][0]) + '.' + i[2] + ' - ' + i[0]
# #     s_win = str(n) + ') ' + name_sim
# #     out_lst.append(s_win)
# #     n += 1
# #
# # with open("second_tour.txt", "w", encoding='utf-8') as f_out:
# #     f_out.write(count + '\n')
# #     s = '\n'.join(out_lst)
# #     f_out.write(s)
# #
# # output = open("second_tour.txt", "r", encoding='utf-8')
# # print(output.read())
# # output.close()
# 
# # # шифрует содержимое текстового файла text.txt шифром Цезаря
# #
# # # Функция шифрования
# # def cipher_encrypt(plain_text, key):
# #     encrypted = ""
# #     for c in plain_text:
# #         if c.isupper(): #проверить, является ли символ прописным
# #             c_index = ord(c) - ord('A')
# #             # сдвиг текущего символа на позицию key
# #             c_shifted = (c_index + key) % 26 + ord('A')
# #             c_new = chr(c_shifted)
# #             encrypted += c_new
# #         elif c.islower(): #проверка наличия символа в нижнем регистре
# #             # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
# #             c_index = ord(c) - ord('a')
# #             c_shifted = (c_index + key) % 26 + ord('a')
# #             c_new = chr(c_shifted)
# #             encrypted += c_new
# #         elif c.isdigit():
# #             # если это число, сдвинуть его фактическое значение
# #             c_new = (int(c) + key) % 10
# #             encrypted += str(c_new)
# #         else:
# #             # если нет ни алфавита, ни числа, оставьте все как есть
# #             encrypted += c
# #     return encrypted
# #
# # new_file = open('text.txt', 'w')
# # string = 'Hello\nHello\nHello\nHello'
# # new_file.write(string)
# # print('Содержимое файла text.txt:')
# # new_file = open('text.txt', 'r')
# # # plain_text = new_file.read()
# # # print(plain_text)
# # count = 0
# # for line in new_file:
# #     count += 1
# #     print(line.rstrip('\n'))
# #     ciphertext = cipher_encrypt((line), count)
# #     cipher_file = open('cipher_text.txt', 'a')
# #     cipher_file.write(ciphertext)
# #
# #
# # print('Содержимое файла cipher_text.txt:')
# # cipher_file = open('cipher_text.txt', 'r')
# # print(cipher_file.read())
# # cipher_file = open('cipher_text.txt', 'w')
# # cipher_file.close()
# # new_file.close()
# 
# # # записывает файл в указанную директорию
# # # дописал try exept
# #
# # import os
# # text = input('Введите строку: ')
# # root_path = os.path.abspath(os.sep) # os.sep - Буква диска откуда запускается скрипт
# # user_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
# # path = os.path.join(root_path, f'{os.sep}'.join(user_path.split()))
# # # соединяем системным разделителем (os.sep), преобразованный в список ввод пользователя
# # # соединяем букву диска root_path c итогом
# # # path = (os.path.abspath(os.getcwd()).split("\\")[0]) + '\\' + ('\\'.join(user_path)) + '\\' # Users Вика Desktop Python
# # # это ввод в лоб
# # print(path)
# # try:
# #     if os.path.isdir(path):
# #         file_name = input('Введите имя файла: ') + '.txt'
# #         file_name = path + file_name
# #         print(file_name)
# #         choice = input('Вы действительно хотите перезаписать файл? ')
# #
# #         if choice == 'да':
# #             new_file = open(file_name, 'w', encoding='utf-8')
# #             new_file.write(text)
# #             print('Файл успешно сохранён!')
# #             print('Содержимое файла:\n')
# #             new_file = open(file_name, 'r', encoding='utf-8')
# #             print(new_file.read())
# #         else:
# #             print('Содержимое файла:\n')
# #             new_file = open(file_name, 'r', encoding='utf-8')
# #             print(new_file.read())
# #         new_file.close()
# #     else:
# #         print('Такой директории нет!')
# #
# # except FileNotFoundError:
# #     print(f'Файла {file_name} не существует')
# 
# # # выводит общее количество файлов и подкаталогов в нём
# # # не могу вспомнить как вернуть 2 значения из функции, если создаю список или словарь, выдает ошибку
# 
# # функция поиска всех файлов в папке, вывод - размер файла
# # см строку 7
# # import os
# #
# # # функция поиска всех файлов в папке, вывод - размер файла
# # path = r'C:\intel'
# # # os.path.abspath(os.getcwd().split(os.sep)[5]) # если вставляю этот путь,
# # # то выдает ошибку name 'dir_path' is not defined, хотя путь определяется нормально
# # total_size = 0
# # count_file = 0
# # count_dir = 0
# #
# # for dir_path, dir_names, file_names in os.walk(path):  # Цикл по директории
# #     for file in file_names:  # Цикл по файлам
# #         count_file += 1
# #         file_path = os.path.join(dir_path, file)
# #         total_size += os.path.getsize(file_path)
# #     for dir in dir_names: # цикл по директориям
# #         count_dir += 1
# #
# # print(f'Анализ директории: \n {dir_path}\n')
# # print('Размер каталога (в Кб): ', round(total_size / 1024))
# # print('Количество подкаталогов: ', count_dir)
# # print('Количество файлов: ', count_file)
# 
# # версия 2 через функцию не работает счет файлов
# # import os
# #
# # # функция поиска всех файлов в папке, вывод - размер файла
# # def find_file(cur_path, count=0, total_size = 0):
# #     for i_elem in os.listdir(cur_path):
# #         path1 = os.path.join(cur_path, i_elem)
# #         if os.path.isfile(path1):
# #             total_size += os.path.getsize(path1)
# #             count += 1
# #         elif os.path.isdir(path1):
# #             result = find_file(path1)
# #             # print(result)
# #             if result:
# #                 total_size += result
# #                 count += 1
# #     return total_size
# #     # return [total_size, count]
# #
# # path = r'C:\Users\123\Desktop\PY\Module14'
# # # os.path.abspath(os.getcwd().split(os.sep)[5])
# # path, dirs, files = next(os.walk(path)) # если здесь взять len(files), то считает только файл в корне директории
# #
# # print('Размер каталога (в Кб): ', find_file(path))
# # print('Количество подкаталогов: ', len(dirs))
# # print('Количество файлов: ', find_file(path))
# 
# # # статистика по строковым даным в файле
# # def uniqe_letter(word):
# #     word_list = list(word)
# #     word_list.sort()
# #     prev_sym = ''
# #     for sym in word_list:
# #         if sym != prev_sym:
# #             prev_sym = sym
# #     return prev_sym
# #
# # letters = 0
# # words = 0
# # lines = 0
# # uniqe = []
# # zen_file = open('zen.txt', 'r')
# # for line in zen_file:
# #     uniqe.append(uniqe_letter(line))
# #     lines += 1
# #     letters += len(line)
# #     for i_word in line.split():
# #         words += 1
# # zen_file.close()
# #
# # print(f'Количество букв в файле: {letters}')
# # print(f'Количество слов в файле:  {words}')
# # print(f'Количество строк в файле: {lines}')
# # print(f'Наиболее редкая буква в каждой строке:  {uniqe}')
# # print(f'Наиболее редкая буква:  {uniqe_letter(uniqe)}')
# 
# 
# # # выводит строки файла в обратном порядке
# # zen_file = open('zen.txt', 'r')
# # data = zen_file.readlines()
# # data.reverse()
# # print(''.join(data))
# # zen_file.close()
# 
# 
# # # запись значений в файл, расчет суммы цифр
# # numbers_sum = 0
# # file_from = open(r"C:\Users\123\Desktop\PY\Lesson22_3\numbers.txt", "r", encoding="Windows-1251")
# # for line in file_from:
# #     clear_line = line.rstrip()
# #     if clear_line:
# #         numbers_sum += int(clear_line)
# # file_from.close()
# #
# # file_to = open('answer.txt', 'w', encoding="Windows-1251")
# # file_to.write(str(numbers_sum))
# # file_to.close()
# 
# # # поиск всех файлов в папке с расширением и запись их содержимого в файл
# # import os
# # def find_file(cur_path, ending):
# #     all_paths = []
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         if i_elem.endswith(ending):
# #             all_paths.append(os.path.abspath(path))
# #         elif os.path.isdir(path):
# #             result = find_file(path, ending)
# #             if result:
# #                 all_paths.extend(result)
# #
# #     return all_paths
# # print(find_file(r'C:\Users\123\Desktop\PY', '.py'))
# #
# # def get_text_from_file(path_to_file):
# #     file = open(path_to_file, "r", encoding="utf8")
# #     result = ""
# #     for line in file:
# #         result += line
# #     return result
# # #print(get_text_from_file(r"C:\Users\123\Desktop\PY\Lesson22_3\numbers.txt"))
# #
# # all_py_files = find_file(r'C:\Users\123\Desktop\PY', '.py')  # вместо ".." можно вставить путь до папки python_basic
# #
# # file_result = open("scripts.txt", "w", encoding="utf8")
# #
# # for file_path in all_py_files:
# #     file_result.write(get_text_from_file(file_path))
# #     file_result.write("\n" * 2 + "*" * 80 + "\n" * 2)
# 
# # # # запись значений в файл, расчет количества символов в строке
# # numbers_sum = 0
# # file_from = open(r"C:\Users\123\Desktop\PY\Lesson22_3\numbers.txt", "r", encoding="Windows-1251")
# # for line in file_from:
# #     clear_line = line.rstrip()
# #     if clear_line:
# #         numbers_sum += int(clear_line)
# # file_from.close()
# #
# # file_in = open("answer.txt", "w", encoding="utf8")
# # file_in.write(str(numbers_sum))
# # file_in.close()
# 
# # # запись значений в файл, расчет количества символов в строке
# # speakers_file = open(r'C:\Users\123\Desktop\PY\Lesson22_3\group_1.txt', 'r', encoding='Windows-1251')
# # sym_count = []
# # for i_line in speakers_file:
# #     print(i_line, end='')
# #     sym_count.append(str(len(i_line)))
# # # print()
# # sym_count_str = '\n'.join(sym_count)
# # speakers_file.close()
# # # print(sym_count_str)
# #
# # counts_file = open('sym_counts.txt', 'w')
# # counts_file.write(sym_count_str)
# 
# # # меняет значения title&h2 в структуре сайта
# # site = {
# #     'html': {
# #         'head': {
# #             'title': 'Куплю/продам телефон недорого'
# #         },
# #         'body': {
# #             'h2': 'У нас самая низкая цена на iphone',
# #             'div': 'Купить',
# #             'p': 'продать'
# #         }
# #     }
# # }
# #
# # def find_key(struct, key, key_value):
# #     if key in struct:
# #         struct[key] = key_value
# #         return site
# #
# #     for sub_struct in struct.values():
# #         if isinstance(sub_struct, dict):
# #             result = find_key(sub_struct, key, key_value)
# #             if result:
# #                 return site
# #
# # number_sites = int(input('Сколько сайтов: '))
# # for _ in range(number_sites):
# #     product_name = input('Введите название продукта для нового сайта: ')
# #     key_dict = {f'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
# #     for keys in key_dict:
# #         find_key(site, keys, key_dict[keys])
# #     print(f'Ваш сайт: \n{site}')
# 
# # import os
# # import random
# #
# # def find_file(cur_path, file_name):
# #     all_paths = []
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         if file_name == i_elem:
# #             all_paths.append(os.path.abspath(path))
# #         elif os.path.isdir(path):
# #             result = find_file(path, file_name)
# #             if result:
# #                 all_paths.extend(result)
# #
# #     return all_paths
# #
# #
# # def check_file_inside(path_to_file):
# #     file = open(path_to_file, 'r', encoding='utf8')
# #     for line in file:
# #         print(line)
# #     file.close()
# #
# #
# # all_paths = find_file('..', 'lesson3.py')
# # print(all_paths)
# # check_file_inside(random.choice(all_paths))
# 
# # # сумма и произведение очков в файле
# # file = open('O:\Python\Lesson22_3\group_1.txt', 'r')
# # summa = 0
# # diff = 0
# # compose = 0
# # for i_line in file:
# #     info = i_line.split()
# #     if info:
# #         summa += int(info[2])
# #         diff -= int(info[2])
# #
# # file_2 = open('O:\Python\Lesson22_3\group_2.txt', 'r')
# # for i_line in file_2:
# #     info = i_line.split()
# #     if info:
# #         compose *= int(info[2])
# #
# # file.close()
# # file_2.close()
# #
# # print(summa)
# # print(diff)
# # print(compose)
# 
# # # выводит все файлы с раширением в текущей папке
# # import os
# # for file in os.listdir("/Python"):
# #     if file.endswith(".py"):
# #         print(os.path.join("/Python", file))
# 
# # # определяет файл или папка и выводит размер файла
# # import os
# #
# # path_to = input("Путь: ")
# #
# # if os.path.isdir(path_to):
# #     print("Это папка!")
# # elif os.path.isfile(path_to):
# #     print("Это файл!")
# #     print("Размер файла:", os.path.getsize(path_to), "байт")
# # else:
# #     print("Указанного пути не существует")
# 
# # # поиск файла из решения к видеоуроку (ищет от корня)
# # import os
# # def find_file(cur_path, file_name):
# #     print(f'переходим в {cur_path}')
# #     if file_name in os.listdir(cur_path):
# #         return os.path.join(cur_path, file_name)
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         print('     смотрим', path)
# #         if file_name == i_elem:
# #             return os.path.abspath(path)
# #         elif os.path.isdir(path):
# #             result = find_file(path, file_name)
# #             if result:
# #                 break
# #     else:
# #         result = None
# #
# #     return result
# #
# # file_path = find_file('..', 'project3_home.py')
# # if file_path:
# #     print(f'Абсолютный путь к файлу: {file_path}')
# # else:
# #     print('Файл не найден')
# 
# # # поиск файла из видеоурока
# # import os
# #
# # def find_file(cur_path, file_name):
# #     print(f'переходим в {cur_path}')
# #     if file_name in os.listdir(cur_path):
# #         return os.path.join(cur_path, file_name)
# #
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         print('     смотрим', path)
# #         if file_name == i_elem:
# #             return path
# #         if os.path.isdir(path):
# #             print('Это директория')
# #             result = find_file(path, file_name)
# #             return result
# #             if result:
# #                 break
# #     else:
# #         result = None
# #
# #     return result
# #
# # file_path = find_file(os.path.abspath(os.path.join('..', 'Python')), 'project3_home.py')
# # if file_path:
# #     print(f'Абсолютный путь к файлу: {file_path}')
# # else:
# #     print('Файл не найден')
# 
# # # список файлов в указанной папке и проверка на существование папки
# # import os
# # def print_dirs(project):
# #     print('\nСодержимое директории:', project)
# #     if os.path.exists(project):
# #         for i_elem in os.listdir(project):
# #             path = os.path.join(project, i_elem)
# #             print(path)
# #     else:
# #         print(f'Каталога {project} не существует')
# #
# # projects_list = ['SkillBox','My project', 'Python']
# # for i_project in projects_list:
# #     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
# #     print_dirs(path_to_project)
# 
# 
# # # путь к файлу в папке
# # import os
# # for path in os.listdir('C:\Windows\Help'):
# #     print(os.path.join(os.path.abspath('C:\Windows\Help'), path))
# 
# 
# # # относительный и абсолютный путь к файлу, корень диска
# # import os
# # file_name = 'lesson3.py'
# # path_abs = os.path.abspath(file_name)
# # path_rel = os.path.join('Skillbox', 'access', file_name)
# # print(path_abs)
# # print(os.listdir('O:\\Python'))
# # print(path_rel)
# # print("Корень диска:", os.path.abspath('.').split("\\")[0])
# 
# # # меняет значения title&h2 в структуре сайта
# # site = {
# #     'html': {
# #         'head': {
# #             'title': 'Куплю/продам телефон недорого'
# #         },
# #         'body': {
# #             'h2': 'У нас самая низкая цена на iphone',
# #             'div': 'Купить',
# #             'p': 'продать'
# #         }
# #     }
# # }
# #
# # def find_key(struct, key, meaning):
# #     if key in struct:
# #         struct[key] = meaning
# #         return site
# #
# #     for sub_struct in struct.values():
# #         if isinstance(sub_struct, dict):
# #             result = find_key(sub_struct, key, meaning)
# #             if result:
# #                 return site
# #
# #
# # number_sites = int(input('Сколько сайтов: '))
# # for _ in range(number_sites):
# #     product_name = input('Введите название продукта для нового сайта: ')
# #     key = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
# #     for i in key:
# #         find_key(site, i, key[i])
# #
# #     print(f'Сайт для {product_name}:')
# #     print(site, '\n')
# 
# # # раскрывает все вложенные списки через рекурсию
# # def my_list(*args):
# #     lst = []
# #     for elem in args:
# #         for sub_elem in elem:
# #             if not isinstance(sub_elem, list):
# #                 lst.append(sub_elem)
# #             else:
# #                 result = my_list(sub_elem)
# #                 lst.extend(result)
# #     return lst
# #
# # nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
# #              [[11, 12, 13], [14, 15], [16, 17, 18]]]
# #
# #
# # print(my_list(nice_list))
# 
# # #функция складывает числа из списка списков и из набора параметров (рекурсия)
# # def summ(*args):
# #     def flatten(a_list):
# #         result = []
# #         for element in a_list:
# #             if isinstance(element, int):
# #                 result.append(element)
# #             else:
# #                 result.extend(flatten(element))
# #         return result
# #     return sum(flatten(args))
# #
# # print(summ(1, 2, 3, 4, 5))
# # print(summ([[1, 2, [3]], [1], 3]))
# 
# 
# # # Ханойские башни
# # def towers(num, x, y):
# #     if num == 1:
# #         print(f'Переложить диск {1} со стержня номер {x} на стержень номер {y}')
# #     else:
# #         towers(num - 1, x, 6 - x - y)
# #         print(f'Переложить диск {num} со стержня номер {x} на стержень номер {y}')
# #         towers(num - 1, 6 - x - y, y)
# #
# #
# # num = int(input('Введите количество дисков: '))
# # towers(num, 1, 3)
# #
# # # Введите количество дисков: 2
# # # Переложить диск 1 со стержня номер 1 на стержень номер 2
# # # Переложить диск 2 со стержня номер 1 на стержень номер 3
# # # Переложить диск 1 со стержня номер 2 на стержень номер 3
# 
# # # раскрывает все вложенные списки
# # def my_list(*args):
# #     lst = []
# #     for elem in args:
# #         for sub_elem in elem:
# #             if not isinstance(sub_elem, list):
# #                 lst.append(sub_elem)
# #             else:
# #                 result = my_list(sub_elem)
# #                 lst.extend(result)
# #     return lst
# #
# # nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
# #              [[11, 12, 13], [14, 15], [16, 17, 18]]]
# #
# #
# # print(my_list(nice_list))
# 
# # # Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень, до которого будет просматриваться структура.
# # def search_key(site, key, depth):
# #     if key in site:
# #         return site[key]
# #     if depth > 1:
# #         for sub_keys in site.values():
# #             if isinstance(sub_keys, dict):
# #                 result = search_key(sub_keys, key, depth - 1)
# #                 if result:
# #                     break
# #         else:
# #             result = None
# #
# #         return result
# #
# # site = {
# # 	'html': {
# # 		'head': {
# # 			'title': 'Мой сайт'
# # 		},
# # 		'body': {
# # 			'h2': 'Здесь будет мой заголовок',
# # 			'div': 'Тут, наверное, какой-то блок',
# # 			'p': 'А вот здесь новый абзац'
# # 		}
# # 	}
# # }
# #
# # key = input('Искомый ключ: ')
# # depth_search = input('Хотите ввести максимальную глубину? Y/N:').lower()
# #
# # if depth_search == 'n':
# #     output = search_key(site, key, depth = 100)
# #     if output:
# #         print(f'Значение ключа {key}: {output}')
# #     else:
# #         print('Такого ключа в структуре сайта нет.')
# # else:
# #     depth = int(input('Введите максимальную глубину: '))
# #     output = search_key(site, key, depth)
# #     if output:
# #         print(f'Значение ключа {key}: {output}')
# #     else:
# #         print('Такого ключа в структуре сайта нет.')
# 
# # # выводит число, стоящее на позиции `num_pos` в ряде Фибоначчи
# # def fib(number):
# #     if number == 1 or number == 2: # 1, 1, 2, 3, 5, 8, 13…
# #         return 1
# #     fib_number = fib(number - 1) + fib(number - 2)
# #     return fib_number
# #
# #
# # num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
# # print('Число:', fib(num_pos))
# 
# # # функция ZIP возвращает список с кортежами, в любых комбинациях
# # def my_zip(*args):
# #     length = min(len(element) for element in args)
# #     tpl_list = [tuple(argument[i] for argument in map(list, args)) for i in range(length)]
# #     return tpl_list
# #
# # # a = [{"x": 4}, "b", "z", "d"]
# # # b = (10, {20,}, [30], "z")
# # # output = my_zip(a, b)
# #
# # a = [1, 2, 3, 4, 5]
# # b = {1: "s", 2: "q", 3: 4}
# # x = (1, 2, 3, 4, 5)
# # output = my_zip(a, b, x)
# #
# # print(f'Упакованный в ZIP список: {output}')
# # print('\nЭлементы списка:')
# # print(*output, sep='\n')
# 
# 
# # # выводит все числа от 1 до num без использования циклов
# # def print_num(num):
# #     if num == 0:
# #         return 1
# #     sub_num = print_num(num - 1)
# #     return print(num)
# #
# # num = int(input('Введите число: '))
# # print_num(num)
# 
# # # args, kwargs передача разных неизвестных аргументов
# # def print_tax_document(tax, *args, **kwargs):
# #     price_sum = 0
# #     for i_price in args:
# #         price_sum += i_price * tax /100
# #     print(f'Сумма цен с учетом налога: {price_sum}')
# #
# #     for i_info, i_value in kwargs.items():
# #         print(f'{i_info}: {i_value}')
# #
# #
# # my_tax = int(input('Величина налога: '))
# # # year = int(input('Год: '))
# # # doc_type = input('Тип документа: ')
# # # operation_id = int(input('Введите ID: '))
# #
# # print_tax_document(my_tax, 1000, 950, 880, 920, 990,
# #                    year=1997, doc_type='Report', operation_id=111034)
# 
# 
# ## Если в списке встретилась строка, то из неё нужно сделать словарь и положить его в итоговый список
# # def create_dict(data, template=None):
# #     if isinstance(data, dict):
# #         return data
# #     elif isinstance(data, (int, float, str)):
# #         template = template or dict()
# #         template[data] = data
# #         return template
# #     else:
# #         return None
# #
# # def data_preparation(old_list):
# #     new_list = []
# #     for i_element in old_list:
# #         new_elem = create_dict(i_element)
# #         if new_elem:
# #             new_list.append(new_elem)
# #     return new_list
# #
# # data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
# # data = data_preparation(data)
# # print(data)
# 
# 
# # # функция со значением аргумента None
# # def add_num(num, nums=None):
# #     nums = nums or []
# #     # хитрая конструкция, которая позволит упростить ввод:
# #     if not nums:
# #        nums = []
# #     # Первый вариант будет выбран, если nums не равен None, иначе будет создан и записан пустой список
# #     nums.append(num)
# #     print(nums)
# #
# # add_num(5)
# # add_num(10)
# # add_num(15)
# 
# # # сообщение о неправильном вводе и количество попыток
# # def ask_user(question, complaint='Неверный ввод, введите да или нет', retries=4):
# #     while True:
# #         answer = input(question).lower()
# #         if answer == 'да':
# #             return 1
# #         if answer == 'нет':
# #             return 0
# #         retries -= 1
# #         if retries == 0:
# #             print('Количество попыток истекло')
# #             break
# #         print(complaint)
# #         print(f'Осталось попыток: {retries}')
# #
# # ask_user('Вы действительно хотите выйти? ', retries=2)
# # ask_user("да?", "ДА ил НЕТ?!")
# 
# # # функция вычисления степени числа через рекурсию
# # def power(a, n):
# #     if n == 0:
# #         return 1
# #     sub_num = power(a, n - 1)
# #     return a * sub_num
# #
# #
# # float_num = float(input('Введите вещественное число: '))
# # int_num = int(input('Введите степень числа: '))
# # print(float_num, '**', int_num, '=', power(float_num, int_num))
# 
# # # функция вычисления факториала с помощью рекурсии
# # def find_fact(num):
# #     if num == 1:
# #         return num
# #     sub_num = find_fact(num - 1)
# #     return num * sub_num
# # num = int(input('Введите число: '))
# # print(f'Факториал числа {num}: {find_fact(num)}')
# 
# # # функция ищет ключ в словаре (поиск ключа в словаре)
# # def search_key(site, key):
# #     if key in site:
# #         return site[key]
# #
# #     for sub_keys in site.values():
# #         if isinstance(sub_keys, dict):
# #             result = search_key(sub_keys, key)
# #             if result:
# #                 break
# #     else:
# #         result = None
# #
# #     return result
# #
# #
# # site = {
# #     'html': {
# #         'head': {
# #             'title': 'Мой сайт'
# #         },
# #         'body': {
# #             'h2': 'Здесь будет мой заголовок',
# #             'div': 'Тут, наверное, какой-то блок',
# #             'p': 'А вот здесь новый абзац'
# #         }
# #     }
# # }
# #
# # key = input('Искомый ключ: ')
# # output = search_key(site, key)
# # if output:
# #     print(output)
# # else:
# #     print('Такого ключа в структуре сайта нет.')
# 
# # # составляет протокол и определяла победителя и призёров
# # point_list = dict()
# # iteration = int(input("Сколько записей вносится в протокол? "))
# #
# # print("Записи (результат и имя):")
# # for i in range(iteration):
# #     value, key = input("{}-я запись: ".format(i + 1)).split()
# #     if int(value) > point_list.get(key, 0):
# #         point_list[key] = int(value)
# #
# # print("\nИтоги соревнований:")
# # for i in range(1, 4):
# #     max_key = ''
# #     max = 0
# #     for key, value in point_list.items():
# #         if max < value:
# #             max = value
# #             max_key = key
# #
# #     print("{0}-е место: {1}({2})".format(i, max_key, max))
# #     if point_list.get(max_key, 0):
# #         point_list.pop(max_key)
# 
# # # функция заполнения телефонной книги и поиска по ней
# # def menu(contacts):
# #     while True:
# #         print('1. Добавить контакт \n2. Найти человека\n3. Завершить работу ')
# #         action = int(input('Введите номер действия: '))
# #         if action == 1:
# #             phonebook(contacts)
# #         elif action == 2:
# #             phonebook_search(contacts)
# #         elif action == 3:
# #             print(f'Работа завершена, ваша телефонная книга:\n {contacts}')
# #             break
# #
# # def phonebook(contacts):
# #     while True:
# #         name = input("Введите имя (end - вернуться в меню): ").lower()
# #         if name == 'end':
# #             return
# #
# #         surname = input("Введите фамилию: ").lower()
# #         name_n_surname = (name, surname)
# #
# #         if name_n_surname not in contacts:
# #             contacts[name_n_surname] = int(input("Введите номер телефона: "))
# #         else:
# #             print("Такой контакт уже есть!")
# #         print(contacts)
# #
# # def phonebook_search(phonebook):
# #     search = input('Введите фамилию для поиска: ').lower()
# #     for item, number in phonebook.items():
# #         if search in item[0].lower():
# #             print(item[0], item[1], number)
# #     print()
# #     menu(contacts)
# #     if search not in item[0].lower():
# #         print('Такого человека нет в контактах')
# #     menu(contacts)
# #
# # contacts = {('Сидоров', 'Никита'): 356456,
# #                 ('Сидорова', 'Алина'): 34334643,
# #                 ('Сидоров', 'Павел'): 1034646}
# # menu(contacts)
# 
# 
# # # аналог функции zip
# # def myzip(a, b):
# #     return ((a[i], b[i]) for i in range(min(len(a), len(b))))
# #
# # string = 'abcd'
# # num_tuple = (10, 20, 30, 40)
# # output = myzip(string, num_tuple)
# #
# # print(output)
# # print(*output, sep='\n')
# 
# 
# # # сортирует по возрастанию кортеж, состоящий из целых чисел, и возвращает его отсортированным
# # def tpl_sort(nums):
# #     nums_list = list(nums)
# #     if all(type(item) is int for item in nums_list):
# #         return tuple(sorted(nums_list))
# #     else:
# #         return tuple(nums_list)
# #
# #
# # print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
# #
# # def tpl_sort(nums):
# #     nums_list = list(nums)
# #     if all(isinstance(item, int) for item in nums_list):
# #         return tuple(sorted(nums_list))
# #     else:
# #         return tuple(nums_list)
# #
# #
# # print(tpl_sort((6, 3, -1, 8, 4.5, 10, -5)))
# 
# # # инициализирует список из 10 случайных целых чисел, а затем делит эти числа на пары кортежей внутри списка
# #
# # num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # temp_list1 = [num for num, index in enumerate(num_list) if index % 2 == 0]
# # temp_list2 = [num for num, index in enumerate(num_list) if index % 2 != 0]
# # new_num = zip(temp_list1, temp_list2)
# # new_list = [num for num in new_num]
# # print(f"Оригинальный список: {num_list}")
# # print(f'Новый список: {new_list}\n')
# #
# #
# # original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # print(original_list[1::2])
# # # print(original_list[::2])
# # result = list(zip(original_list[::2], original_list[1::2]))
# # print(f"Новый список: {result}")
# 
# # # запрашивает у пользователя фамилию и выводит на экран возраст всех членов одной семьи
# # family = {('Сидоров', 'Никита'): 35,
# #           ('Сидорова', 'Алина'): 34,
# #           ('Сидоров', 'Павел'): 10}
# # print(family)
# #
# # surname = input('Введите фамилию: ')
# # if surname.endswith('а'):
# #     surname = surname[:-1]
# # for name, age in family.items():
# #     if surname.lower() in name[0].lower():
# #        print(name[0], name[1], age)
# 
# 
# # # объединяет ключ словаря со значением в один кортеж
# # players = {
# #     ("Ivan", "Volkin"): (10, 5, 13),
# #     ("Bob", "Robbin"): (7, 5, 14),
# #     ("Rob", "Bobbin"): (12, 8, 2)
# # }
# #
# # players_list = [name+value for name, value in players.items()]
# #
# # print(players_list)
# # # [('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]
# 
# # #Функция возвращает новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым его появлением включительно
# # def slicer(elems, num):
# #     if num not in elems:
# #         return ()
# #     if elems.count(num) == 1:
# #         return elems[elems.index(num):]
# #     return elems[elems.index(num):elems.index(num, elems.index(num) + 1) + 1]
# #
# # print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
# # # Ответ в консоли: (2, 3, 4, 5, 6, 7, 8, 2)
# 
# # # выводит список, где индекс - простое число
# # def is_prime(number):
# #     for i in range(2, int(number ** 0.5) + 1):
# #         if number % i == 0:
# #             return False
# #     return True
# #     # for divider in range(2, number):
# #     #     if number % divider == 0:
# #     #         return False
# #     # return True
# # def crypto(symbols):
# #     elems = [sym for index, sym in enumerate(symbols) if is_prime(index)]
# #     return elems
# #
# # print(crypto('О Дивный Новый мир!'))
# # print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# 
# # #выводит данные из словаря
# # students = {
# #     1: {
# #         'name': 'Bob',
# #         'surname': 'Vazovski',
# #         'age': 23,
# #         'interests': ['biology, swimming']
# #     },
# #     2: {
# #         'name': 'Rob',
# #         'surname': 'Stepanov',
# #         'age': 24,
# #         'interests': ['math', 'computer games', 'running']
# #     },
# #     3: {
# #         'name': 'Alexander',
# #         'surname': 'Krug',
# #         'age': 22,
# #         'interests': ['languages', 'health food']
# #     }
# # }
# #
# # def hobby_surnamecount(data):
# #     hobby_list = [interest['interests'] for interest in data.values()]
# #     surnames = ''
# #     for interest in data:
# #         surnames += data[interest]['surname']
# #
# #     return hobby_list, len(surnames)
# #
# # pos_age = [(position, student['age']) for position, student in students.items()]
# #
# # print(f'Список пар "ID студента — возраст": {pos_age}')
# # print(f'Полный список интересов всех студентов: {hobby_surnamecount(students)[0]}')
# # print(f'Общая длина всех фамилий студентов: {hobby_surnamecount(students)[1]}')
# 
# # # функция заполнения телефонной книги
# # def phonebook():
# #     contacts = {}
# #     while True:
# #         name = input("Введите имя: ")
# #         if name == 'end':
# #             break
# #         surname = input("Введите фамилию: ")
# #         name_n_surname = (name, surname)
# #         if name_n_surname not in contacts:
# #             contacts[name_n_surname] = int(input("Введите номер телефона: "))
# #         else:
# #             print("Такой контакт уже есть!")
# #         print(contacts)
# # phonebook()
# 
# # # функция, которая по номеру и серии паспорта выдаёт имя и фамилию человека.
# # def find_person(input, base):
# #     if input in base:
# #         print(base[input])
# #     else:
# #         print("Такого человека нет")
# # data = {
# #     (5000, 123456): ('Иванов', 'Василий'),
# #     (6000, 111111): ('Иванов', 'Петр'),
# #     (7000, 222222): ('Медведев', 'Алексей'),
# #     (8000, 333333): ('Алексеев', 'Георгий'),
# #     (9000, 444444): ('Георгиева', 'Мария')
# # }
# #
# # series = int(input('Введите серию паспорта: '))
# # number = int(input('Введите номер паспорта: '))
# # num_ser = (series, number)
# #
# # find_person(num_ser, data)
# 
# # # решение друга - привести код без повторений
# # # print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])
# #
# # print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])
# #
# # # отображается значения словаря в красивои виде
# # server_data = {
# #     "server": {
# #         "host": "127.0.0.1",
# #         "port": "10"
# #     },
# #     "configuration": {
# #         "access": "true",
# #         "login": "Ivan",
# #         "password": "qwerty"
# #     }
# # }
# #
# # for server, config in server_data.items():
# #     print(f'{server}:')
# #     for key, value in config.items():
# #         print(f'\t{key}:{value}')
# 
# 
# # # заполняет словарь случайными буквами из списка, герериует случайные буквы
# # import random
# # import string
# # import secrets
# # # first_list = ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# # # second_list = ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
# # letters = string.ascii_lowercase
# #
# # first_list = [secrets.choice(letters) for i in range(10)]
# # second_list = [secrets.choice(letters) for i in range(10)]
# # second_list = [secrets.choice(letters) for i in range(10)]
# # print(first_list)
# # print(second_list)
# #
# # first_dict = dict()
# # second_dict = dict()
# #
# # for index, sym in enumerate(first_list):
# #     first_dict[index] = sym
# # for index, sym in enumerate(second_list):
# #     second_dict[index] = sym
# #
# # print(first_dict)
# # print(second_dict)
# 
# # # функция расчёта площади боковой поверхности цилиндра и его полной площади.
# # import math
# # radius_in = int(input("Введите радиус: "))
# # height_in = int(input("Введите высоту: "))
# #
# # def cylynder(r, height):
# #     side = 2 * math.pi * r * height
# #     full = side + 2 * math.pi * r ** 2
# #     return side, full
# #
# # s_side, full_s = cylynder(radius_in, height_in)
# # print(f'площади боковой поверхности цилиндра - {s_side} полной площади - {full_s}')
# 
# # # на вход кортеж чисел, генерирует случайный индекс и случайное значение, а затем по этим индексу и значению меняет сам кортеж
# # import random
# # def change(nums):
# #     nums = list(nums)
# #     index = random.randint(0, 5)
# #     value = random.randint(100, 1000)
# #     nums[index] = value
# #     return tuple(nums), value
# #
# # my_nums = 1, 2, 3, 4, 5
# # new_nums, rand_val = change(my_nums)
# # print(new_nums, rand_val)
# #
# # new_nums, rand_val2 = change(my_nums)
# #
# # print(new_nums, rand_val2)
# # rand_val += rand_val2
# # print(new_nums, rand_val)
# 
# # # Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно
# # import random
# #
# # def create_random_tuple(a, b, n):
# #     return tuple([random.randint(a, b) for _ in range(n)])
# #
# # first = create_random_tuple(0, 5, 10)
# # second = create_random_tuple(-5, 0, 10)
# # third = first + second
# # nulls_count = third.count(0)
# # print(third, nulls_count)
# 
# # # # определяет, существует ли у этой строки такая перестановка, при которой она станет палиндромом
# # def is_poly(string):
# #     char_dict = dict()
# #     for i_sym in string:
# #         char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
# #
# #     odd_count = 0
# #     for i in char_dict.values():
# #         if i % 2 != 0:
# #             odd_count += 1
# #     return odd_count <= 1
# #
# # my_string = input('Введите строку: ')
# # print(is_poly(my_string))
# # if is_poly(my_string):
# #     print('Можно сделать палиндром')
# # else:
# #     print('Нельзя сделать палиндром')
# 
# # # определяет, существует ли у этой строки такая перестановка, при которой она станет палиндромом
# # word = input('Введите строку: ').lower()
# # chars = set()
# #
# # for i in word:
# #     if i in chars:
# #         chars.remove(i)
# #     else:
# #         chars.add(i)
# #         print(chars)
# # print(('Можно', 'Нельзя')[len(chars) > 1], 'сделать палиндромом')
# 
# # # программу, которая по заданному генеалогическому древу определяет высоту всех его элементов
# # number_people = int(input('Введите количество человек: '))
# # data_dict = dict()
# # level_dict = dict()
# #
# # for i in range(1, number_people):
# #     descendant_name, parent_name = input(f'{i} пара: ').split()
# #     data_dict[descendant_name] = parent_name
# #     level_dict[descendant_name] = 0
# #     level_dict[parent_name] = 0
# #
# # for i in data_dict:
# #     people = i
# #     while people in data_dict:
# #         people = data_dict[people]
# #         level_dict[i] += 1
# #
# # print('\n“Высота” каждого члена семьи:')
# # for i in sorted(level_dict):
# #     print(i, level_dict[i])
# 
# # # имитирует диалог Артёма и Бориса угадай число
# # numbers = int(input('Введите максимальное число: '))
# # all_nums = set(range(1, numbers + 1))
# #
# # while True:
# #     guess = input('Нужное число есть среди вот этих чисел: ')
# #     if guess == 'Помогите!':
# #         break
# #     guess = {int(x) for x in guess.split()}
# #     answer = input('Ответ Артёма: ')
# #     if answer == 'Да':
# #         all_nums &= guess
# #     else:
# #         all_nums -= guess
# #
# # print('Артём мог загадать следующие числа:', *all_nums)
# 
# # # выводит список покупателей и их заказов по алфавиту.
# # order_num = int(input('Введите количество заказов: '))
# # orders_dict = dict()
# # for i in range(1, order_num + 1):
# #     order = input(f'{i}-й заказ: ') # Иванов Пепперони 1
# #     name, pizza, amount = order.rsplit(maxsplit=3)
# #     amount = int(amount)
# #     if name not in orders_dict:
# #         orders_dict[name] = {pizza: amount}
# #     else:
# #         if pizza not in orders_dict[name]:
# #             orders_dict[name][pizza] = amount
# #         else:
# #             orders_dict[name][pizza] += amount
# # print(orders_dict)
# #
# # for name, order in sorted(orders_dict.items()):
# #     print(f'{name}:')
# #     for pizza, amount in sorted(order.items()):
# #         print('\t', pizza, amount)
# 
# # # запрашивает у пользователя слово и выводит на экран его синоним
# # num = int(input('Введите количество пар слов: '))
# #
# # synonym_dict = dict()
# # for i in range(1, num + 1):
# #     synonym = input(f'{i}-я пара: ').lower().split(' — ') #Привет — Здравствуйте
# #     synonym_dict.setdefault(synonym[0], synonym[1])
# # #print(synonym_dict)
# #
# # while True:
# #     user_word = input('Введите слово: ').lower()
# #     if user_word not in synonym_dict:
# #         print('Такого слова в словаре нет.')
# #     for word, synonym in synonym_dict.items():
# #         if user_word == word:
# #             print(f'Синоним: {synonym}')
# #         elif user_word == synonym:
# #             print(f'Синоним: {word}')
# 
# 
# # инвертирует ключи со значениями в словаре
# # def histogram(string):
# #     sym_dict = dict()
# #     for sym in string:
# #         if sym in sym_dict:
# #             sym_dict[sym] += 1
# #         else:
# #             sym_dict[sym] = 1
# #     return sym_dict
# #
# # def histogram_invert(sym_dict):
# #     new_dict = dict()
# #     for letter, num in sym_dict.items():
# #         new_dict.setdefault(num, []).append(letter)
# #     return new_dict
# #
# # text = input('Введите текст: ').lower()
# #
# #
# # print('Оригинальный словарь частот: ')
# # hist = histogram(text)
# # print(hist)
# # for i_sym in sorted(hist.keys()):
# #     print(f'{i_sym}: {hist[i_sym]}')
# #
# # print('\nИнвертированный словарь частот: ')
# # hist2 = histogram_invert(hist)
# # for i_sym in hist2.keys():
# #     print(f'{i_sym}: {hist2[i_sym]}')
# 
# # # рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран
# # goods = {
# #     'Лампа': '12345',
# #     'Стол': '23456',
# #     'Диван': '34567',
# #     'Стул': '45678',
# # }
# #
# # store = {
# #     '12345': [
# #         {'quantity': 27, 'price': 42},
# #     ],
# #     '23456': [
# #         {'quantity': 22, 'price': 510},
# #         {'quantity': 32, 'price': 520},
# #     ],
# #     '34567': [
# #         {'quantity': 2, 'price': 1200},
# #         {'quantity': 1, 'price': 1150},
# #     ],
# #     '45678': [
# #         {'quantity': 50, 'price': 100},
# #         {'quantity': 12, 'price': 95},
# #         {'quantity': 43, 'price': 97},
# #     ],
# # }
# #
# # for product_name, product_code in goods.items():
# #     quantity = 0
# #     price = 0
# #     for product in store[product_code]:
# #         quantity += product['quantity']
# #         price += product['price']
# #     print(f'{product_name} - {quantity} штук, стоимость {price} рублей')
# 
# # # операции со словарем
# # data = {
# #     "address": "0x544444444444",
# #     "ETH": {
# #         "balance": 444,
# #         "total_in": 444,
# #         "total_out": 4
# #     },
# #     "count_txs": 2,
# #     "tokens": [
# #         {
# #             "fst_token_info": {
# #                 "address": "0x44444",
# #                 "name": "fdf",
# #                 "decimals": 0,
# #                 "symbol": "dsfdsf",
# #                 "total_supply": "3228562189",
# #                 "owner": "0x44444",
# #                 "last_updated": 1519022607901,
# #                 "issuances_count": 0,
# #                 "holders_count": 137528,
# #                 "price": False
# #             },
# #             "balance": 5000,
# #             "totalIn": 0,
# #             "total_out": 0
# #         },
# #         {
# #             "sec_token_info": {
# #                 "address": "0x44444",
# #                 "name": "ggg",
# #                 "decimals": "2",
# #                 "symbol": "fff",
# #                 "total_supply": "250000000000",
# #                 "owner": "0x44444",
# #                 "last_updated": 1520452201,
# #                 "issuances_count": 0,
# #                 "holders_count": 20707,
# #                 "price": False
# #             },
# #             "balance": 500,
# #             "totalIn": 0,
# #             "total_out": 0
# #         }
# #     ]
# # }
# #
# #
# # print(f'Вывести списки ключей и значений словаря: \n{data.keys(), data.values()}')
# #
# # print('\nВ “ETH” добавить ключ “total_diff” со значением 100:')
# # data['ETH']['total_diff'] = 100
# # print(data['ETH'])
# #
# # print('\nВнутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.')
# # data['tokens'][0]['fst_token_info']['name'] = 'doge'
# # print(data['tokens'][0]['fst_token_info'])
# #
# # print('\nУдалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.')
# # total_out = 0
# # for i_value in data['tokens']:
# #     total_out += i_value.pop('total_out')
# # data['ETH']['total_out'] = total_out
# # print(data['ETH'])
# #
# # print('\nВнутри "sec_token_info" изменить название ключа “price” на “total_price”.')
# # old_price = data['tokens'][1]['sec_token_info'].pop('price')
# # data['tokens'][1]['sec_token_info']['total_price'] = old_price
# # print(data['tokens'][1]['sec_token_info'])
# #
# # # формирует список из строки введенной пользователем и определяет нахождение города в списке
# # data_set = {}
# # amount_country = int(input('Кол-во стран: '))
# #
# # for i in range(1, amount_country + 1):
# #     cities_list = input(f'{i} страна: ').split()
# #     for city in cities_list[1:]:
# #         data_set[city] = cities_list[0]
# #         #print(data_set)
# # for i in range(1, 4):
# #     city = input(f'\n{i} город: ')
# #     country = data_set.get(city)
# #     if country:
# #         print(f'Город {city} расположен в стране {country}.')
# #     else:
# #         print(f'По городу {city} данных нет.')
# 
# # # находит все различные цифры в символьной строке
# # text = 'ab1n32kz2'
# # text_set = set(text)
# # result = text_set & set('0123456789')
# # print('Различные цифры строки:', ','.join(sorted(result)))
# #
# # new_result = set()
# # for symbol in text:
# #     if '0' <= symbol <= '9':
# #         new_result.add(symbol)
# #
# # print(''.join(new_result))
# 
# # методы множеств
# # import random
# # nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
# # nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
# #
# # num1_rand = random.randint(100, 200)
# # num2_rand = random.randint(100, 200)
# # print(f'Случайное число для 1-го множества: {num1_rand}')
# # print(f'Случайное число для 2-го множества: {num2_rand}')
# #
# # num_1_set = set(nums_1)
# # num_2_set = set(nums_2)
# # print(num_1_set)
# # print(num_2_set)
# # print()
# #
# # print('Удаляем мин элемент')
# # num_1_set.remove(min(num_1_set))
# # num_2_set.remove(min(num_2_set))
# # print(num_1_set)
# # print(num_2_set)
# # print()
# #
# # print('добавляем случайное число')
# # num_1_set.add(num1_rand)
# # num_2_set.add(num2_rand)
# #
# # print('Операции')
# # print(num_1_set | num_2_set)
# # print(num_1_set & num_2_set)
# # print(num_2_set - num_1_set)
# 
# # # реализует такую структуру: имя, фамилия, хобби, кол-во лет и дети.
# # family_member = {
# #     "name": "Jane",
# #     "surname": "Doe",
# #     "hobbies": ["running", "sky diving", "singing"],
# #     "age": 35,
# #     "children": [{"name": "Alice", "age": 6}, {"name": "Bob", "age": 8}]
# # }
# # print(family_member)
# # childrens_dict = {}
# # for child in family_member["children"]:
# #     childrens_dict[child["name"]] = child["age"]
# # print(childrens_dict)
# # if childrens_dict.get('Bob', None):
# #     print("Bob найден")
# # else:
# #     print("Bob-а нету!")
# #
# # print('Surname') if childrens_dict.get('Surname') else print("Nosurname")
# 
# 
# # Напишите программу, которая выводит на экран вот такие данные в разных строчках:
# #
# # Все члены команды из команды А, которые отдыхают.
# # Все члены команды из группы B, которые тренируются.
# # Все члены команды из команды C, которые путешествуют.
# # players_dict = {
# #     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
# #     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
# #     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
# #     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
# #     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
# #     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
# #     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
# #     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# # }
# # team_a_members = [player['name'] for player in players_dict.values() if player['team'] == 'A' and player['status'] == 'Rest']
# # team_b_members = [player['name'] for player in players_dict.values() if player['team'] == 'B' and player['status'] == 'Training']
# # team_c_members = [player['name'] for player in players_dict.values() if player['team'] == 'C' and player['status'] == 'Travel']
# #
# #
# # print(f'Все члены команды из команды А, которые отдыхают: {team_a_members}')
# # print(f'Все члены команды из команды B, которые отдыхают: {team_b_members}')
# # print(f'Все члены команды из команды C, которые отдыхают: {team_c_members}')
# 
# # второй вариант
# # # Чтобы не прописывать решение "в лоб", вручную подставляя статус и команду - попробуем сформировать дополнительные словарь и список,
# # # чтобы автоматизировать этот процесс:
# # help_dict = {"Rest": "отдыхают",
# #              "Training": "тренируются",
# #              "Travel": "путешествуют"}
# #
# # team_order = ["A", "B", "C"]
# #
# # # Запустим цикл по словарю состояний и одновременно будем вести счёт состояний, чтобы на каждой итерации выбирать одну из команд:
# # for index, state in enumerate(help_dict):
# #
# #    print(f"Все члены команды из команды {team_order[index]}, которые {help_dict[state]}:")
# #    for i, player in players_dict.items():
# #        if player["status"] == state and player["team"] == team_order[index]:
# #           print(player["name"])
# 
# # # находит общий доход, затем выводит фрукт с минимальным доходом и удаляет его из словаря
# # incomes = {
# #     'apple': 5600.20,
# #     'orange': 3500.45,
# #     'banana': 5000.00,
# #     'bergamot': 3700.56,
# #     'durian': 5987.23,
# #     'grapefruit': 300.40,
# #     'peach': 10000.50,
# #     'pear': 1020.00,
# #     'persimmon': 310.00,
# # }
# # def get_value(x):
# #     return x[1]
# #
# # print(f'Общий доход за год составил: {sum(incomes.values())} рублей')
# # min_name, min_value = min(incomes.items(), key=get_value)
# # incomes.pop(min_name)
# #
# # print(f'Самый маленький доход у {min_name}. Он составляет {min_value} рублей, удаляем')
# # print(f'Итоговый словарь: {incomes}')
# 
# # #объединяет оба словаря в один
# # small_storage = {
# #     'гвозди': 5000,
# #     'шурупы': 3040,
# #     'саморезы': 2000
# # }
# #
# # big_storage = {
# #     'доски': 1000,
# #     'балки': 150,
# #     'рейки': 600
# # }
# #
# # big_storage.update(small_storage)
# # name = input('Введите название товарв: ')
# # print(f'Количество товара {name}: {big_storage.get(name)}')
# 
# 
# # гистограмма - максимальная частота букв в тексте
# # def histogram(string):
# #     sym_dict = dict()
# #     for sym in string:
# #         if sym in sym_dict:
# #             sym_dict[sym] += 1
# #         else:
# #             sym_dict[sym] = 1
# #     return sym_dict
# #
# # text = input('Введите текст: ').lower()
# # hist = histogram(text)
# # print(hist)
# # print(sorted(hist.keys()))
# #
# # for i_sym in sorted(hist.keys()):
# #     print(f'{i_sym}: {hist[i_sym]}')
# # print(f'Максимальная частота: {max(hist.values())}')
# 
# # # телефонная книга
# # phonebook = dict()
# # while True:
# #     print('Текущие контакты на телефоне:')
# #     if phonebook:
# #         for i_name in phonebook:
# #             print(f'{i_name}: {phonebook[i_name]}')
# #     else:
# #         print('<Пусто>')
# #
# #     name = input('\nВведите имя: ')
# #     if name == 'конец':
# #         break
# #
# #     phone_num = input('Введите номер телефона: ')
# #     if name in phonebook:
# #         print('Ошибка: такое имя уже существует.')
# #     else:
# #         phonebook[name] = phone_num
# #
# # print('Текущие контакты на телефоне:')
# # for i_name in phonebook:
# #     print(f'{i_name}: {phonebook[i_name]}')
# 
# # # составит словарь и выведет его на экран
# # student_str = input(
# #     'Введите информацию о студенте через пробел\n'
# #     ' (имя, фамилия, город, место учёбы, оценки): '
# # )
# # print(student_str)
# # # Илья Иванов Москва МГУ 5 4 4 4 5
# # student_info = student_str.split()
# # print(student_info)
# # student = dict()
# # student['Имя'] = student_info[0]
# # student['Фамилия'] = student_info[1]
# # student['Город'] = student_info[2]
# # student['Место учебы'] = student_info[3]
# # student['Оценки'] = []
# # print(student)
# # for i_grade in student_info[4:]:
# #     student['Оценки'].append(int(i_grade))
# # for i_info in student:
# #     print(f'{i_info} - {student[i_info]}')
# 
# 
# # # расшифровка дешифровка цезаря
# # def decryption(messenge):
# #     translated = ""
# #     for i_word in messenge:
# #         if i_word in letters:
# #             num_index = letters.find(i_word)
# #             translated += letters[num_index - 1]
# #         else:
# #             translated += i_word
# #     return translated
# #
# #
# # def shift(text, key):
# #     word_ln = len(text)
# #     shift = key % word_ln
# #     text = text[-shift:] + text[:-shift]
# #     return text
# #
# #
# # text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/' \
# #        'dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/' \
# #        'ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/' \
# #        'qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/' \
# #        'hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
# #        'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /' \
# #        'ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /' \
# #        'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
# #        'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()
# #
# # letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# #
# # text_2 = []
# # key = 3
# # for i_word in text:
# #     text_decryption = decryption(i_word)
# #     shift_text = shift(text_decryption, key)
# #     if shift_text.endswith("/"):
# #         key += 1
# #         text_2.append(shift_text)
# #     else:
# #         text_2.append(shift_text)
# #
# # text_2 = " ".join(text_2)
# # text_2 = text_2.replace("+", "*")
# # text_2 = text_2.replace("-", ",")
# # text_2 = text_2.replace("(", "'")
# # text_2 = text_2.replace("..", "--")
# # text_2 = text_2.replace('"', "!")
# # text_2 = text_2.replace("/", ".\n")
# #
# # print(text_2)
# 
# # # переворачивает все слова текста, оставив знаки препинания
# # import string
# # def reverse_word(word):
# #     return ''.join(reversed(word))
# #
# # text = input('Сообщение: ').split() # Это задание очень! простое.
# # result = []
# #
# # for word in text:
# #     word_part = ''
# #     word_back = ''
# #     for sym in word:
# #         if not sym in string.punctuation:
# #             word_part += sym
# #         else:
# #             word_back += reverse_word(word_part) + sym
# #             word_part = ''
# #
# #     word_back += reverse_word(word_part)
# #     result.append(word_back)
# #
# # print('Новое сообщение:', *result, sep=' ')
# 
# # # определяет, можно ли первую строку получить из второй циклическим сдвигом
# #
# # str_1 = input('Первая строка: ') # abcd
# # str_2 = input('Вторая строка: ') # cdab cdba
# #
# # if str_1 == str_2:
# #     print('Строки одинаковые.')
# # else:
# #     if len(str_1) != len(str_2):
# #         print('Строки имеют разную длину.')
# #     else:
# #         shift = 1
# #         flag = False
# #         for i in range(len(str_1) - 1):
# #             str_2 = str_2[-1] + str_2[:-1]
# #             if str_1 == str_2:
# #                 print(f'Первая строка получается из второй со сдвигом {shift}.')
# #                 flag = True
# #                 break
# #             else:
# #                 shift += 1
# #         if not flag:
# #             print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
# 
# # #  определяет, является ли заданная строка правильным IP-адресом
# # split_ip = input('Введите IP: ').split('.') #128.16.35.a4 34.56.42,5 240.127.56.340 128.0.0.255
# #
# # if len(split_ip) < 4:
# #     print('Адрес - это четыре числа, разделённые точками')
# # else:
# #     number = 0
# #     out_of_range = 0
# #     for num in split_ip:
# #         if num.isdigit():
# #             number += 1
# #             if int(num) > 255:
# #                 out_of_range += 1
# #                 print(f'{num} превышает 255')
# #         else:
# #             print(f'{num} - не целое число')
# #     if out_of_range == 0 and number == 4:
# #         print('IP-адрес корректен')
# 
# # # считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность
# # def compress(str_txt):
# #     str_len = len(str_txt)
# #     result = ''
# #
# #     if str_len > 0:
# #         i = 0
# #         while i < str_len:
# #             counter = 0
# #             curr_char = str_txt[i:i + 1]
# #             while i < str_len and str_txt[i] == curr_char:
# #                 i += 1
# #                 counter += 1
# #             result += curr_char + str(counter)
# #     return result
# #
# # text = input('Введите строку: ') #aaAAbbсaaaA
# # print(compress(text))
# 
# # # запрашивает у пользователя пароль до тех пор, пока он не введёт надёжный пароль.
# #
# # while True:
# #     password = input('Придумайте пароль: ') # qWErty123
# #     pass_len = len(password)
# #     pass_low = sum(map(str.islower, password))
# #     print(pass_low)
# #     pass_up = sum(map(str.isupper, password))
# #     pass_dig = sum(map(str.isdigit, password))
# #
# #     if (pass_len < 8) or (pass_up < 1) or (pass_dig < 3):
# #         print('Пароль ненадёжный. Попробуйте ещё раз.')
# #     else:
# #         print('Это надёжный пароль!')
# #         break
# 
# # # запрашивает у пользователя пароль до тех пор, пока он не введёт надёжный пароль.
# # #count_lower = 0
# # count_upper = 0
# # count_digit = 0
# # while True:
# #     password = input('Придумайте пароль: ') # qWErty123
# #     pass_len = len(password)
# #     for sym in password:
# # #        if sym.islower():
# # #            count_lower += 1
# #         if sym.upper():
# #             count_upper += 1
# #         if sym.isdigit():
# #             count_digit += 1
# #
# #     if (pass_len < 8) or (count_upper < 1) or (count_digit < 3):
# #         print('Пароль ненадёжный. Попробуйте ещё раз.')
# #     else:
# #         print('Это надёжный пароль!')
# #         break
# 
# # #  самое длинное слово
# # text = input('Введите строку: ').split() #я есть строка
# # max_len = 0
# # max_word = ''
# #
# # for word in text:
# #     if len(word) > max_len:
# #         max_len = len(word)
# #         max_word = word
# #
# # print(f'Самое длинное слово: {max_word}')
# # print(f'Длина этого слова: {max_len}')
# 
# 
# # # меняет точку с запятой на запятую
# # menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
# # new_menu = menu.replace(';', ', ')
# #
# # print(f'Доступное меню: {menu}')
# # print(f'На данный момент в меню есть: {new_menu}')
# 
# # # проверяет, каких букв в строке больше, прописных или заглавных
# # text = input("Введите текст: ")
# # lowers = len([letter for letter in text if letter.islower()])
# # uppers = len([letter for letter in text if letter.isupper()])
# #
# # if lowers > uppers:
# #     print("Результат:", text.lower())
# # else:
# #     print("Результат:", text.upper())
# # print(f'Прописных букв: {lowers}')
# # print(f'Заглавных букв: {uppers}')
# 
# # # Путь к файлу
# # path = input("Путь к файлу: ")
# # disk = input("На каком диске должен лежать файл: ")
# # extension = input("Требуемое расширение файла: ")
# #
# # if path.startswith(disk) and path.endswith(extension):
# #     print("Путь корректен!")
# # else:
# #     print("Путь некорректен!")
# 
# # зашифрует это сообщение при помощи шифра Цезаря (модифицированный через строки).
# # print(ord("а"), ord("я"), ord("ё"), chr(1104))
# #
# # text = input("Введите текст: ")
# # delta = int(input("Введите сдвиг: "))
# # alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]  # заполняем список буквами алфавита
# # # Думаем над структурой алгоритма: [вариант_1 если условие_1 иначе вариант_2 for буква in текст]
# # new_text = [alphabet[(alphabet.index(letter) + delta) % len(alphabet)] if letter in alphabet else letter for letter in text.lower()]
# # print(''.join(new_text))
# 
# # # удаляет пробелы
# # text = 'У       нас         пошёл                    снег    !    '
# #
# # print(' '.join(text.split()))
# 
# # # считает, сколько раз слова пользователя встречаются в тексте
# #
# # words_list = input('Введите слова через пробел: ').split()
# # print(words_list)
# # text = input('Текст произведения: ').split()
# #
# # words_count = ([str(text.count(word)) for word in words_list])
# # for i in range(len(words_list)):
# #     print(f"{words_list[i]} : {words_count[i]}")
# 
# 
# 
# # # рассылку поздравлений для определённого списка людей. Поздравления для разных людей он хочет написать по-разному
# # while True:
# #
# #     grats_template = 'С днем рождения, {name}! Тебе уже {age} лет! ' # input('Введите шаблон поздравления {name} {age}: ')
# #     if '{name}' in grats_template and '{age}' in grats_template:
# #         break
# #     else:
# #         print('Ошибка: отсутствует конструкция {name} или {age}')
# #
# #
# # names_list = 'Максим Боярский, Павел Носов'.split(', ') # input('Введите список имен: ').split(', ')
# # ages_str = '39 40' # input('Возраст людей через пробел: ')
# # ages = [int(i_number) for i_number in ages_str.split()]
# #
# # for i_man in range(len(names_list)):
# #     print(grats_template.format(name=names_list[i_man], age=ages[i_man]))
# #
# # people = [
# #     ' '.join([names_list[i_man], str(ages[i_man])])
# #     for i_man in range(len(names_list))
# # ]
# # people_str = ', '.join(people)
# # print(people)
# # print(people_str)
# 
# # # получает на вход 4 числа и выводит на экран IP-адрес.
# #
# # ip_address = "{0}.{1}.{2}.{3}"
# # count = 0
# # numbers = []
# # while count < 4:
# #     new_number = int(input("Введите число: "))
# #     if 0 <= new_number <= 255:
# #         numbers.append(new_number)
# #         count += 1
# #     else:
# #         print('ВВедите число до 255!')
# #
# # print(ip_address.format(*numbers))
# 
# ## шаблон поздравления
# # while True:
# #
# #     grats_template = input('Введите шаблон поздравления {name}: ')
# #     if '{name}' in grats_template:
# #         break
# #     else:
# #         print('Ошибка: отсутствует конструкция {name}')
# #
# # print('Введите список имен, зак-ся на end: ')
# # names_list = []
# # while True:
# #     name = input('Имя: ')
# #     if name != 'end':
# #         names_list.append(name)
# #     else:
# #         break
# # for i_name in names_list:
# #     print(grats_template.format(name=i_name))
# 
# 
# # # зашифрует это сообщение при помощи шифра Цезаря.
# # def caesar_cipher(string, user_shift):
# #     char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in string]
# #     new_str = ''
# #     for i_char in char_list:
# #         new_str += i_char
# #     return new_str
# #
# # alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# # input_srt = input('Введите сообщение: ').upper()
# # shift = int(input('Шаг шифровки: '))
# #
# # output_str = caesar_cipher(input_srt, shift)
# # print(f'Зашифрованное сообщение: {output_str}')
# 
# # # зашифрует это сообщение при помощи шифра Цезаря.
# # alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# # new = alphabet[39]
# # #print(new)
# # message = input('Введите сообщение: ').upper()
# # shift = int(input('Шаг шифровки: '))
# # decoded = ''
# #
# # for i in message:
# #     index = alphabet.find(i)
# # #    print(f'Индекс в алфавите {index}')
# #     new_index = index + shift
# # #    print(f'Новый индекс {new_index}')
# #     if i in alphabet:
# #         decoded += alphabet[new_index]
# #     else:
# #         decoded += i
# #
# # print(f'Зашифрованное сообщение: {decoded}')
# 
# # # вывести последовательность из N символов, где j-й символ есть “I”, если j-я палка осталась стоять, или “.”, если j-я палка была сбита
# # sticks = int(input('Количество палок: '))
# # throws = int(input('Количество бросков: '))
# # arr = [i for lst in [list(range(int(input(f'Бросок {i+1}. Сбиты палки с номера: '))-1,
# #                     int(input(f'по номер: ')))) for i in range(throws)] for i in lst]
# # print(f"Результат: {''.join(['I' if i not in arr else '.' for i in range(sticks)])}")
# #
# # #код, который «раскрывает» все вложенные списки
# # nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# #              [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# #
# # numbers_in_list = [lvl_3 for lvl_1 in nice_list for lvl_2 in lvl_1 for lvl_3 in lvl_2]
# # print(f'Ответ: {numbers_in_list}')
# 
# # # генерирует такой список и выводит его на экран. Используйте только list comprehensions.
# # temp_list = [x for x in range(1, 13)]
# # client_list = []
# # odds = [x for x in temp_list if x % 2 != 0]
# # even = [x for x in temp_list if x % 2 == 0]
# #
# # client_list.append(odds[::2])
# # client_list.append(even[::2])
# # client_list.append(odds[1::2])
# # client_list.append(even[1::2])
# #
# # print(client_list)
# # #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# 
# # # выполняет «сжатие списка» — переставляет все нулевые элементы в конец массив
# # import random
# # n = int(input('Количество чисел в списке: '))
# # temp_list = [random.randint(0, 2) for i in range(n)]
# #
# # num_list = [x for x in temp_list if x > 0] # без нулей
# # num_list.extend([x for x in temp_list if x == 0]) # c нулями
# # num_list = [x for x in temp_list if x > 0] # без нулей
# #
# # print(f'Список до сжатия: {temp_list}')
# # print(f'Список после сжатия: {num_list}')
# 
# # # разворачивает последовательность символов, заключённую между первым и последним появлением буквы h
# # text = input('Введите строку:')
# # #text = 'hqwehrty'
# #
# # letters_index = [index for index, letter in enumerate(text) if letter == 'h']
# # #print(letters_index)
# #
# # start = letters_index[0]
# # #print(start)
# # end = letters_index[len(letters_index) - 1] - 1
# # #print(end)
# # print('Развернутая последовательность между первым и последним h:', text[end:start:-1])
# 
# # # Тренируемся со срезами
# # alphabet = 'abcdefg'
# #
# # print(f'1: {alphabet[:]}')
# # print(f'2: {alphabet[::-1]}')
# # print(f'3: {alphabet[::2]}') # Каждый второй элемент строки (включая самый первый).
# # print(f'4: {alphabet[1::2]}') # Каждый второй элемент строки после первого.
# # print(f'5: {alphabet[:1]}')
# # print(f'6: {alphabet[-1:]}') # Все элементы начиная с конца до предпоследнего.
# # print(f'7: {alphabet[3:4]}')
# # print(f'8: {alphabet[-3:]}') # Последние три элемента строки.
# # print(f'9: {alphabet[3:5]}')
# # print(f'10: {alphabet[4:2:-1]}') # Все элементы в диапазоне индексов от 3 до 4 в обратном порядке
# 
# # # генерирует два списка участников и третий список победителей
# # import random
# #
# # team1 = [round(random.uniform(5, 10), 2) for i in range(20)]
# # team2 = [round(random.uniform(5, 10), 2) for i in range(20)]
# # team3 = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(len(team1))]
# #
# # print(f'Первая команда: {team1}')
# # print(f'Вторая команда: {team2}')
# # print(f'Победители тура: {team3}')
# 
# # # генерирует список из N чисел, на чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5
# # n = int(input('Введите длину списка: '))
# # temp_list = [i for i in range(n)]
# # num_list = [1 if index % 2 == 0 else index % 5 for index, num in enumerate(temp_list)]
# #
# # print(f'Результат: {num_list}')
# 
# # # генерирует список из гласных букв этого текста
# # text = input('Введите текст: ') # Нужно отнести кольцо в Мордор!
# # #vowels_list = []
# # vowels = set('аеиоуыэюя')
# # #count = 0
# # vowels_list = [i for i in text if i in vowels]
# # # for i in text if i in vowels:
# # #         count += 1
# # #         vowels_list.append(i)
# #
# # print(f'Список гласных букв: {vowels_list}')
# # print(f'Длина списка: {len(vowels_list)}')
# 
# # удаляет элементы списка с индексами от А до В
# # import random
# # n = 5 # int(input("Введите количество чисел N: "))
# #
# # numbers = [random.randint(-10, 10) for _ in range(n)]
# #
# # a = random.randint(0, len(numbers) - 2)
# # b = random.randint(a + 1, len(numbers) - 1)
# # # Генерируем числа так, чтобы они не выходили за границу списка
# # print(numbers, a, b)
# # numbers = numbers[:a] + numbers[b + 1:]
# # print(numbers)
# 
# # # если есть отрицательные цены, то программа их зануляет и в конце выводит на экран,
# # # # сколько денег мы по итогу потеряли
# # import random
# #
# # original_prices = [random.randint(-100, 100) for _ in range(10)]
# #
# # new_prices = original_prices[:]
# #
# # for i in range(len(original_prices)):
# #
# #     if new_prices[i] < 0:
# #
# #         new_prices[i] = 0
# #
# # print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
# 
# # # палиндром из чисел определяет, какое минимальное количество и каких чисел надо приписать в конец этой последовательности
# # def is_palindrome(num_list):
# #     reverse_list = num_list[::-1]
# #     if num_list == reverse_list:
# #         return True
# #     else:
# #         return False
# #
# # nums = [1, 2, 3, 4, 5]
# # answer = []
# #
# # for i_nums in range(0, len(nums)):
# #     if is_palindrome(nums[i_nums:len(nums)]):
# #         answer = nums[:i_nums]
# #         answer.reverse()
# #         break
# #
# # print(f'Исходный список: {nums}')
# # print(f'Нужно чисел для палиндрома: {len(answer)}')
# # print(f'Список этих чисел: {answer}')
# 
# # генерирует новый список из первого списка, заменяя все отрицательные числа на ноль
# # original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# # new_list = [x if x > 0 else 0 for x in original_prices]
# # print(new_list)
# 
# # # генерирует список из чётных чисел в диапазоне от А до B. Используйте list comprehensions
# # import random
# # a = 1
# # b = random.randint(10, 300)
# # even_list = [x for x in range(a, b) if x % 2 == 0]
# # print(even_list)
# 
# # # генерирует случайные значения в первых двух списках в заданных диапазонах, а также генерирует список, состоящий из фраз
# # import random
# #
# # squad_1 = [random.randint(50, 80) for _ in range(10)]
# # squad_2 = [random.randint(30, 60) for _ in range(10)]
# # squad_3 = [('Погиб' if squad_1[i_damage] + squad_2[i_damage] > 100 else 'Выжил') for i_damage in range(10)]
# #
# # print(f'Урон первого отряда: {squad_1}')
# # print(f'Урон второго отряда: {squad_2}')
# # print(f'Состояние третьего отряда: {squad_3}')
# 
# # text = input('Введите строку: ') # привет
# # symbol = input('Введите символ: ')  # !
# #
# # double_letter = [x * 2 for x in text]
# # double_letter_symbol = [x + symbol for x in double_letter]
# #
# # print(f'Список удвоенных символов: {double_letter}')
# # print(f'Склейка с дополнительным символом:: {double_letter_symbol}')
# 
# # # генерирует два списка: в первом лежат кубы чисел в диапазоне от А до В, во втором — квадраты чисел в этом же диапазоне
# # left = int(input('Левая граница: '))
# # right = int(input('Правая граница: '))
# # cubes_list = [x ** 3 for x in range(left, right + 1)]
# # quadro_list = [x ** 2 for x in range(left, right + 1)]
# #
# #
# # print(f'Список кубов чисел в диапазоне от 5 до 10: {cubes_list}')
# # print(f'Список квадратов чисел в диапазоне от 5 до 10: {quadro_list}')
# 
# ##  list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.
# # def get_higher_price(percent, price):
# #     return round(price * (1 + percent / 100), 2)
# #
# # prices_now = [93.83, 93.83, 103.22]
# #
# # first_year = int(input("Повышение на первый год: "))
# # second_year = int(input("Повышение на второй год: "))
# #
# # prices_first = [get_higher_price(first_year, i_price) for i_price in prices_now]
# # prices_second = [get_higher_price(second_year, i_price) for i_price in prices_first]
# #
# # print(f'Сумма цен за каждый год: {sum(prices_now), sum(prices_first), sum(prices_second)}')
# 
# # # палиндром из чисел определяет, какое минимальное количество и каких чисел надо приписать в конец этой последовательности
# # def is_palindrome(num_list):
# #     reverse_list = []
# #     for i_num in range(len(num_list) - 1, -1, -1):
# #         reverse_list.append(num_list[i_num])
# #         if num_list == reverse_list:
# #             return True
# #         else:
# #             return False
# #
# # nums = [1, 2, 3, 4, 5]
# # new_nums = []
# # answer = []
# #
# # for i_nums in range(0, len(nums)):
# #     for j_elem in range(i_nums, len(nums)):
# #         new_nums.append(nums[j_elem])
# #         if is_palindrome(new_nums):
# #             for i_answer in range(0, i_nums):
# #                 answer.append(nums[i_answer])
# #             answer.reverse()
# #             break
# #     new_nums = []
# #
# # print(f'Исходный список: {nums}')
# # print(f'Нужно чисел для палиндрома: {len(answer)}')
# # print(f'Список этих чисел: {answer}')
# 
# 
# # reverse_list = []
# # for i in range(len(nums) -1, 0, -1):
# #     reverse_list.append(i)
# #
# # print(reverse_list)
# 
# # определяет, какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной
# # number = int(input('Кол-во чисел: '))
# # arr = []
# #
# # for i in range(number):
# #     # query = str(i + 1) + ' число: '
# #     arr.append(int(input('Число: ')))
# # print(f'\nПоследовательность: {arr}')
# # counter = 0
# # while arr != arr[::-1]:
# #     arr.insert(number, arr[counter])
# #     counter += 1
# #
# # print('Нужно приписать чисел:', counter)
# # print('Сами числа:', arr[:counter][::-1])
# 
# # # Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья
# # friends = int(input('Кол-во друзей: '))
# # loans = int(input('Долговых расписок: '))
# # friends_list = []
# #
# # for _ in range(friends):
# #     friends_list.append(0)
# #
# # for i in range(1, loans + 1):
# #     print(f'\n{i}-я расписка')
# #     to_whom = int(input('Кому: '))
# #     from_whom = int(input('От кого: '))
# #     how_much = int(input('Сколько: '))
# #     friends_list[from_whom - 1] += how_much
# #     friends_list[to_whom - 1] -= how_much
# #
# # print('\nБаланс друзей:')
# # for index in range(len(friends_list)):
# #     print(f'{index + 1} : {friends_list[index]}')
# 
# # # программу, которая выводит число от 1 до N — это номер человека, который останется в кругу последним.
# # man_list = []
# # out = 0
# #
# # man = int(input('Кол-во человек: '))
# # num = int(input('Какое число в считалке? '))
# # print(f'Значит, выбывает каждый {num}-й человек')
# #
# # for i in range(1, man + 1):
# #     man_list.append(i)
# #
# # while len(man_list) > 1:
# #
# #     for i_man in man_list:
# #         print(f'\nТекущий круг людей: {man_list}')
# #         print(f'Начало счёта с номера: {man_list[0]}')
# #         start_count = out % len(man_list)
# #         out = (start_count + num - 1) % len(man_list)
# #         print(f'Выбывает человек под номером: {man_list[out]}')
# #         man_list.remove(man_list[out])
# #
# # print()
# # print(f'Остался человек под номером: {man_list[0]}')
# #
# # # определяет, какое наибольшее число человек сможет одновременно взять ролики и пойти покататься
# # skates_list = []
# # man_list = []
# # count = 0
# #
# # skates = int(input('Кол-во коньков: '))
# # for i in range(1, skates + 1):
# #     size = int(input(f'Размер {i}-й пары: '))
# #     skates_list.append(size)
# #
# # man = int(input('Кол-во людей: '))
# # for i in range(1, man + 1):
# #     size_leg = int(input(f'Размер ноги {i}-го человека: '))
# #     man_list.append(size_leg)
# #
# # for leg in man_list:
# #     if leg in skates_list:
# #         skates_list.remove(leg)
# #         count += 1
# # print(f'Наибольшее кол-во людей, которые могут взять ролики: {count}')
# 
# # # два списка вывод и второй вывод уникальные
# # num_list1 = []
# # num_list2 = []
# #
# # for i in range(1, 4):
# #     num1 = int(input(f'Введите {i}-е число для первого списка: '))
# #     num_list1.append(num1)
# #
# # for i in range(1, 8):
# #     num2 = int(input(f'Введите {i}-е число для второго списка: '))
# #     num_list2.append(num2)
# # print(f'Первый список: {num_list1}')
# # print(f'Второй список: {num_list2}')
# # num_list1.extend(num_list2)
# # num_unique = list(set(num_list1))
# # print(f'Новый первый список с уникальными элементами: {num_unique}')
# 
# # # запрашивает у пользователя количество песен из списка и затем названия этих песен, а на экран выводит общее время их звучания
# # violator_songs = [
# #     ['World in My Eyes', 4.86],
# #     ['Sweetest Perfection', 4.43],
# #     ['Personal Jesus', 4.56],
# #     ['Halo', 4.9],
# #     ['Waiting for the Night', 6.07],
# #     ['Enjoy the Silence', 4.20],
# #     ['Policy of Truth', 4.76],
# #     ['Blue Dress', 4.29],
# #     ['Clean', 5.83]
# # ]
# # favorite = []
# # music_lengh = 0
# # count = int(input('Сколько песен выбрать? '))
# # for i in range(1, count + 1):
# #     song = input(f'Название {i}-й песни: ')
# #     for i_find in violator_songs:
# #         if i_find[0] == song:
# #             favorite.append(i_find)
# # for music in favorite:
# #     music_lengh += music[1]
# #
# # print(f'Общее время звучания песен: {music_lengh} минуты')
# # print(f'Список избранных песен: {favorite}')
# 
# 
# # # спрашивает у пользователя, ушёл человек или пришёл новый гость, и, исходя из ответа, добавляет в список или удаляет из него нужное имя
# # guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# #
# # command = ''
# # while True:
# #     print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
# #     command = input('Гость пришел или ушел? ')
# #     if command == 'пора спать':
# #         break
# #     guest_name = input('Имя гостя: ')
# #     if command == 'пришел':
# #         if len(guests) >= 6:
# #             print(f'Прости, {guest_name}, но мест нет.')
# #         else:
# #             guests.append(guest_name)
# #             print(f'Привет, {guest_name}!')
# #     elif command == 'ушел':
# #         guests.remove(guest_name)
# #         print(f'Пока, {guest_name}!')
# #     print()
# #
# # print('\nВечеринка закончилась, все легли спать.')
# 
# # # запрашивает у пользователя деталь, считает их количество, а также общую стоимость
# # shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
# #         ['педаль', 100], ['седло', 1500], ['рама', 12000],
# #         ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# #
# # detail_count = 0
# # detail_summ = 0
# # detail_name = input('Название детали: ')
# #
# # for i_detail in shop:
# #         if i_detail[0] == detail_name:
# #                 detail_summ += i_detail[1]
# #                 detail_count += 1
# #
# # print(f'Кол-во деталей - {detail_count}')
# # print(f'Общая стоимость: {detail_summ}')
# 
# # # генерирует списки роста для каждого в классе, затем объединяет их в один список и сортирует его
# # students = []
# # first_class = []
# # second_class = []
# # for height in range(160, 177, 2):
# #     first_class.append(height)
# # for height in range(162, 181, 3):
# #     second_class.append(height)
# #
# # students.extend(first_class)
# # students.extend(second_class)
# # students.sort()
# # print(f'Отсортированный список учеников: {students}')
# 
# # # добавляет в список считает и удаляет
# # a = [1, 5, 3]
# # b = [1, 5, 1, 5]
# # c = [1, 3, 1, 5, 3, 3]
# # a.extend(b)
# # print(f'Кол-во цифр 5 при первом объединении: {a.count(5)}')
# # for num in a:
# #     if num == 5:
# #         a.remove(num)
# # a.extend(c)
# # print(f'Кол-во цифр 3 при втором объединении: {a.count(3)}')
# # print(f'Итоговый список: {a}') # [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
# 
# # for i in a:
# #     if i != 5:
# #         d.append(i)
# #
# # print(t)
# # print(d)
# 
# # # добавляет в список goods ещё один список с новым фруктом и ценой
# # goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
# #
# # new_fruit_name = input("Новый фрукт: ")
# # new_fruit_price = int(input("Цена: "))
# # new_fruit_list = [new_fruit_name, new_fruit_price]
# # goods.append(new_fruit_list)
# #
# # print("Новый ассортимент:", goods)
# #
# # for fruit in goods:
# #     fruit[1] = round(fruit[1] * 1.08, 2)
# #
# # print("Новый ассортимент с увел. ценой:", goods)
# 
# #  # Общий список команд: [[1, 2 ,3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# # command_list = []
# # number = 0
# #
# # n = int(input("Кол-во участников: ")) # 12
# # k = int(input("Кол-во человек в команде: ")) # 4
# #
# # if n % k == 0:
# #     for i_1 in range(n // k): # поделили команды на 4
# #         team = [] # определили 12/4 команду
# #         for i_2 in range(k): # берем в диапазоне 4
# #             number += 1
# #             team.append(number)
# #             print(team)
# #         command_list.append(team)
# #     print(command_list)
# # else:
# #     print(f"{n} невозможно поделить на команды по {k} человек!")
# 
# # # выводит элементы этого списка в виде привычной нам матрицы
# # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # for i_members in matrix:
# #     for second_members in i_members:
# #         print(second_members, end=' ')
# #     print()
# 
# 
# # # добавлять в свой рейтинг фильмы, удалять их оттуда, а также вставлять на нужное пользователю место
# # films = [
# #     'Крепкий орешек', 'Назад в будущее', 'Таксист',
# #     'Леон', 'Богемская рапсодия', 'Город грехов',
# #     'Мементо', 'Отступники', 'Деревня',
# #     'Проклятый остров', 'Начало', 'Матрица'
# # ]
# #
# # n = int(input("Сколько фильмов выбрать? "))
# # your_films = []
# # for i in range(n):
# #     print("Ваш текущий топ фильмов:", your_films)
# #     film_name = input("Имя фильма: ")
# #     print("Команды: добавить, вставить, удалить")
# #     command = input("Введите команду: ")
# #     if film_name not in your_films:
# #         if command == "добавить":
# #             your_films.append(film_name)
# #         elif command == "вставить":
# #             insert_index = int(input("Введите индекс для вставки "))
# #             insert_index %= len(your_films)  # ограничим индекс списка, чтобы он не вылезал за границу списка
# #             your_films.insert(insert_index, film_name)
# #     else:
# #         if command == "удалить":
# #             your_films.remove(film_name)
# #
# # print("Ваш текущий топ фильмов:", your_films)
# 
# # # запрашивает у пользователя количество сотрудников и их зарплаты, затем удаляет все элементы списка со значением 0
# # staff = int(input('Кол-во сотрудников: '))
# # salary_list = []
# # for i in range(1, staff + 1):
# #     salary = float(input(f'Зарплата {i} сотрудника: '))
# #     salary_list.append(salary)
# # print(f'\nЗарплаты: {salary_list}')
# # for digit in salary_list:
# #     if digit == 0:
# #         salary_list.remove(digit)
# # print(f'Осталось сотрудников: {len(salary_list)}')
# # print(f'Зарплаты без уволенных: {salary_list}')
# # print(f'Минимальная зарплата: {min(salary_list)}')
# # print(f'Максимальная зарплата: {max(salary_list)}')
# 
# # # в какой клетке сидят лев и обезьяна. Для этого используйте методы списков.
# # zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# # zoo.insert(1, 'Bear')
# # zoo.remove('elephant')
# # leon = zoo.index('lion')
# # monkey = zoo.index('monkey')
# # print(f'Зоопарк: {zoo}')
# # print(f'Лев сидит в клетке номер: {leon + 1}')
# # print(f'Обезьяна сидит в клетке номер: {monkey + 1}')
# 
# # # сортировка списка
# # def selection_sort(my_list):
# #     for i_mn in range(len(my_list)):
# #         for curr in range(i_mn, len(my_list)):
# #             if my_list[curr] < my_list[i_mn]:
# #                 my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]
# #
# # nums = [6, 4, 3, 9, 5]
# # selection_sort(nums)
# # print(nums)
# 
# # # Программа выводит номер, под которым будет лежать новый контейнер
# # container = int(input('Количество контейнеров: '))
# # container_list = []
# #
# # for i in range(1, container + 1):
# #     weight = int(input(f'Введите вес контейнера {i}: '))
# #     if weight <= 200:
# #         container_list.append(weight)
# #     else:
# #         print('Вес контейнера должен быть не больше 200')
# # weight_new = int(input('Введите вес нового контейнера: '))
# # # container_list.append(weight_new)
# # # print(container_list)
# #
# # for index, num in enumerate(container_list): # проходим по номерам и значениям списка
# #     if num <= weight_new <= num + 1: # если новое значение больше/равно текущему, но меньше/равно следующему
# #         container_list.insert(index + 1, weight_new) # то вставляем за этим номером в список введенное значение
# #         print(f'Номер, который получит новый контейнер: {index + 2}')
# #         break
# # print(f'Новый список контейнеров: {container_list}')
# 
# # находить слова, которые одинаково читается слева направо и справа налево
# # word = input('Введите слово: ')
# # if word == word[::-1]: # тоже взял из инета, как я понял команда переворачивает слово
# #     print('Слово является палиндромом')
# # else:
# #     print('Слово не является палиндромом')
# 
# # циклически сдвигает элементы списка вправо на K позиций
# # подсмотрел решение задачи в инете, но я не могу найти и понять, что значит команда [n:] [:n]. где найти информацию?
# # task = [1, 2, 3, 4, 5]
# # shift = 1
# # print('Изначальный список:', task)
# # task = task[-shift:] + task[:-shift]
# # print('Сдвинутый список:', task)
# 
# # # считает количество уникальных букв в слове
# # word = input('Введите слово: ')
# # word_list = list(word)
# # word_list.sort()
# # print(word_list)
# # count = 0
# # prev_sym = ''
# # for sym in word_list:
# #     if sym != prev_sym:
# #         prev_sym = sym
# #         count += 1
# #     else:
# #         count = 0
# # print(f'Количество уникальных букв: {count}') # лава
# 
# # # список любимых фильмов
# # films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
# #          'Леон', 'Богемская рапсодия', 'Город грехов',
# #          'Мементо', 'Отступники', 'Деревня']
# # favorite_films = []
# #
# # count = int(input('Сколько фильмов хотите добавить? '))
# # for i in range(1, count + 1):
# #     favorite = input(f'Введите название фильма {i}: ')
# #     favorite_films.append(favorite)
# #     if favorite not in films:
# #         print(f'Ошибка: фильма {favorite} у нас нет :(')
# #         favorite_films.remove(favorite)
# #
# # print(f'Ваш список любимых фильмов: {favorite_films}')
# # print('Ваш список любимых фильмов: ', end='')
# # print(*favorite_films, sep=', ')
# 
# # удаляет из списка наибольшие элементы
# # list_vcard = ['3070', '2060', '3090', '3070', '3090']
# # print(f'Старый список видеокарт: {list_vcard}')
# # for sym in list_vcard:
# #    if sym == max(list_vcard):
# #        list_vcard.remove(sym)
# #
# # #for index, sym in enumerate(list_vcard):
# # #    if sym == max(list_vcard):
# # #        list_vcard.pop(index)
# # print(f'Новый список видеокарт: {list_vcard}')
# 
# ## выводит на экран элементы списка, значения которых меньше их индекса
# # решение задачи с N = любая
# # cells = int(input('Количество клеток: ')) # 5
# # cells_list = [] # [0, 1, 2, 3, 4, 5]
# # rank = [] #[3, 0, 6, 2, 10]
# #           #[0, 2, 4, 6, 8]
# # inappropriate = []
# # for num in range(cells + 1):
# #     cells_list.append(num)
# #     rank.append(num * 2)
# # for i in range(1, cells + 1):
# #     print(f'Эффективность {cells_list[i]} клетки: {rank[i-1]}')
# #     if cells_list[i] > rank[i-1]:
# #         inappropriate.append(rank[i-1])
# # print(f'Неподходящие значения: {inappropriate}')
# 
# # решение задачи с N = 5
# # cells = int(input('Количество клеток: ')) # 5
# # cells_list = [] # [0, 1, 2, 3, 4, 5]
# # rank = [3, 0, 6, 2, 10]
# # inappropriate = []
# # for num in range(cells + 1):
# #     cells_list.append(num)
# # for i in range(1, cells + 1):
# #     print(f'Эффективность {cells_list[i]} клетки: {rank[i-1]}')
# #     if cells_list[i] > rank[i-1]:
# #         inappropriate.append(rank[i-1])
# # print(f'Неподходящие значения: {inappropriate}')
# 
# ## выводит элементы списка только с чётными индексами
# # names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# # first_day = []
# # for index, name in enumerate(names):
# #     if index % 2 == 0:
# #         first_day.append(name)
# #
# # print(f'Первый день: {first_day}')
# 
# ## Список из нечётных чисел от одного до N
# # n = int(input('Введите число: '))
# # odd_numbers = []
# # for num in range(1, n + 1):
# #     if num % 2 != 0:
# #         odd_numbers.append(num)
# # print(f'Список из нечётных чисел от одного до N: {odd_numbers}')
# 
# 
# ## считает, сколько раз слова пользователя встречаются в тексте
# # words_list = []
# # counts = [0, 0, 0]
# #
# # for i in range(3):
# #     word = input(f'Введите {i+1} слово')
# #     words_list.append(word)
# #
# # text = input("Слово из текста: ")
# # while text != "end":
# #     for index in range(3):
# #         if words_list[index] == text:
# #             counts[index] += 1
# #     text = input("Слово из текста: ")
# 
# # print("Подсчёт слов в тексте")
# # for i in range(3):
# #     print(words_list[i], ':', counts[i])
# 
# ## выводит соседей этого символа и сообщение о количестве таких же символов среди этих соседей
# # text = input('Введите строку: ') # abbc abсd
# # sym_num = int(input('Номер символа: ')) - 1
# # sym_found = ''
# # text_list = list(text)
# # count = 0
# # for index, symbol in enumerate(text_list):
# #     if index == sym_num:
# #         print(f'Символ слева: {text_list[index - 1]}')
# #         print(f'Символ спрва: {text_list[index + 1]}')
# #         sym_found = symbol
# # for i in text_list:
# #     if i == sym_found:
# #         count += 1
# # print(f'В тексте таких же символов: {count}')
# 
# 
# 
# ## заменяет в строке все двоеточия (:) на точки с запятой (;)
# # text = input('Введите строку: ') # гвозди:шурупы:гайки
# # text_list = list(text)
# # new_text = ''
# # count = 0
# # what_replace = ":"
# # for_what_replace = ";"
# # for index, symbol in enumerate(text_list):
# #     if symbol == ':':
# #         text_list[index] = for_what_replace
# #         count += 1
# # for i in text_list:
# #     new_text += i
# # print(f'Исправленная строка: {new_text}')
# # print(f'Кол-во замен: {count}')
# 
# # ## программу, которая меняет местами наибольший и наименьший элементы в списке
# # nums_list = []
# # N = int(input('Кол-во собак в списке: '))
# #
# # for _ in range(N):
# #     num = int(input('Количество очков у собаки: '))
# #     nums_list.append(num)
# #
# # if nums_list:
# #     maximum = nums_list[0]
# #     minimum = nums_list[0]
# #     minimum_index = 0
# #     maximum_index = 0
# #
# #     for index, i in enumerate(nums_list):
# #         if maximum < i:
# #             maximum = i
# #             maximum_index = index
# #         if minimum > i:
# #             minimum = i
# #             minimum_index = index
# #
# #     print('Максимальное число в списке:', maximum)
# #     print('Минимальное число в списке:', minimum)
# #
# #     print(nums_list)
# #     nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
# #     print(nums_list)
# # else:
# #     print('В списке нет чисел')
# 
# # ## код, выводящий на экран сумму индексов элементов списка, которые кратны K
# # list = []
# # #new_list = []
# # summ = 0
# # index = 0
# # count = int(input('Кол-во чисел в списке: '))
# #
# # for i in range(count):
# #     num = int(input(f'Введите {i+1} число: '))
# #     list.append(num)
# # divider = int(input('Введите делитель: '))
# # for i_number in list:
# #     if i_number % divider == 0:
# #         print(f'Индекс числа {i_number}: {index}')
# #         summ += index
# #     index += 1
# # print(f'Сумма индексов: {summ}')
# #
# # #        new_list.append(number)
# # #print(new_list)
# 
# 
# # # находить минимальное и максимальное числа в списке.
# # nums_list = []
# # N = int(input('Кол-во чисел в списке: '))
# # for _ in range(N):
# #     num = int(input('Очередное число: '))
# #     nums_list.append(num)
# # maximum = nums_list[0]
# # minimum = nums_list[0]
# # for i in nums_list:
# #     if maximum < i:
# #         maximum = i
# #     if minimum > i:
# #         minimum = i
# #
# # print('Максимальное число в списке:', maximum)
# # print('Минимальное число в списке:', minimum)
# 
# ## урон монтсров в списке
# # monster_count = int(input('Количество монстров: '))
# # mage_index = int(input('Номер мага в списке: '))
# # monsters_damage = []
# #
# # for monster in range(monster_count):
# #     damage = int(input(f'Урон у {monster + 1} монстра: '))
# #     monsters_damage.append(damage)
# #
# # for i_monster in range(monster_count):
# #     if monsters_damage[i_monster] <= 100 and i_monster != mage_index - 1:
# #         monsters_damage[i_monster] += monsters_damage[mage_index - 1]
# #
# # print(monsters_damage)
# 
# # office = []
# # staff = int(input('Кол-во сотрудников в офисе: '))
# # for i in range(staff):
# #     staff_ID = int(input('ID сотрудника: '))
# #     office.append(staff_ID)
# # search = int(input('Какой ID ищем? '))
# # if search not in office:
# #     print('Сотрудника нет')
# # else:
# #     print('Сотрудник на месте')
# 
# ## Поиск монеты монетки радар
# # def coin_radar(point_x, point_y, radius):
# #     gip = point_x ** 2 + point_y ** 2
# #     if gip <= radius:
# #         print('Монетка где-то рядом')
# #     else:
# #         print('Монетки в области нет')
# #
# # point_x = float(input('Введите координату Х: '))
# # point_y = float(input('Введите координату Y: '))
# # radius = int(input('Введите радиус: '))
# #
# # coin_radar(point_x, point_y, radius)
# 
# ## поиск 3 одинаковых цифр в числе
# # for year in range(start_year, end_year + 1):
# #     for i in range(10):
# #         digit_to_str = str(year)
# #         if 3 == digit_to_str.count(str(i)):
# #             print(year)
# 
# # numbers = []
# # for i in range(101):
# #     numbers.append(i)
# # print('Текущий список чисел:', numbers)
# 
# # ## Таблица степеней
# # numbers = [3,7,5]
# # number = int(input('Новое число: '))
# # numbers.append(number)
# # print('Текущий список чисел:', numbers)
# # for i in numbers:
# #     print(i ** 2, i ** 3, i ** 4)
# # print()
# 
# ##учет книг в библиотеке
# # books_ID = [50, 34, -1, -1, 2, 23, -1]
# # new_books_ID = []
# # returned = 0
# #
# # for _ in range(10):
# #     id = int(input('ВВедите ID книги: '))
# #     books_ID.append(id)
# # for id in books_ID:
# #     if id == -1:
# #         returned += 1
# #     else:
# #         new_books_ID.append(id)
# #
# # print('Новый список выданных книг: ', new_books_ID)
# # print('Вернули за день: ', returned)
# # находит три одинаковые цифры в 4 значном числе из периода
# # def same(year1, year2):
# #     for i in range(year1, year2 + 1):
# #         a,b,c,d = i // 1000, i // 100 % 10, i // 10 % 10, i % 10
# #         if a == b == c or b == c == d or c == d == a or a == b == d:
# #             print(a * 1000 + b * 100 + c * 10 + d)
# #
# # year1 = int(input("Введите первый год: "))
# # year2 = int(input("введите второй год: "))
# # print("Годы от", year1, "до", year2, "c тремя одинаковыми цифрами: ")
# # same(year1, year2)
# 
# # # проверяет, лежит ли точка с координатами (x, y) внутри круга с радиусом r
# # def coin_radar(point_x, point_y, radius):
# #     if -radius <= point_x <= radius and -radius <= point_y <= radius:
# #         print('Монетка где-то рядом')
# #     else:
# #         print('Монетки в области нет')
# #
# # point_x = float(input('Введите координату Х: '))
# # point_y = float(input('Введите координату Y: '))
# # radius = int(input('Введите радиус: '))
# # coin_radar(point_x, point_y, radius)
# 
# # находит его наименьший делитель, отличный от 1
# # def min_del(n):
# #     i = 1
# #     while i <= n:
# #         i = i + 1
# #         if n % i == 0:
# #             return i
# #             break
# # def min_divider(n, d=2):
# #     return d if n % d == 0 else min_divider(n, d + 1)
# #
# # num = int(input('Введите число: '))
# # print('Наименьший делитель, отличный от единицы:', min_del(num))
# # print('Наименьший делитель, отличный от единицы (2 способ):', min_divider(num))
# 
# # # Задача 3. Сумма и разность
# #
# # # функция расчет подсчет цифр в числе
# # def count_digit(number):
# #     num_count = 0
# #     temp = number
# #     while temp > 0:
# #         num_count += 1
# #         temp = temp // 10
# #     return num_count
# #
# # # находит сумму всех цифр в числе
# #
# # def summa_n(num):
# #   summ_num = 0
# #   while num > 0:
# #     summ_num += num % 10
# #     num = num // 10
# #   return summ_num
# #
# # n = int(input('ВВедите число: '))
# # summ = summa_n(n)
# # digits = count_digit(n)
# #
# # print('Сумма чисел: ', summ)
# # print('Количество цифр в числе: ', digits)
# # print('Разность суммы и количества цифр: ', summ - digits)
# 
# 
# ## заменяет целую часть на число, цифры записаны в обратном порядке.
# # def reverse_num(number):
# #     n = 0
# #     while number > 0:
# #         digit = number % 10
# #         number //= 10
# #         n *= 10
# #         n = n + digit
# #     return n
# #
# #
# # n = float(input('Введите первое число: '))
# # k = float(input('Введите второе число: '))
# #
# # num1 = int(n)
# # num2 = int(k)
# # num1_fraction = int(n % 1 * 100)
# # num2_fraction = int(k % 1 * 100)
# #
# # reverse_num1 = reverse_num(num1) + reverse_num(num1_fraction) / 100
# # reverse_num2 = reverse_num(num2) + reverse_num(num2_fraction) / 100
# # summ_num1_2 = reverse_num1 + reverse_num2
# #
# # print('Первое число наоборот: ', reverse_num1)
# # print('Второе число наоборот: ', reverse_num2)
# # print('Сумма: ', summ_num1_2)
# 
# #
# # # Введите первое число: 102.12
# # # Введите второе число: 123.34
# # #
# # # Первое число наоборот: 201.21
# # # Второе число наоборот: 321.43
# # # Сумма: 522.64
# 
# # d_from = 0
# # d_to = 4
# # max_danger = float(input('Введите максимально допустимый уровень опасности: '))
# #
# # depth = d_from + (d_to - d_from) / 2
# # danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
# #
# # if max_danger < 0:
# #         print('Максимально допустимый уровеньопасности должен быть больше 0')
# # else:
# #         print('Глубина: ', depth, 'Опасность: ', danger)
# #         while abs(danger) > max_danger:
# #                 if danger > 0:
# #                         d_from = depth
# #                 else:
# #                         d_to = depth
# #                 depth = d_from + (d_to - d_from) / 2
# #                 danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
# #                 print('Глубина: ', depth, 'Опасность: ', danger)
# #         print('Приблизительная глубина безпасной кладки равна: ', depth)
# 
# # sum_ = float(input('Введите сумму кредита: '))
# # year_ = int(input('На сколько лет выдан? '))
# # percent_ = float(input('Сколько процентов годовых? ')) / 100
# # def payment(s, n, i):
# #         k = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
# #         a = round(k * s, 2)
# #         return a
# # def specified_period(sum, percent, a, period):
# #         for q in range(1, period + 1):
# #                 paid_percent = sum * percent
# #                 paid_credit = a - paid_percent
# #                 print('\nПериод: ', q)
# #                 print('Остаток долга на начало периода: ', sum)
# #                 print('Выплачено процентов: ', paid_percent)
# #                 print('Выплачено тело кредита: ', paid_credit)
# #                 sum -= paid_credit
# #         else:
# #                 print('\nОстаток долга: ', sum)
# #         return sum
# # a_ = payment(sum_, year_, percent_)
# # new_sum_ = specified_period(sum_, percent_, a_, 3)
# # new_year_ = int(input('\nНа сколько лет продлевается договор? '))
# # new_percent_ = float(input('Увеличение ставки до: ')) / 100
# # new_year_ = new_year_ + (year_ - 3)
# # new_payment = payment(new_sum_, new_year_, new_percent_)
# # new_sum = specified_period(new_sum_, new_percent_, new_payment, new_year_)
# 
# # def factorial(num):
# #     f = 1
# #     for i in range(1, num +1):
# #         f *= i
# #     return f
# # precision = float(input('Введите точность: '))
# # x = int(input('Введите x: '))
# # n = 0
# # sum_ = 0
# # func = 1
# # while abs(func) > precision:
# #     func = (- 1) ** n * (x ** (2 * n) / factorial(2 * n))
# #     n += 1
# #     sum_ += func
# # print('Сумма ряда = ', sum_)
# 
# # # Задача 7. Яйца
# # depth_min = 0
# # depth_max = 4
# # danger_max = float(input('Введите максимальный уровень опасности: '))
# # depth = depth_min + (depth_max - depth_min) / 2
# # danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
# # if danger_max <= 0:
# #     print('Ошибка. Максимально допустимый уровень опасности должен быть больше нуля.')
# # else:
# #     #print('Глубина ', depth, 'Опасность ', danger)
# #     while abs(danger) > danger_max:
# #         if danger > 0:
# #             depth_min = depth
# #         else:
# #             depth_max = depth
# #         depth = depth_min + (depth_max - depth_min) / 2
# #         danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
# #         #print('Глубина ', depth, 'Опасность ', danger)
# #     print('Приблизительная глубина безопасной кладки: ', depth)
# 
# 
# # ampl_start = float(input('Введите начальную амплитуду: '))
# # ampl_end = float(input('Введите амплитуду остановки: '))
# # count = 0
# # while ampl_start > ampl_end:
# #     ampl_start = ampl_start - (ampl_start * 8.4) / 100
# #     count += 1
# # print('Маятник считается остановившимся через', count, 'колебаний')
# 
# ## функция расчет подсчет цифр в числе
# # def count_digit(number):
# #     num_count = 0
# #     temp = number
# #     while temp > 0:
# #         num_count += 1
# #         temp = temp // 10
# #     return num_count
# ## функция поменять местами первую и последнюю цифру
# # def change_num(num, count):
# #     last_digit = num % 10
# #     first_digit = num // 10 ** (count - 1)
# #     between_digits = num % 10 ** (count - 1) // 10
# #     num = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
# #     return num
# #
# # first_n = int(input("Введите первое число: "))
# # second_n = int(input("Введите второе число: "))
# #
# # count1 = count_digit(first_n)
# # count2 = count_digit(second_n)
# # reverse1 = change_num(first_n, count1)
# # reverse2 = change_num(second_n, count2)
# #
# # if count1 < 3:
# #     print("В первом числе меньше трёх цифр.")
# # elif count2 < 4:
# #     print("Во втором числе меньше четырёх цифр.")
# # else:
# #     print('\nИзменённое первое число:', reverse1)
# #     print('Изменённое второе число:', reverse2)
# # print('\nСумма чисел:', reverse1 + reverse2)
# 
# # # выводит отдельно мантиссу и отдельно порядок этого числа
# # text = input('Введите число в экспотенциальной форме: ')
# # m = ''
# # b = ''
# # flag = True
# # for i in text:
# #     if i == 'e' or i == 'E':
# #         flag = False
# #     elif flag:
# #         m += i
# #     else:
# #         b += i
# # print(m, b)
# 
# 
# # Задача 3. Число наоборот 2
# # def reverse(number):
# #     n = 0
# #     while number > 0:
# #         digit = number % 10
# #         number //= 10
# #         n *= 10
# #         n = n + digit
# #     return n
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# # print('Первое число наоборот: ', reverse(a))
# # print('Второе число наоборот: ', reverse(b))
# # sum_ = reverse(a) + reverse(b)
# # print('Сумма: ', sum_)
# # print('Сумма наоборот: ', reverse(sum_))
# 
# # #  находит максимум из трёх чисел
# # def max3(a, b, c):
# #     return max(max(a, b), max(b, c))
# #
# # first = float(input("Введите первое число: "))
# # second = float(input("Введите второе число: "))
# # third = float(input("Введите третье число: "))
# #
# # print('Максимальное число: ', max3(first, second, third))
# 
# 
# # def prec():
# #     precision = float(input('Точность: '))
# #     result = 0
# #     i = 0
# #     add_member = 1
# #     while add_member > precision
# #         add_member = 1 / math.factorial(i)
# #         result =+ add_member
# #         i += 1
# 
# # num = float(input('Введите число: ')) # 0.0012
# # b = 0
# # if num < 1:
# #     while num < 1:
# #       num *= 10
# #       b -= 1
# # elif num >= 10:
# #     while num >= 10:
# #       num /= 10
# #       b += 1
# # print(f'Формат плавающей точки: x = {num} * 10 ** {b}')
# 
# 
# 
# # # функцию eqv, которая принимает три числа и затем сравнивает сумму первых двух чисел с третьим
# # def eqv(a, b, c):
# #     return abs((a + b) - c) <= 1e-15
# #
# #
# # first = float(input("Введите первое число: "))
# # second = float(input("Введите второе число: "))
# # third = float(input("Введите третье число: "))
# # print(eqv(first, second, third))
# #
# #
# # def eqv():
# #     a = float(input("Введите число 1: "))
# #     b = float(input("Введите число 2: "))
# #     c = float(input("Введите число 3: "))
# #     if abs((a + b) - c) <= 1e-15:
# #         print(True)
# #     else:
# #         print(False)
# # eqv()
# 
# # # Функция должна проверять, возможно ли сложить эти два числа или нет
# # # budget = float(input("Введите бюджет страны: "))
# # # new_tax = float(input("Новые поступления (налог): "))
# # budget = 1.23e2
# # new_tax = 1.2e1
# #
# # while budget % 10 == 0:
# #     budget /= 10
# #     new_tax /= 10
# #
# # if int(budget + new_tax) == int(budget):
# #     print("Бюджет не изменился")
# # else:
# #     print("Бюджет изменился")
# 
# 
# 
# # # Числа с плавающей точкой
# # start_number = float(input("Введите число: "))
# # count = 0
# # while start_number > 10:
# #     count += 1
# #     start_number /= 10
# #
# # print(f"Формат плавающей точки: x = {start_number} * 10 ** {count}")
# #
# # # вычислениями вещественных чисел
# # num_exp = float(input('Введе число в эксп-й форме от 1 до 9: ')) # 1e-3
# # x = 1
# # count = 0
# # while x <= 2:
# #     x += num_exp
# #     count += 1
# # print(count)
# 
# 
# # # постоянного деления числа на 2
# # x = 1
# # count = 0
# # while x != 0:
# #     x /= 2
# #     count += 1
# #     print(x)
# # print('Итераций: ', count)
# 
# # # Задача 3. Приоритет задач
# # def numeral_count(number):
# #     if number < 0:
# #         print('Число отрицательное, обнуляем.')
# #         return 0
# #     count = 0
# #     while number > 0:
# #         number //= 10
# #         count += 1
# #     return count
# #
# # x = int(input('Введе число 1: '))
# # y = int(input('Введе число 2: '))
# # num_1 = numeral_count(x)
# # num_2 = numeral_count(y)
# # if num_1 > num_2:
# #     print('Число', x, ' больше')
# # elif num_1 < num_2:
# #     print('Число', y, ' больше')
# # else:
# #     print('Числа равны')
# 
# 
# # # Задача 1. Сумма чисел 2
# #
# # def summa_n(number):
# #     count = 0
# #     for i in range(1, number + 1):
# #         count += i
# #     return count
# #
# # num = int(input('Введите число: '))
# # print('Сумма от 1 до', num, '=', summa_n(num))
# # num2 = summa_n(num)
# # print('Сумма от 1 до', num2, '=', summa_n(num2))
# 
# 
# # def min_x(number1, number2):
# #    return (number1 + number2 - abs(number1 - number2)) / 2
# #
# # a = float(input('Введите первое число: '))
# # b = float(input('Введите второе число: '))
# # print('\nНаименьшее число: ', min_x(a, b))
# 
# # print('Задача 3. Апгрейд калькулятора')
# #
# #
# # def main_menu():
# #     act = int(input('1. Вывести сумму, 2. максимальную цифру, 3. Минимальную цифру: '))
# #     if act == 1:
# #         summa_n(num)
# #     elif act == 2:
# #         max(num)
# #     elif act == 3:
# #         min(num)
# #     else:
# #         print('Ошибка ввода.')
# #         main_menu()
# #
# # def summa_n(num):
# #   summ_num = 0
# #   while num > 0:
# #     summ_num += num % 10
# #     num = num // 10
# #   print(f'Сумма цифр числа равна {summ_num}\n')
# #   main_menu()
# #
# # def max(num):
# #   max_numb = num % 10
# #   while num > 0:
# #     num = num // 10
# #     if max_numb < num % 10:
# #       max_numb = num % 10
# #   print(f'Максимальная цифра в числе равна {max_numb}\n')
# #   main_menu()
# #
# # def min(num):
# #   min_numb = num % 10
# #   while num > 0:
# #     num = num // 10
# #     if num == 0:
# #       break
# #     if min_numb > num % 10:
# #       min_numb = num % 10
# #   print(f'Минимальная цифра в числе равна {min_numb}\n')
# #   main_menu()
# #
# # num = int(input('Введите число: '))
# #
# # main_menu()
# #
# 
# # def rock_paper_scissors():
# #     # Здесь будет игра "Камень, ножницы, бумага"
# #     game1 = int(input('Камень = 1, Ножницы = 2, Бумага = 3, что выбираешь? '))
# #     if game1 == 1:
# #         print('У меня ножницы, ты выйграл!')
# #     if game1 == 2:
# #         print('У меня камень, ты проиграл!')
# #     elif game1 == 3:
# #         print('У меня камень, ты выйграл!')
# #     else:
# #         print('ВВедите 1,2 или 3')
# #     mainMenu()
# #
# # def guess_the_number():
# #     # Здесь будет игра "Угадай число"
# #     start = 1
# #     finish = 101
# #
# #     count = 0
# #     answer = 0
# #     print('Вы загадали число 100?')
# #     first_question = True
# #     while answer != 1:
# #         if not first_question:
# #             print('Вы загадали число', n, '?')
# #
# #         answer = int(input('1 - равно, 2 - меньше, 3 - больше '))
# #         if answer == 2 and not first_question:
# #             finish = n
# #         elif answer == 3:
# #             start = n
# #
# #         count += 1
# #         n = (start + finish) // 2
# #         first_question = False
# #
# #     print('Я угадал ваше число с', count, 'попытки')
# #     mainMenu()
# #
# # def mainMenu():
# #     # Здесь главное меню игры
# #     choice = int(input('Выбери игру: 1 - КНБ, 2 - Угадай число, любая клавиша - завершение работы: '))
# #     if choice == 1:
# #         rock_paper_scissors()
# #     elif choice == 2:
# #         guess_the_number()
# #     else:
# #         print('Завершение работы')
# #
# # mainMenu()
# 
# # import math
# #
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# # print('Наибольший общий делитель: ', math.gcd(a, b))
# 
# 
# 
# # #наименьшее число без условных операторов
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# # print('Наименьшее число: ', min(a,b))
# 
# # def coin_radar():
# #     point_x = int(input('Введите координату Х: '))
# #     point_y = int(input('Введите координату Y: '))
# #     if -1 <= point_x <= 1 and -1 <= point_y <= 1:
# #         print('Монетка где-то рядом')
# #     else:
# #         print('Монетки в области нет')
# #
# #
# # coin_radar()
# 
# 
# ## принимает на вход текст и подсчитывает, какое в нём количество цифр
# # def contra_num():
# #     num = input("Введите целое число: ")
# #     num_list = list(num)
# #     print(num_list)
# #     num_list.reverse()
# #     num2 = "".join(num_list)
# #     print('"Обратное" ему число:', num2)
# #
# # contra_num()
# 
# ## Апгрейд калькулятора
# # def main_menu():
# #     act = int(input('1. Вывести сумму, 2. максимальную цифру, 3. Минимальную цифру: '))
# #     if act == 1:
# #         summa_n()
# #     elif act == 2:
# #         max()
# #     elif act == 3:
# #         min()
# #     else:
# #         print('Ошибка ввода.')
# #         main_menu()
# #
# # def summa_n():
# #     count = 0
# #     for i in range(1, num + 1):
# #         count += i
# #     print('Я знаю, что сумма чисел от 1 до', num, 'равна', count)
# #     main_menu()
# #
# # def max():
# #     max1 = num % 10
# #     max2 = num // 10
# #     if max1 > max2:
# #         print('Максимальная цифра: ', max1)
# #     elif max1 < max2:
# #         print('Максимальная цифра: ', max2)
# #     else:
# #         print('Цифры в числе равны.')
# #     main_menu()
# #
# # def min():
# #     max1 = num % 10
# #     max2 = num // 10
# #     if max1 > max2:
# #         print('Минимальная цифра: ', max2)
# #     elif max1 < max2:
# #         print('Минимальная цифра: ', max1)
# #     else:
# #         print('Цифры в числе равны.')
# #     main_menu()
# #
# # num = int(input('Введите число: '))
# # main_menu()
# 
# 
# # def test():
# #     num = int(input('Введите целое число: '))
# #     if num >= 0:
# #         positive()
# #     else:
# #         negative()
# #
# # def positive():
# #     print('Положительное')
# #
# # def negative():
# #     print('Отрицательное')
# #
# # test()
# 
# # def summa_n():
# #     num = int(input('Введите число: '))
# #     count = 0
# #     for i in range(1, num + 1):
# #         count += i
# #     print('Я знаю, что сумма чисел от 1 до', num, 'равна', count)
# #
# # summa_n()
# 
# # def main_menu():
# #     print('1. Сделать хорошее')
# #     print('2. Сделать плохое')
# #     choice = int(input('Введите номер действия: '))
# #     if choice == 1:
# #         good()
# #     elif choice == 2:
# #         bad()
# #     else:
# #         print('Ошибка ввода')
# #         main_menu()
# # def good():
# #     print('Все хорошо')
# #     input('Нажмите любую клавишу для возврата в меню: ')
# #     main_menu()
# # def bad():
# #     print('Все плохо')
# #     input('Нажмите любую клавишу для возврата в меню: ')
# #     main_menu()
# #
# # main_menu()
# 
# ### Напишите программу, где у пользователя спрашивается, чего он хочет — найти расстояние от себя до точки или
# # найти расстояние между двумя произвольными точками
# # def my_distance(x, y):
# #     distance = math.sqrt(x ** 2 + y ** 2)
# #     print(distance)
# #
# #
# # def their_distance(x_1, x_2, y_1, y_2):
# #     distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
# #     print(distance)
# #
# #
# # user_choice = int(input("Найти расстояние от себя до точки (1) или найти расстояние между двумя произвольными точками (2)? "))
# # if user_choice == 1:
# #     target_x = float(input("Введите координату X цели: "))
# #     target_y = float(input("Введите координату Y цели: "))
# #     my_distance(target_x, target_y)
# # elif user_choice == 2:
# #     target_x_1 = float(input("Введите координату X цели 1: "))
# #     target_y_1 = float(input("Введите координату Y цели 1: "))
# #     target_x_2 = float(input("Введите координату X цели 2: "))
# #     target_y_2 = float(input("Введите координату Y цели 2: "))
# #     their_distance(target_x_1, target_x_2, target_y_1, target_y_2)
# # else:
# #     print("Ввод неверный")
# 
# ## фамилии на почта
# # def print_all_info(surname, name, country, city, street, house, flat):
# #     print('\nФамилия:', surname,
# #           '\nИмя: ', name,
# #           '\nСтрана проживания:', country,
# #           '\nГород: ', city,
# #           '\nУлица: ', street,
# #           '\nНомер дома: ', house,
# #           '\nНомер квартиры: ', flat)
# #
# #
# # user_surname = input("Введите фамилию: ")
# # user_name = input("Введите имя: ")
# # user_street = input("Введите улицу: ")
# # user_house = input("Введите номер дома: ")
# #
# # for _ in range(3):
# #     user_surname = input("Введите фамилию: ")
# #     user_name = input("Введите имя: ")
# #     user_country = input("Введите страну проживания: ")
# #     user_city = input("Введите город: ")
# #     user_street = input("Введите улицу: ")
# #     user_house = input("Введите номер дома: ")
# #     user_flat = input("Введите номер квартиры: ")
# 
# #    print_all_info(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)
# 
# 
# # #Среднее арифметическое
# # import math
# # def mean_calc(x, y):
# #     sum_of_numbers, count_of_numbers = 0, 0
# #     for i in range(x, y + 1):
# #         sum_of_numbers += i
# #         count_of_numbers += 1
# #
# #     print("Среднее:", round(sum_of_numbers / count_of_numbers, 2))
# #
# # a = int(input("Введите a: "))
# # b = int(input("Введите b: "))
# #
# # if a > b:
# #     a, b = b, a
# #
# # mean_calc(a, b)
# 
# # # функция определения простого числа
# # def is_prime(number):
# #     for i in range(2, int(number ** 0.5) + 1):
# #         if number % i == 0:
# #             return False
# #     return True
# #
# #
# # n = int(input("Введите количество чисел в последовательности: "))
# # count = 0
# # for i in range(n):
# #     new_number = int(input("Введите число: "))
# #     if is_prime(new_number):
# #         count += 1
# #
# # print(count)
# 
# 
# # # Формула для площади сферы:
# # def sphere_area(radius):
# #     print(4 * math.pi * radius ** 2)
# #
# # # Формула для объёма шара:
# # def sphere_volume(radius):
# #     print(4 / 3 * math.pi * radius ** 3)
# #
# # radius_of_planet = float(input("Введите радиус планеты: "))
# # sphere_area(radius_of_planet)
# # sphere_volume(radius_of_planet)
# 
# # def f_print(name):
# #     print('Фамилия: Иванов')
# #     print('Имя: ', name)
# #     print('Улица: Пушкина')
# #     print('Дом: 32')
# #     print('')
# #
# # f_print('Василий')
# # f_print('Игорь')
# # f_print('Алена')
# 
# # def product_count():
# #     a = int(input())
# #     b = int(input())
# #     print("Всего", a + b, "шт.")
# #
# # print("Сколько мешков рыбы и мяса?")
# # product_count()
# # print("Сколько буханок белого и чёрного хлеба?")
# # product_count()
# # print("Сколько вёдер воды и молока?")
# # product_count()
# 
# 
# # def greeting():
# #     print('Привет!')
# #     print('Добро пожаловать!')
# #
# # while True:
# #     a = input('Зайдёте? Да/Нет: ')
# #     if a == 'Да':
# #         greeting()
# #     print('Следующий.\n')
# 
# 
# # # функция печати треугольника
# # def triangle():
# #     stars = 1
# #     for line in range(5):
# #         print(' ' * (5 - line - 1), end='')
# #         print('*' * stars)
# #         stars += 2
# #
# # #функция печати прямоугольника
# #
# # def rectangle():
# #     for line in range(5):
# #         if line == 0 or line == 4:
# #             print('*' * 5)
# #         else:
# #             print('*' + ' ' * 3 + '*')
# #
# # choice = int(input('Нарисовать треугольник - 1, прямоугольник - 2: '))
# #
# # if choice == 1:
# #     triangle()
# # elif choice == 2:
# #     rectangle()
# # else:
# #     print('Введите 1 или 2')
# 
# 
# 
# # #наибольшее число через модуль и без условных операторов
# # a = int(input('Введите первое число: '))
# # b = int(input('Введите второе число: '))
# #
# # print('Наибольшее число:', (a // b * a + b // a * b) // (a // b + b // a))
# # print('Наибольшее число, способ два:', (a + b + abs(a - b)) / 2)
# 
# # import math
# #
# # a = float(input('Введите a: '))
# # b = float(input('Введите b: '))
# # c = float(input('Введите c: '))
# # di = b ** 2 - 4 * a * c
# #
# # if di > 0:
# #     x1 = (-b + math.sqrt(di)) / (2 * a)
# #     x2 = (-b - math.sqrt(di)) / (2 * a)
# # elif di == 0:
# #     x = -b / (2 * a)
# #     print(x)
# # else:
# #     print()
# # if di > 0 and x1 < x2:
# #     print('Корень:', x1, 'Корень: ', x2)
# # else:
# #     print('Корень:', x2, 'Корень: ', x1)
# 
# # α = float(input('Угол поворота часовой стрелки: '))
# # print('Угол поворота минутной стрелки за последний час: ', (α % 30) * 12)
# # # print((α * 12) % 360)
# 
# 
# # За час минутная стрелка совершает полный оборот (1 круг == 360°), а часовая стрелка передвигается на один час (1/12 круга == 30°). Поэтому полный угол поворота минутной стрелки в 12 раз больше, чем угол поворота часовой стрелки.
# #
# # Угол поворота часовой стрелки с начала последнего часа это остаток от деления на 30:
# #
# # α = float(input('Угол поворота часовой стрелки: '))
# # print((α % 30) * 12)  # угол поворота минутной стрелки за последний час
# # Может быть проще запомнить формулу, если сперва преобразовать угол поворота часовой стрелки в угол поворота минутной стрелки (α * 12), а затем найти угол поворота минутной стрелки, который относится только к последнему часу — последнему обороту (% 360 — один оборот это 360°) как предложил @StateItPrimitive в комментарии:
# #
# # α = float(input('Угол поворота часовой стрелки: '))
# # print((α * 12) % 360)  # угол поворота минутной стрелки за последний час
# 
# # x = float(input('Расположение коня по горизонтали: '))
# # y = float(input('Расположение коня по вертикали: '))
# # x_horse = float(input('Введите местоположение точки на доске по горизонтали: '))
# # y_horse = float(input('Введите местоположение точки на доске по вертикали: '))
# #
# # if 0 < x < 0.8 and 0 < y < 0.8:
# #
# #     xSquare = int(x * 10)
# #     ySquare = int(y * 10)
# #     print()
# #     print(f"Конь находится в клетке ({xSquare}, {ySquare})")
# #     x_horse_square = int(x_horse * 10)
# #     y_horse_square = int(y_horse * 10)
# #     print(f"Точка находится в клетке ({x_horse_square}, {y_horse_square})")
# #
# #     if x_horse_square <= xSquare + 2 and y_horse_square <= ySquare + 2:
# #         print('Да, конь может ходить в эту точку.')
# #     else:
# #         print('Нет, конь не может ходить в эту точку.')
# #
# # else:
# #     print("Клетки с такой координатой не существует")
# 
# # # Метеостанция
# # down = int(input('Нижняя граница: '))
# # up = int(input('Верхняя граница: '))
# # step = int(input('Шаг: '))
# # print('C F')
# # # if up != int(up) and down != int(down) and step !=int(step):
# # #     print('Введите целые числа ')
# # #else:
# # for cel in range(down, up+1, step):
# #     convert = cel * 1.8 + 32
# #     print(cel, int(convert))
# # print(up, int(up * 1.8 + 32))
# # print()
# #
# 
# 
# 
# # # объёмы двух планет
# # import math
# #
# # rad_new_planet = float(input('Введите радиус случайной планеты: '))
# # volume_earth = 10.8321 * 10 ** 11
# # volume_new_planet = (4 / 3) * math.pi * (rad_new_planet ** 3)
# #
# # if volume_earth > volume_new_planet:
# #     print('Объём планеты Земля больше в',
# #           round(volume_earth / volume_new_planet, 3), 'раз')
# #
# # else:
# #     print('Объём планеты Земля меньше в',
# #           round(volume_new_planet / volume_earth, 3), 'раз')
# 
# 
# # num = float(input('Введите положительное действительное число X: '))
# # num1 = int(num * 10) % 10
# # print('Первая цифра данного числа после десятичной точки: ', num1)
# 
# 
# # #Вы пишете программу-инсталлятор для компьютерной игры
# # import math
# #
# # f_size = float(input('Укажите размер файла для скачивания: '))
# # i_speed = float(input('Какова скорость вашего соединения? '))
# # full_size = math.ceil(f_size / i_speed)
# # for i in range(1, full_size + 1):
# #     progress = int(i * i_speed)
# #
# #     if progress < f_size:
# #         print('Прошло', i, 'сек.',
# #           'Скачано', progress,
# #           'из', f_size,
# #           'Мб (', math.ceil((progress / f_size)*100), '%)')
# #
# #     else:
# #         print('Прошло', i, 'сек.',
# #               'Скачано', f_size,
# #               'из', f_size,
# #               'Мб (', math.ceil((f_size / f_size) * 100), '%)')
# 
# # import math
# # num_end = int(input('Введите кол-во чисел: '))
# # count = 0
# # for x in range(num_end):
# #     number = float(input('Введите число: '))
# #     if number > 0:
# #         number = math.ceil(number)
# #         print('x =', number, 'log(x) =', math.log(number))
# #     elif number < 0:
# #         number = math.floor(number)
# #         print('x =', number, 'exp(x) =', math.exp(number))
# 
# # #1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей
# # # если купить что-то в евро, то сначала эта сумма конвертируется в доллары, а уже потом - в рубли
# # product = float(input('Введите стоимость покупки в евро: '))
# #
# # price = (product * 1.25) * 60.87
# #
# # print('Стоимость покупки в рублях: ', price)
# 
# # import math
# #
# # number = float(input('Введите число: '))
# #
# # print(math.floor(number))
# # print(math.ceil(number))
# # print(math.sqrt(number))
# # print(math.exp(number))
# # print(math.log(number))
# # print(abs(number))
# #
# #
# # if number % 1 == 0:
# #     print(math.factorial(number))
# 
# 
# 
# # import math
# #
# # distance = float(input('Введите расстояние до танка: '))
# # angle = float(input('Введите угол поворота радара: '))
# #
# # angle /= 57.2958
# # x = math.cos(angle) * distance
# # y = math.sin(angle) * distance
# #
# # print('Координаты танка: ', x, ',', y)
# 
# 
# # import math
# #
# # a = int(input(f'Введите сторону треугольника a: '))
# # b = int(input(f'Введите сторону треугольника b: '))
# # c = int(input(f'Введите сторону треугольника c: '))
# # p = (a + b + c) / 2
# # s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# #
# # print('Площадь треугольника: ', s)
# 
# 
# # print('Задача 5. Простые числа')
# #
# # num_end = int(input('Введите кол-во чисел: '))
# # count = 0
# # is_prime = True
# # for x in range(num_end):
# #     number = int(input('Введите число: '))
# #     for divider in range(2, number):
# #         if number % divider == 0:
# #             is_prime = False
# #             break
# #     if is_prime:
# #         count += 1
# 
# # print('Количество простых чисел в последовательности: ', count)
# 
# # # Компьютерное зрение Точность и аккуратность
# # x = float(input('Расположение по горизонтали: '))
# # y = float(input('Расположение по вертикали: '))
# #
# # if 0 < x < 0.8 and 0 < y < 0.8:
# #     xSquare = int(x * 10)
# #     ySquare = int(y * 10)
# #     print(f"Фигура находится в клетке ({xSquare}, {ySquare})")
# #     center_x = xSquare / 10 + 0.05
# #     center_y = ySquare / 10 + 0.05
# #     delta_x = round(center_x - x, 3)
# #     delta_y = round(center_y - y, 3)
# #     print(f"Поправьте положение фигуры на ({delta_x}, {delta_y})")
# # else:
# #     print("Клетки с такой координатой не существует")
# 
# 
# 
# 
# # height = int(input('Возраст: '))
# # weight = float(input('температура: '))
# #
# # x = round((height * 1.5) * weight)
# # print(x)
# 
# # #Задача 3. Индекс массы тела
# # height = float(input('Ваш рост: '))
# # weight = float(input('Ваш вес: '))
# #
# # bmi = round(weight / height ** 2, 2)
# # print('Ваш индекс массы тела: ', bmi)
# #
# # if bmi < 18.5:
# #     print('У вас недостаточная масса тела')
# # elif bmi < 25:
# #     print('У вас нормальная масса тела')
# # elif bmi < 30:
# #     print('У вас избыточная масса тела')
# # else:
# #     print('У вас ожирение')
# 
# # bet= int(input('Введите ставку: '))
# # coef = float(input('Введите коэффициент: '))
# #
# # win = round(bet * coef, 2)
# # print('Выйгрыш: ', win)
# 
# 
# 
# # # Задача 10. Яма
# # depth = int(input('Введите глубину ямы: '))
# # for line in range(depth):
# #         for leftnumber in range(depth, depth - line - 1, -1):
# #                 print(leftnumber, end='')
# #         point_count = 2 * (depth - line - 1)
# #         print(point_count * '.', end='')
# #         for rightnumber in range(depth - line, depth + 1):
# #                 print(rightnumber, end='')
# #         print()
# 
# 
# # height = int(input('Введите общую высоту пирамиды: '))
# # num = 1
# # for row in range(height):
# #         space_count = height - row - 1
# #         print(space_count * '   ', end='')
# # #        for space in range(height - row - 1, 0, -1):
# # #                print(end='   ')
# #         for number in range(row + 1):
# #                 print(num, end='    ')
# #                 num += 2
# #         print()
# 
# # #Пирамидка
# # height = int(input('Введите общую высоту пирамиды: '))
# # for row in range(height):
# #         print(' ' * (height - row) + '#' * (1 + row * 2))
# 
# 
# 
# # #Наибольшая сумма цифр
# # maxNumSum = 0
# # maxNum = 0
# #
# #
# # n = int(input("Сколько чисел будем смотреть? "))
# # for numbers in range(n):
# #         sum = 0
# #         natur_num = int(input("Введите натуральное число: "))
# #         temp_number = natur_num
# #         while natur_num != 0:
# #                 sum += natur_num % 10 #посчитали сумму цифр в числе
# #                 natur_num //= 10
# #         if sum > maxNumSum: # если сумма цифр в числе максимальная, присвоили в переменную maxNumSum
# #                 maxNumSum = sum
# #                 maxNum = temp_number
# #
# # print('Найбольшая сумма цифр', maxNumSum, 'в числе: ', maxNum)
# 
# 
# # countSum = 0
# # countNum = 0
# # n = int(input("Сколько чисел будем смотреть? "))
# # for i in range(n):
# #     natur_num = int(input("Введите натуральное число: "))
# #     x = (natur_num % 10) + (natur_num // 10)
# #     if countSum < x:
# #         countSum = x
# #         countNum = natur_num
# #
# # print('Найбольшая сумма цифр', countSum, 'в числе: ', countNum)
# 
# 
# # #Сумма факториалов
# # factorial = 1
# # count = 1
# # n = int(input("Введите число, чтобы найти сумму факториалов: "))
# # for i in range(2, n+1):
# #     count *= i
# #     factorial += count
# # print('Факториал числа', n, ':', factorial)
# 
# 
# # # Простые числа см модуль 7.5. алгоритмы
# # num_end = int(input('Введите кол-во чисел: '))
# # count = 0
# # isPrime = True
# # for x in range(num_end):
# #     number = int(input('Введите число: '))
# #     for divider in range(2, number):
# #         if number % divider == 0:
# #             isPrime = False
# #     if isPrime:
# #         #print(isPrime)
# #         count += 1
# #
# # print('Количество простых чисел в последовательности: ', count)
# 
# # Крест
# # for row in range(20):
# #     for col in range(20):
# #
# #         if col == row:
# #             print('^', end='')
# #         elif col == -row + 19:
# #             print('^', end='')
# #         else:
# #             print(' ', end='')
# #     print()
# 
# # Рамка
# # width = int(input("Введите ширину рамки: "))
# # height = int(input("Введите высоту рамки: "))
# #
# # for row in range(width + 1):
# #     for col in range(height + 1):
# #         if col == 0 or col == height:
# #             print('|', end='')
# #         elif row == 0 or row == width:
# #             print('-', end='')
# #         else:
# #             print(' ', end='')
# #     print()
# 
# 
# # # Лестница чисел
# # n = int(input("Введите число: "))
# # for row in range(1, n + 1):
# #     for col in range(1, row + 1):
# #         print(row, end='\t')
# #     print()
# 
# # Лестница чисел
# # n = int(input("Введите число: "))
# # for start in range(n + 1):
# #     for number in range(start, n + 1):
# #         print(number, end='\t')
# #     print()
# 
# 
# 
# # for row in range(6):
# #     for col in range(11):
# #         if col % 2 == 0:
# #             print(col+row, end='\t')
# #     print()
# 
# 
# 
# # n = int(input("Введите число: "))
# # for start in range(n):
# #     for number in range(start, n):
# #         print(number, end='\t')
# #     print()
# 
# # count = 0
# # num = input('Введите последовательность из N чисел: ')
# # for i in num:
# #     i = int(i)
# #     if i > 5:
# #         count += 1
# # print('общее количество цифр больше пяти: ', count)
# 
# 
# 
# #очередь
# # people = int(input('Сколько людей в очереди?: '))
# # for hour in range(people+1):
# #     print('Идет ', hour, 'час')
# #     for num in range(hour, people):
# #         print('Номер в очереди: ', num)
# #     print()
# # print('Очередь облсужена!')
# 
# # матрица
# # n = int(input('Введите размер матрицы: '))
# # for row in range(n):
# #     for col in range(n):
# #         buf_col = (n - 1) - row
# #         if buf_col > col:
# #             print(8, end='\t')
# #         elif buf_col == col:
# #             print(1, end='\t')
# #         else:
# #             print(3, end='\t')
# #
# #     print()
# 
# # # Задача 1. Врата ворота
# # for row in range(20):
# #     for col in range(30):
# #         if row == 0:
# #             print('-', end='')
# #         elif col == 0 or col == 29:
# #             print('|', end='')
# #         else:
# #             print(' ', end='')
# #     print()
# 
# # дорога
# # for row in range(20):
# #     for col in range(50):
# #         if col == 24:
# #             print('|', end='')
# #         elif col == row + 29:
# #             print('\\', end='')
# #         elif col == -row + 19:
# #             print('/', end='')
# #         elif row == 9:
# #             print('-', end='')
# #         else:
# #             print(' ', end='')
# #     print()
# 
# # n = int(input('Введите размер матрицы: '))
# # for row in range(n):
# #     for col in range(n):
# #         if col > row:
# #             print(0, end='\t')
# #         elif col < row:
# #             print(2, end='\t')
# #         else:
# #             print(1, end='\t')
# #
# #     print()
# 
# # for row in range(20):
# #     for col in range(50):
# #         if col == 24:
# #             print('|', end='')
# #
# #         elif row == 9:
# #             print('-', end='')
# #         else:
# #             print(' ', end='')
# #     print()
# 
# # n = int(input('Введите размер матрицы: '))
# # for row in range(1, n + 1):
# #     for col in range(1, n + 1):
# #         if col == 3 or col == 6 and col % 2 == 0:
# #             print(col, end='\t')
# #         else:
# #             print(row, end='\t')
# #
# #     print()
# 
# # for col in range(10):
# #     for row in range(0, -10, -1):
# #         print(row + col, end = '\t')
# #     print()
# 
# # n = int(input('Введите число для расчета таблицы умножения: '))
# #
# # for row in range(1, n + 1):
# #     for col in range(1, n + 1):
# #         print(row + col, end = '\t')
# #     print()
# 
# 
# # string = input('\nВведите строку с символом "s": ') #ssbbbsssbc
# # count = 0
# # countMax = 0
# #
# # # как сделать проверку на отсутствие символа, чтобы программа не печатала этот текст, когда s есть?
# # # for letter in string:
# # #     if letter != 's':
# # #         print('В строке нет символа "s"')
# # #         break
# #
# # for letter in string:
# #    if letter != 's':
# #         count = 0
# #    else:
# #         count += 1
# #    if countMax < count:
# #         countMax = count
# # print('\nСамая длинная последовательность: ', countMax)
# 
# # count = 0
# # countMax = 0
# # string = input('Введите текст: ') #Меня зовут Петр
# # for letter in string:
# #     count += 1
# #     if letter == ' ': # если равно пробелу, то обнуляем,
# #         count = 0
# #
# #     if countMax < count: # на первой итерации countMax = 0, присваиваем 4, на второй итерации 4 меньше 5, присваиваем 5, на третьей итерации 5 больше 4, ничего не делаем
# #         countMax = count
# 
# # decrypted1 = ''
# # decrypted2 = ''
# # count = 0
# # message = input('Введите зашифрованное сообщение: ') #shacnidw sandwich
# # for symbol in message:
# #     count += 1 # 1,2,3,4,5,6,7,8 а нужно 1,3,5,7,  8,6,4,2
# #     if (count % 2 == 1):
# #         decrypted1 += symbol # 1,3,5,7
# # #        print(decrypted1)
# #     else:
# #         #decrypted2 = decrypted2 + symbol не понимаю, почему от перемены мест слагаемых сумма меняется???
# #         decrypted2 = symbol + decrypted2
# # print('Расшифрованное сообщение: ', decrypted1 + decrypted2)
# 
# 
# # count = 0
# # milk = 0
# # stall = input('Введите строку: ') #ababababab
# #
# # for symbol in stall:
# #     count += 1
# #     #print('Счетчик символов', count)
# #     if symbol == 'b':
# #         milk += count * 2 # если корова на месте, то прибавить к молоку позицию символа умна 2
# #         #print(milk)
# # print('В итоге будет произведено молока за день: ', milk)
# 
# # footer_Len = int(input('Введите общую длину колонтитула в символах: '))
# # footer_mark = int(input('Введите желаемое количество восклицательных знаков: '))
# # footer_side = footer_Len // 2
# #
# # print(footer_side * '~', end='')
# # print(footer_mark * '!', end='')
# # print(footer_side * '~', end='')
# 
# 
# 
# # count = 0
# # countMax = 0
# # string = input('Введите текст: ') #Меня зовут Петр
# # for letter in string:
# #     if letter == ' ': # если равно пробелу, то обнуляем,
# #         count = 0
# #     else:
# #         count += 1 #иначе считаем с начала списка
# #         #print(count)
# #     if countMax < count: # на первой итерации countMax = 0, присваиваем 4, на второй итерации 4 меньше 5, присваиваем 5, на третьей итерации 5 больше 4, ничего не делаем
# #         countMax = count
# 
# #print('Самое длинное слово, букв: ', countMax)
# 
# # string = input('Введите строку: ') #ssbbbsssbc
# # prevSym = ''
# # countSym = 0
# # for letter in string:
# #     if prevSym == letter and prevSym == 's':
# #         countSym += 1
# #       #  print(countSym)
# #     else:
# #         prevSym = letter
# # print('Самая длинная последовательность: ', countSym)
# 
# 
# # rover = 8
# # rover2 = 10
# #
# # while True:
# #     manage = input('Введите команду движения: ')
# #     if rover >= 15 or rover <= 1 or rover2 >= 20 or rover2 <= 1:
# #         print('Марсоход уперся в стену! Движение невозможно!')
# #         break
# #     elif manage == 'W' or manage == 'w':
# #         rover += 1
# #     elif manage == 'S' or manage == 's':
# #         rover -= 1
# #     elif manage == 'A' or manage == 'a':
# #         rover2 += 1
# #     elif manage == 'D' or manage == 'd':
# #         rover2 -= 1
# #     print('Марсоход находится на позиции, ', rover, ',', rover2, 'введите команду')
# 
# 
# 
# 
# # point_a = 0
# # point_b = 0
# #
# # while point_a != 15 or point_b != 20:
# #     for rover in range(1, 15):
# #         point_a = 14
# #         manage = input('Введите команду движения по высоте: ')
# #         if manage == 'W' or manage == 'w':
# #             point_a += 1
# #         if manage == 'S' or manage == 's':
# #             point_a -= 1
# #         print('Марсоход находится на позиции, ', point_a, ',', point_b, 'введите команду')
# #
# #     for rover in range(1, 20):
# #         point_b = 19
# #         manage = input('Введите команду движения по длине: ')
# #         if manage == 'A' or manage == 'a':
# #             point_b += 1
# #         if manage == 'D' or manage == 'd':
# #             point_b -= 1
# #         print('Марсоход находится на позиции, ', point_a, ',', point_b, 'введите команду')
# # break
# # print('Марсоход уперся в стену! Движение невозможно!')
# 
# 
# 
# # raw_p = ''
# # chair_p = '='
# # width_p = '*'
# #
# # raw = int(input('Введите количество рядов: '))
# # chair = int(input('Введите количество сидений в ряде: '))
# # width = int(input('Введите кол-во метров между рядами: '))
# #
# # for i in range (raw):
# #     print (chair_p*chair, width*width_p, chair_p*chair)
# 
# 
# # count = 1
# # word = input('Введите текст: ') # Пр*ивет как дела
# # for symbol in word:
# #     if symbol == '*':
# #         print('Символ ‘*’ стоит на позиции: ', count)
# #     else:
# #         count += 1
# 
# 
# # count = 0
# # for i in range(1, 11):
# #     word = input(f'Введите слово, которое будете кричать {i}: ')
# #     if word == "Карамба" or word == "карамба":
# #         count += 1
# # print(count, 'человек попали на борт. Поздравляю!')
# 
# 
# # count = 1
# # name = input('Введите день недели: ')
# #
# # for day in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'):
# #     if name == day:
# #         print('Номер дня недели: ', count)
# #     else:
# #         count +=1
# 
# 
# # x = int(input('Введите x: '))
# # for n in range(1, x + 1):
# #     res = ((x-(2 ** n)) * (x-(2 ** n-1))) / ((x-(2 ** n)) * (x-(2 ** n)))
# #     print('При x равном ', x, 'ответ', res)
# 
# 
# # x = int(input('Введите значение x: '))
# # numerator = denominator = 1 # Определили числитель и знаменатель
# #
# # for n in range(1, 7):
# #     # В цикле умножаем расчеты скобок
# #     numerator *= x - (2 ** n - 1) # В числителе это 2 ** n - 1
# #     denominator *= x - 2 ** n  # В знаменателе это 2 ** n
# # res = numerator / denominator
# # print('При x равном ', x, 'ответ', res)
# 
# 
# # x = int(input('Введите x: '))
# # for n in range(1, x + 1):
# #     res = ((x-(2 ** n - 1)) * (x-(2 ** n-3)) * (x-(2 ** n-7)) * (x-(2 ** n-15)) * (x-(2 ** n-31)) * (x-(2 ** n-63))) /
# #            ((x-(2 ** n-2)) * (x-(2 ** n-4)) * (x-(2 ** n-8)) * (x-(2 ** n-16)) * (x-(2 ** n-32)) * (x-(2 ** n)))
# #     print('При x равном ', x, 'ответ', res)
# 
# # n = int(input('Введите число: '))
# # total = 1 # Определили сумму
# #
# # for i in range(1, n + 1):
# #     result = (-1) ** i * 1 / 2 ** i # Рассчитали
# #     total += result #  Увеличили сумму
# # print(total)
# 
# # n = int(input('Введите натуральное число n: '))
# # #if n == 0:
# # #    print(1)
# # for i in range(1, n + 1):
# #     s = (+1) ** i * 1/2 ** i
# #     print(s)
# 
# # string = input('Введите строку ') #aabc
# # prevSym = ''
# # equalSym = False
# # for letter in string:
# #     if prevSym == letter:
# #         equalSym = True
# #     else:
# #         prevSym = letter
# # if equalSym:
# #     print('В тексте есть две одинаковые буквы')
# # else:
# #     print('Нет двух букв подряд')
# 
# # text = input ('Введите текст: ')
# # summ = 0
# #
# # print ('\nОтфильтрованный текст: ', end = ' ')
# # for symbol in text:
# #     if symbol == '1' or symbol == '9':
# #         summ += int(symbol)
# #     else:
# #         print(symbol, end = '')
# # print('\nСумма', summ)
# 
# # x = int(input('Введите x: '))
# # res = ((x-1) * (x-3) * (x-7) * (x-15) * (x-31) * (x-63)) / \
# #       ((x-2) * (x-4) * (x-8) * (x-16) * (x-32) * (x-64))
# # print('При x равном ', x, 'ответ', res)
# 
# 
# 
# # n = int(input('Введите натуральное число n: '))
# # #if n == 0:
# # #    print(1)
# # for i in range(1, n + 1):
# #     s = (-1) ** n * 1/2 ** n
# #     print(s)
# 
# # print('Задача 7. Стипендия')
# #
# # educational_grant = int(input('Введите стипендию: '))
# # expenses = int(input('Введите расходы на проживание в месяц: '))
# # expenses_summ = expenses
# # for month in range(2, 11):
# #     expenses *= 1+(3/100)
# #     expenses_summ += expenses
# # print('Итого расходы на проживание: ', expenses_summ)
# # print('У родителей необходимо попросить: ', expenses_summ - educational_grant*10)
# 
# # text = input("")
# 
# # number = int(input('Введите число: '))
# # print('-=-', end = ' ')
# # for i in range(0, number +1, 10):
# #     print(i, end = ' -=- ')
# 
# # print('-' * 10)
# # print('|' + '0' * 8 + '|')
# # print('|' + '0' * 8 + '|')
# # print('|' + '0' * 8 + '|')
# # print('|' + '0' * 8 + '|')
# # print('|' + '0' * 8 + '|')
# # print('|' + '0' * 8 + '|')
# # print('-' * 10)
# 
# 
# 
# # number = int(input('Введите первое число: '))
# # step = int(input('Введите шаг: '))
# # summ = 0
# # print('\nIP адрес', end = ' ')
# # for count in range(3):
# #     print(number, end = '.')
# #     summ += number
# #     number += step
# # print(summ)
# 
# 
# # text = input('Введите текст: ')
# # #first_sym = input('Введите первую букву: ')
# # #second_sym = input('Введите вторую букву: ')
# # firstSymCount = 05
# # secondSymCount = 0
# #
# # for symbol in text:
# #     if symbol == 'Ы':
# #         firstSymCount += 1
# #     if symbol == 'ы':
# #         secondSymCount += 1
# #
# # print('Больших букв Ы: ', firstSymCount)
# # print('Маленьких букв ы: ', secondSymCount)
# 
# # text = input('Введите текст: ')
# # first_sym = input('Введите первую букву: ')
# # second_sym = input('Введите вторую букву: ')
# # firstSymCount = 0
# # secondSymCount = 0
# #
# # for symbol in text:
# #     if symbol == first_sym:
# #         firstSymCount += 1
# #     if symbol == second_sym:
# #         secondSymCount += 1
# #
# # print(firstSymCount, secondSymCount)
# 
# # phrase = input('Введите слово: ')
# # for i in phrase:
# #     print(i*5)
# #     print('=' * 10)
# 
# # username = input('Как тебя зовут? ')
# # print(username + ',', 'купи слона!')
# # while True:
# #     answer = input('')
# #     print('Все говорят', answer + ',', 'а ты купи слона!')
# 
# 
# # chief = ''
# # while chief != 'Да, конечно, сделал':
# #     if chief == 'Да, конечно, сделал' or chief == 'да, конечно, сделал':
# #         print('Молодец! ')
# #         break
# #     chief = input('Ты выполнил задание? ')
# 
# 
# 
# # badGradeCount = 0
# # for stundent in range(5):
# #     answer = input('Кто написан Евгений Онегин? ')
# #     if answer == ('Пушкин') or answer == ('пушкин'):
# #         print('Молодец! Садись, пять!')
# #         break
# #     print('Плохо! Садись, два! ')
# #     badGradeCount += 1
# # print('Количество двоек: ', badGradeCount)
# 
# # boys = int(input('Введите количество мальчиков: '))
# # girls = int(input('Введите количество девочек: '))
# # answer = ''
# # if (boys > 2 * girls) or (girls > 2*boys):
# #     print('Нет решения! ')
# # elif boys >= girls:
# #     k = boys - girls
# #     for bgb in range(k):
# #         answer += 'BGB'
# #     for bg in range(girls - k):
# #         answer += 'BG'
# # else:
# #     k = girls - boys
# #     for gbg in range(k):
# #         answer += 'GBG'
# #     for gb in range(boys - k):
# #         answer += 'GB'
# # print(answer)
# 
# 
# # x = int(input('Введите x: '))
# # for num in range(2, 65 // 2):
# #     num *= 2
# #     print(num)
# # for den in range(1, 64 // 2):
# #     den = den * 2 + 1
# #     print(den)
# # #res = ((x-1)(x-3)(x-7)…(x-63) / ((x-2)(x-4)(x-8)…(x-64))
# # #print(res)
# 
# # n = int(input('Введите натуральное число n: '))
# # for i in range(1, n + 1):
# #     s = 1 - 1/2 + 1/4 - 1/8 + (-1)**n * 1/2**n
# #     print(s)
# 
# # educational_grant = int(input('Введите стипендию: '))
# # expenses = int(input('Введите расходы на проживание в месяц: '))
# # expenses_summ = expenses
# # for month in range(2, 11):
# #     expenses_summ += expenses * (1+(3/100))
# # print('Итого расходы на проживание: ', expenses_summ)
# # print('У родителей необходимо попросить: ', expenses_summ - educational_grant)
# 
# # length = int(input('Введите длину письма: '))
# # count = 0
# # while length > 12:
# #     length //= 2
# #     print(length)
# #     count += 1
# # print('Сложите пополам', count, 'раза и письмо войдет в конверт')
# 
# 
# #if length > 12 or width > 12:
# #    print('Сложите ', (length // 12) - 2, 'раз')
# #else:
# #    print('Письмо входит')
# 
# 
# 
# # a = int(input('Введите начало отрезка: '))
# # b = int(input('Введите конец отрезка: '))
# # step = int(input('Введите шаг: '))
# # for x in range(b, a - 1, step):
# #     y = x**3 + 2*x**2 - 4*x + 1
# #     print('В точке', x, 'функция равна', y)
# 
# 
# # a = int(input('Введите число a: '))
# # b = int(input('Введите число b: '))
# # c = int(input('Введите число c: '))
# # summ = 0
# # count = 0
# # for i in range(a, b+1):
# #     if i % c == 0:
# #         count += 1
# #         print(i)
# #         summ += i
# # print('Среднее арифметическое данных чисел: ', summ / count)
# 
# 
# # count = 0
# # for num in range(1, 11):
# #     num_input = int(input(f'Введите число {num}: '))
# #     if num_input % 2 == 0 and num_input >= 0:
# #         count += 1
# # print('Четных и положительных чисел: ', count)
# 
# # salary_year = 0
# # for month in range(1, 13):
# #     salary_month = int(input(f"Введите зарплату за {month} месяц: "))
# #     salary_year += salary_month
# # print('Ваша средняя зарплата за год: ', salary_year / 12)
# 
# # reverse_timer = int(input('Сколько секунд готовить? '))
# # count = 0
# # for sec in range(reverse_timer, 0, -1):
# #     print('Секунда', sec - 1)
# #     finish = int(input('Вы готовы забрать еду? '))
# #     count += 1
# #     if finish == 1:
# #         print('Ваша еда готова, можете забрать')
# #         print('Еда готовилась', count, 'секунды')
# #         break
# # print()
# # print('Ваша еда готова, осторожно горячo!')
# 
# 
# # debtor = int(input('Введите количество должников: '))
# # count = 0
# # for i in range(0, debtor + 1, 5):
# #     print('Должник с номером', i)
# #     debt = int(input('Сколько должны? '))
# #     count += debt
# # print()
# # print('Общая сумма долга:', count)
# 
# # print('Расход гречки 4 кг в месяц. Я рассчитаю, на сколько вам хватит запаса')
# # buckwheat = int(input('Сколько кг гречки у вас есть? '))
# # n = 0
# # for month in range(buckwheat, 1, -4):
# #     n += 1
# #     print('Запас', n, 'месяца: ', month, 'кг')
# # print()
# # print('Вам хватит гречки на', n, 'месяцев')
# 
# # sec = int(input('Введите количество секунд: '))
# # for i in range (sec // 2, 0, -1):
# #     i *= 2
# #     print(i)
# # print('Я иду искать! ')
# 
# #6 5 4 3 2 1
# #6 4 2
# # totalsoldiers = int(input('Количество солдат: '))
# # totalrules = int(input('Сколько правил в уставе? '))
# # pushups = 0
# # for soldier in range(totalsoldiers, 0, -4):
# #     soldierrules = int(input("Сколько правил в уставе? "))
# #     if totalrules != soldierrules:
# #         print('Неправильно', 10 * soldier, 'отжиманий')
# #         pushups += 10 * soldier
# # print('Всего отжиманий: ', pushups )
# 
# 
# # count = 0
# # n = int(input('Введите число стульев: '))
# # for number in range(1, n + 1, 5):
# #     count += number
# #     print('Номер стула: ', number)
# # print('Сумма: ', count)
# 
# # wake_up = int(input('Во сколько проснулся? '))
# # water = 0
# # awake_h = 0
# # cal_sum = 0
# #
# # for hours in range(wake_up, 23, 3):
# #     water += 1
# #     print('Сейчас', hours, 'часов')
# #     calories = int(input('Сколько сьел за час '))
# #     cal_sum += calories
# #     if cal_sum >= 2000:
# #         print('Хорошо поел, поспи')
# #         break
# #     awake_h += 1
# # print('Сьедено калорий за день', cal_sum)
# # print('часов не спал', awake_h)
# # print('выпито листров воды', water)
# 
# 
# # n = int(input('Введите число: '))
# # for number in range(1, n // 2 + 1 + n%2):
# #     number = number * 2 - 1
# #     print(number, '** 2 = ', number ** 2)
# 
# # n = int(input('Введите число: '))
# # number = 1
# # while number <= n:
# #     print(number, '** 2 = ', number ** 2)
# #     number += 2
# 
# # total_h = int(input('Введите число: '))
# # cells = 1
# # for hour in range(1, total_h // 3 + 1):
# #     cells *= 2
# #     print('Прошло часов: ', hour * 3)
# #     print('Количество клеток: ', cells)
# #     print('Осталось часов: ', total_h - hour * 3)
# #     print()
# # print('Наблюдение завершилось! ')
# 
# # n = int(input('Введите число: '))
# # for number in range(1, n // 2 + 1):
# #     number *=2
# #     print(number, '** 3 = ', number ** 3)
# 
# # card_num = int(input('Введите количество карточек: '))
# # count = 0
# # summ = 0
# # for i in range(1, card_num + 1):
# #     count += i
# # for i in range(card_num - 1):
# #     card = int(input('Введите номер оставшейся карточки: '))
# #     count -= card
# # print('Потерянная карта: ', count)
# 
# # card_num = int(input('Введите количество карточек: '))
# # count = 0
# # summ = 0
# # for i in range(1, card_num + 1):
# #     count += i
# # for i in range(card_num - 1):
# #     card = int(input('Введите номер оставшейся карточки: '))
# #     summ += card
# # card_x = count - summ
# # print('Потерянная карта: ', card_x)
# 
# 
# # for i in range(15, 99):
# #     if (i // 10) * (i % 10) * 3 == i:
# #         print(i)
# 
# # a = int(input('Введите число а: '))
# # b = int(input('Введите число b: '))
# # summ = 0
# # count = 0
# # for i in range(a, b + 1):
# #     if i % 3 == 0:
# #         count += 1
# #         summ += i
# # print('Сумма чисел кратных 3: ', summ)
# # print('Всего чисел, удовлетворяющих условию: ', count)
# # print('Среднее арифметическое суммы чисел: ', summ / count)
# 
# 
# # student = int(input('Сколько человек в классе? '))
# # summ = 0
# # sat = 0
# # good = 0
# # exc = 0
# # for i in range(1, student + 1):
# #     rate = int(input('Введите оценку: '))
# #     if rate == 3:
# #         sat += 1
# #     if rate == 4:
# #         good += 1
# #     if rate == 5:
# #         exc += 1
# # if sat > good and sat > exc:
# #     print('Сегодня больше троечников!')
# # elif good > sat and good > exc:
# #     print('Сегодня больше хорошистов')
# # else:
# #     print('Сегодня больше отличников')
# # #elif exc > good and exc > sat:
# # #    print('Сегодня больше отличников')
# 
# # num = int(input('Введите число для расчета факториала: '))
# # n = 1
# # for i in range(1, num + 1):
# #     n *= i
# # print('Факториал числа', num, 'равен', n)
# 
# 
# # income1 = int(input('Зарплата за 1 месяц: '))
# # income2 = int(input('Зарплата за 2 месяц: '))
# # income3 = int(input('Зарплата за 3 месяц: '))
# # income4 = int(input('Зарплата за 4 месяц: '))
# # income5 = int(input('Зарплата за 5 месяц: '))
# # income6 = int(input('Зарплата за 6 месяц: '))
# # income7 = int(input('Зарплата за 7 месяц: '))
# # income8 = int(input('Зарплата за 8 месяц: '))
# # income9 = int(input('Зарплата за 9 месяц: '))
# # income10 = int(input('Зарплата за 10 месяц: '))
# # income11 = int(input('Зарплата за 11 месяц: '))
# # income12 = int(input('Зарплата за 12 месяц: '))
# # average = 0
# # summ = 0
# # for i in income1, income2, income3, income4, income5, income6, income7, income8, income9, income10, income11, income12:
# #     summ += i
# # print(summ)
# # average = summ / 12
# # print('Ваша средняя зарплата за год: ', average)
# 
# # num1 = int(input('Введите число 1: '))
# # num2 = int(input('Введите число 2: '))
# # num3 = int(input('Введите число 3: '))
# # num4 = int(input('Введите число 4: '))
# # num5 = int(input('Введите число 5: '))
# # num6 = int(input('Введите число 6: '))
# # num7 = int(input('Введите число 7: '))
# # num8 = int(input('Введите число 8: '))
# # num9 = int(input('Введите число 9: '))
# # num10 = int(input('Введите число 10: '))
# # count = 0
# # for i in range(num1, num10 + 1):
# #     if i % 2 == 0 and i >= 0:
# #         count += 1
# #         print(i)
# # print('Четных и положительных чисел: ', count)
# 
# 
# # start = 1
# # finish = 101
# #
# # count = 0
# # answer = 0
# # print('Вы загадали число 100?')
# # first_question = True
# # while answer != 1:
# #     if not first_question:
# #         print('Вы загадали число', n, '?')
# #
# #     answer = int(input('1 - равно, 2 - меньше, 3 - больше '))
# #     if answer == 2 and not first_question:
# #         finish = n
# #     elif answer == 3:
# #         start = n
# #
# #     count += 1
# #     n = (start + finish) // 2
# #     first_question = False
# #
# # print('Я угадал ваше число с', count, 'попытки')
# 
# # begin = int(input('Введите начальное число: '))
# # end = int(input('Введите конечное число: '))
# # summ = 0
# # for i in range(1, end + 1):
# #     summ *= i
# #     print(i)
# # print(summ)
# 
# # wake_up = int(input('Во сколько проснулся? '))
# # awake_h = 0
# # cal_sum = 0
# # for hours in range(wake_up, 23):
# #     print('Сейчас', hours, 'часов')
# #     calories = int(input('Сколько сьел за час ')
# #     cal_sum += calories
# #     if cal_sum >= 2000:
# #         print('Хорошо поел, поспи')
# #         break
# #     awake_h += 1
# # print('Сьедено калорий за день', cal_sum)
# # print('часов не спал', awake_h)
# 
# # begin = int(input('Введите начальное число: '))
# # end = int(input('Введите конечное число: '))
# # for number in range(begin, end + 1):
# #     print(number ** 3)
# 
# # num = 2
# # for num in range(21):
# #     print(num ** 2)
# 
# # hour = int(input('Который час? '))
# # for kuku in range(hour):
# #     print('Ку-ку!', kuku)
# 
# # for num in range(11):
# #     print(num ** 2)
# 
# # tmonths = int(input('Сколько месяцев будем копить? '))
# # summ = 0
# # for months in range(tmonths):
# #     print(('Месяц', months))
# #     money = int(input('Сколько рублей откладываем? '))
# #     summ += money
# # print('За', tmonths, 'месяцев ты накопишь', summ, 'рублей')
# 
# # winners = 0
# # for number in 345, 19, 87, 1020, 421:
# #     if number % 5 == 0 and number // 1000 == 0:
# #         print(number)
# #         winners += 1
# # print(winners)
# 
# 
# # for number in 3,7,5,6,4:
# #     print(number ** 2, number ** 3, number ** 4)
# 
# # for meters in 100,90,95,87,102:
# #  if meters % 3 == 0:
# #    print(meters, 'Подходит')
# #  else:
# #    print(meters, 'Не подходит')
# 
# # winners = 0
# # for number in 345, 19, 87, 1020, 421:
# #     if number % 5 == 0:
# #         print(number)
# #         winners += 1
# # print(winners)
# 
# # left = 1
# # right = 100
# # count = 0
# # middle = (left + right) // 2
# # print('Загадай любое число от 1 до 100!')
# # while True:
# #     num = int(input('Твоё число: 1 — равно, 2 — больше, 3 — меньше 50? '))
# #     count += 1
# #     middle = (left + right) // 2
# #     if num == 2:
# #         left = middle + 1
# #         right = (middle + right) // 2 - 1
# #         print('Может это: ', middle)
# #         print(left, 'левая граница', right, 'правая граница')
# #     if num == 3:
# #         right = middle - 1
# #         print('Может это: ', middle)
# #         print(left, 'левая граница', right, 'правая граница')
# #     if num == 1:
# #         print('Я молодец, я угадал!')
# #         break
# # print('Число попыток: ', count)
# 
# # n = (1 + 100) // 2
# # count = 0
# # print('Загадай любое число от 1 до 100!')
# # print('Твоё число равно?', n)
# # while True:
# #     num = int(input('Твоё число: 1 — равно, 2 — больше, 3 — меньше '))
# #     count += 1
# #     if num == 2:
# #         n += 1
# #         print('Может это: ', n)
# #     if num == 3:
# #         n -= 1
# #         print('Может это: ', n)
# #     if num == 1:
# #         print('Я молодец, я угадал!')
# #         break
# # print('Число попыток: ', count)
# 
# 
# 
# # target = 785
# # count = 0
# # while True:
# #     num = int(input('Введите число: '))
# #     if num < target:
# #         count += 1
# #         print('Число меньше, чем нужно. Попробуйте ещё раз!')
# #     if num > target:
# #         count += 1
# #         print('Число больше, чем нужно. Попробуйте ещё раз!')
# #     if num == target:
# #         count += 1
# #         print('Вы угадали! Число попыток: ', count)
# #         break
# 
# 
# # deposit_x = int(input('Сколько денег на вкладе? '))
# # percent_p = int(input('Какой процент по депозиту? '))
# # target_y = int(input('Сколько денег хочешь? '))
# # count = 0
# #
# # while deposit_x <= target_y:
# #     deposit_x += (deposit_x * percent_p) // 100
# #     count += 1
# #     print(deposit_x, count, '- год')
# # print('Деньги должны пролежать на вкладе, лет: ', count)
# 
# 
# # print('Начался восьмичасовой рабочий день.')
# # job_day = 1
# # summ_task = 0
# # summ_wife = 0
# # while job_day <= 8:
# #     print(job_day, '-й час')
# #     job_day += 1
# #     task = int(input('Сколько задач решит Максим? '))
# #     summ_task += task
# #     wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
# #     summ_wife += wife
# # print('Рабочий день закончился. Всего выполнено задач:', summ_task)
# # if summ_wife > 0:
# #     print('Нужно зайти в магазин.')
# 
# # count_plus = 0
# # count_minus = 0
# # while True:
# #     num = int(input('Введите число: '))
# #     if num > 0:
# #         count_plus += 1
# #     if num < 0:
# #         count_minus += 1
# #     if num == 0:
# #         break
# # print('Кол-во положительных чисел:', count_plus)
# # print('Кол-во отрицательных чисел:', count_minus)
# 
# # number = int(input('Введите число для подсчета количества цифр: '))
# # count = 0
# # while number != 0:
# #     last_num = number % 10
# #     count += 1
# #     #print(count)
# #     if last_num == 0:
# #         break
# #     number //= 10
# # print('Количество чисел: ', count)
# 
# 
# 
# # print('Василий, ваша задолженность составляет 100 рублей.')
# # while True:
# #     debt_pay = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
# #     if debt_pay >= 100:
# #         print('Отлично, Василий! Вы погасили долг. Спасибо!')
# #         break
# #     print('Маловато, Василий. Давайте ещё раз.')
# 
# 
# # num = int(input('Сколько чисел возвести в степень? '))
# # count = 1
# # while count <= num:
# #     print(count ** 3)
# #     count += 1
# 
# # text = 'Я программист! '
# # count = 0
# # num = int(input('Сколько раз вывести текст? '))
# # while count < num:
# #     print(text)
# #     count += 1
# 
# 
# 
# # bags = int(input('Сколько нужно перетащить мешков? '))
# # totalweight = 0
# # bags_count = 0
# # while bags_count < bags:
# #     weight = int(input('Сколько весит мешок? '))
# #     totalweight += weight
# #     bags_count += 1
# #     print('Перенесли мешков', bags_count)
# # print(totalweight)
# 
# # count = 0
# # text = 'Python!'
# # while count < 100:
# #     print(text)
# #     count += 1
# 
# # while True:
# #     print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
# #     code = int(input('Введите код: '))
# #     if code == 550:
# #         break
# # print('Код верный, завершаю работу...')
# 
# # #work = int(input('Продолжаем работать? 1/0: '))
# # while True:
# #     work = int(input('Продолжаем работать? 1/0: '))
# #     if work == False:
# #         print('Приложение закрывается…')
# #         break
# # print('Работа завершена')
# 
# # count = 10
# # while  count >= 0:
# #     print(count)
# #     if count == 0:
# #         break
# #     count -= 1
# # print('Время вышло!')
# 
# # count = 10
# # while count + 1:
# #     print(count)
# #     count -= 1
# # print('Время вышло!')
# 
# 
# 
# 
# # balance = int(input('Введите стартовую сумму: '))
# # while balance < 10000:
# #     cube = int(input('Сколько выпало на кубике? '))
# #     if cube == 3:
# #         balance = 0
# #         print('Вы проиграли всё!')
# #     print('Выйграли 500 рублей')
# #     balance += 500
# # print('Game over')
# # print('Баланс:', balance)
# 
# # number = int(input("Введите число: "))
# # summ = 0
# # while number != 0:
# #     summ += number
# #     number = int(input("Введите число: "))
# #
# # print(summ)
# #
# # number = int(input('Введите число: '))
# # summ = 0
# # while number != 0:
# #     summ += number
# #     number = int(input('Введите число: '))
# # print(summ)
# 
# 
# # numbers = int(input("Введите число: "))
# # summ_of_numbers = 0
# # while numbers != 0:
# #     last_number = numbers % 10
# #     if last_number == 5:
# #         print("Обнаружен разрыв")
# #         break
# #     summ_of_numbers += last_number
# #     numbers //= 10
# #
# # print(summ_of_numbers)
# #
# # number = int(input('Введите число: '))
# # summ = 0
# # while number != 0:
# #     last_num = number % 10
# #     print(last_num)
# #     if last_num == 5:
# #         print('Обнаружен разрыв')
# #         break
# #     summ += last_num
# #     number //= 10
# # print('Сумма: ', summ)
# 
# # t = int(input('сколько на улице градусов?? '))
# # distance = 0
# # while t > 15:
# #     distance += 20
# #     t -= 2
# #     if t <= 15:
# #         break
# #         print('Температура упала')
# #     distance += 10
# # print(distance)
# 
# 
# 
# 
# # balance = int(input('Сколько отложить денег?? '))
# # while balance < 500000:
# #     bank = int(input('В копилке еще недостаточно. Сколько отложить денег?? '))
# #     balance += bank
# #     print('Баланс: ', balance)
# # print('Ты накопил!')
# # print('Баланс счета: ', balance)
# 
# 
# # number = int(input('Введите число: '))
# # x = 0
# # while number > 0:
# #     summ = int(input('Введите число: '))
# #     x += summ + number
# #     print(number)
# # print(number)
# 
# 
# # number = int(input('Введите число: '))
# # while number != 0:
# #     print('Число не равно нулю!')
# #     new = int(input('Введите число: '))
# #     summ = new + number
# #     print('Сумма чисел равно: ', summ)
# # print('Число равно нулю')
# # print('Сумма введенных чисел равна: ', number)
# 
# # balance = int(input('сколько денег пришло? '))
# # while balance > 5000:
# #     product_cost = int(input('Введите стоимость товара: '))
# #     balance -= product_cost
# # print('Внимание! на карте осталось мало денег')
# # print('Баланс счета: ', balance)
# 
# 
# # experience = int(input('Введите количество опыта: '))
# #
# # level = 1
# # if 1000 <= experience < 2500:
# #     level += 1
# # elif 2500 <= experience < 5000:
# #     level += 2
# # elif 5000 <= experience:
# #     level += 3
# # print('Ваш уровень: ', level)
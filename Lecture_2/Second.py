# _________________________________Данные,функции и модули._____________________________________
# Файлы
# Работа с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+,r+

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()

# ___________________________Функции и модули_____________________________

# Это фрагмент программы используемый многократно

# def function_name(x):
# body line 1
# . . .
# body line n
# optional return

# import hello as h # import hello
# print(h.f(1))
# _____________________________________________________________________________________________
# def new_string(symbol, count):
#     return symbol*count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required

# def new_string(symbol, count = 3):
#     return symbol*count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12
# _______________________________________________________________________________________________
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...
# _______________________________________________________________________________________________
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34

# ___________________________________Кортежи____________________________________________________
# Кортеж- это неизменяемый "список"

# Example:
# a = (3, 1, 41, 4)
# a = (3,) --Кортеж из одного элемента делается с выставлением (,)
# print(a)
# print(a[3])
# a[0] = 12 Вылетит ошибка так как присвоить новое значение мы не можем!
# a = (3,4,5)
# for item in a:
#     print(item)

# ______________________________________________________________________________
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# ___________________________Распаковка кортежа________________________________________________

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# ______________________________Словари_____________________________________________________

# Словарь -- это неупорядоченные коллекции произвольных обьектов с доступом по ключу 

# dictionary = {}  #Обратный \ внизу, чтобы не писать все в одну строчку
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary['up'])
# dictionary['up'] = 'w'
# print(dictionary['up'])

# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ←
# # типы ключей могут отличатьсяfor
# for k in dictionary.keys():
#     print(k)

# ______________________________Множества_____________________________________________________

# Неупорядоченная совокупность элементов

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}
# _____________________________________________________________________________________________

# colors = {'red', 'green', 'blue'}
# print(type(colors))
# #exit()
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # Можно добавлять элементы
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # Удаление элементов
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok исключения
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } Отчиска множества
# print(colors) # set()
# ________________________________________________________________________________________________

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} Копирование множества 
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} Обьединение множества
# i = a.intersection(b) # i = {8, 2, 5} Пересечение множества
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# ______________________________Списки_____________________________________________________
# list1 = [1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e,end=" ")
# print()
# for e in list2:
#     print(e,end=" ")
# print()
# list1[0] =123
# for e in list1:
#     print(e,end=" ")
# print()
# for e in list2:
#     print(e,end=" ")
#____________________________________________________________________________________________
# list1 = [1,2,3,4,5]
# print(list1.pop())
# print(len(list1))
# print(list1)
# print(list1.pop())
# print(len(list1))
# print(list1)
# print(list1.pop(1))
# print(list1)
# print(list1.insert(1,11))
# print(list1)
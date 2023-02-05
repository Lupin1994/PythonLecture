# Урок 3. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# 
# def calc(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc, 10)

#____________________________________________________________________________
# def sum(x, y):
#     return x + y

# f = sum
#______________________________________________________________________________

# sum = lambda x,y: x+y # ТОже самое что и выше (def sum)


# def mult(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))


#     # return op(a,b)
# calc(lambda x,y: x+y, 3, 6)

# List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна из
# культовых фишек Python — list comprehension (редко переводится на русский, но можно
# использовать определение «генератора списка»). Comprehension легко читать, и их
# используют как начинающие, так и опытные разработчики. List comprehension — это
# упрощенный подход к созданию списка, который задействует цикл for, а также инструкции
# if-else для определения того, что в итоге окажется в финальном списке
#___________________________________________________________________________________________
# list = []

# for i in range(1,101):
#     if(i%2 == 0):
#         list.append(i)
# print(list)
#______________________________________Тоже самое только короче_____________________________
# list = [i for i in range(1,21) if i%2 == 0]
# print(list)
# #_________________________список кортежей____________________________________________________
# list = [(i , i) for i in range(1,21) if i%2 == 0]
# print(list)
#__________________________________________________________________________________________________
# def f(x):
#     return x**3
# list = [(i,f(i)) for i in range(1,21) if i%2 == 0]
# print(list)
#____________________________Добавление файла и работа с ним!!______________________________________
# path = "/Users/Comp/OneDrive/Рабочий стол/PythonLecture/Lecture_3/Nums.txt"
# f = open(path, 'r')
# data = f.read() + ' ' 
# f.close()
# print(data)

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
# print(numbers)    
# out = []

# for e in numbers:
#     if not e%2:
#         out.append((e, e **2))
# print(out)
#_________________________________________Тоже самое только с lambda __________________________________
# def select(f, col):
#     return [f(x) for x in col]
# def where(f,col):
#     return[x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x%2,res)
# res = select(lambda x: (x,x**2),res)
# print(res)


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2,res)
# res = list(map(lambda x: (x,x**2),res))
# print(res)
# #______________________________________________________________________________________________________

# Функция map
# Функция map() принимает указанную функцию к каждому эдементы итерируемого обьекта и возвращает 
# итератор с новым обьектами. 
# НЕЛЬЗЯ пройтись дважды!

# li = [x for x in range(1,20)]
# li = list(map(lambda x: x+10,li))
# print(li)
#_________________________________________________________________________
# data = list(map(int,input().split()))
# print(data)

# data = map(int,'1 2 3 5 46 8'.split())
# for e in data:
#     print(e*10)
# print('--')
# for e in data:
#     print(e)
    
# data = list(map(int,'1 2 3 5 46 8'.split()))
# for e in data:
#     print(e*10)
# print('--')
# for e in data:
#     print(e)

#___________________________________Функция filter________________________________________
# Функция filter() применяет указанную функцию к каждому элементу итерируемого обьекта и возвращет
# итератор с теми обьектами, для которых функция вернула True
# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2,data))
# print(res)
#___________________________________Функция zip________________________________________
# Функция zip() применяется к набору итерируемых обьектов и возвращает иератор с кортежем из 
# элементов входных данных. НЕЛЬЗЯ пройтись дважды!

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4,5,9,14,7]
# data = list(zip(users,ids))
# print(data)
#___________________________________Внизу особенность ________________________________________
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4,5,9,14,7]
# salary = [111,222,333]
# data = list(zip(users,ids,salary))
# print(data)
#___________________________________Функция enumerate________________________________________
# Функция enumerate() применяется к итерируемому обьекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных. НЕЛЬЗЯ пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,7]
salary = [111,222,333]
data = list(enumerate(users))
print(data)
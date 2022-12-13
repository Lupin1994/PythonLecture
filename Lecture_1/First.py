print("Hello worlds")


# Типы данных справедливы
# int, float, boolean, str, list и др.

#value = None
#a = 123
#b = 1.23
# print(a)
# print(type(b))
#value = 3
# print(type(value))
# s = 'Hello \'world' # эскейп последовательность,
# чтобы апостров был (\n - переход на новую строку)
# print(s) # write string
# print(a,'-',b,'-',s)
#print('{} - {} - {}'.format(a,b,s))
# print('{1} - {2} - {0}'.format(a,b,s)) # цифры это индексы
#print(f'{a} - {b} - {s}')

#f = True
#F = False
# print(f,F)
#list = [2,3, 'hello', True]
#col = [2,3,4, 'hello', True]
# print(list)
# print(col)
# print('Write a:')
# a = float(input())
# print('Write b:')
# b = int(input())
# print(a,'+',b,'=',a+b)
# a = 1.3123
# b = 3
# c=round(a*b,5)  #функция округления до ..
# Цыфра указавается отдельно
# print(c)
# a = 3
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,
# ^
# Кое-что ещё: is, is not, in, not in

# f = [1, 2, 4, 5]
# print(f)
# print(2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# Цикл While
# original = 232143
# inverted = 0
# while original!= 0:
#     inverted= inverted*10+(original%10)
#     original //=10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Цикл for


# for i in range(1,15,2):
#     print(i)

# list = [1,23,4,55,75,9]
# for i in list:
#     print(i**2)

# for i in 1,2,3,4,5,6:
#     print(i**2)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Описание функций

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))
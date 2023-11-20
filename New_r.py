# ывод содержимого списков
# a = [1, 2, 3, 'a', True]
# a = 'aboba'
# for i in a:
#     print(i)
# print()
# for i in range(len(a)):
#     print(a[i])
# print()
# print(*a) #распоковка списка, (обозначается звёздочкой)

# Строковые методы split() и join()
# lang = 'Python  C# Java'.split()
# print(lang)
#
# numbers = '1 2 3 4 5'.split()
# print(numbers)
# # print(int(numbers[0] + numbers[1])) склеивание
#
# words = 'To be or not to be that is the question'.split()
# print(words)
#
# ip = '192.168.1.1'.split('.')
# print(ip)
#
# terms = '1 + 2 + 3 + 4 = 10'.split('+')
# print(terms)
#
# Метод join()
# lang = ' '.join(['Python', 'C#', 'Java'])
# print(lang)
#
# numbers = ' '.join(['1', '2', '3', '4', '5'])
# print(numbers)
#
# words = 'To be or not to be that is the question'.split()
# print(words)
# words = ' '.join(words)
#
# ip = ['192', '168', '1', '1']
# print('.'.join(ip))
#
# terms = ['1', '2', '3', '4 = 10']
# print(' + '.join(terms))

# Словари
# a = {ключ: значение}

# a = {}
# print(a)
# print(type(a))
#
# a = {'a': 1, 'b': 2}
# print(a)
#
# a = dict([(1, 2), [4, 5]])
# print(a)
#
# a = {'a': 1}
# print(a['a'])
# a['a'] = 4
# a['b'] = 2
# print(a)

# Методы словарей
# clear() - очищает словарь
# copy() - возвращает копию словаря
# get() - возращает значение ключа, если ег нет, вернети None
# items() - возращает пары (ключ, значение)
# keys() - возвращает ключи в словаре
# pop() - удаляет ключ и возвращает его значение
# popitem() - удаляет и возвращает пару (ключ, значение)
# setdefault() - озвращает значение ключа, если его нет, создает ключ со значением
# uptade() - обновляет словарь, добавляя пары (ключ, значение)
# values() - возвращает значения в словаре

# a = {2: 1}
# print(a)
# a.clear()
# print(a)

# b = a.copy()
#print(b)
# c = a
# print(b is a)
# print(c is a)

#print(a.get(2, 3))
#print(a.get(1, 3))

# a = {2: 1, 'a': 4}
#print(a.items())

#print(a.keys())

# b = a.popitem()
# print(b)
# print(a)

# a.setdefault(3)
# print(a)

# a = {2: 1}
# a.update({'a': 2})
# print(a)
#
# print(a.values())

# Перебод словаря
# a = {2: 1, 'a': 2}
# for key in a:
#     print(key)
#
# for key, value in a.items():
#     print(key, value)
#
# for item in a.items():
#     print(item)

# Множества
# a = {1, 2, 3}
# a = set()
# print(a)

# set_1 = {1, 3, 4}
# set_1.add(2)
# print(set_1)
#
# set_1.update([4, 5, 6])
# print(set_1)

# emove()
# discard
# pop()

set_1 = {1, 2, 3, 4, 'a', 'p'}
set_1.remove(2)
print(set_1)

set_1.discard('a')
print(set_1)

set_1.pop()
print(set_1)

list_1 = [1, 2, 1, 3]
print(list_1)
list_1 = set(list_1)
print(list_1)
list_1 = list(list_1)
print(list_1)


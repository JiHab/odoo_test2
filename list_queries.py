# Вводим список
l = []
for l_i in range(2):
    l_temp = list(map(str, input().strip().split(' ')))
    l.append(l_temp)
print(l)
# Разбиваем на список/запрос
lx = l[0]
ly = l[1]
# Запрашиваем не по всему списку запросов, а по кол-ву указанову в начале.
count_y = int(ly[0])
# Ищем со второго элемента
index = 1
while index <= count_y:
    print(lx.count(ly[index]))
    index += 1
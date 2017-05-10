# Сама "обертка"
def make_it_cool(func):

    def wrapper():
        pers_list = func()
        # формируем список чобы отработал мап, иначе просто формирует объект.
        # Можно как-то по другому заставить отработать.
        a = list(map(f, pers_list))

    def f(l):
        # Проверка на пол
        if l[2] == 'М':
            string = 'Г-н'
        else:
            string = 'Г-жа'
        # Берем только имя и фамилию
        for i in range(2):
            string = string + ' ' + l[i]
        # Выводим
        print(string)
        return string
    return wrapper()

# Ну и обертываем
@make_it_cool
def getperson():
    l = []
    for l_i in range(3):
        l_temp = list(map(str, input().strip().split(' ')))
        l.append(l_temp)
    # Срезаем 1вый элемент
    person_list = l[1:]
    # Сортируем по ключу
    sorted_p_list = sorted(person_list, key=lambda person: person[3])
    return sorted_p_list






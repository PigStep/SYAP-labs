def func1():
    i=1
    s=0
    while s < 3:
        s+= 1 / i
        i+=1
    
    print(f"Результат задания 1: {i}")

def func2():
    s = input("Введите строку для задания 2: ").split()
    lst = []
    for i in s:
        if i.isdigit():
            lst.append(i)
    print(lst if len(lst) > 0 else "Строка не содержит чисел")

def func3():
    lst = list(map(int, input("Целые числа задания 3: ").split()))
    C = int(input("Ваше число C: "))

    num_counter = 0
    for i in lst:
        if i and i > C:
            num_counter +=1

    abs_lst = list(map(abs,(lst)))
    index_max = abs_lst.index(max(abs_lst))
    if index_max != len(lst) - 1:
        print(f"Числа больших {C} встречается в списке {num_counter} раз")
        multiplied_lst = 1
        for i in range(index_max, len(lst)):
            multiplied_lst *= lst[i]
        print(f"Произведение чисел, после {abs_lst[index_max]} в списке: {multiplied_lst}")
    else:
        print(f"Индекс максимального числа последний, Числа, большие {C} встречается в списке {num_counter} раз")
    
    pos = [lst[i] for i in range(len(lst)) if lst[i] > 0]
    for i in pos:
        lst.remove(i)

    print(f"Список без положительных чисел: {lst}")

def func4(s = 'I Love Python'):
    
    dct = {letter: s.count(letter) for letter in s}
    
    print(dct)

def func5():
    keys = ['цена', 'состав', 'количество на складе']

    s = int(input("Введите количество изделий: "))
    items = {}
    itm ={}

    for _ in range(s):
        name = input("Введите название изделия: ")
        for key in keys:
            param = input(f"Введите параметр ({key}): ")
            itm[key] = param

        items[name] = itm

    def see_descr(name):
        print(items[name]['состав'])
    
    def see_price(name):
        print(items[name]['цена'])

    def see_count(name):
        print(items[name]['количество на складе'])
    
    def see_all(name):
        print(items[name])
    
    def buy(name):
        items[name]['количество на складе'] = int(items[name]['количество на складе']) - 1
        if items[name]['количество на складе'] <= 0:
            items.pop(name)
            print('Изделие уже продано, исключение из списка')
            return
        print('Покупка успешна')
    
    def menu():
        choice = 0

        while choice != 6:
            print('1. Просмотр названия')
            print('2. Просмотр цены')
            print('3. Просмотр количества')
            print('4. Всю информацию')
            print('5. Покупка')
            print('6. Выход')
            
            choice = int(input('Выберите опцию: '))

            if choice == 6:
                return
            
            name = input('Введите название: ')

            if name not in items.keys():
                print('Изделие не найдено')
            else:
                if choice == 1:
                    see_descr(name)
                elif choice == 2:
                    see_price(name)
                elif choice == 3:
                    see_count(name)
                elif choice == 4:
                    see_all(name)
                elif choice == 5:
                    buy(name)
            
    menu()

def func6():
    a = set(input('Введите множество A: ').split())
    b = set(input('Введите множество B: ').split())

    print(f'Множества А, которых нет в В: {a - b}')

func1()
func2()
func3()
func4()
func5()
func6()
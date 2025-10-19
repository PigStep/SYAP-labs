"""
Вариант 19:
1. Написать функцию, которая считает сумму четных цифр введенного
натурального числа – 2 балла
2. Напишите функцию, которая будет принимать один аргумент. Если в
функцию передаётся список, найти среднее арифметическое всех чисел.
3. Напишите функцию, которая будет принимать один аргумент. Если
множество, вывести первые три наибольших значения.
Число – определить простое, или нет.
Строка – посчитать количество гласных. Удалить все знаки препинания
(, . ! ?).
Сделать проверку со всеми этими случаями. – 4 балла
3. Даны два числа n и m. Создайте двумерный массив размером n×m и
заполните его символами "." и "*" в шахматном порядке. В левом верхнем
углу должна стоять точка. – 2 балла
4. Напишите программу, демонстрирующую работу try except finally –
2 балла
"""

def func1():
    try:
        num = int(input("ЗАДАНИЕ 1=======\n Введите число: "))

        if num <= 0:
            print("Введенное число не является натуральным")

        hasOneFlag = False
        sum = 0
        for letter in str(num):
            if int(letter) % 2 ==0:
                hasOneFlag = True
                sum+= int(letter)
        
        if hasOneFlag:
            print("Сумма четных цифр введенного числа:", sum)
        else:
            print("Введенное число не содержит четных цифр")
    
    except ValueError as e:
        print("Введены не числовые данные:", e)
    except Exception as e:
        print("Ошибка выполнения задания 1: ", e)
    finally:
        print("Выполнение задания 1 завершено")


def _func2(x: int | list):
    try:
        if isinstance(x, list):
            sum = 0
            for i in x:
                if i.isdigit():
                    sum+=int(i)
            print("Среднее арифметическое всех чисел:", sum/len(x))
        else:
            print("Введенное число не является списком:",x)
    except Exception as e:
        print("Ошибка выполнения задания 2: ", e)
    finally:
        print("Выполнение задания 2 завершено")

def func2():
    _func2(input("Введите число для задания 2: "))
    _func2(input("Введите список для задания 2: ").split())

def _func3(x: int | set | str):
    try:
        if isinstance(x, int):
            isSimple = True
            for i in range(2, x // 2):
                if x % i == 0:
                    isSimple = False
                    break
            if isSimple:
                print(x, " - простое число")
            else:
                print(x, " - это НЕ простое число")

        elif isinstance(x, set):
            if len(x) < 3:
                raise ValueError("Введенное множество меньше трех элементов")
            
            max1 = 0
            max2 = 0
            max3 = 0

            for i in x:
                if i > max1:
                    max3 = max2
                    max2 = max1
                    max1 = i
                elif i > max2:
                    max3 = max2
                    max2 = i
                elif i > max3:
                    max3 = i
            print("Первые три наибольших значения:", max1, max2, max3)
        else:
            vowels = set('аеиоуыэюяё')
            punct = set('.,!?')
            vowels_count = 0

            for i in x.lower():
                if i in vowels:
                    vowels_count += 1
            
            print("Количество гласных:", vowels_count)

            for i in x:
                if i in punct:
                    x = x.replace(i, "")
            if len(x) == 0:
                x = "Строка была только из знаков препинания"
            print(f"Строк без знаков препинания: {x}")
            
    except Exception as e:
        print("Ошибка выполнения задания 3: ", e)
    finally:
        print("Выполнение части задания 3 завершено")


def func3():
    _func3(int(input("Введите число для задания 3: ")))
    _func3(set(map(int, input("Введите множество для задания 3: ").split())))
    _func3(input("Введите строку для задания 3: "))

def func4(n, m):
    try:
        if n < 1 or m < 1:
            raise ValueError("Введенные значения не являются натуральными")
        
        second_row = ["*" if i % 2 == 0 else "." for i in range(m) ]
        first_row = ["." if i % 2 != 0 else "*" for i in range(1,m+1) ]
        
        matrix = [first_row if i % 2 == 0 else second_row for i in range(n)]
        print("Матрица:")
        for i in range(n):
                print(matrix[i][::])
    except Exception as e:
        print("Ошибка выполнения задания 4: ", e)
    finally:
        print("Выполнение задания 4 завершено")

def func5(x):
    try:
        if x.isdigit():
            1 / int(x)
        else:
            raise ValueError("Введенное число не является натуральным")
    except Exception as e:
        print("Ошибка выполнения задания 5: ", e)
    finally:
        print("Выполнение задания 5 завершено")


func1()
func2()
func3()
func4(int(input("Введите количество строк: ")), int(input("Введите количество столбцов: ")))
func5(input("Задание 5: Введите 0 для проверки ошибки или другое число для выражения: 1 / "))
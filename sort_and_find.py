def listInput(): # ввод последовательности и проверка на использование пробела в качестве разделителя
    try:
        string = input("Введите последовательность чисел разделяя пробелом: ")
        list_of_strings = string.split(sep=" ")
        return list(map(int, list_of_strings))
    except ValueError as e:
        print("Введите корректную последовательность!")
        return listInput()


def sort(list_of_numbers): # сортировка
    for i in range(1, len(list_of_numbers)):
        x = list_of_numbers[i]
        idx = i
        while idx > 0 and list_of_numbers[idx - 1] > x:
            list_of_numbers[idx] = list_of_numbers[idx - 1]
            idx -= 1
        list_of_numbers[idx] = x
    print("Список был отсортирован: ", list_of_numbers)
    return list_of_numbers


def numInput(): # ввод числа
    global list_of_numbers_
    try:
        ind = int(input("Введите одно число из предоставленного ранее списка: "))
        if ind not in list_of_numbers_:  # проверка введенного числа на присутствие в списке
            print("Число отсутствует в списке, повторите ввод")
            return numInput()
        else:
            return ind
    except ValueError as e:
        print("Ошибка ввода!")


def binary_search(array, element, left, right): # поиск позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу
    if left > right:
        return "Такой элемент отсутствует"
    middle = (right + left) // 2
    if array[middle] < element <= array[middle+1]:
        return "Индекс искомого элемента = " + str(middle)
    elif element <= array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


list_of_numbers_ = listInput()
list_of_numbers_ = sort(list_of_numbers_)

print(binary_search(list_of_numbers_, numInput(), 0, len(list_of_numbers_)-1))
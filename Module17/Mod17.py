import math


# Введение последовательности чисел и ее проверка
now_input = input("Введите любую последовательность чисел (через пробел) - ")
try:
    None_Sort_List = [int(i) for i in now_input.split()]
    if len(None_Sort_List) < 2: raise Exception
except:
    print("Последовательность состоит не из чисел либо она слишком короткая")
    exit()


# Вводим число для вставки
try:
    number = int(input("Введите какое-либо число - "))
except:
    print("Это не число!")
    exit()


# Сортируем полученный массив
for i in range(1, len(None_Sort_List)):
    x = None_Sort_List[i]
    idx = i
    while idx > 0 and None_Sort_List[idx-1] > x:
        None_Sort_List[idx] = None_Sort_List[idx-1]
        idx -= 1
    None_Sort_List[idx] = x
print("Полностью отсортированный список:", None_Sort_List)


# Вставка через алгоритм двойного бинарного поиска
def double_bin_search(List, now_number, left, right):
    while True:
        # Это поиск индекса, если число больше или меньше всего списка или длина списка равна 1
        if (right - left) == 0:
            if List[left] > now_number:
                return 0
            elif List[right] < now_number:
                return len(List)

        # Находим 2 середины
        sum_rl = right + left
        if sum_rl % 2 != 0:
            middle_min = int(math.floor(sum_rl / 2))
            middle_max = int(math.ceil(sum_rl / 2))
        else:
            middle_min = int(sum_rl / 2)
            middle_max = middle_min + 1

        # Если подходит - то возвращаем позицию для команды insert
        if List[middle_min] <= now_number <= List[middle_max]:
            return middle_max

        elif List[middle_min] > now_number:
            left = middle_min + 1
            continue

        elif List[middle_max] < now_number:
            right = middle_max - 1
            continue


# Ищем индекс для вставки и вставляем элемент
index_insert = double_bin_search(None_Sort_List, number, 0, len(None_Sort_List)-1)
None_Sort_List.insert(index_insert, number)
print(None_Sort_List)

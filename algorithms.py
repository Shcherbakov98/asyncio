"""
Базовы алгоритмы (сортировки и поиска)

Временные сложности (от наиболее быстрого к медленному):
    Постоянное время O(n)
    Логарифмическое время O(logn)
    Линейное время O(n)
    Линейно-логаримфическое время O(nlogn)
    Квадратичное время O(n^2)
    Экспоненциальное время O(e^n)
"""
from bisect import bisect_left


# Рекурсия:


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Поисковые алгоритмы:


def linear_search(a_list, n):  # Линейный поиск или использовать оператор in: n in a_list
    for i in a_list:
        if i == n:
            return True
    return False


def binary_search(a_list, n):  # Двоичный (бинарный) поиск (только для отсортированных данных)
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


def binary_search_built(iterable, target):
    index = bisect_left(iterable, target)
    if index <= (len(iterable) - 1) and iterable[index] == target:
        return True
    return False


#  Алгоритмы сортировки:
def bubble_sort(a_list):  # сортировка пузырьком
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

    return a_list


def insertion_sort(alist):
    for i in range(1, len(alist)):
        value = alist[i]
        j = i - 1
        while j >= 0 and value < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = value
    return alist

insertion_sort([6, 5, 3])
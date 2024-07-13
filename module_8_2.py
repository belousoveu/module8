def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы {number, type(number)}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        # В условии - среднее арифметическое всех чисел. Соответственное не числа не учитываем в знаменателе
        return result[0] / (len(numbers) - result[1])
    except TypeError:
        print(f'Некорректный тип данных {numbers, type(numbers)}')
    except ZeroDivisionError:
        print(f'Деление на ноль. В переданных параметрах {numbers, type(numbers)} нет числовых значений')


if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
    print(f'Результат 5: {calculate_average([])}')  # пустой список

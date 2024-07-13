class IncorrectVinNumber(Exception):

    def __init__(self, message="Некорректный VIN номер"):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message="Некорректный номер"):
        self.message = message


class Car:

    @staticmethod
    def __is_valid_vin(vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип VIN номера')
        if vin not in range(1000000, 10000000):
            raise IncorrectVinNumber('Неверный диапазон для VIN номера')

    @staticmethod
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        if not numbers.isalnum():
            raise IncorrectCarNumbers('Некорректные символы для номеров')

    def __init__(self, model, vin, numbers):
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    def __setattr__(self, name, value):
        if name == '__vin':
            self.__is_valid_vin(value)
        if name == '__numbers':
            self.__is_valid_numbers(value)
        super().__setattr__(name, value)

    def __str__(self):
        return f'{self.model} {self.__vin} {self.__numbers}'

    def __repr__(self):
        return f'{self.model} {self.__vin} {self.__numbers}'

    def __hash__(self):
        return hash((self.model, self.__vin, self.__numbers))


if __name__ == '__main__':

    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

    try:
        forth= Car('Model3', 2020202, '1edf@1')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{forth.model} успешно создан')
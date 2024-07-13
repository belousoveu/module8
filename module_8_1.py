def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


if __name__ == '__main__':
    print(add_everything_up(1, 2))
    print(add_everything_up(1, '2'))
    print(add_everything_up(1, 2.0))
    print(add_everything_up('12', '2.0'))
    print(add_everything_up(12, 2.0))
    print(add_everything_up(2, False))
    print(add_everything_up('12', [12, 'abc', True]))
    print(add_everything_up('12', {12: 'abc', 13: 'abc', 14: True}))

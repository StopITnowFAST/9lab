#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
# числa

if __name__ == '__main__':
    new = {}
    numbers = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }
    x = numbers.items()
    for x, y in numbers.items():
        new.setdefault(y, x)
    print(new)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: 
# 1. ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; 
# 2. записи должны быть упорядочены по алфавиту; 
# 3. вывод на дисплей фамилий и номеров групп для всех студентов, имеющих хотя бы одну оценку 2;
# 4. если таких студентов нет, вывести соответствующее сообщение.

if __name__ == '__main__':

    N = 5
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            buf = [int(a) for a in input().split()]
            marks = list(filter(lambda x: x > 0 and x < 6, buf))
            if len(marks) != N:
                continue

            student = {
              'name': name,
              'group': group,
              'marks': marks,
            }

            students.append(student)

            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Группа",
                    "Успеваемость"
                )
            )
            print(line)

            for idx, student in enumerate(students, 1):
                marks = student.get('marks', ''),

                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        ' '.join(map(str, marks)),
                    )
                )
            print(line)

        elif command == 'marks':
            count = 0
            line = '+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 10
            )
            for student in students:
                if 2 in student.get('marks'):
                    count += 1
                    if count == 1:
                        print(line)
                    print(
                        '| {:<30} | {:^10} |'.format(
                            student.get('name', ''),
                            student.get('group', ''),
                        )
                    )
                    print(line)

            if count == 0:
                print("Студенты не найдены.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

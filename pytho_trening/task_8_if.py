# # Программа проверяет является ли положительным
# # или отрицателььным и выводит соответствующее.
#
# num = 3
#
# Так же попробуйте следующие вырианты значений num.
# num = -5
# num = 0
#
# if num >= 0:
#     print('Число больше либо равно 0')
# else:
#     print('Число отрицательное')
#
# def task_yes_no (str_1, str_2):
#     if str_1 in str_2:
#         print('Да')
#     else:
#         print("Нет")
#
# task_yes_no(str_1='test', str_2='test1')
#
# str_1 = 'test'
# str_2 = 'test1'
#
# if num >= 0:
#     print('Число больше либо равно 0')
# else:
#     print('Число отрицательное')


# num_float = -3.4
#
# # Так же попробуйте варианты
# # num_float = 0
# # num_float = -4.5
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('Ноль')
# else:
# print('Число отрицательное')


#
# num = 8
#
# permit_print = True
#
# if num > 0 and permit_print:
#     print('num - Положительное число')
# elif not permit_print:
#     print('Печать запрещена')
#
#

# def student_rank(year_of_study):
#     if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
#         print('Вы бакалавр')
#     elif year_of_study in range(5, 7):
#             print('Вы магистр')
#     elif 7 <= year_of_study <= 9:
#             print("Вы аспирант")
#     else:
#         print('Введите корректный год обучения')
#
# student_rank(12)

a = -200

if a > 100 or a < -100:
    print("-")
else:
    print('+')
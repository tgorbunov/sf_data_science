"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
#Disclaimer: по PEP8 все аннотации должны быть на англ, но так как это учебный курс, делаю сноску что все комментарии будут на русском.

import numpy as np

#мы можем задать любой диапазон чисел (не только от 1 до 100)
num_start = 1 # число "от"
num_stop = 101 # число "до" (не включительно)

#рандит в зависимости от условий (по условию домашней работы от 1 до 100)
number = np.random.randint(num_start, num_stop) # программа загадывает псевдослучайное число

#функция по угадыванию числа
def guess_number(number, num_start, num_stop):
  count = 0 #счетчик попыток
  low = num_start  # переменная на нижнюю границу
  high = num_stop - 1  # переменная на верхнюю границу

  while True:
    count += 1
    predict_number = (low + high) // 2  #по умолчанию програма будет начинать с середины данного промежутка
    #программа будет уменьшать промежуток в 2 раза за каждый проход
    if predict_number == number:
       print(f"Вы угадали, это число = {predict_number}! Задача решена за {count} попыток.")
       break
    elif predict_number > number:
       print(f"Попытка {count}: число {predict_number} меньше загаданного!")
       high = predict_number - 1  # делаем коррекцию на верхний край т.к. загаданное число меньше
    elif predict_number < number:
       print(f"Попытка {count}: число {predict_number} больше загаданного!")
       low = predict_number + 1  # делаем коррекцию на нижний край т.к. загаданное число больше


# RUN
guess_number(number, num_start, num_stop)
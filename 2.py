#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import sys 

if __name__ == "__main__":


    # Проверяем, что программе был передан только один аргумент командной строки
    LINES = 10

    # Открываем файл на чтение
    x = input("Введите имя файла: ")
    inf = open(x, "r", encoding="utf-8")
    
    # Читаем файл, сохраняя LINES последних строк
    lines = []
    for line in inf:
        # Добавляем последнюю прочитанную строку к концу списка
        lines.append(line)
        # Если у нас накопилось больше LINES строк, удаляем самую старую
        if len(lines) > LINES:
            lines.pop(0)
    
    # Отображаем последние строки из файла
    for line in lines:
        print(line, end="")
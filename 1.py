#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    text = "Python is the modern day language. It makes things so simple.\n It is the fastest-growing programing language\n \nasssss Python has an easy syntax and user-friendly interaction.". split() #(.split() преобразует текст в список слов)
    word = input("какое слово Вас интересует?")
    if word in text:
        print(text)

    else:
        print("таких слов нет в данном тексте")
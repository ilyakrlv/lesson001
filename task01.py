"""
Первое задание.
Строки документации находятся между трех двойных кавычек.
Согласно документации PEP8 этот стиль комментария называется - documentation string aka 'docstrings'.
PEP8 унаследовал его из правил PEP257, и рекомендует писать в начале каждого модуля, функции, класса или метода.
Причем, если речь идет о комментировании функции, то писать docstrings надо сразу после строки def.
Важно, что последние три двойные кавычки, должны находится на отдельной строке.

На самом деле, это ведь обычная строка. Она не присвоена никакой переменной, а ей значит не выделяется место
в памяти. И эту особенность как раз и используют программисты Python.
"""

# Это обычный комментарий. Символ # пишется вначале строки, после него должен быть пробел.
# PEP8 рекомендует писать комментарий на английском, чтобы ваши мысли были понятны разработчикам из разных стран.
# Желательно чтобы строка комментария содержала одно предложение, начиналась с большой буквы и заканчивалась точкой.

print('hello world')  # Такой стиль комментария называется inline comment. От последнего символа не менее двух пробелов.
a = 1
if a == 1:
    # А это блочный комментарий. Их пишут внутри блоков (как здесь, например).
    # Символ # должен отступить от начала строки, столько же сколько и блок.
    b = 1
else:
    b = 0

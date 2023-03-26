"""
Третье задание.
Строки. Операции со строками. + *.
Кавычки " против ', кавычки внутри кавычек. Спецсимволы \t, \n и экранирование \.
Форматированные строки s = f'Привет {name}}'. Сырые строки s = r'Все что \tebe угод\nо'
Многострочные строки:
verse = 'Я пришел к тебе с приветом\n \
рассказать, что солнце встало'
---
verse = ('Я пришел к тебе с приветом\n'
		 'рассказать, что солнце встало')
---
verse = 'Я пришел к тебе с приветом\n'\
		 'рассказать, что солнце встало'
---
verse = '''\
Я пришел к тебе с приветом
рассказать, что солнце встало'''
---
Индексация: s[0]; s[len(s)-1]; s[-1]; s[-len(s)]. Только для чтения, вот так s[0]='A' присваивать - нельзя
Срезы:
s[START:FINISH:STEP]		# START и FINISH м.б. больше  len(s)
							# Опуская параметр START - получим строку с начала
							# Опуская параметр FINISH - получим строку до конца
							# Отрицательный STEP - переворачивает направление чтения
+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | W | o | r | l | d |
+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9   10  11
-11-10 -9  -8  -7  -6  -5  -4  -3  -2  -1

TODO: Есть список клубов: myFavs = 'Реал Мадрид, Манчестер Юнайтед, Локомотив, Тоттенхэм Хотспур, Торпедо НН'
TODO: При помощи срезов вывести названия футбольных клубов, название хоккейного клуба вывести задом-наперед.

Методы строк: Наиболее ходовые strip; split\join; upper\lower; find; replace; isdigit\isalpha
TODO: Найти описание функций и привести примеры их использования.

Согласно документации PEP8 правила именований переменных туманны. Но, PEP8 не рекомендует использовать одиночные символы
o,O,l,I - в качестве переменных (O похоже на 0, l на I). Не рекомендуется начинать и заканчивать переменные символом _.
CamelStyle + snake_style = Camel_Snake это ugly! Не следует делать имена файлов длинее 8 символов, это может привести
к неработотспособности кода на старых системах.
"""

print('y', 'x', 'z', 'F') #Напечатаем заголовки таблицы
for y in range(2): #Берём все переменные и меняем их в циклах '0' и '1'
	for x in range(2):
		for z in range(2):
			for w in range(2):
				F = ((not x or y) == (not z or w)) or (x and w) #Записываем функцию
				if not F:
					print(x, y, z, F) #Выводим результат
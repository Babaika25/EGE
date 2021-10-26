a = '9' * 1000

while '999' in a or '888' in a:
	if '888' in a:
		a = a.replace('888', '9', 1)
	else:
		a = a.replace('999', '8', 1)
print(a)
def convert_base(num, to_base=10, from_base=10):
    # Перевод в десятичную систему
    if isinstance(num, str): # Если число - строка, то ...
        n = int(num, from_base) # ... переводим его в нужную систему счисления
    else: # Если же ввели число, то ...
        n = int(num) # ... просто воспринять его как число
    # Перевод десятичной в 'to_base' систему
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Берём алфавит
    if n < to_base: # Если число меньше системы счисления в которую переводить...
        return alphabet[n] # ... вернуть значения номера в алфавите (остаток от деления)
    else: # Иначе...
        return convert_base(n // to_base, to_base) + alphabet[n % to_base] # ... рекурсивно обратиться к функии нахождения остатка

print(convert_base('23', 21, 4))
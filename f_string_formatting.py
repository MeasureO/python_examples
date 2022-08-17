x = 11
y = 98
print(f"{x=}, {y=}")
#пробелы будут учтены
print(f"{x  =}, {y= }")


n = 12345
print(f'{n:8d}')
print(f'{n:7d}')
print(f'{n:6d}')
print(f'{n:5d}')
print(f'{n:4d}')

n = 12345
print(f'{n:08d}')
print(f'{n:07d}')
print(f'{n:06d}')
print(f'{n:05d}')
print(f'{n:04d}')

n = 12345678912345

print(f'{n:,d}')
print(f'{n:_d}')

sep = '%'
print(f'{n:{sep}d}') # вложенная f-строка


print(f'Число\t\tКвадрат\t\tКуб')
for x in range(1, 11):
   print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')
    
    
    

number = 12345.6789
print(f"Число {number = }")
print(f"|{number:25}|")
print(f"|{number:<25}|")
print(f"|{number:>25}|")
print(f"|{number:^25}|")
print('-'*25)
text = "Python 3.10"
print(f"Строка {text = }")
print(f"|{text:25}|")
print(f"|{text:<25}|")
print(f"|{text:>25}|")
print(f"|{text:^25}|")




number = 12345.6789
print(f"Число {number = }")
print(f"|{number:=<25}|")
print(f"|{number:=>25}|")
print(f"|{number:=^25}|")
print('-'*25)
text = "Python 3.10"
print(f"Строка {text = }")
print(f"|{text:-<25}|")
print(f"|{text:!>25}|")
print(f"|{text:?^25}|")

APPLES = .50
BREAD = 1.50
CHEESE = 2.25
num_apples = 3
num_bread = 10
num_cheese = 6
price_apples = num_apples * APPLES
price_bread = num_bread * BREAD
price_cheese = num_cheese * CHEESE
str_apples = 'Яблоки'
str_bread = 'Хлеб'
str_cheese = 'Сыр'
total = price_bread + price_cheese + price_apples
print(f'{"Список покупок":^30s}')
print(f'{"=" * 30}')
print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
print(f'{str_cheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
print(f'{"Total:":>20s}\t${total:>5.2f}')

a = int(input('Введите тута первое число: '))
b = int(input('Здеся второе: '))
c = int(input('Кстати, а как решать задачу с шахматами? Ой, 3 число: '))
if a > b < c:
    print(b)
elif b > a < c:
    print(a)
else:
    print(c)
a = int(input('Введите тута первое число: '))
b = int(input('Здеся второе: '))
c = int(input('Кстати, а как решать задачу с шахматами? Ой, 3 число: '))
def print_min(min):
    print('Минимальное число = ', min)
if a > b < c:
    print_min(b)
elif b > a < c:
    print_min(a)
else:
    print_min(c)
#Если нет ни одного нуля - вывести: "Нет нулевых значений!!!"
a = int(input())
b = a !=0 and ('no 0 here')
print (b)
#Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" 
a=int(input())
b=int(input())
c=int(input())
print (a != 0 and b!=0 and c!=0 and 'No 0 values')
nul = a or b or c or 'All numbers are 0'
print (f'First no 0 value = {nul}')

#Если первое значение  больше чем сумма второго и третьего вывести a - b - c
a=int(input())
b=int(input())
c=int(input())
if a > b + c:
    print (a - b - c)
#Если первое значение меньше чем сумма второго и третьего вывести b + c - a
a=int(input())
b=int(input())
c=int(input())
if a < b + c:
    print(b + c - a)
#Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
a=int(input())
b=int(input())
c=int(input())
if a > 50 and b > a or c > a:
    print('Вася')
#Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
a=int(input())
b=int(input())
c=int(input())
if a > 5 or b == 7 or c == 7:
    print('Петя')
elif a != 0 or b != 0 or c !=0:
    print('Нет нулевых значений!!!')

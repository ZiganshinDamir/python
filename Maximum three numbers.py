#Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).


a = int(input())
b = int(input())
c = int(input())
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
else:
    print(c)

# calc.


x=float(input("Введите первое число: "))
a=str(input("Введите действие +,-,*,/: "))
y=float(input("Введите второе число: "))
if a=="+":
    print(x+y)
elif a=="-":
    print(x-y)
elif a=="*":
    print(x*y)
else:
    print(x/y)
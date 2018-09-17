def calc(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('不正な引数が指定されました。')

print(calc(100, 10))
print(calc(100, 0))
print(calc(5, 2))

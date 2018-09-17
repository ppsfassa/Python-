def calc(num1, num2):
        return num1 / num2

try:
    print(calc(100, 10))
    print(calc(100, 0))
    print(calc(5, 2))
except Exception:
    print('不正な引数が指定されました。')

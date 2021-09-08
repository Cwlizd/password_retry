
n = 3
while True:
    X = input('請輸入你的密碼:')
    if X == ('abcd'):
        print('登入成功')
        break
    n = n - 1
    if n == 0:
        break
    print('密碼錯誤，你剩下',n,'次機會')


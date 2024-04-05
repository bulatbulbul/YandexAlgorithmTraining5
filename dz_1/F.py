def f():
    n = int(input())
    input_string = input()
    mas = [int(x) for x in input_string.split()]
    if mas[0] % 2 == 1:
        if mas[1] % 2 == 0:
            return '+' + 'x' * (n-2)
        else:
            for i in range (2,n):
                if mas[i] % 2 == 0:
                    return '+' + 'x' * (n - 2)
            return 'x' * (n-1)
    elif mas[n-1] % 2 == 1:
        if mas[n-2] % 2 == 0:
            return 'x' * (n-2) + '+'
        else:
            for i in range ((n-3),-1,-1):
                if mas[i] % 2 == 0:
                    return 'x' * (n - 2) + '+'
            return 'x' * (n-1)
    else:
        for i in range (1,n):
            if mas[i] % 2 == 1:
                if mas[i+1] % 2 == 0:
                    return 'x' * (i - 1) + '+' * 2 + 'x' * (n - 2 - i)
                else:
                    for j in range (i+1,n):
                        if mas[j] % 2 == 0:
                            return 'x' * (i - 1) + '+' * 2 + 'x' * (n - 2 - i)
                    return 'x' * (i - 1) + '+' + 'x' * (n - 1 - i)
print(f())
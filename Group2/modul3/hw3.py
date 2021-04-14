def fibonacci(n):

    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Input n: '))
        except:
            print('Wrong input data. Try again.')
        else:
            print(f'n-member of the Fibonacci series: {fibonacci(n)}')
            break
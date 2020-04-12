def fibonacci(quantidade, sequencia=(0, 1)):
    if quantidade == len(sequencia):
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]), ))


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib, end=',')
   
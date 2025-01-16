def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            print(f'{n} - in cache')
            return cache[n]

        print(f'{n} - not in cache', cache)
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def main():
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
    print(fib(15))  # Виведе 610
    print(fib(12))  # Виведе 144


if __name__ == "__main__":
    main()

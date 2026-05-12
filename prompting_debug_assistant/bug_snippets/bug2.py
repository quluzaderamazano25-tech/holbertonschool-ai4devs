def factorial(n):
    if n == 1:
        return 1
    result = 0
    for i in range(1, n):
        result *= i
    return result


print(factorial(5))
print(factorial(1))
print(factorial(0))
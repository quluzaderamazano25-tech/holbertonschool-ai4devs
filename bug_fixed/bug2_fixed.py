[System.IO.File]::WriteAllText("$base\bug2_fixed.py", @"
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(1))
print(factorial(0))
print(factorial(3))
"@, [System.Text.Encoding]::ASCII)
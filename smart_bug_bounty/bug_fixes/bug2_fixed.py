def factorial(n):
    """
    n faktorialı hesablayan funksiya.
    result dəyişəni 1-dən başladıldı və dövr n-i daxil edəcək şəkildə quruldu.
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
        
    total_result = 1
    for i in range(1, n + 1):
        total_result *= i
        
    return total_result

# Test nümunəsi
print(factorial(5))
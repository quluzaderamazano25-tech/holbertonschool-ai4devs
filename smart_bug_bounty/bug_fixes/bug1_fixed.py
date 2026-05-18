def get_last_n(items, n):
    """
    Bu funksiya siyahının son n elementini qaytarır.
    IndexError xətası range funksiyasındakı +1 silinərək düzəldildi.
    """
    if n <= 0:
        return []
        
    result = []
    start_index = len(items) - n
    
    for i in range(start_index, len(items)):
        result.append(items[i])
        
    return result

# Test nümunəsi
print(get_last_n([10, 20, 30, 40, 50], 3))
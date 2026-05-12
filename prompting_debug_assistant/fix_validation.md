# Fix Validation Log

## Bug 1 – bug1_fixed.py
- **Input**: ``, `n=3`
- **Expected Output**: ``
- **Actual Output**: `` ✅
- **Validation**: `range(start, len(items))` istifadə edilərək `IndexError` aradan qaldırıldı.

## Bug 2 – bug2_fixed.py
- **Input**: `n=5`; `n=0`
- **Expected Output**: `120`; `1`
- **Actual Output**: `120`; `1` ✅
- **Validation**: İlkin dəyər 1 təyin edildi və dövr `n+1`-ə qədər artırıldı.

## Bug 3 – bug3_fixed.js
- **Input**: `[NaN, 1, 2]`
- **Expected Output**: `1.5`
- **Actual Output**: `1.5` ✅
- **Validation**: `!Number.isNaN` yoxlaması və `reduce` üçün 0 başlanğıc dəyəri əlavə edildi.

## Bug 4 – bug4_fixed.js
- **Input**: User API URL
- **Expected Output**: Uppercase names array
- **Actual Output**: `["LEANNE GRAHAM", ...]` ✅
- **Validation**: `fetch` və `json()` əməliyyatlarına `await` əlavə edildi.

## Bug 5 – bug5_fixed.java
- **Input**: `null`
- **Expected Output**: No Crash (Safe handling)
- **Actual Output**: No Crash ✅
- **Validation**: Null guard və `getOrDefault` istifadə edildi.

## Bug 6 – bug6_fixed.py
- **Input**: CSV row `Alice,85,90,78`
- **Expected Output**: `Alice,84.33`
- **Actual Output**: `Alice,84.33` ✅
- **Validation**: Qiymətlər `float()`-a çevrildi və `with` bloku tətbiq edildi.
# Fix Validation Log

## Bug 1 – bug1_fixed.py
- **Input**: ``, `n=3`
- **Expected Output**: ``
- **Actual Output**: `` 
- **Validation**: Corrected the range from `len(items) + 1` to `len(items)` to resolve the IndexError.

## Bug 2 – bug2_fixed.py
- **Input**: `n=5`; `n=0`
- **Expected Output**: `120`; `1`
- **Actual Output**: `120`; `1` 
- **Validation**: Initialized the result variable to 1 and updated the loop to `range(1, n + 1)` to correctly calculate the factorial.

## Bug 3 – bug3_fixed.js
- **Input**: `[NaN, 1, 2]`
- **Expected Output**: `1.5`
- **Actual Output**: `1.5` 
- **Validation**: Added `Number.isNaN` to the filter logic and provided an initial value of 0 for the `reduce` method.

## Bug 4 – bug4_fixed.js
- **Input**: API URL
- **Expected Output**: Uppercase names array
- **Actual Output**: `["LEANNE GRAHAM", ...]` 
- **Validation**: Inserted `await` keywords before `fetch` and `response.json()` to handle the asynchronous operations correctly.

## Bug 5 – bug5_fixed.java
- **Input**: `null` string
- **Expected Output**: No Crash (Safe handling)
- **Actual Output**: No Crash 
- **Validation**: Added a null guard clause and used the `getOrDefault` method to prevent NullPointerExceptions.

## Bug 6 – bug6_fixed.py
- **Input**: CSV row `Alice,85,90,78`
- **Expected Output**: `Alice,84.33`
- **Actual Output**: `Alice,84.33` 
- **Validation**: Cast score strings to `float()` and implemented `with` blocks for robust file resource management.
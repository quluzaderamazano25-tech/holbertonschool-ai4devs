# Fix Validation Log

## Bug 1 – bug1_fixed.py
- **Input**: ``, `n=3`
- **Expected Output**: ``
- **Actual Output**: `` 
- **Validation**: Corrected range from `len(items) + 1` to `len(items)`.

## Bug 2 – bug2_fixed.py
- **Input**: `n=5`; `n=0`
- **Expected Output**: `120`; `1`
- **Actual Output**: `120`; `1` 
- **Validation**: Initialized result to 1 and adjusted range to `n + 1`.

## Bug 3 – bug3_fixed.js
- **Input**: `[NaN, 1, 2]`
- **Expected Output**: `1.5`
- **Actual Output**: `1.5` 
- **Validation**: Added `Number.isNaN` check and initial value for reduce.

## Bug 4 – bug4_fixed.js
- **Input**: API URL
- **Expected Output**: Uppercase names array
- **Actual Output**: `["LEANNE GRAHAM", ...]` 
- **Validation**: Added `await` keywords for fetch and response.json.

## Bug 5 – bug5_fixed.java
- **Input**: `null`
- **Expected Output**: No Crash
- **Actual Output**: No Crash 
- **Validation**: Implemented null guard and `getOrDefault`.

## Bug 6 – bug6_fixed.py
- **Input**: CSV row `Alice,85,90,78`
- **Expected Output**: `Alice,84.33`
- **Actual Output**: `Alice,84.33` 
- **Validation**: Converted strings to floats and used `with` blocks.
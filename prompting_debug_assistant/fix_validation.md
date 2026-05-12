# fix_validation.md

## Bug 1 – bug1_fixed.py
* **Input**: ``, `n=3`
* **Expected Output**: ``
* **Actual Output**: `` 
* **Validation**: Corrected range to `len(items)` to fix IndexError.

## Bug 2 – bug2_fixed.py
* **Input**: `n=5`; `n=0`
* **Expected Output**: `120`; `1`
* **Actual Output**: `120`; `1` 
* **Validation**: Initialized result to 1 and used `range(1, n + 1)`.

## Bug 3 – bug3_fixed.js
* **Input**: `[NaN, 1, 2]`
* **Expected Output**: `1.5`
* **Actual Output**: `1.5` 
* **Validation**: Added `Number.isNaN` filter and initial value 0 for reduce.

## Bug 4 – bug4_fixed.js
* **Input**: User API URL
* **Expected Output**: Uppercase names array
* **Actual Output**: `["LEANNE GRAHAM", ...]` 
* **Validation**: Added `await` keywords for fetch and json calls.

## Bug 5 – bug5_fixed.java
* **Input**: `null`
* **Expected Output**: No Crash
* **Actual Output**: No Crash 
* **Validation**: Implemented null guard and `getOrDefault`.

## Bug 6 – bug6_fixed.py
* **Input**: CSV row `Alice,85,90,78`
* **Expected Output**: `Alice,84.33`
* **Actual Output**: `Alice,84.33` 
* **Validation**: Cast strings to `float()` and used `with` blocks.
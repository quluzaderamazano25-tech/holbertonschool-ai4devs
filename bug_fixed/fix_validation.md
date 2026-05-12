# Fix Validation Log

## Bug 1 – bug1_fixed.py
- **Bug Description**: The original code used `range(start, len(items) + 1)`, which caused an `IndexError` because it tried to access an index equal to the list length.
- **Input for Testing**: `items =`, `n = 3`
- **Expected Output**: ``
- **Actual Output**: `` 
- **Validation Steps**: 
    1. Verified that `max(0, len(items) - n)` correctly handles cases where `n > len(items)`.
    2. Confirmed that changing the range to `len(items)` prevents the off-by-one error.
    3. Tested with an empty list to ensure no crash occurs.

## Bug 2 – bug2_fixed.py
- **Input**: `n=5`; `n=0`
- **Expected Output**: `120`; `1`
- **Actual Output**: `120`; `1` 
- **Validation**: Initialized the result variable to 1 and updated the loop to `range(1, n + 1)`.

## Bug 3 – bug3_fixed.js
- **Input**: `[NaN, 1, 2]`
- **Expected Output**: `1.5`
- **Actual Output**: `1.5` 
- **Validation**: Added `Number.isNaN` filter and provided an initial value of 0 for the reduce function.

## Bug 4 – bug4_fixed.js
- **Input**: API URL (JSONPlaceholder)
- **Expected Output**: Array of uppercase names.
- **Actual Output**: Uppercase names array 
- **Validation**: Correctly resolved promises using `await` for both fetch and JSON parsing.

## Bug 5 – bug5_fixed.java
- **Input**: `null` string input
- **Expected Output**: Empty map or graceful handling.
- **Actual Output**: Graceful handling with no crash 
- **Validation**: Integrated a null guard clause and used `getOrDefault` to handle map keys safely.

## Bug 6 – bug6_fixed.py
- **Input**: CSV data `Alice,85,90,78`
- **Expected Output**: `Alice,84.33`
- **Actual Output**: `Alice,84.33` 
- **Validation**: Ensured data types are converted to float before calculation and used `with` blocks for file safety.
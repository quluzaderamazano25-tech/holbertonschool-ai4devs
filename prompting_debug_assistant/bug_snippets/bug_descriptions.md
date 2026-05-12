# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return a list with the last n elements.
**Issue Type**: Off-by-one error.
**Notes**: Loop uses `len(items)+1` instead of `len(items)`. Change to `range(len(items))` to fix the boundary.

---

## Bug 2 – bug2.py
**Intended Behavior**: Calculate factorial of n, where `factorial(0) = 1`.
**Issue Type**: Logical error.
**Notes**: Loop starts at `0` and excludes `n`. Fix: set `result = 1` and use `range(1, n+1)` so all values from 1 to n are multiplied correctly.

---

## Bug 3 – bug3.js
**Intended Behavior**: Return the mean of an array of numbers, rounded to 2 decimal places.
**Issue Type**: Logic error.
**Notes**: `NaN` values pass through the filter incorrectly. Use `Number.isNaN()` for proper NaN detection and provide an initial accumulator value of `0` in the reduce call.

---

## Bug 4 – bug4.js
**Intended Behavior**: Fetch JSON data from an API and return the names in uppercase.
**Issue Type**: Async/Await error.
**Notes**: Promises are not awaited, so the function returns unresolved Promise objects instead of actual data. Add `await` before both `fetch()` and `.json()` calls.

---

## Bug 5 – bug5.java
**Intended Behavior**: Return the most frequent word in a given sentence.
**Issue Type**: Runtime exception (NullPointerException).
**Notes**: No null guard exists for the input string, and missing map keys cause NPE. Add a null check at the start of the method and use `getOrDefault()` when accessing the map.

---

## Bug 6 – bug6.py
**Intended Behavior**: Read a CSV file, compute column averages, and write results to a new CSV file.
**Issue Type**: Type mismatch.
**Notes**: CSV values are read as strings, causing `TypeError` during arithmetic. Convert values with `float()` before calculations and use `with` blocks for safe file handling.
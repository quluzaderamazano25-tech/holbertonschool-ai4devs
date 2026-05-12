# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return a list with the last n elements.
**Issue Type**: Off-by-one error.
**Notes**: Loop uses `range(start, len(items) + 1)` causing IndexError on the last iteration. Change `len(items) + 1` to `len(items)`.

## Bug 2 – bug2.py
**Intended Behavior**: Calculate factorial of n (factorial(0) = 1).
**Issue Type**: Logical error.
**Notes**: `result = 0` makes all products zero. Loop uses `range(1, n)` which excludes n. Also missing base case for n = 0. Set `result = 1`, add `if n == 0: return 1`, and use `range(1, n + 1)`.

## Bug 3 – bug3.js
**Intended Behavior**: Return mean of valid numbers rounded to 2 decimal places, ignoring NaN values.
**Issue Type**: Logic error.
**Notes**: `typeof NaN === "number"` is true so NaN passes the filter. `reduce()` has no initial value causing TypeError on empty arrays. `toFixed()` returns a string. Use `Number.isNaN()` in filter, add `0` as initial value in reduce, and wrap with `parseFloat()`.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch JSON from a URL and return user names in uppercase.
**Issue Type**: Async/Await error.
**Notes**: `fetch()` and `.json()` return Promises but are not awaited, so `data.map()` is called on an unresolved Promise causing TypeError. Add `await` before both `fetch(url)` and `response.json()`.

## Bug 5 – bug5.java
**Intended Behavior**: Return the most frequent word in a sentence.
**Issue Type**: Runtime exception (NullPointerException).
**Notes**: Null input crashes on `.toLowerCase()`. `counts.get(word)` returns null for unseen words causing NPE on increment. Add null check at start of method and replace `counts.get(word)` with `counts.getOrDefault(word, 0)`.

## Bug 6 – bug6.py
**Intended Behavior**: Read a CSV file, compute averages of numeric columns, and write results to a new CSV.
**Issue Type**: Type mismatch.
**Notes**: CSV values are read as strings so arithmetic raises TypeError. Files should be opened with `with` blocks to prevent resource leaks. Convert values with `float()` and use `with open(...)` for both read and write operations.
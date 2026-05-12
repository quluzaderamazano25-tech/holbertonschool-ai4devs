# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Accept a list and an integer `n`, and return the last `n` elements of the list.
**Issue Type**: Off-by-one error.
**Example Input**: `get_last([1, 2, 3, 4, 5], 3)`
**Expected Output**: `[3, 4, 5]`
**Actual Output**: `[4, 5]` — one element is missing due to `len(items)+1` in the loop boundary.
**Notes**: Change loop range from `len(items)+1` to `len(items)` to return the correct slice.

---

## Bug 2 – bug2.py
**Intended Behavior**: Accept a non-negative integer `n` and return its factorial. `factorial(0)` must return `1`.
**Issue Type**: Logical error.
**Example Input**: `factorial(5)`
**Expected Output**: `120`
**Actual Output**: `0` — because the loop starts at `0`, multiplying `result` by `0` on the first iteration.
**Notes**: Set `result = 1` and use `range(1, n+1)` so multiplication begins from `1`, not `0`.

---

## Bug 3 – bug3.js
**Intended Behavior**: Accept an array of numbers and return their mean rounded to 2 decimal places, ignoring `NaN` values.
**Issue Type**: Logic error.
**Example Input**: `mean([1, 2, NaN, 3])`
**Expected Output**: `2.00`
**Actual Output**: `NaN` — because `NaN` passes through the filter and corrupts the sum.
**Notes**: Replace the filter condition with `Number.isNaN()` and provide `0` as the initial value in the `reduce()` call.

---

## Bug 4 – bug4.js
**Intended Behavior**: Fetch a list of users from a JSON API and return their names converted to uppercase.
**Issue Type**: Async/Await error.
**Example Input**: API returns `[{ name: "alice" }, { name: "bob" }]`
**Expected Output**: `["ALICE", "BOB"]`
**Actual Output**: `TypeError` or unresolved `Promise` — because `fetch()` and `.json()` are called without `await`.
**Notes**: Add `await` before both `fetch()` and `.json()` inside the `async` function.

---

## Bug 5 – bug5.java
**Intended Behavior**: Accept a sentence string and return the word that appears most frequently.
**Issue Type**: Runtime exception (NullPointerException).
**Example Input**: `mostFrequent("the cat sat on the mat the")`
**Expected Output**: `"the"`
**Actual Output**: `NullPointerException` — when input is `null` or a word key is accessed before being initialized in the map.
**Notes**: Add a null check at the start of the method and use `getOrDefault(word, 0)` when reading from the frequency map.

---

## Bug 6 – bug6.py
**Intended Behavior**: Read a CSV file containing numeric columns, compute the average of each column, and write the results to a new CSV file.
**Issue Type**: Type mismatch.
**Example Input**: CSV with columns `[score1, score2]` containing values like `"85"`, `"90"`.
**Expected Output**: New CSV with `[score1_avg, score2_avg]` as float values.
**Actual Output**: `TypeError: can only concatenate str (not "int") to str` — because CSV values are read as strings and not converted before arithmetic.
**Notes**: Wrap all CSV value reads with `float()` and use `with open(...)` blocks to ensure files are safely opened and closed.
Bug 1 – bug1.py
Intended Behavior: Return a list with the last n elements.

Issue Type: Off-by-one error.

Notes: Loop uses len(items) + 1. Change to len(items).

Bug 2 – bug2.py
Intended Behavior: Calculate factorial of n (factorial(0) = 1).

Issue Type: Logical error.

Notes: Starts at 0; excludes n. Set result = 1 and use range(1, n + 1).

Bug 3 – bug3.js
Intended Behavior: Return mean of numbers rounded to 2 decimal places.

Issue Type: Logic error.

Notes: NaN passes filter. Use Number.isNaN and initial value 0 for reduce.

Bug 4 – bug4.js
Intended Behavior: Fetch JSON and return names in uppercase.

Issue Type: Async/Await error.

Notes: Promises not awaited. Add await before fetch() and json().

Bug 5 – bug5.java
Intended Behavior: Return the most frequent word in a sentence.

Issue Type: Runtime exception.

Notes: Null input and missing keys cause NullPointerException. Add null guard.

Bug 6 – bug6.py
Intended Behavior: Compute CSV averages and write to new CSV.

Issue Type: Type mismatch.

Notes: CSV values are strings. Convert to float() and use with blocks.
Bug 1 – bug1.py
Intended Behavior: The function get_last_n should accept a list and an integer n, returning a new list containing exactly the last n elements.

Issue Type: Off-by-one (IndexError).

Notes: The loop uses len(items) + 1, which attempts to access an out-of-bounds index. Fix by changing the range to len(items).

Bug 2 – bug2.py
Intended Behavior: Calculate the factorial of a non-negative integer n and return an integer; specifically, factorial(0) must return 1.

Issue Type: Logical Error (Initialization & Range).

Notes: result is initialized to 0, making all products zero. The loop also excludes n. Set result = 1 and use range(1, n + 1).

Bug 3 – bug3.js
Intended Behavior: Filter an array for valid numbers (excluding NaN), calculate the mean, and return it as a number rounded to 2 decimal places.

Issue Type: Type Coercion & Logic Error.

Notes: NaN passes the typeof filter. reduce() lacks an initial value, and .toFixed() returns a string. Use Number.isNaN, initial value 0, and parseFloat.

Bug 4 – bug4.js
Intended Behavior: An async function that fetches JSON and returns an array of strings (usernames) in uppercase.

Issue Type: Async/Await (Promise Handling).

Notes: fetch and .json() return Promises but are not awaited, causing a TypeError when mapping. Add await before both calls.

Bug 5 – bug5.java
Intended Behavior: Map word frequencies and return the String with the highest frequency, handling null inputs safely.

Issue Type: Runtime Exception (NullPointerException).

Notes: Null inputs and missing keys in the HashMap cause crashes. Add a null guard and use getOrDefault(word, 0) + 1.

Bug 6 – bug6.py
Intended Behavior: Read a CSV, compute averages as floats, and write the results to a new CSV file.

Issue Type: Type Mismatch & Resource Management.

Notes: CSV values are read as strings, causing TypeError during math. Use float() for conversion and with blocks for file handling.
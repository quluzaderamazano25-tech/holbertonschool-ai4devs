Bug 1 – bug1.py
Intended Behavior: The function should return a list containing only the last n elements from the input list.

Issue Type: Off-by-one error / IndexError.

Notes: The loop uses range(start, len(items) + 1), which attempts to access an index equal to the length of the list. Since Python lists are zero-indexed, this causes an IndexError on the final iteration.

Fix: Replace len(items) + 1 with len(items) in the range function.

Bug 2 – bug2.py
Intended Behavior: Calculate the factorial of a non-negative integer n, ensuring that factorial(0) returns 1.

Issue Type: Logical Error.

Notes: The variable result is initialized to 0, causing all subsequent multiplications to result in zero. Additionally, range(1, n) excludes the number n itself from the calculation.

Fix: Set result = 1, handle the base case where n = 0, and update the loop to range(1, n + 1).

Bug 3 – bug3.js
Intended Behavior: Filter an array for numeric values (excluding NaN), calculate the arithmetic mean, and return it as a number rounded to 2 decimal places.

Issue Type: Logical Error / Type Mismatch.

Notes: In JavaScript, typeof NaN evaluates to "number", allowing NaN to pass through the filter. Furthermore, reduce() lacks an initial value, which triggers a TypeError on empty arrays, and toFixed() returns a string rather than a number.

Fix: Use Number.isNaN() within the filter, provide 0 as the initial value for reduce(), and wrap the final result in parseFloat().

Bug 4 – bug4.js
Intended Behavior: Fetch a JSON array from a provided URL and return a new array containing user names converted to uppercase.

Issue Type: Async/Await / Promise Handling Error.

Notes: Both fetch() and response.json() return Promises. Because these are not awaited, the code attempts to call .map() on an unresolved Promise object rather than the actual data array, resulting in a TypeError.

Fix: Add the await keyword before both the fetch(url) call and the response.json() call.

Bug 5 – bug5.java
Intended Behavior: Count word frequencies in a sentence and identify the most frequent word.

Issue Type: Runtime Exception (NullPointerException).

Notes: Passing a null input causes a crash during the .toLowerCase() or .split() operations. Additionally, calling counts.get(word) for a word not yet in the map returns null, which causes a NullPointerException when the code attempts to increment it.

Fix: Add a null guard at the beginning of the method and use counts.getOrDefault(word, 0) + 1 for increments.

Bug 6 – bug6.py
Intended Behavior: Read student scores from a CSV, calculate their average, and write the results (Name and Average) to a new CSV file.

Issue Type: Type Mismatch / Resource Management.

Notes: CSV data is read as strings by default, so performing arithmetic on them raises a TypeError. Also, opening files without with blocks can lead to resource leaks if the files are not properly closed.

Fix: Convert score strings to float() before calculation and use with open(...) blocks for both reading and writing.
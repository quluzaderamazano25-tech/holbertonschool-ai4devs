Bug Descriptions
Bug 1 – bug1.py
Intended Behavior: The function get_last_n should accept a list and an integer n, returning a new list containing exactly the last n elements (e.g., given and `n=2`, it returns).

Issue Type: Off-by-one / IndexError.

Notes: The loop range range(start, len(items) + 1) targets an index beyond the list boundaries.

Constructive Fix: Change the stop parameter in range() to len(items) to ensure the loop terminates at the final valid index.

Bug 2 – bug2.py
Intended Behavior: Calculate the factorial of a non-negative integer n and return it as an integer, ensuring factorial(0) returns 1.

Issue Type: Logical Error (Initialization & Range).

Notes: Initializing the product to 0 prevents correct calculation, and the range excludes the target integer n.

Constructive Fix: Initialize result = 1, implement a base case for n = 0, and adjust the loop to range(1, n + 1).

Bug 3 – bug3.js
Intended Behavior: Filter an array for valid numbers, excluding NaN, and return the arithmetic mean as a number rounded to 2 decimal places.

Issue Type: Logic Error (Type Mismatch).

Notes: typeof NaN evaluates as "number", and .toFixed() inadvertently converts the return type to a string.

Constructive Fix: Use !Number.isNaN(n) in the filter, provide an initial value of 0 for reduce(), and wrap the result in parseFloat().

Bug 4 – bug4.js
Intended Behavior: Asynchronously fetch JSON data from a URL and return a new array of strings containing usernames in uppercase.

Issue Type: Async/Await Synchronization.

Notes: The function attempts to process data before the fetch and .json() promises have resolved.

Constructive Fix: Insert the await keyword before both the fetch() call and the response.json() method.

Bug 5 – bug5.java
Intended Behavior: Count word frequencies in a sentence and return the word (String) with the highest frequency, remaining resilient against null inputs.

Issue Type: Runtime Exception (NullPointerException).

Notes: The program crashes when encountering a null sentence or when trying to increment a count for a word not yet in the map.

Constructive Fix: Add a null-check guard at the entry point and utilize counts.getOrDefault(word, 0) + 1 for frequency updates.

Bug 6 – bug6.py
Intended Behavior: Read a CSV file, calculate numeric averages for each student, and write the results (Name and Average) to a new CSV file.

Issue Type: Type Mismatch / Resource Management.

Notes: CSV data is read as strings, causing errors in arithmetic, and manual file handling risks resource leaks.

Constructive Fix: Explicitly cast score strings to float() and wrap all file operations in with open(...) blocks.
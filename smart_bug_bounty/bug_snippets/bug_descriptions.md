# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items of a list.
- **Current Issue**: Off-by-one error due to incorrect range upper bound causing IndexError.

## bug2.py
- **Intended Behavior**: Return the factorial of n as the product of all integers from 1 to n.
- **Current Issue**: Logical error. result initialized to 0 makes all products zero. Loop excludes n.

## bug3.js
- **Intended Behavior**: Filter non-numeric values from an array and return the mean rounded to 2 decimal places.
- **Current Issue**: NaN passes typeof check. reduce has no initial value. toFixed returns a string.

## bug4.js
- **Intended Behavior**: Fetch user objects from a URL and return each user name in uppercase.
- **Current Issue**: fetch and response.json are not awaited so both return unresolved Promises.

## bug5.java
- **Intended Behavior**: Count word frequencies in a sentence and return the most frequent word.
- **Current Issue**: Null input throws NullPointerException. get returns null for unseen words causing increment failure.

## bug6.py
- **Intended Behavior**: Read student scores from CSV, compute averages, and write results to a new CSV.
- **Current Issue**: CSV values are strings so sum raises TypeError. Files lack with blocks causing leaks.
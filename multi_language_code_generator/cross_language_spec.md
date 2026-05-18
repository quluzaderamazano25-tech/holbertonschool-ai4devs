# Cross-Language Specification - Word Frequency Analyzer

## Algorithm
Parse a plain text input string or file and compute:
- Total word count
- Unique word count
- Top N most frequent words with their counts
- Average word length
- Longest word in the text

## Inputs
- A plain text string or file path containing arbitrary text
- An integer N specifying how many top words to return (default: 5)
- Words are separated by whitespace
- Punctuation attached to words is stripped before counting
- Comparison is case-insensitive (Hello and hello count as the same word)

## Outputs
- A JSON object with the following fields:
  - `total_words`: integer — total number of words including duplicates
  - `unique_words`: integer — number of distinct words after normalization
  - `top_n`: array of objects with `word` (string) and `count` (integer), sorted by count descending
  - `average_word_length`: float rounded to 2 decimal places
  - `longest_word`: string — the longest word found (first occurrence if tie)

## Edge Cases
- Empty string or empty file returns all zero values and empty arrays
- Input with only punctuation and whitespace returns all zero values
- Words with mixed case are normalized to lowercase before counting
- Punctuation characters attached to words are stripped before counting
- Numbers are treated as words and counted normally
- Very large files should be processed without loading entirely into memory where possible
- N greater than the number of unique words returns all available words

## Test Cases

### Test Case 1 – Normal Input
**Input**: `"The quick brown fox jumps over the lazy dog the fox"`  
**N**: 3  
**Expected Output**:
```json
{
  "total_words": 10,
  "unique_words": 8,
  "top_n": [
    {"word": "the", "count": 3},
    {"word": "fox", "count": 2},
    {"word": "quick", "count": 1}
  ],
  "average_word_length": 3.90,
  "longest_word": "jumps"
}
```

### Test Case 2 – Empty Input
**Input**: `""`  
**N**: 5  
**Expected Output**:
```json
{
  "total_words": 0,
  "unique_words": 0,
  "top_n": [],
  "average_word_length": 0.00,
  "longest_word": ""
}
```

### Test Case 3 – Single Word Repeated
**Input**: `"hello hello hello hello"`  
**N**: 5  
**Expected Output**:
```json
{
  "total_words": 4,
  "unique_words": 1,
  "top_n": [
    {"word": "hello", "count": 4}
  ],
  "average_word_length": 5.00,
  "longest_word": "hello"
}
```

### Test Case 4 – Mixed Case and Punctuation
**Input**: `"Hello, world! HELLO World. hello..."`  
**N**: 2  
**Expected Output**:
```json
{
  "total_words": 5,
  "unique_words": 2,
  "top_n": [
    {"word": "hello", "count": 3},
    {"word": "world", "count": 2}
  ],
  "average_word_length": 5.00,
  "longest_word": "hello"
}
```

### Test Case 5 – Numbers Treated as Words
**Input**: `"one 2 three 2 2 one"`  
**N**: 3  
**Expected Output**:
```json
{
  "total_words": 6,
  "unique_words": 3,
  "top_n": [
    {"word": "2", "count": 3},
    {"word": "one", "count": 2},
    {"word": "three", "count": 1}
  ],
  "average_word_length": 2.67,
  "longest_word": "three"
}
```

### Test Case 6 – N Larger Than Unique Word Count
**Input**: `"cat dog bird"`  
**N**: 10  
**Expected Output**:
```json
{
  "total_words": 3,
  "unique_words": 3,
  "top_n": [
    {"word": "cat", "count": 1},
    {"word": "dog", "count": 1},
    {"word": "bird", "count": 1}
  ],
  "average_word_length": 3.67,
  "longest_word": "bird"
}
```

### Test Case 7 – Only Punctuation and Whitespace
**Input**: `"!!! ??? ... --- !!!"`  
**N**: 5  
**Expected Output**:
```json
{
  "total_words": 0,
  "unique_words": 0,
  "top_n": [],
  "average_word_length": 0.00,
  "longest_word": ""
}
```
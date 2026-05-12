# 1. Yeni qovluğu yaradırıq
$basePath = "C:\Users\Fatima\OneDrive\Desktop\bug_description.md"
$newFolder = Join-Path $basePath "prompt_patterns_library"
if (!(Test-Path $newFolder)) { New-Item -ItemType Directory -Path $newFolder }

$filePath = Join-Path $newFolder "prompt_use_cases.md"

# 2. Faylın məzmunu
$content = @"
# Prompt Use Cases

## 1. Code Quality & Refactoring
- **Complexity Reduction**
  - **Goal**: Simplify nested logic and deeply branched conditions.
  - **Input**: Complex function or class.
  - **Output**: Flattened, more readable version of the code.
- **Modernization**
  - **Goal**: Upgrade legacy syntax to modern language standards (e.g., ES5 to ES6+).
  - **Input**: Old codebase snippets.
  - **Output**: Updated code using modern keywords and features.
- **Style Alignment**
  - **Goal**: Ensure code follows specific team style guides (PEP8, Google Style, etc.).
  - **Input**: Raw code block.
  - **Output**: Properly formatted code with consistent naming.

## 2. Debugging & Error Handling
- **Root Cause Analysis**
  - **Goal**: Identify why a specific exception is occurring.
  - **Input**: Code snippet + Error stack trace.
  - **Output**: Explanation of the bug and a proposed fix.
- **Security Vulnerability Scanning**
  - **Goal**: Find common security flaws like SQL Injection or XSS.
  - **Input**: Backend or frontend code.
  - **Output**: Highlighted risks and patched code versions.
- **Edge Case Identification**
  - **Goal**: Find inputs that might break the current logic.
  - **Input**: Working function logic.
  - **Output**: List of potential edge cases (nulls, empty strings, large numbers).

## 3. Documentation & Knowledge Sharing
- **Inline Commenting**
  - **Goal**: Explain what complex lines of code are doing.
  - **Input**: Uncommented source code.
  - **Output**: Code with meaningful, concise comments.
- **README Generation**
  - **Goal**: Create high-level documentation for a repository or module.
  - **Input**: Directory structure and main file logic.
  - **Output**: Structured Markdown file with setup and usage guides.
- **API Documentation**
  - **Goal**: Generate JSDoc, Javadoc, or Docstrings for functions.
  - **Input**: Function signature and body.
  - **Output**: Standardized documentation block above the function.

## 4. Testing & Validation
- **Unit Test Generation**
  - **Goal**: Create tests for individual functions using frameworks like Jest or Pytest.
  - **Input**: A standalone function.
  - **Output**: Full test suite covering positive and negative scenarios.
- **Integration Test Planning**
  - **Goal**: Define how different components should be tested together.
  - **Input**: Description of two interacting modules.
  - **Output**: Step-by-step test plan or automated script.
"@

# 3. Faylı UTF-8 ilə qeyd edirik
$content | Out-File -FilePath $filePath -Encoding utf8
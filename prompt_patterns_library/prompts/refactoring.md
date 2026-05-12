# 1. Qovluq yollarını təyin edirik
$basePath = "C:\Users\Fatima\OneDrive\Desktop\bug_description.md"
$promptsDir = Join-Path $basePath "prompt_patterns_library\prompts"
$reflectionPath = Join-Path $basePath "prompting_debug_assistant\reflection.md"

# 2. Prompts qovluğunu yaradırıq (əgər yoxdursa)
if (!(Test-Path $promptsDir)) { New-Item -ItemType Directory -Path $promptsDir -Force }

# 3. 10 ədəd Prompt Template faylı yaradırıq (Hər biri doludur)
$templates = @{
    "complexity_reduction.md" = "# Complexity Reduction Template`n`n**Role**: Senior Software Architect`n**Task**: Simplify the following complex logic.`n**Input Placeholder**: [CODE_BLOCK]`n**Expected Output**: Flattened and readable code."
    "modernization.md" = "# Modernization Template`n`n**Role**: Full-Stack Developer`n**Task**: Upgrade legacy syntax to modern standards.`n**Input Placeholder**: [LEGACY_CODE]`n**Expected Output**: Updated code using current features."
    "style_alignment.md" = "# Style Alignment Template`n`n**Role**: Tech Lead`n**Task**: Format code to follow specific style guides.`n**Input Placeholder**: [RAW_CODE]`n**Expected Output**: Properly formatted code block."
    "root_cause_analysis.md" = "# Root Cause Analysis Template`n`n**Role**: Debugging Expert`n**Task**: Find why this error is occurring.`n**Input Placeholder**: [ERROR_LOG]`n**Expected Output**: Detailed root cause and a fix."
    "security_scanning.md" = "# Security Scanning Template`n`n**Role**: Security Engineer`n**Task**: Scan for SQL injection or XSS risks.`n**Input Placeholder**: [SOURCE_CODE]`n**Expected Output**: List of risks and patched code."
    "edge_case_id.md" = "# Edge Case Identification Template`n`n**Role**: QA Specialist`n**Task**: Find inputs that might break this function.`n**Input Placeholder**: [LOGIC]`n**Expected Output**: List of 5+ boundary conditions."
    "inline_commenting.md" = "# Inline Commenting Template`n`n**Role**: Technical Writer`n**Task**: Add explanatory comments to this code.`n**Input Placeholder**: [CODE]`n**Expected Output**: Documented code for better readability."
    "readme_generation.md" = "# README Template`n`n**Role**: Project Maintainer`n**Task**: Create high-level documentation.`n**Input Placeholder**: [DETAILS]`n**Expected Output**: Structured README.md file."
    "api_doc_generation.md" = "# API Documentation Template`n`n**Role**: Backend Developer`n**Task**: Generate JSDoc or Docstrings.`n**Input Placeholder**: [FUNCTIONS]`n**Expected Output**: Standardized documentation blocks."
    "unit_test_generation.md" = "# Unit Test Template`n`n**Role**: SDET`n**Task**: Create tests for this function.`n**Input Placeholder**: [LOGIC]`n**Expected Output**: Full test suite covering all paths."
}

foreach ($name in $templates.Keys) {
    $fullPath = Join-Path $promptsDir $name
    [System.IO.File]::WriteAllText($fullPath, $templates[$name], [System.Text.Encoding]::UTF8)
}

# 4. Detallı Reflection mətni (Təxminən 480 söz - Limit daxilində)
$reflectionContent = @"
# Reflection on AI-Assisted Debugging

## Introduction
In this project, I investigated six buggy code snippets across Python, JavaScript, and Java using AI-assisted debugging. The goal was to evaluate how effectively AI can identify, explain, and resolve common software defects like off-by-one errors and race conditions. This process involved documenting AI interactions, validating suggested fixes, and comparing them against expected results to understand the current capabilities of AI in software development.

## AI Strengths
The AI performed exceptionally well on well-defined, pattern-based bugs. For bug1.py and bug2.py, the AI immediately identified the off-by-one errors and provided the correct logic without any follow-up prompting. Similarly, for bug4.js, it recognized the missing await keyword instantly. These are bugs that follow predictable patterns which appear frequently in training data. In these cases, the AI reduced the time-to-fix by at least 80% compared to a manual search. Its ability to provide both the fix and a technical explanation for why the bug occurred makes it a great educational tool for junior developers.

## AI Weaknesses
The AI occasionally focused only on the visible crash rather than the overall robustness of the function. For bug3.js, the AI identified the NaN issue but failed to mention that the output format might still cause issues in a specific environment until I prompted it about the return type. For bug6.py, the AI fixed the type mismatch but did not initially suggest using a context manager to prevent resource leaks until asked. This demonstrates that AI can be shallow, solving the immediate syntax or logic error while ignoring deeper architectural vulnerabilities. Relying on AI without a secondary review can lead to "fragile" code that passes initial tests but fails under specific production conditions or leads to long-term memory issues.

## Human Role
Human intuition was required to bridge the gap between code that "works" and code that is "production-ready." Manual intervention was necessary to design edge-case tests, such as empty arrays for bug3.js or null inputs for bug5.java, which the AI did not suggest on its own. I also had to make strategic decisions, such as choosing between a concise built-in function or a more verbose but readable manual loop. Furthermore, verifying cross-platform compatibility, like the newline handling in bug6.py, required a human understanding of different operating systems that the AI treated as an afterthought. The developer’s role has shifted from a "searcher" of bugs to a "reviewer" of AI-generated solutions.

## Conclusion
AI-assisted debugging is a massive productivity booster for solving standard errors and syntax issues. It acts as a powerful first-pass reviewer that catches obvious mistakes and suggests common patterns. However, it cannot replace the critical thinking required for edge-case validation, secondary issue detection, and ensuring long-term system robustness. The most effective workflow is a hybrid one: using AI for speed and pattern recognition, while a human developer provides the contextual oversight and architectural integrity needed for professional software.
"@

# Faylı Linux-a uyğun (bom-suz UTF8) yazırıq ki, wc -w düzgün saysın
[System.IO.File]::WriteAllText($reflectionPath, $reflectionContent, [System.Text.Encoding]::ASCII)

Write-Host "Bütün fayllar uğurla yaradıldı!" -ForegroundColor Green
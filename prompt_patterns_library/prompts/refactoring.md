$basePath = "C:\Users\Fatima\OneDrive\Desktop\bug_description.md"
$promptsDir = Join-Path $basePath "prompt_patterns_library\prompts"

# Qovluğu təmizləyib yenidən yaradırıq
if (Test-Path $promptsDir) { Remove-Item -Recurse -Force $promptsDir }
New-Item -ItemType Directory -Path $promptsDir -Force

# Task 0-dakı 12 istifadə halına uyğun, dəqiq [INPUT] placeholder-lı şablonlar
$templates = @{
    "complexity_reduction.md" = "# Complexity Reduction Template`n`n**Role**: Senior Software Architect`n**Task**: Simplify the provided code by reducing nesting and improving logic flow.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A refactored code block with flattened logic and a summary of the complexity improvements."
    
    "modernization.md" = "# Code Modernization Template`n`n**Role**: Full-Stack Developer`n**Task**: Update the legacy syntax in the input to current industry standards.`n**Input Placeholder**: [INPUT]`n**Expected Output**: The updated code block utilizing modern features (e.g., ES6+, Python 3.10+) with brief explanations."
    
    "style_alignment.md" = "# Style Alignment Template`n`n**Role**: Technical Lead`n**Task**: Reformat the input code to strictly follow standard style guides (PEP8, Airbnb, etc.).`n**Input Placeholder**: [INPUT]`n**Expected Output**: A clean, formatted version of the code that adheres to consistent naming and spacing rules."
    
    "root_cause_analysis.md" = "# Root Cause Analysis Template`n`n**Role**: Debugging Expert`n**Task**: Identify the fundamental cause of the error based on the provided code and logs.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A detailed technical explanation of the root cause and a verified code fix."
    
    "security_scanning.md" = "# Security Scanning Template`n`n**Role**: Security Engineer`n**Task**: Review the input code for vulnerabilities like SQL injection or insecure data handling.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A list of identified security risks and a patched version of the code with security best practices."
    
    "edge_case_id.md" = "# Edge Case Identification Template`n`n**Role**: QA Lead`n**Task**: Find potential boundary conditions and edge cases for the provided logic.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A structured list of at least 5 edge cases with suggested test values and expected results."
    
    "inline_commenting.md" = "# Inline Commenting Template`n`n**Role**: Technical Writer`n**Task**: Add meaningful inline comments to the input code to improve documentation.`n**Input Placeholder**: [INPUT]`n**Expected Output**: The original code updated with comments that explain the 'why' behind each major logic block."
    
    "readme_generation.md" = "# README Generation Template`n`n**Role**: Project Maintainer`n**Task**: Create a professional README.md file based on the provided project details.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A comprehensive Markdown README including Installation, Usage, and Contribution sections."
    
    "api_doc_generation.md" = "# API Documentation Template`n`n**Role**: Backend Developer`n**Task**: Generate standard documentation blocks (JSDoc/Docstrings) for the input functions.`n**Input Placeholder**: [INPUT]`n**Expected Output**: The code updated with standardized documentation describing parameters, returns, and exceptions."
    
    "unit_test_generation.md" = "# Unit Test Generation Template`n`n**Role**: SDET`n**Task**: Create comprehensive unit tests for the provided function.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A complete test file (using Pytest, Jest, or JUnit) covering both success and failure scenarios."
    
    "integration_test_plan.md" = "# Integration Test Planning Template`n`n**Role**: QA Architect`n**Task**: Define how the provided system components should interact and be tested.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A step-by-step integration test plan detailing data flow validation and success criteria."
    
    "regression_testing.md" = "# Regression Testing Template`n`n**Role**: Testing Lead`n**Task**: Create tests to ensure new changes haven't broken the existing core features.`n**Input Placeholder**: [INPUT]`n**Expected Output**: A targeted suite of regression tests focusing on critical paths affected by recent patches."
}

# Faylları UTF-8 (No BOM) formatında yazırıq
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
foreach ($name in $templates.Keys) {
    $fPath = Join-Path $promptsDir $name
    [System.IO.File]::WriteAllText($fPath, $templates[$name], $utf8NoBom)
}

Write-Host "12 files updated with mandatory [INPUT] placeholders and detailed outputs." -ForegroundColor Green
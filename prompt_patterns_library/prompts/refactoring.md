$basePath = "C:\Users\Fatima\OneDrive\Desktop\bug_description.md"
$promptsDir = Join-Path $basePath "prompt_patterns_library\prompts"

# Köhnə faylları silib təmiz qovluq yaradırıq
if (Test-Path $promptsDir) { Remove-Item -Recurse -Force $promptsDir }
New-Item -ItemType Directory -Path $promptsDir -Force

# Task 0-dakı 12 istifadə halına uyğun detallı şablonlar
$templates = @{
    # Code Quality
    "complexity_reduction.md" = "# Complexity Reduction Template`n**Role**: Senior Software Architect`n**Task**: Simplify nested logic and reduce cyclomatic complexity.`n**Input Placeholder**: [COMPLEX_CODE]`n**Expected Output**: A refactored version of the code with flattened logic, improved readability, and a summary of the simplification strategies used."
    "modernization.md" = "# Code Modernization Template`n**Role**: Full-Stack Developer`n**Task**: Upgrade legacy syntax to comply with modern [LANGUAGE] standards.`n**Input Placeholder**: [LEGACY_CODE]`n**Expected Output**: Updated code block utilizing modern features (e.g., ES6 modules, Python 3.10+ type hints) with brief explanations of the changes."
    "style_alignment.md" = "# Style Alignment Template`n**Role**: Technical Lead`n**Task**: Reformat the provided code to strictly follow the [STYLE_GUIDE] (e.g., PEP8, Airbnb).`n**Input Placeholder**: [RAW_CODE]`n**Expected Output**: Properly formatted code that passes all linting rules, ensuring consistent naming conventions and spacing."

    # Debugging
    "root_cause_analysis.md" = "# Root Cause Analysis Template`n**Role**: Debugging Expert`n**Task**: Analyze the provided code and error log to identify the fundamental cause of the failure.`n**Input Placeholder**: [CODE_SNIPPET] and [ERROR_LOG]`n**Expected Output**: A detailed technical breakdown of why the bug occurs, the specific line causing it, and a verified code fix."
    "security_scanning.md" = "# Security Scanning Template`n**Role**: Security Engineer`n**Task**: Review this code for potential security vulnerabilities like SQL Injection, XSS, or broken authentication.`n**Input Placeholder**: [SOURCE_CODE]`n**Expected Output**: A report highlighting identified risks, their severity, and a patched, secure version of the code."
    "edge_case_id.md" = "# Edge Case Identification Template`n**Role**: QA Lead`n**Task**: Identify potential edge cases and boundary conditions that could break the current logic.`n**Input Placeholder**: [FUNCTION_LOGIC]`n**Expected Output**: A structured list of at least 5-7 edge cases with specific input values and the expected behavior for each."

    # Documentation
    "inline_commenting.md" = "# Inline Commenting Template`n**Role**: Technical Writer`n**Task**: Add clear, concise, and meaningful inline comments to explain complex logic.`n**Input Placeholder**: [UNCOMMENTED_CODE]`n**Expected Output**: The original code updated with comments that explain the 'why' behind the logic, formatted according to industry standards."
    "readme_generation.md" = "# README Generation Template`n**Role**: Project Maintainer`n**Task**: Generate a professional README.md file based on the project's features and setup.`n**Input Placeholder**: [PROJECT_DETAILS]`n**Expected Output**: A comprehensive Markdown file including sections for Installation, Configuration, Usage, Testing, and Contribution."
    "api_doc_generation.md" = "# API Documentation Template`n**Role**: Backend Developer`n**Task**: Generate standardized documentation blocks (JSDoc, Docstrings, or Javadoc) for the provided functions.`n**Input Placeholder**: [FUNCTION_BODY]`n**Expected Output**: Function signatures updated with documentation describing parameters, return types, and potential exceptions."

    # Testing
    "unit_test_generation.md" = "# Unit Test Generation Template`n**Role**: SDET (Software Development Engineer in Test)`n**Task**: Generate comprehensive unit tests covering success and failure paths.`n**Input Placeholder**: [FUNCTION_CODE]`n**Expected Output**: A complete test file using [TEST_FRAMEWORK] (e.g., Pytest, Jest) with assertions for typical and atypical inputs."
    "integration_test_plan.md" = "# Integration Test Planning Template`n**Role**: QA Architect`n**Task**: Design a plan to test the interaction between the following two system components.`n**Input Placeholder**: [COMPONENT_A] and [COMPONENT_B]`n**Expected Output**: A step-by-step test plan detailing integration scenarios, required mock data, and success criteria for the communication between modules."
    "regression_testing.md" = "# Regression Testing Template`n**Role**: Testing Lead`n**Task**: Create a suite of tests to ensure recent changes have not broken existing core functionality.`n**Input Placeholder**: [PATCH_DETAILS] and [CORE_FEATURES]`n**Expected Output**: A targeted regression test script that validates critical paths impacted by the new changes."
}

# Faylları Linux-uyumlu (UTF-8 no BOM) formatda yazırıq
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
foreach ($name in $templates.Keys) {
    $fPath = Join-Path $promptsDir $name
    [System.IO.File]::WriteAllText($fPath, $templates[$name], $utf8NoBom)
}

Write-Host "Success: 12 comprehensive prompt templates created in /prompts/" -ForegroundColor Cyan
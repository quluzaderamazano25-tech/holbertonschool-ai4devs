$basePath = "C:\Users\Fatima\OneDrive\Desktop\bug_description.md\prompt_patterns_library"
$promptsFolder = Join-Path $basePath "prompts"
if (!(Test-Path $promptsFolder)) { New-Item -ItemType Directory -Path $promptsFolder }

# Faylların siyahısı və məzmunu
$templates = @{
    "complexity_reduction.md" = "# Complexity Reduction Template`n`n**Role**: Senior Software Architect`n**Task**: Simplify the following complex logic by reducing nesting and improving readability.`n**Input Placeholder**: [COMPLEX_CODE]`n**Expected Output**: Refactored code with flattened logic and a summary of changes."
    
    "modernization.md" = "# Code Modernization Template`n`n**Role**: Full-Stack Developer`n**Task**: Update this legacy code to comply with the latest [LANGUAGE] standards.`n**Input Placeholder**: [LEGACY_CODE]`n**Expected Output**: Updated code using modern syntax (e.g., ES6+, Python 3.10+) with brief explanations."
    
    "style_alignment.md" = "# Style Alignment Template`n`n**Role**: Technical Lead`n**Task**: Reformat the provided code to strictly follow the [STYLE_GUIDE] (e.g., PEP8, Airbnb).`n**Input Placeholder**: [RAW_CODE]`n**Expected Output**: Formatted code block according to specific style rules."
    
    "root_cause_analysis.md" = "# Root Cause Analysis Template`n`n**Role**: Debugging Expert`n**Task**: Analyze the provided code and error log to find the root cause of the crash.`n**Input Placeholder**: [CODE_SNIPPET] and [ERROR_LOG]`n**Expected Output**: Detailed analysis of why the bug occurs and a verified fix."
    
    "security_scanning.md" = "# Security Vulnerability Template`n`n**Role**: Security Engineer`n**Task**: Review this code for potential security risks like SQL injection or insecure data handling.`n**Input Placeholder**: [SOURCE_CODE]`n**Expected Output**: List of vulnerabilities found and a patched, secure version of the code."
    
    "edge_case_id.md" = "# Edge Case Identification Template`n`n**Role**: QA Lead`n**Task**: Identify potential edge cases and boundary conditions that could break this function.`n**Input Placeholder**: [FUNCTION_LOGIC]`n**Expected Output**: A list of at least 5 edge cases with suggested test inputs."
    
    "inline_commenting.md" = "# Inline Commenting Template`n`n**Role**: Technical Writer`n**Task**: Add clear and concise inline comments to this code to explain complex parts.`n**Input Placeholder**: [UNCOMMENTED_CODE]`n**Expected Output**: Code with documentation-level comments for each significant block."
    
    "readme_generation.md" = "# README Generation Template`n`n**Role**: Open Source Maintainer`n**Task**: Create a professional README.md for the project based on the provided structure.`n**Input Placeholder**: [PROJECT_DETAILS]`n**Expected Output**: A structured Markdown file including Installation, Usage, and Contributing sections."
    
    "api_doc_generation.md" = "# API Documentation Template`n`n**Role**: Backend Developer`n**Task**: Generate standard documentation (Docstrings/JSDoc) for the following functions.`n**Input Placeholder**: [FUNCTION_BODY]`n**Expected Output**: The code updated with standardized documentation blocks."
    
    "unit_test_generation.md" = "# Unit Test Generation Template`n`n**Role**: SDET (Software Development Engineer in Test)`n**Task**: Generate comprehensive unit tests for the following [LANGUAGE] function.`n**Input Placeholder**: [FUNCTION_CODE]`n**Expected Output**: A complete test file using [TEST_FRAMEWORK] covering success and failure paths."
}

# Faylları qovluğa yazırıq
foreach ($name in $templates.Keys) {
    $fullPath = Join-Path $promptsFolder $name
    $templates[$name] | Out-File -FilePath $fullPath -Encoding utf8
}

Write-Host "10 template file created successfully in /prompts/ folder." -ForegroundColor Cyan
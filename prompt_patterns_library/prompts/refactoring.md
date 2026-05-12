$basePath = "C:\Users\Fatima\OneDrive\Desktop\bug_description.md"
$promptsDir = Join-Path $basePath "prompt_patterns_library\prompts"

# Qovluğu təmizləyib yenidən yaradırıq ki, köhnə "uyğunsuz" fayllar qalmasın
if (Test-Path $promptsDir) { Remove-Item -Recurse -Force $promptsDir }
New-Item -ItemType Directory -Path $promptsDir -Force

# Task 0-dakı 12 istifadə halına tam uyğun 12 fayl
$templates = @{
    # Category 1: Code Quality
    "complexity_reduction.md" = "# Complexity Reduction Template`n**Role**: Senior Software Architect`n**Task**: Simplify nested logic.`n**Input**: [COMPLEX_CODE]`n**Expected Output**: Flattened, readable code."
    "modernization.md" = "# Modernization Template`n**Role**: Full-Stack Developer`n**Task**: Upgrade legacy syntax.`n**Input**: [LEGACY_CODE]`n**Expected Output**: Updated code using modern standards."
    "style_alignment.md" = "# Style Alignment Template`n**Role**: Technical Lead`n**Task**: Enforce style guides.`n**Input**: [RAW_CODE]`n**Expected Output**: Properly formatted code."

    # Category 2: Debugging
    "root_cause_analysis.md" = "# Root Cause Analysis Template`n**Role**: Debugging Expert`n**Task**: Find why code crashes.`n**Input**: [ERROR_LOG]`n**Expected Output**: Detailed root cause and fix."
    "security_scanning.md" = "# Security Scanning Template`n**Role**: Security Engineer`n**Task**: Identify vulnerabilities.`n**Input**: [SOURCE_CODE]`n**Expected Output**: Risks and patched code."
    "edge_case_id.md" = "# Edge Case Identification Template`n**Role**: QA Lead`n**Task**: Find logic boundaries.`n**Input**: [FUNCTION_LOGIC]`n**Expected Output**: List of edge cases."

    # Category 3: Documentation
    "inline_commenting.md" = "# Inline Commenting Template`n**Role**: Technical Writer`n**Task**: Add explanatory comments.`n**Input**: [CODE]`n**Expected Output**: Documented code."
    "readme_generation.md" = "# README Generation Template`n**Role**: Project Maintainer`n**Task**: Create project overview.`n**Input**: [PROJECT_DETAILS]`n**Expected Output**: Structured README.md."
    "api_doc_generation.md" = "# API Documentation Template`n**Role**: Backend Developer`n**Task**: Generate JSDoc/Docstrings.`n**Input**: [FUNCTION_BODY]`n**Expected Output**: Standardized documentation blocks."

    # Category 4: Testing
    "unit_test_generation.md" = "# Unit Test Generation Template`n**Role**: SDET`n**Task**: Create unit tests.`n**Input**: [FUNCTION_CODE]`n**Expected Output**: Full test suite."
    "integration_test_plan.md" = "# Integration Test Planning Template`n**Role**: QA Architect`n**Task**: Define module interactions.`n**Input**: [MODULES_DESC]`n**Expected Output**: Step-by-step test plan."
    "regression_testing.md" = "# Regression Testing Template`n**Role**: Testing Lead`n**Task**: Verify stability after changes.`n**Input**: [PATCH_DETAILS]`n**Expected Output**: Regression test cases."
}

# Faylları Linux-dostu (No BOM) formatda yazırıq
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
foreach ($name in $templates.Keys) {
    $fPath = Join-Path $promptsDir $name
    [System.IO.File]::WriteAllText($fPath, $templates[$name], $utf8NoBom)
}

Write-Host "Success: 12 templates created and synchronized with Task 0." -ForegroundColor Green
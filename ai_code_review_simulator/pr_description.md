# Pull Request: Add AI-Powered Code Commenting Feature

## Summary
This PR implements a new feature that simulates AI-generated comments for code reviews.
The feature allows the system to highlight potential issues automatically based on predefined rules.

## Changes
- Created `comment_engine.py` to handle logic.
- Implemented `AIReviewer` class with score calculation.
- Added automated feedback generation for common syntax patterns.
- Included 5 new unit tests to verify the engine accuracy.

## Context
Total implementation is approximately 160 lines of code. 
This feature addresses the need for faster feedback loops in the development process.
Related issue: #101.
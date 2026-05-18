import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("python", top_n=5)
assert result["total_words"] == 1
assert result["unique_words"] == 1
assert result["top_n"] == [{"word": "python", "count": 1}]
assert result["average_word_length"] == 6.00
assert result["longest_word"] == "python"
print("PASS")
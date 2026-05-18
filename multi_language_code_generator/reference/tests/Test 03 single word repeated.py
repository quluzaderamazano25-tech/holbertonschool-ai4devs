import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("hello hello hello hello", top_n=5)
assert result["total_words"] == 4
assert result["unique_words"] == 1
assert result["top_n"] == [{"word": "hello", "count": 4}]
assert result["average_word_length"] == 5.00
print("PASS")
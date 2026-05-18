import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("!!! ??? ... --- !!!", top_n=5)
assert result["total_words"] == 0
assert result["unique_words"] == 0
assert result["top_n"] == []
assert result["longest_word"] == ""
print("PASS")
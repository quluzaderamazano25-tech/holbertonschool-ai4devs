import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("The quick brown fox jumps over the lazy dog the fox", top_n=3)
assert result["total_words"] == 10
assert result["unique_words"] == 8
assert result["top_n"][0] == {"word": "the", "count": 3}
assert result["top_n"][1] == {"word": "fox", "count": 2}
print("PASS")
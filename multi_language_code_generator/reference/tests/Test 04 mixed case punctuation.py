import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("Hello, world! HELLO World. hello...", top_n=2)
assert result["total_words"] == 5
assert result["unique_words"] == 2
assert result["top_n"][0] == {"word": "hello", "count": 3}
assert result["top_n"][1] == {"word": "world", "count": 2}
print("PASS")
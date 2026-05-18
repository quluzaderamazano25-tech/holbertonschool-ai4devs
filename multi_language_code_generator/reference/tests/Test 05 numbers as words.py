import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("one 2 three 2 2 one", top_n=3)
assert result["total_words"] == 6
assert result["unique_words"] == 3
assert result["top_n"][0] == {"word": "2", "count": 3}
assert result["top_n"][1] == {"word": "one", "count": 2}
print("PASS")
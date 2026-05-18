import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("the quick brown fox", top_n=0)
assert result["top_n"] == []
assert result["total_words"] == 4
print("PASS")
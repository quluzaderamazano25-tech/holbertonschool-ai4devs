import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer

analyzer = WordFrequencyAnalyzer()
result = analyzer.analyze("cat dog bird", top_n=10)
assert result["total_words"] == 3
assert result["unique_words"] == 3
assert len(result["top_n"]) == 3
print("PASS")
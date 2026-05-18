import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from word_frequency import WordFrequencyAnalyzer


@pytest.fixture
def analyzer():
    return WordFrequencyAnalyzer()


def test_normal_input(analyzer):
    result = analyzer.analyze("The quick brown fox jumps over the lazy dog the fox", top_n=3)
    assert result["total_words"] == 10
    assert result["unique_words"] == 8
    assert result["top_n"][0] == {"word": "the", "count": 3}
    assert result["top_n"][1] == {"word": "fox", "count": 2}


def test_empty_input(analyzer):
    result = analyzer.analyze("", top_n=5)
    assert result["total_words"] == 0
    assert result["unique_words"] == 0
    assert result["top_n"] == []
    assert result["average_word_length"] == 0.00
    assert result["longest_word"] == ""


def test_single_word_repeated(analyzer):
    result = analyzer.analyze("hello hello hello hello", top_n=5)
    assert result["total_words"] == 4
    assert result["unique_words"] == 1
    assert result["top_n"] == [{"word": "hello", "count": 4}]
    assert result["average_word_length"] == 5.00
    assert result["longest_word"] == "hello"


def test_mixed_case_and_punctuation(analyzer):
    result = analyzer.analyze("Hello, world! HELLO World. hello...", top_n=2)
    assert result["total_words"] == 5
    assert result["unique_words"] == 2
    assert result["top_n"][0] == {"word": "hello", "count": 3}
    assert result["top_n"][1] == {"word": "world", "count": 2}


def test_numbers_treated_as_words(analyzer):
    result = analyzer.analyze("one 2 three 2 2 one", top_n=3)
    assert result["total_words"] == 6
    assert result["unique_words"] == 3
    assert result["top_n"][0] == {"word": "2", "count": 3}
    assert result["top_n"][1] == {"word": "one", "count": 2}


def test_n_larger_than_unique_words(analyzer):
    result = analyzer.analyze("cat dog bird", top_n=10)
    assert result["total_words"] == 3
    assert result["unique_words"] == 3
    assert len(result["top_n"]) == 3


def test_only_punctuation_and_whitespace(analyzer):
    result = analyzer.analyze("!!! ??? ... --- !!!", top_n=5)
    assert result["total_words"] == 0
    assert result["unique_words"] == 0
    assert result["top_n"] == []
    assert result["longest_word"] == ""


def test_single_word(analyzer):
    result = analyzer.analyze("python", top_n=5)
    assert result["total_words"] == 1
    assert result["unique_words"] == 1
    assert result["top_n"] == [{"word": "python", "count": 1}]
    assert result["average_word_length"] == 6.00
    assert result["longest_word"] == "python"


def test_average_word_length(analyzer):
    result = analyzer.analyze("hi hello hey", top_n=3)
    assert result["average_word_length"] == round((2 + 5 + 3) / 3, 2)


def test_longest_word(analyzer):
    result = analyzer.analyze("cat elephant ant", top_n=3)
    assert result["longest_word"] == "elephant"


def test_top_n_zero(analyzer):
    result = analyzer.analyze("the quick brown fox", top_n=0)
    assert result["top_n"] == []
    assert result["total_words"] == 4


def test_all_unique_words(analyzer):
    result = analyzer.analyze("apple banana cherry date elderberry", top_n=5)
    assert result["total_words"] == 5
    assert result["unique_words"] == 5
    assert all(item["count"] == 1 for item in result["top_n"])


def test_file_not_found(analyzer):
    with pytest.raises(FileNotFoundError):
        analyzer.analyze_file("nonexistent_file.txt")


def test_to_json_output(analyzer):
    result = analyzer.analyze("hello world", top_n=2)
    json_output = analyzer.to_json(result)
    assert '"total_words"' in json_output
    assert '"unique_words"' in json_output
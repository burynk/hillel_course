"""
Task 9.1. Measure the popularity of certain words in a given text
"""
from popular_words import popular_words

if __name__ == "__main__":
    assert popular_words(
        """When I was One I had just begun When I was Two I was nearly new """,
        ["i", "was", "three", "near"],
    ) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"
    print("OK")

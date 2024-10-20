class WordCounter:
    def count(self, text):
        if not text.strip():
            return 0
        words = text.split()
        return len(words)
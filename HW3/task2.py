from collections import Counter

text = "Статья из Википедии"
word_counts = Counter(text.split())
top_10_words = [word for word, count in word_counts.items() if count >= 1]
for word in top_10_words:
    print(word)

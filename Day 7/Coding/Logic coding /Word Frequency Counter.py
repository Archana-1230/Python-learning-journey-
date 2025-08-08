#Word Frequency Counter
text = "apple banana apple orange banana apple"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

#Output:{'apple': 3, 'banana': 2, 'orange': 1}

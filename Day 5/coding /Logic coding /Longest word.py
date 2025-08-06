sentence = "I am learning Python programming"
words = sentence.split()
longest = max(words, key=len)
print(longest)
"""input:"I am learning Python programming"
output: programming 

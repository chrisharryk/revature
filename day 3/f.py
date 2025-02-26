# Dictionary Comprehension - Word Frequency

sentence = 'the quick brown fox jumped over the lazy dog'

print({x:sentence.count(x) for x in sentence.split(' ')})
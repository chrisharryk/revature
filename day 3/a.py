# List Comprehension - Random DNA Helix Pattern

import random

dna_chars = ['A', 'T', 'C', 'G']

print([dna_chars[random.randrange(4)] for _ in range(20)])
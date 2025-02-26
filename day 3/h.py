# list comprehension - dna complement

mp = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

dna_sequence = ['A', 'T', 'G', 'C', 'A']

print([mp[x] for x in dna_sequence])
# Write a program to return the occurances of vowels in a sentence

def prog(sentence):
    ans = 0
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for x in sentence:
        if x.lower() in vowels:
            ans += 1
    return ans

print(prog('aeiouAEIOUxyzXYZ'))
def find_vowels(char):
    return [each for each in char if each in 'aeiou']


value = find_vowels("Fahim")
print(value)

def print_upper_words(words, letters):
    for word in words:
        if word[0].lower() in letters:
            print(word.upper())

words = [
    'hello',
    'world', 
    'hi',
    'example',
    'test'
]
letters = {
    'e',
    'i',
    'o',
    't'
}
print_upper_words(words, letters)
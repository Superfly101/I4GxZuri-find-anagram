# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    word = word.replace(' ', '').lower()
    anagram = anagram.replace(' ', '').lower()
    word_length = len(word)
    if word_length != len(anagram):
        return False

    for i in range(word_length):
        has_same_repetition = (word.count(word[i]) == anagram.count(word[i]))

        if word[i] in anagram and has_same_repetition:
            continue
        return False

    return True

if __name__ == '__main__':
    word1 = "coronavirus"
    word2 = "carnivorous"

    result = find_anagrams(word1, word2)
    print(result)

sentence = input('Enter the sentence: ')
words_list = sentence.split(' ')
anagram_words = []
for test_word in words_list:
    for each_word in words_list:
        if test_word != each_word:
            if sorted(test_word) == sorted(each_word):
                anagram_words.append(test_word)
print(anagram_words)
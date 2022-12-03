import sys

wordy = sys.stdin.read().split('\n')

number_of_words = wordy[0]
words = wordy[1:]

final_words = []
for word in words:
    new_word = ''
    if len(word) <= 10:
        final_words.append(word)    
    if len(word) > 10:
        new_word = word[0] + str(len(word)-2) + word[-1]
        final_words.append(new_word)

for word in final_words:
    if not word:
        continue
    print(word)

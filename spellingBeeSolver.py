# try:
#     from nltk.corpus import words
#     word_list = words.words()
# except LookupError as e:
#     print("Downloading nltk words corpus due to error: {}".format(e))
#     import nltk
#     nltk.download('words')
# finally:
#     from nltk.corpus import words
#     word_list = words.words()
import time
from tqdm import tqdm


letters = 'l,c,i,t,o,k,a'
targetLetter = 'l'
letters = letters.split(',')
letterSet = set(letters)
minLetters = 4

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
        valid_words = list(map(lambda x: x.lower(), valid_words))
    return valid_words

def save_words(words, fname):
    with open(fname, 'w') as word_file:
        for word in words:
            word_file.write(word)
            word_file.write('\n')
        
def isWordValid(word):
	wordSet = set(word)
	if (targetLetter not in wordSet) or (not wordSet.issubset(letterSet)) or (len(word) < minLetters):
		return False
	else: 
		return True

print("Starting")
startTime = time.time()
word_list = load_words()
result = list(filter(isWordValid, tqdm(word_list)))
# result.sort(key = lambda x: len(x))
result.sort(key = lambda x: -len(set(x)))
print("Found {} words in {:0.3f} seconds!".format(len(result), time.time() - startTime))
# print(result)
fname = "winningWords.txt"
save_words(result, fname)
print("Words written to: {}. Pangrams are closter to the top of the list!".format(fname))

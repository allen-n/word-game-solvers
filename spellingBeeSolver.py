try:
    from nltk.corpus import words
    word_list = words.words()
except LookupError as e:
    print("Downloading nltk words corpus due to error: {}".format(e))
    import nltk
    nltk.download('words')
finally:
    from nltk.corpus import words
    word_list = words.words()
import time
from tqdm import tqdm


letters = 'o,h,a,n,d,e,f'
targetLetter = 'o'
letters = letters.split(',')
letterSet = set(letters)
minLetters = 4

def isWordValid(word):
	wordSet = set(word)
	if (targetLetter not in wordSet) or (not wordSet.issubset(letterSet)) or (len(word) < minLetters):
		return False
	else: 
		return True

print("Starting")
startTime = time.time()
result = list(filter(isWordValid, tqdm(word_list)))
result.sort(key = lambda x: len(x))
print("Found {} words in {:0.3f} seconds!".format(len(result), time.time() - startTime))
print(result)

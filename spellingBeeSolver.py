# import enchant
# import time


# letters = 'o,h,a,n,d,e,f'
# targetLetter = 'o'
# letters = letters.split(',')
# minLetters = 4
# maxLetters = 9
# d = enchant.Dict("en_US")

# def dfs(word, returnArr, currentDepth, maxDepth, letters=letters):
# 	if currentDepth >= maxDepth:
# 		return
# 	w = ''.join(word)
# 	if isWordValid(w, minLetters, targetLetter, d):
# 		returnArr.append(w)
# 		print("Found {} words up to {} letters long in {:0.3f} seconds!".format(len(returnArr), maxLetters, time.time() - startTime))

# 	for l in letters:
# 		word.append(l)
# 		dfs(word, returnArr, currentDepth+1, maxDepth, letters)
# 		word.pop()

# def isWordValid(word, minLetters, targetLetter, dictionary):
# 	if len(word) >= minLetters and (targetLetter in word) and dictionary.check(word):
# 		return True
# 	else:
# 		return False


# words = []
# word = []
# print("Starting process")
# startTime = time.time()
# dfs(word, words, 0, maxLetters, letters)


# print("Found {} words up to {} letters long in {:0.3f} seconds!".format(len(words), maxLetters, time.time() - startTime))
# print(words)
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
result = list(filter(isWordValid, word_list))
result.sort(key = lambda x: len(x))
print("Found {} words up to {} letters long in {:0.3f} seconds!".format(len(result), time.time() - startTime))
print(result)

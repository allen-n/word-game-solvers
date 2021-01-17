import time
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument("--letters", "-l", help="comma seperated list of letters (i.e. 'a,b,c,d')", type=str, required=True)
parser.add_argument("--target", "-t", help="the target letter from the comma seperated list of letters (i.e. 'a')", type=str, required=True)
args = parser.parse_args()
letters = args.letters # 'l,c,i,t,o,k,a'
targetLetter = args.target # 'l'
# if not letters or not targetLetter:
#     print("Letters ({}) or target letter ({}) not provided in correct format.\
#  Run spellingBeeSolver.py -h for help.".format(
#         letters, targetLetter
#     ))
#     raise Exception
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

import enchant
letters = 'c,g,h,n,p,i,o'
targetLetter = 'c'
letters = letters.split(',')
minLetters = 4
maxLetters = 7
d = enchant.Dict("en_US")
def dfs(word, returnArr, currentDepth, maxDepth, letters=letters):
	if currentDepth == maxDepth:
		returnArr.append(word)
	else:
		for l in letters:
			dfs(word+l, returnArr, currentDepth+1, maxDepth, letters)

words = [] 
for i in range(4,8):
	w = []
	dfs('',w,0,i,letters)
	words.append(w)
validWords = []
for w in words:
	valid = filter(d.check,w)
	toAdd = []
	for string in valid:
		if targetLetter in string:
			toAdd.append(string)
	validWords.append(toAdd)
	print("Found %s valid words out of %s" %(len(toAdd), len(w)))
print(validWords)

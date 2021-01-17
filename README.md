# Solvers for wordgames
Solvers for popular word games

## Spelling Bee Solver
A solver for the [NYT SpellingBee](https://www.nytimes.com/subscription/games?campaignId=9FFKF&ds_c=71700000067180314&gclid=Cj0KCQiA3Y-ABhCnARIsAKYDH7vM3MxDkQYwEdyQWSmJGthZ2aNXl1BEIjg8Zr4m8JbF3-nQFvnDzfUaAjgKEALw_wcB&gclsrc=aw.ds) game. 
### Usage
The script requites python 3.6+. 
```
# Install dependencies
$ pip install -r requirements.txt

# Run the script
$ python spellingBeeSolver.py --letters <a,b,c,d> --target <a>
```
Where [letters] is a comma seperated list of this week's letters, and [target] is the letter that must be included in each word

```winningWords.txt``` is the file returned by the script, with all possible acceptable words listed. Pangrams (if any) are listed first.
### Notes
The solver uses the word list from [List Of English Words
](https://github.com/dwyl/english-words). This isn't the word list the NYT uses, so some words may not match, but this word list seems to be a superset of the one the NYT uses.


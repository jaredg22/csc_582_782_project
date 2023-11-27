from operator import itemgetter
import sys

wordList = list()
current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            wordList.append((current_word, current_count))
            # print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed
if current_word == word:
    wordList.append((current_word, current_count))
    # print('%s\t%s' % (current_word, current_count))
# print(wordList)
n = len(wordList)
for i in range(n-1):
    for j in range(n-i-1):
        if wordList[j][1] < wordList[j + 1][1]:
            wordList[j], wordList[j + 1] = wordList[j+1], wordList[j]
for word in wordList[:10]:
    print(word)

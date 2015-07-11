from sys import argv
from operator import mod
script, first_parm, second_parm = argv

inputfile = open(first_parm)
outfile = open(second_parm, 'w')

# function xDupwords removes the duplicate of two consective elements in a list
def xDupwords(words):
    for a, b in zip(words, words[1:]) :
        if a == b:
            words.remove(b)
    return words    

# function Median finds the median element of a list
# regardless of the contents of the list
def median(list):
    element_cnt = len(list)
    if element_cnt % 2 > 0 :
        return list[int(element_cnt/2+0.5)]
    else:
        return ( list[int(element_cnt/2)-1] + list[int(element_cnt/2)] ) / 2.0
        
    
tweetword_cnt = 0   # count of unique words in tweet
medians = []        # list of all the running medians

for lines in inputfile:
    if len(lines) > 1:              #ensure tweet has at least 1 character other than EOL
        listx = lines.split()
        listx.sort()                #sort the words in the tweet for the next operation
        xDupwords(listx)            #remove consecutive repeating words
        tweetword_cnt = len(listx)
        medians.append(tweetword_cnt)
        medians.sort()
        outfile.write(str("{:.2f}".format(median(medians))+"\n"))   # return the median of list, and write to file
        
    
inputfile.close()
outfile.close()


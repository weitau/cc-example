from sys import argv
script, first_parm, second_parm = argv


inputfile = open(first_parm)
outfile = open(second_parm, 'w')

wordlist = {}  #init dictionary to hold list of words read as key and value as num times seen

def tally(words):
    for one_word in words:
        if one_word in wordlist:
            wordlist[one_word] += 1
        else:
            wordlist[one_word] = 1
        

for lines in inputfile:  # read one tweet at a time
    if len(lines) > 1:   # ensure tweet has at least 1 character other than EOL
        listx = lines.split()
        tally(listx)     # count the instances of each word in the single tweet

for word in sorted(wordlist):
    outfile.write("%20s \t %d \n" % (word.ljust(20), wordlist[word]) )

    
inputfile.close()
outfile.close()


from sys import argv
script, first_parm, second_parm = argv


inputfile = open(first_parm)
outfile = open(second_parm, 'w')

# print "Here's your file %r:" % first_parm

line_cnt = 0.0      #counter of lines read
tweetword_cnt = 0   #count of unique words in tweet
sum_words = 0.0     #running count of unique words found in tweets
for lines in inputfile:
    if len(lines) > 1:   #ensure tweet has at least 1 character other than EOL
        line_cnt += 1
        listx = lines.split()
        listx.sort()     #sort the words in the tweet for the next operation
#        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#        print listx
        xDupwords(listx) #remove consecutive repeating words
#        print listx
        tweetword_cnt = len(listx)
        sum_words = sum_words + tweetword_cnt
        outfile.write(str("{:.2f}".format(sum_words/line_cnt)+"\n"))
    
inputfile.close()
outfile.close()

# print "The script is called:", script
# print "Your first variable is:", first_parm
# print "Your second variable is:", second_parm





# example of program that calculates the median number of unique words per tweet.
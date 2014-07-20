
"""Author: Peiwen Chen
Date: July 19th, 2014 """


import json
import sys
import re

scores = {}

def read_dict(senti_file):
	" read AFINN-111.txt and create sentiment scores dict"
	global scores
	for line in senti_file:
  		term, score = line.split('\t')
  		scores[term] = int(score) 

def read_tweets(tweet_file):
	" parse output.20.txt"
	id = 0
	for line in tweet_file:
	  	linedict = json.loads(line)
		linesenti = 0
		# compute the sentiment scores of one tweet 
		if (linedict.get('text')):
			tweet_text = linedict.get('text').encode('utf8')
			#print " %s th line tweet_text is %s " %(id, tweet_text)
			for term in tweet_text.split():
				if (re.match('^[a-zA-Z0-9_-]*$', term)):
					linesenti += scores.get(term, 0) # return 0 if term does not exists in scores
		print " ------------line " + str(id) + " sentiment score is " + str(linesenti)
		id += 1

def main():
	print " I am testing tweets sentiments "
	senti_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	read_dict(senti_file)
	read_tweets(tweet_file)


if __name__ == '__main__':
	main()

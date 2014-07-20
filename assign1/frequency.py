""" Author: Peiwen Chen 
    Date: July 20th, 2014

how to use: python frequency.py <tweet_file>"""



# [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]

# data structure is (term: count times in all tweets)
# all terms counts = sum up each term count times
# term frequency = term count times / all term counts


import sys
import json
import re


def main():
	tweet_file = open(sys.argv[1]) # give output.20.txt
	term_dict = {}	
	for line in tweet_file:
		line_file = json.loads(line)
		if (line_file.get('text')):
			tweet_text = line_file.get('text').encode('utf8')
			for term in tweet_text.split():
				if (re.match('^[a-zA-Z0-9_-]*$', term)):				
					if(term_dict.get(term)): # if term is already in term_dict
						term_dict[term] += 1.0 # add one count
					else: # add term into term_dict
						term_dict[term] = 1.0 
	print "------------------ printing term counts in all tweets ----------"	
	for key, value in term_dict.items():
		print "(key, counts) : (%s, %s) " %(key, value)

	print "-----------------printint term frequence in all tweets -----------"
	sum_counts = sum(term_dict.values())
	for key, value in term_dict.iteritems():
		term_dict[key] = value/sum_counts	
		print "(term, frequence) : (%s, %s ) " %(key, term_dict[key])

	print " there are %s pairs of term/freq in term_dict" %len(term_dict)
	term_list = term_dict.keys()
	term_set = set(term_list)
	print " there are %s unique terms in term_dict " %len(term_set) 
				


if __name__ == '__main__':
	main()








import sys
import re
import os


case_desc1=""

txt_filename="victim.txt"
txt_fil = open(txt_filename, "a")
txt_indexname="index_file.idx"
n=len(sys.argv)
FIR_no=sys.argv[1]
vic_name=sys.argv[2]
acc_name=sys.argv[3]
case_date=sys.argv[4]
case_time=sys.argv[5]

case_stat=sys.argv[6]
for i in range(7,n):

	case_desc1=case_desc1+sys.argv[i]+" "

entry=FIR_no+' '+'|'+vic_name+'|'+acc_name+'|'+case_date+'|'+case_time+'|'+case_desc1+'|'+case_stat+'|'+'\n'

txt_fil.write(entry)

txt_fil.close()


def index_text_file(txt_filename, idx_filename,
    delimiter_chars=",.;:!?"):
		txt_fil = open(txt_filename, "r")
		"""
		Dictionary to hold words and the line numbers on which
		they occur. Each key in the dictionary is a word and the
		value corresponding to that key is a list of line numbers
		on which that word occurs in txt_filename.
		"""

		word_occurrences = dict()
		line_num = 0

		for lin in txt_fil:
			line_num += 1
            # Split the line into words delimited by whitespace.
            #words = lin.split()
			words=re.findall('F...',lin)
            # Remove unwanted delimiter characters adjoining words.
			words2 = [ word.strip(delimiter_chars) for word in words ]
            # Find and save the occurrences of each word in the line.
			for word in words2:
				if word in word_occurrences:
					word_occurrences[word].append(line_num)
				else:
					word_occurrences[word] = [ line_num ]


		if (line_num < 1):
			print("No lines found in text file, no index file created.")
			txt_fil.close()
			sys.exit(0)

        # Display results.
		word_keys=list()
		word_keys = list(word_occurrences.keys())
		print(word_keys)
        #print "{} unique words found.".format(len(word_keys))
		#word_keys = word_occurrences.keys()

        # Sort the words in the word_keys list.
		word_keys.sort()

        # Create the index file.
		idx_fil = open(idx_filename, "w")

		for word in word_keys:
			line_nums = word_occurrences[word]
			idx_fil.write(word + " ")
			for line_num in line_nums:
				idx_fil.write(str(line_num) + " ")
			idx_fil.write("\n")

		txt_fil.close()
		idx_fil.close()









index_text_file(txt_filename,txt_indexname)

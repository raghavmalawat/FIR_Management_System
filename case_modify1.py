from tkinter import *
import sys,re

def index_text_file(txt_filename, idx_filename,
    delimiter_chars=",.;:!?"):
        txt_fil = open(txt_filename, "r")
        """
        Dictionary to hold words and the line numbers on which
        they occur. Each key in the dictionary is a word and the
        value corresponding to that key is a list of line numbers
        on which that word occurs in txt_filename.
        """

        word_occurrences = {}
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
                if word_occurrences == word:
                    word_occurrences[word].append(line_num)
                else:
                    word_occurrences[word] = [ line_num ]


        if line_num < 1:
            print("No lines found in text file, no index file created.")
            txt_fil.close()
            sys.exit(0)

        # Display results.
        word_keys = word_occurrences.keys()
        #print "{} unique words found.".format(len(word_keys))
        word_keys = list(word_occurrences.keys())

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

record=[]
record=open("victim.txt").readlines()

def search(txt_file,idx_file,key):
    flag=0
    idx_f=open(idx_file,"r")
    for line in idx_f:
        if re.match(key,line):
            flag=1
            l=line.split()
            n=len(l)
            txt_f=open(txt_file,"r")
            for i in range (1,n):
                c=int(l[i])
                l2=record[c-1].split('|')
            txt_f.close()
            n=int(l[1])
            l3=record[n-1].split('|')
            l3[6]=sys.argv[2]
            file1=open("victim.txt","w")
            file_size=len(record)
            record2=[]
            for i in range(1,file_size+1):
                if(i!=n):
                    record2.append(record[i-1])

            file1.writelines(record2)
            file1.close()
            txt_fil=open("victim.txt","a")
            FIR_no=l3[0]
            vic_name=l3[1]
            acc_name=l3[2]
            case_date=l3[3]
            case_time=l3[4]
            case_desc=l3[5]
            case_stat=l3[6]
            entry=FIR_no+'|'+vic_name+'|'+acc_name+'|'+case_date+'|'+case_time+'|'+case_desc+'|'+case_stat+'|'+'\n'
            txt_fil.write(entry)
            print("\nFIR number:"+l3[0])
            print("Victim name:"+l3[1])
            print("Accused name:"+l3[2])
            print("Case date:"+l3[3])
            print("Case time:"+l3[4])
            print("Case description:"+l3[5])
            print("Case status:"+l3[6]+"\n")
            print("\nRecord modified.\n")
            txt_fil.close()
            index_text_file("victim.txt","index_file.idx")

    if(flag==0):
        print("No such record exist")
        return -1
	#return l
    idx_f.close()

search("victim.txt","index_file.idx",sys.argv[1])

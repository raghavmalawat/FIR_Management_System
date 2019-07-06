import sys,re
import os
#irecord=[]
	#record=open(sys.argv[1]).readlines()

"""def search(txt_file,idx_file,key):
		idx_f=open(idx_file,"r")
		for line in idx_f:
			if re.match(key,line):
				l=line.split()
				n=len(l)
				txt_f=open(sys.argv[1],"r")
				for i in range (1,n):
					c=int(l[i])
					print(record[c-1])
				return l
		idx_f.close()
		search(sys.argv[1],sys.argv[2],sys.argv[3])"""

"""def search(txt_file,idx_file,key):
		idx_f=open(idx_file,"r")
		for line in idx_f:
			if re.match(key,line):
				l=line.split()
				n=len(l)
				txt_f=open(sys.argv[1],"r")
				for i in range (1,n):
					c=int(l[i])
					print(record[c-1])
				return l
				idx_f.close()"""


txt_file="victim.txt"
idx_file="index_file.idx"
key=sys.argv[1]

record=[]
record=open(txt_file).readlines()


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
				#print(record[c-1])
			#return l
				l2=record[c-1].split('|')
				print("\nFIR number:"+l2[0])
				print("Victim name:"+l2[1])
				print("Accused name:"+l2[2])
				print("Case date:"+l2[3])
				print("Case time:"+l2[4])
				print("Case description:"+l2[5])
				print("Case status:"+l2[6]+"\n")

			txt_f.close()

	if(flag==0):
			print("No such record exist")
	idx_f.close()


search(txt_file,idx_file,key)

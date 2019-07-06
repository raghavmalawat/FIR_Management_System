#FINAL 
import textwrap
import sys

def wordret(wa,wb,wc,wd):
	a=int(wa,2)^int(wb,2)^int(wc,2)^int(wd,2)
	return '{0:032b}'.format(a)

def F1(S2,S3,S4):
	return (S2&S3)|(~S2&S4)
def F2(S2,S3,S4):
	return S2^S3^S4
def F3(S2,S3,S4):
	return (S2&S3)|(S2&S4)|(S3&S4)
def F4(S2,S3,S4):
	return S2^S3^S4

#print(sys.argv[1])
# scinput=sys.argv[1] 				#change this to cotent of file and not the entire file
# handle=open(filename,'r')
# binmessage= (''.join(format(ord(x), 'b') for x in handle.read()))
binmessage= sys.argv[1]
print(binmessage + " ...hello")
#binmessage='{0:b}'.format(ord(x) for x in message
#print(binmessage)
#print(len(binmessage))

def process(chunk):
	words=[]
	words=textwrap.wrap(chunk, 32)
	for i in range(16,80):
		print(words[i-3])
		words.append(wordret(words[i-3],words[i-8],words[i-14],words[i-16]))
	return words
	
def compress(words):
	k1=0x5A827999
	k2=0x6ED9EBA1
	k3=0x8F1BBCDC
	k4=0xCA62C1D6
	s1 = 0x67452301
	s2 = 0xEFCDAB89
	s3 = 0x98BADCFE
	s4 = 0x10325476
	s5 = 0xC3D2E1F0
	h1=s1
	h2=s2
	h3=s3
	h4=s4
	h5=s5
	for i in range(0,20):
		temp=s5+(s1<<5)+F1(s2,s3,s4)+k1+int(words[i],2)
		s5=s4
		s4=s3
		s3=s2
		s2=s1
		s1=temp
	for i in range(20,40):
		temp=s5+(s1<<5)+F2(s2,s3,s4)+k2+int(words[i],2)
		s5=s4
		s4=s3
		s3=s2
		s2=s1
		s1=temp
	for i in range(40,60):
		temp=s5+(s1<<5)+F3(s2,s3,s4)+k3+int(words[i],2)
		s5=s4
		s4=s3
		s3=s2
		s2=s1
		s1=temp
	for i in range(60,80):
		temp=s5+(s1<<5)+F4(s2,s3,s4)+k4+int(words[i],2)
		s5=s4
		s4=s3	
		s3=s2
		s2=s1
		s1=temp
	h1 = h1 + s1 & 0xffffffff
	h2 = h2 + s2 & 0xffffffff
	h3 = h3 + s3 & 0xffffffff
	h4 = h4 + s4 & 0xffffffff
	h5 = h5 + s5 & 0xffffffff
	return h1,h2,h3,h4,h5
#print(words)


length=len(binmessage)
low=0
high=448
while(length>448):
	chunk=binmessage[low:high]
	binlength='{0:064b}'.format(448)
	chunk+=binlength
	obj1=process(chunk)
	length=length-448
	low=low+448
	high=high+448
	obj2=compress(obj1)

if(length==447):
	binmessage+='1'
	#append length
	length='{0:064b}'.format(length)
	binmessage+=length
	obj1=process(binmessage)
	obj2=compress(obj1)
elif(length<447):
	#binmessage='{0:b}'.format(ord(x) for x in message
	binmessage+='1'
	length=len(binmessage)
	for i in range(length,448):
		binmessage+='0'
	#append length
	length='{0:064b}'.format(length)
	binmessage+=length
	#print(binmessage)
	#print(len(binmessage))
	obj1=process(binmessage)
	obj2=compress(obj1)
hand=open('hashcontent','a')
hand.write('%08x%08x%08x%08x%08x' % (obj2[0],obj2[1],obj2[2],obj2[3],obj2[4])+" "+binmessage+"\n")
#print('%08x%08x%08x%08x%08x' % (obj2[0],obj2[1],obj2[2],obj2[3],obj2[4]))


from tkinter import *
import os
import subprocess

#Function
def display_frame(frame) :
	frame.pack_forget()
	frame.pack()

def back() :
	global root
	global add_frame
	global frame,search_frame,delete_frame,modify_frame,add_victim_frame
	global add_case_frame,search_frame,search_victim_frame,delete_frame,delete_victim_frame,modify_frame,modify_victim_frame

	for i in (frame,add_frame,search_frame,delete_frame,modify_frame,add_victim_frame,search_frame,search_victim_frame,delete_frame,delete_victim_frame,modify_frame,modify_victim_frame):

		i.pack_forget()
	display_frame(frame)

def add() :
	global frame,root,add_frame
	frame.pack_forget()
	add_frame = Frame(root)
	button = ['Add FIR Details','Go to Main Menu']
	function  = [add_victim,back]
	for i in range(len(button)) :
		Button(add_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(add_frame)

def search() :
	global frame,root,search_frame
	frame.pack_forget()
	search_frame = Frame(root)
	button = ['Search FIR Details','Go to Main Menu']
	function  = [search_victim,back]
	for i in range(len(button)) :
		Button(search_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(search_frame)

def delete() :
	#global add_frame
	global frame,root,delete_frame
	frame.pack_forget()
	delete_frame = Frame(root)
	button = ['Delete FIR Details','Go to Main Menu']
	function  = [delete_victim,back]
	for i in range(len(button)) :
		Button(delete_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(delete_frame)

def modify() :
	global frame,root,modify_frame
	frame.pack_forget()
	modify_frame = Frame(root)
	button = ['Modify FIR Details','Go to Main Menu']
	function  = [modify_victim,back]
	for i in range(len(button)) :
		Button(modify_frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(modify_frame)


#Add Menu
def add_victim() :
	global add_frame,root,add_victim_frame
	global v1,v2,v3,v4,v5,v6,v7
	add_frame.pack_forget()
	add_victim_frame = Frame(root)
	label1=Label(add_victim_frame,text="Enter the FIR NO.")
	label1.pack()
	v1=Entry(add_victim_frame)
	v1.pack()

	label2=Label(add_victim_frame,text="Enter the VICTIM name")
	label2.pack()
	v2=Entry(add_victim_frame)
	v2.pack()

	label3=Label(add_victim_frame,text="Enter ACCUSED name")
	label3.pack()
	v3=Entry(add_victim_frame)
	v3.pack()

	label4=Label(add_victim_frame,text="Enter the CASE DATE")
	label4.pack()
	v4=Entry(add_victim_frame)
	v4.pack()

	label5=Label(add_victim_frame,text="Enter the CASE TIME")
	label5.pack()
	v5=Entry(add_victim_frame)
	v5.pack()

	label6=Label(add_victim_frame,text="Enter the CASE DESCRIPTION")
	label6.pack()
	v7=Entry(add_victim_frame)
	v7.pack()

	label7=Label(add_victim_frame,text="Enter the CASE STATUS")
	label7.pack()
	v6=Entry(add_victim_frame)
	v6.pack()

	b1=Button(add_victim_frame,text="Enter",command=gett)
	b1.pack(side = LEFT)

	b2=Button(add_victim_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(add_victim_frame)


def gett():

	command='python case_insert1.py '+v1.get()+" "+v2.get()+" "+v3.get()+" "+v4.get()+" "+v5.get()+" "+v6.get()+" "+v7.get()
	os.system(command)
	print(command)



#Search
def search_victim() :
	global search_frame,root,search_victim_frame
	global vs1,vs2,vs3,vs4
	global lbl
	search_frame.pack_forget()
	search_victim_frame = Frame(root)
	global vs1,vs2,vs3

	lbl = Label(search_victim_frame, text='')
	lbl.pack()


	key=Label(search_victim_frame,text="Enter FIR NO.")
	key.pack()
	vs3=Entry(search_victim_frame)
	vs3.pack()

	b1=Button(search_victim_frame,text="Enter",command=get1)
	b1.pack(side=LEFT)

	b2=Button(search_victim_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(search_victim_frame)


def get1():

	command='python case_search.py '+" "+vs3.get()



	output = subprocess.check_output(command, shell=True)

	lbl['text'] = output.strip()


	os.system(command)
	print(command)




#Delete
def delete_victim() :
	#global add_frame
	global delete_frame,root,delete_victim_frame
	global vd1,vd2,vd3
	global lbl1
	delete_frame.pack_forget()
	delete_victim_frame = Frame(root)
#	global vs1,vs2,vs3
	global lbl
	lbl1 = Label(delete_victim_frame, text='')
	lbl1.pack()



	key=Label(delete_victim_frame,text="Enter FIR NO.")
	key.pack()
	vd3=Entry(delete_victim_frame)
	vd3.pack()

	b1=Button(delete_victim_frame,text="Enter",command=delete1)
	b1.pack(side=LEFT)

	b2=Button(delete_victim_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(delete_victim_frame)

def delete1():
	command='python case_delete.py '+" "+vd3.get()



	output = subprocess.check_output(command, shell=True)

	lbl1['text'] = output.strip()

	os.system(command)
	print(command)

	display_frame(delete_victim_frame)


def get_modify():
	command='python case_modify1.py '+" "+v3.get()+" "+vs4.get()


	print("modified")
	output = subprocess.check_output(command, shell=True)

	lbl1['text'] = output.strip()

	os.system(command)
	print(command)

	display_frame(modify_victim_frame)

#Modify
def modify_victim():
	global modify_frame,root,modify_victim_frame
	global v1,v2,v3,v4,v5,vs4
	global lbl1


	modify_frame.pack_forget()
	modify_victim_frame = Frame(root)

	lbl1 = Label(modify_victim_frame, text='')
	lbl1.pack()




	label3=Label(modify_victim_frame,text="Enter FIR NO.")
	label3.pack()
	v3=Entry(modify_victim_frame)
	v3.pack()

	key1=Label(modify_victim_frame,text="Enter new Status.")
	key1.pack()
	vs4=Entry(modify_victim_frame)
	vs4.pack()

	b1=Button(modify_victim_frame,text="Enter",command=get_modify)
	b1.pack(side = LEFT)

	b2=Button(modify_victim_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(modify_victim_frame)




#Main Program
root = Tk(className = "GUI")
frame=add_frame=search_frame=delete_frame=modify_frame = Frame(root)
root.minsize(200,200)
root.geometry("1000x1000")
root.title("Crime Files")

add_victim_frame = add_case_frame = Frame(root)
search_victim_frame  = Frame(root)
delete_victim_frame  = Frame(root)
modify_victim_frame = Frame(root)

#Creating Main_Menu Frame
button = ['Add','Search','Delete','Modify']
function = [add,search,delete,modify]
for i in range(len(button)) :
	Button(frame,text=button[i],command=function[i],height=1,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
#Display
display_frame(frame)
root.mainloop()

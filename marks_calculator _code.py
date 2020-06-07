import tkinter as tk

print('Choose an option\n1: Theory,Lab and Project\n2: Theory and Lab\n3: Theory and Project\n4: Only Theory')

option=0
try:
	option = int(input())
except:
	print('Please choose from the options above')

if(option==1):
	fields = ('CAT-1', 'CAT-2', 'DA-1', 'DA-2', 'Quiz','LAB (Out of 60)', 'Additional','Project(Out of 100)')

elif(option==2):
	fields = ('CAT-1', 'CAT-2', 'DA-1', 'DA-2', 'Quiz','LAB (Out of 60)', 'Additional')

elif(option==3):
	fields = ('CAT-1', 'CAT-2', 'DA-1', 'DA-2', 'Quiz', 'Additional','Project(Out of 100)')

elif(option==4):
	fields = ('CAT-1', 'CAT-2', 'DA-1', 'DA-2', 'Quiz', 'Additional')

else:
	print('Sorry :( Cant Find suitable option')


def generate_new_window(TOTAL_SCORE):
	window = tk.Toplevel()
	text = "Your Total Score: " + str(round(TOTAL_SCORE,2)) +" !!!"
	window.title("Final Score Out of 100")
	label = tk.Label(window, text=text)
	label.config(font=("Roboto", 30))
	label.pack(side=tk.LEFT, padx=25, pady=25)

    
def final_score(entries):
	if(option==1):
		#Theory
		cat1 = float(entries['CAT-1'].get())
		cat2 = float(entries['CAT-2'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+FAT_Marks+additional
		if(THEORY_TOTAL>100):
			THEORY_TOTAL = 100
			
		#Lab
		
		lab_internals = float(entries['LAB (Out of 60)'].get())
		labfat_Marks = (lab_internals*2)/3.0
		LAB_TOTAL = lab_internals + labfat_Marks
		
		#Project
		
		project = float(entries['Project(Out of 100)'].get())
		
		
		TOTAL_SCORE = THEORY_TOTAL/2.0 + LAB_TOTAL/4.0 + project/4.0
		print("Total Score: %f" % float(TOTAL_SCORE))
		generate_new_window(TOTAL_SCORE)
	
	elif(option==2):
		#Theory
		cat1 = float(entries['CAT-1'].get())
		cat2 = float(entries['CAT-2'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+FAT_Marks+additional
		if(THEORY_TOTAL>100):
			THEORY_TOTAL=100
			
		#Lab
		lab_internals = float(entries['LAB (Out of 60)'].get())
		
		labfat_Marks = (lab_internals*2)/3.0
		
		LAB_TOTAL = lab_internals + labfat_Marks
		
		TOTAL_SCORE = (THEORY_TOTAL*3.0)/4.0 + LAB_TOTAL/4.0
		generate_new_window(TOTAL_SCORE)
	
	elif(option==3):
		#Theory
		cat1 = float(entries['CAT-1'].get())
		cat2 = float(entries['CAT-2'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+FAT_Marks+additional
		if(THEORY_TOTAL>100):
			THEORY_TOTAL=100
			
		#Project
		project = float(entries['Project(Out of 100)'].get())
		
		TOTAL_SCORE = (THEORY_TOTAL*3.0)/4.0 + project/4.0
		print('Your Total Score', TOTAL_SCORE)
		generate_new_window(TOTAL_SCORE)
	
	
	elif(option==4):
		cat1 = float(entries['CAT-1'].get())
		cat2 = float(entries['CAT-2'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+FAT_Marks+additional
		if(THEORY_TOTAL>100):
			THEORY_TOTAL=100
		
		print('Your Total Score', THEORY_TOTAL)
		generate_new_window(THEORY_TOTAL)

def only_numbers(char):
	return char.replace(".", "0", 1).isdigit()
		
    
def makeform(root, fields):
	entries = {}
	for field in fields:
		
		row = tk.Frame(root)
		lab = tk.Label(row, width=22, text=field+": ", anchor='w')
		lab.config(font=("Roboto",16))
		validation = row.register(only_numbers)
		ent = tk.Entry(row, validate="key", validatecommand=(validation, '%S'))
		ent.config(font=("Roboto",16))
		row.pack(side=tk.TOP, 
				 fill=tk.X, 
				 padx=5, 
				 pady=5)
		lab.pack(side=tk.LEFT)
		ent.pack(side=tk.RIGHT, 
				 expand=tk.YES, 
				 fill=tk.X)
		entries[field] = ent
	return entries

if __name__ == '__main__':
	if(option>=1 and option<=4):
		root = tk.Tk()
		root.title("Simple VIT Marks Calculator")
		ents = makeform(root, fields)
		b1 = tk.Button(root, text='Final Score',
			   command=(lambda e=ents: final_score(e)))
		b1.config(font=("Roboto", 18))   
		b1.pack(side=tk.LEFT, padx=5, pady=5)
		
		b3 = tk.Button(root, text='Quit', command=root.quit)
		b3.config(font=("Roboto", 18))   
		b3.pack(side=tk.LEFT, padx=10, pady=5)
		
		root.mainloop()

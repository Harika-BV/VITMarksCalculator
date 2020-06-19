import tkinter as tk
from tkinter import * 

option = 1
fields = ('CAT-1 (Out of 15)', 'CAT-2 (Out of 15)', 'DA-1', 'DA-2', 'Quiz','LAB (Out of 60)', 'Additional','Project(Out of 100)')

def sel(var):
	option = var.get()

class SampleApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.geometry("1000x700")
		self._frame = None
		self.switch_frame(StartPage)
	
	def switch_frame(self, frame_class):
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()

class StartPage(tk.Frame):
	
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		text = "Choose the course type"
		label = tk.Label(self, text=text)
		label.config(font=("Roboto", 16))
		label.pack(side=tk.TOP, padx=25, pady=25)
		
		master.v = IntVar()
		values = {"ETLP" : 1,  
		"ETL" : 2, 
		"ETP" : 3, 
		"ET" : 4}
		
		etlp = Radiobutton(self,text='ETLP', value=1,variable = master.v, indicator = 0, font = ("Roboto",12), background = "light blue", command = lambda: sel(master.v)).pack(fill = X, ipady = 20) 
		
		etp = Radiobutton(self,text='ETP', value=2,variable = master.v, indicator = 0,font = ("Roboto",12), background = "light blue", command =lambda: sel(master.v)).pack(fill = X, ipady = 20) 
		
		etp = Radiobutton(self,text='ELP', value=3,variable = master.v, indicator = 0,font = ("Roboto",12), background = "light blue", command =lambda: sel(master.v)).pack(fill = X, ipady = 20) 
		
		et = Radiobutton(self,text='ET', value=4,variable = master.v, indicator = 0,font = ("Roboto",12), background = "light blue", command =lambda: sel(master.v)).pack(fill = X, ipady = 20) 
	
		tk.Button(self, text="Next", background = "light green",font = ("Roboto",12), command = lambda: master.switch_frame(PageOne)).pack(fill = X, padx=50, pady = 50)

class PageOne(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		text = "Enter the Marks"
		label = tk.Label(self, text=text)
		label.config(font=("Roboto", 16))
		label.pack(side=tk.TOP, padx=25, pady=25)
		
		option = master.v.get()
		fields = find_fields(option)
		ents = makeform(self, fields)
		
		b1 = tk.Button(self, text='Final Score', command=(lambda e=ents: final_score(e, option)))
		b1.config(font=("Roboto", 12))   
		b1.pack(side=tk.RIGHT,fill = X, ipadx=10, ipady = 10)
		
		b3 = tk.Button(self, text='Quit', command=master.quit)
		b3.config(font=("Roboto", 12))   
		b3.pack(side=tk.RIGHT,fill = X, ipadx=10, ipady = 10)
	
		tk.Button(self, text="Back",font=("Roboto", 12), background = "light green", command=lambda: master.switch_frame(StartPage)).pack(side=tk.LEFT,fill = X, pady = 50,ipadx=10, ipady = 10)

def final_score(entries, option):
	if(option==1):
		#Theory
		cat1 = float(entries['CAT-1 (Out of 15)'].get())
		cat2 = float(entries['CAT-2 (Out of 15)'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+additional
		if(THEORY_TOTAL>60):
			THEORY_TOTAL = 60
		
		THEORY_TOTAL = THEORY_TOTAL + FAT_Marks
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
		cat1 = float(entries['CAT-1 (Out of 15)'].get())
		cat2 = float(entries['CAT-2 (Out of 15)'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+additional
		if(THEORY_TOTAL>60):
			THEORY_TOTAL = 60
		
		THEORY_TOTAL = THEORY_TOTAL + FAT_Marks
		if(THEORY_TOTAL>100):
			THEORY_TOTAL = 100
			
		#Lab
		lab_internals = float(entries['LAB (Out of 60)'].get())
		
		labfat_Marks = (lab_internals*2)/3.0
		
		LAB_TOTAL = lab_internals + labfat_Marks
		
		TOTAL_SCORE = (THEORY_TOTAL*3.0)/4.0 + LAB_TOTAL/4.0
		generate_new_window(TOTAL_SCORE)
	
	elif(option==3):
		#Theory
		cat1 = float(entries['CAT-1 (Out of 15)'].get())
		cat2 = float(entries['CAT-2 (Out of 15)'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+additional
		if(THEORY_TOTAL>60):
			THEORY_TOTAL = 60
		
		THEORY_TOTAL = THEORY_TOTAL + FAT_Marks
		if(THEORY_TOTAL>100):
			THEORY_TOTAL = 100
			
		#Project
		project = float(entries['Project(Out of 100)'].get())
		
		TOTAL_SCORE = (THEORY_TOTAL*3.0)/4.0 + project/4.0
		print('Your Total Score', TOTAL_SCORE)
		generate_new_window(TOTAL_SCORE)
	
	
	elif(option==4):
		cat1 = float(entries['CAT-1 (Out of 15)'].get())
		cat2 = float(entries['CAT-2 (Out of 15)'].get())
		da1  = float(entries['DA-1'].get())
		da2  = float(entries['DA-2'].get())
		quiz1 = float(entries['Quiz'].get())
		
		FAT_Marks = ((cat1+cat2+da1+da2+quiz1)*2)/3.0
		additional = float(entries['Additional'].get())
		
		THEORY_TOTAL = cat1+cat2+da1+da2+quiz1+additional
		if(THEORY_TOTAL>60):
			THEORY_TOTAL = 60
		
		THEORY_TOTAL = THEORY_TOTAL + FAT_Marks
		if(THEORY_TOTAL>100):
			THEORY_TOTAL = 100
		
		print('Your Total Score', THEORY_TOTAL)
		generate_new_window(THEORY_TOTAL)


def generate_new_window(TOTAL_SCORE):
	window = tk.Toplevel()
	text = "Your Total Score: " + str(round(TOTAL_SCORE,2)) +" !!!"
	window.title("Final Score Out of 100")
	label = tk.Label(window, text=text)
	label.config(font=("Roboto", 30))
	label.pack(side=tk.LEFT, padx=25, pady=25)

    
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
	
def find_fields(option):
	
	if(option==1):
		fields = ('CAT-1 (Out of 15)', 'CAT-2 (Out of 15)', 'DA-1', 'DA-2', 'Quiz','LAB (Out of 60)', 'Additional','Project(Out of 100)')

	elif(option==2):
		fields = ('CAT-1 (Out of 15)', 'CAT-2 (Out of 15)', 'DA-1', 'DA-2', 'Quiz','LAB (Out of 60)', 'Additional')

	elif(option==3):
		fields = ('CAT-1 (Out of 15)', 'CAT-2 (Out of 15)', 'DA-1', 'DA-2', 'Quiz', 'Additional','Project(Out of 100)')

	elif(option==4):
		fields = ('CAT-1 (Out of 15)', 'CAT-2 (Out of 15)', 'DA-1', 'DA-2', 'Quiz', 'Additional')

	else:
		print('Sorry :( Cant Find suitable option')
	
	return fields

option = 0
app = SampleApp()
app.mainloop()

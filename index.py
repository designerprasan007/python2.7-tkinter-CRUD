from Tkinter import *
import ttk
import pymysql
import tkMessageBox



class Student:
	def __init__(self, root):
		self.root = root
		self.root.title('Student management')
		self.root.geometry("1350x800+0+0")

		title=Label(self.root, text='Student Management System', font=("times of roman", 40, "bold"), bg='orange', fg='black')
		title.pack(side=TOP, fill=X)


		# variables

		self.Roll_no_var=StringVar()
		self.name_var=StringVar()
		self.emial_var=StringVar()
		self.gender_var=StringVar()
		self.dob_var=StringVar()
		self.contact_var=StringVar()
		self.addr_txt=StringVar()
		
		# search variables
		self.search_by=StringVar()
		self.search_val=StringVar()

		# manage side

		manage = Frame(self.root, bd=4, relief=RIDGE, bg='yellow')
		manage.place(x=20, y=100, width=550, height=720)

		manage_title = Label(manage, text='Manage Student', font=("times of roman", 30), bg='yellow', fg='black')
		manage_title.grid(row=0, columnspan=2, pady=20, padx=20)


		lbl_roll = Label(manage, text='roll_num', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')
	
		roll_txt = Entry(manage, textvar=self.Roll_no_var, font=("times of roman", 15), bd=5, relief=GROOVE)
		roll_txt.grid(row=1, column=1, pady=10, padx=20, sticky='w')

		lbl_name = Label(manage, text='Name', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
	
		name_txt = Entry(manage, textvar=self.name_var, font=("times of roman", 15), bd=5, relief=GROOVE)
		name_txt.grid(row=2, column=1, pady=10, padx=20, sticky='w')

		lbl_email = Label(manage, text='Email', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')
	
		email_txt = Entry(manage, textvar=self.emial_var, font=("times of roman", 15), bd=5, relief=GROOVE)
		email_txt.grid(row=3, column=1, pady=10, padx=20, sticky='w')

		lbl_gend = Label(manage, text='Gender', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_gend.grid(row=4, column=0, pady=10, padx=20, sticky='w')

		gend_combo = ttk.Combobox(manage, textvar=self.gender_var, font=("times of roman", 15), state='readonly')	
		gend_combo['values']=('male','female','others')
		gend_combo.grid(row=4, column=1, pady=10, padx=20, sticky='w')

		lbl_cont = Label(manage, text='Contact', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_cont.grid(row=5, column=0, pady=10, padx=20, sticky='w')
	
		cont_txt = Entry(manage, textvar=self.contact_var, font=("times of roman", 15), bd=5, relief=GROOVE)
		cont_txt.grid(row=5, column=1, pady=10, padx=20, sticky='w')

		lbl_dob = Label(manage, text='D.O.B', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')
	
		dob_txt = Entry(manage, textvar=self.dob_var, font=("times of roman", 15), bd=5, relief=GROOVE)
		dob_txt.grid(row=6, column=1, pady=10, padx=20, sticky='w')

		lbl_addr = Label(manage, text='Address', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_addr.grid(row=7, column=0, pady=10, padx=20, sticky='w')
	
		self.addr_txt = Text(manage, width=15, height=3, font=("times of roman", 20), bd=5, relief=GROOVE)
		self.addr_txt.grid(row=7, column=1, pady=10, padx=20, sticky='w')

		# buttons
		btn_frame = Frame(manage, bg='yellow', bd=4, relief=GROOVE)
		btn_frame.place(x=15, y=580, width=480)  

		addbtn =Button(btn_frame, text='Add', width=8, command=self.add_students).grid(row=0, column=0, padx=10,pady=10)
		editbtn =Button(btn_frame, text='Update', width=8, command=self.update_student).grid(row=0, column=1, padx=10,pady=10)
		deletebtn =Button(btn_frame, text='Delete', width=8, command=self.delete_student).grid(row=0, column=2, padx=10,pady=10)
		clearbtn =Button(btn_frame, text='Clear', width=8, command=self.clear_vals).grid(row=0, column=3, padx=10,pady=10)

		# detail side

		detail = Frame(self.root, bd=4, relief=RIDGE, bg='yellow')
		detail.place(x=600, y=100, width=950, height=720)

		lbl_search = Label(detail, text='Search By', font=("times of roman", 20), bg='yellow', fg='black')
		lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')
	
		srch_combo = ttk.Combobox(detail, textvar=self.search_by, width=10, font=("times of roman", 15), state='readonly')	
		srch_combo['values']=('Roll num','Name','Contact')
		srch_combo.grid(row=0, column=1, pady=10, padx=20, sticky='w')

		search_text = Entry(detail, textvar=self.search_val, font=("times of roman", 15), width=10, bd=5, relief=GROOVE)
		search_text.grid(row=0, column=2, pady=10, padx=10)
 

		searchbtn =Button(detail, text='Search', command=self.search_student, width=8).grid(row=0, column=3, padx=10,pady=10)
		showallbtn =Button(detail, text='Show', command=self.fetch_students, width=8).grid(row=0, column=4, padx=10,pady=10)

		# table section
		Table_frame = Frame(detail, bd=4, relief=RIDGE, bg='yellow')
		Table_frame.place(x=15, y=80, width=910, height=600)

		scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
		scroll_y = Scrollbar(Table_frame, orient=VERTICAL)

		self.Student_table = ttk.Treeview(Table_frame, columns=("roll","name","email","gender","contact", "dob","address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		self.Student_table.heading("roll", text="ROLL NUM")
		self.Student_table.heading("name", text="Name")
		self.Student_table.heading("email", text="Email")
		self.Student_table.heading("gender", text="Gender")
		self.Student_table.heading("dob", text="DOB")
		self.Student_table.heading("contact", text="Contact")
		self.Student_table.heading("address", text="Address")
		self.Student_table['show']="headings"
		self.Student_table.column('roll', width=127)
		self.Student_table.column('name', width=127)
		self.Student_table.column('email', width=127)
		self.Student_table.column('gender', width=127)
		self.Student_table.column('contact', width=127)
		self.Student_table.column('dob', width=127)
		self.Student_table.column('address', width=122)
		self.Student_table.pack(fill=BOTH, expand=1)
		self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)

		self.fetch_students()

		# add user to db
	def add_students(self):
		if self.Roll_no_var.get() == "" or self.name_var.get() == "":
			 tkMessageBox.showerror("Error", "All Fields Required")
		else:	
			conn = pymysql.connect(host='localhost',user='root',password='root',database='python_student')
			cur = conn.cursor()
			cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s)',(self.Roll_no_var.get(),
																			 self.name_var.get(),
																			 self.emial_var.get(),
																			 self.gender_var.get(),
																			 self.contact_var.get(),
																			 self.dob_var.get(),
																			 self.addr_txt.get('1.0',END)	
																			))
			conn.commit()
			self.fetch_students()
			self.clear_vals()
			conn.close
			tkMessageBox.showinfo("Success", "Student added")


	def fetch_students(self):
		conn = pymysql.connect(host='localhost',user='root',password='root',database='python_student')
		cur = conn.cursor()
		cur.execute("select * from students")
		rows = cur.fetchall()
		if len(rows)!= 0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('', END, values=row)
				conn.commit()
		conn.close()


	#clear input values

	def clear_vals(self):
		self.Roll_no_var.set('')
		self.name_var.set('') 
		self.emial_var.set('') 
		self.gender_var.set('') 
		self.addr_txt.delete('1.0', END) 
		self.contact_var.set('') 
		self.dob_var.set('') 

			
		# get selected row values
	def get_cursor(self, eve):
		self.clear_vals()
		current_row = self.Student_table.focus()
		row_content = self.Student_table.item(current_row)
		content= row_content['values']
		self.Roll_no_var.set(content[0])
		self.name_var.set(content[1]) 
		self.emial_var.set(content[2]) 
		self.gender_var.set(content[3]) 
		self.addr_txt.insert(END, content[6]) 
		self.contact_var.set(content[4]) 
		self.dob_var.set(content[5]) 


# update student data
	def update_student(self):
		conn = pymysql.connect(host='localhost',user='root',password='root',database='python_student')
		cur = conn.cursor()
		cur.execute('update students set name = %s, email = %s, gender = %s, contact = %s, dob = %s, address = %s where roll_num = %s',
			(self.name_var.get(), self.emial_var.get(), self.gender_var.get(), self.contact_var.get(),self.dob_var.get(),self.addr_txt.get('1.0',END),self.Roll_no_var.get()))
		conn.commit()
		self.fetch_students()
		self.clear_vals()
		conn.close	

	# update student data
	def delete_student(self):
		conn = pymysql.connect(host='localhost',user='root',password='root',database='python_student')
		cur = conn.cursor()
		cur.execute('delete from students where roll_num = %s',self.Roll_no_var.get())
		conn.commit()
		self.fetch_students()
		self.clear_vals()
		conn.close			


	# search  student

	def search_student(self):
		print(self.search_by.get().lower(), str(self.search_val.get()))
		conn = pymysql.connect(host='localhost',user='root',password='root',database='python_student')
		cur = conn.cursor()
		cur.execute("select * from students where "+str(self.search_by.get().lower())+" like '%"+str(self.search_val.get())+"%'")
		rows = cur.fetchall()
		if len(rows) == 0:
			self.Student_table.delete(*self.Student_table.get_children())
			self.Student_table.insert('', END, values='NO DATA FOUND')
		else :
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('', END, values=row)
				conn.commit()
		conn.close()

root = Tk()
ob = Student(root)
root.mainloop()
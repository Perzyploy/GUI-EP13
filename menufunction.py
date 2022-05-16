from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *
import os


class ProductIcon:

	def __init__(self):
		self.quantity = None 
		self.table_product = None
		self.v_radio = None
		self.button_list = None #เก็บข้อมูลปุ่ม
		self.button_frame = None # ตำแหน่งที่เก็บ
		self.function_add = None
	
	def popup(self):
		# PGUI = Product GUI
		PGUI = Toplevel()
		PGUI.geometry('500x500')
		PGUI.title('ตั้งค่า -> โชว์รไอคอนรายการสินค้า')

		# ตารางสินค้า
		header = ['ID','รหัสสินค้า', 'ชื่อสินค้า', 'แสดงไอคอน']
		hwidth = [50,50,200,70]

		self.table_product = ttk.Treeview(PGUI,columns=header, show='headings',height=15)
		self.table_product.pack()

		for hd,hw in zip(header,hwidth):
			self.table_product.column(hd,width=hw)
			self.table_product.heading(hd,text=hd)

		self.table_product.bind('<Double-1>',self.change_status)
		self.insert_table()
		PGUI.mainloop()




	def insert_table(self):
		self.table_product.delete(*self.table_product.get_children()) # เพื่อให้มันลบข้อมูลหลังอัพเดท
		data = View_product_table_icon()
		print(data)
		for d in data:
			row = list(d) # เพราะ d เป็น tuple ต้องแปลงเป็น list ก่อนถึงจะ append ได้
			
			check = View_product_status(row[0])

			# โชว์สถานะของสินค้าไปทำปุ่ม
			if check[-1] == 'show': # ให้เช็คสถานะ ถ้ามีให้แสดงติ้กถูก ถ้าไม่มีไม่ต้องแสดง
				row.append('✔')

			else:
				row.append('')

			self.table_product.insert('','end',value=row)




	def change_status(self,event=None): # ทุกครั้งที่มีการ bind ต้องใส่ event เสมอ

		select = self.table_product.selection()
		pid = self.table_product.item(select)['values'][0]
		#print('PID[check]:',pid)



		SGUI = Toplevel() #SGUI = Status GUI
		SGUI.geometry('400x200')

		self.v_radio = StringVar()


		# Radio button
		RB1 = ttk.Radiobutton(SGUI, text= 'โชว์ไอคอน', variable = self.v_radio, value = 'show', command = lambda x=None:insert_product_status(int(pid),'show'))
		RB2 = ttk.Radiobutton(SGUI, text= 'ไม่โชว์ไอคอน', variable = self.v_radio, value = 'None', command = lambda x=None:insert_product_status(int(pid),''))
		RB1.pack(pady=20)
		RB2.pack()

		check = View_product_status(pid)
		print('CHECK:',check)
		if check[-1] == 'show': #ถ้าสถานะของ obj index -1 เป็นโชว์ จะให้ default เป็นปุ่ม RB1 คือคาที่คำว่า show
			RB1.invoke()

		else:
			RB2.invoke() #ถ้าไม่ จะให้แสดงปุ่ม RB2

		#RB1.invoke() # set ค่า default ของ radio อันนี้ให้แสดงที่ RB1 เป็น defaultถ้าเอา . pack ไปว่างข้างหลังแต่แรกจะตั้งค่าไม่ได้

		# Dropdown 
		# dropdown = ttk.Combobox(SGUI, value = ['โชว์ไอคอน','ไม่โชว์ไอคอน'])
		# dropdown.pack()
		# dropdown.set('โชว์ไอคอน')
		# dropdown.bind('<<ComboboxSelected>>',lambda x= None: print(dropdown.get()))


		def check_close():
			print('closed')
			SGUI.destroy() #หน้าต่างย่อยจะไม่ปิดแล้ว เพราะมันมองเป็นปุ่มกด ต้องใช้คำสั่ง destroy เพื่อสั่งปิดหน้าต่าง
			self.insert_table() #เพื่อให้มันแทรกข้อมูลในตาราง
			self.clearbutton() # เรียกฟังก์ชันเคลียร์ปุ่ม
			self.create_button() # เรียกฟังก์ชันสร้างปุ่ม
		


		SGUI.protocol('WM_DELETE_WINDOW', check_close) #เป็นคำสั่งของ TK


		SGUI.mainloop()

	def command(self):
		self.popup()

	# REFRESH หน้าแสดงปุ่ม
	def clearbutton(self):
		print('CLEAR_BUTTON')
		for b in self.button_list.values():
				# b = {'button':B, 'row':row, 'column':column} 
				b['button'].grid_forget() # ทำให้ปุ่ม index ที่ 1 ที่เก็
				#b['button'].destroy() # เราไม่ใช้ forget แล้ว เราจะ destroy คือลบทั้งหมดทิ้งไปเลย ค่อยแอดใหม่ทั้งแพ

	def create_button(self): # สร้างปุ่มใหม่ทั้งหมด หลังจาก destroy ไป
		print('CREATE_BUTTON')
		product = product_icon_list() # ดึงมาจาก productdb

		global button_dict # ประกาศ global เพื่อให้ dict อันนี้ใช้งานนอกฟังก์ชันได้
		button_dict = {} # สร้าง dict ขึ้นมาเพื่อเอาไว้เก็บ icon รายการสินค้า


		row = 0
		column = 0
		column_quan = 3 # ใส่จำนวนคอลัมน์ที่ต้องการให้มันแสดงบน GUI
		for i,(k,v) in enumerate(product.items()):
			if column == column_quan:
				column = 0 
				row += 1 

			print('IMG:', v['icon'])
			new_icon = PhotoImage(file=v['icon']) # ดึง icon มาจาก database
			B = ttk.Button(self.button_frame,text=v['name'],compound='top') # เอาปุ่มที่สร้างขึ้นมาใหม่หลังจากลบ ไปแปะที่ button frame 
			button_dict[v['id']] = {'button':B, 'row':row, 'column':column} # เอา id ของสินค้ามาใส่เป็น key ของ dict ชื่อ button_dict ปุ่มกดให้อ้างอิงจาก B row กับ column อ้างอิงจากบรรทัดบน
			B.configure(command=lambda m=k: self.function_add(m)) #เป็นคำสั่งของ TK
    

			B.configure(image= new_icon) # icon ใหม่ที่เรียกมาจาก databse
			B.image = new_icon # ต้องมาประกาศบรรทัดนี้ใหม่ด้วย ไม่งั้นรูปไม่ขึ้น
   

			B.grid(row=row, column=column)
			column += 1


		self.button_list = button_dict # ทำให้มีการอัพเดทจำนวนปุ่มตัวใหม่





class Addproduct:

	def __init__(self):
		self.v_productid = None
		self.v_title = None
		self.v_price = None
		self.v_imagepath = None
		self.MGUI = None
		self.ProductImage = None 
		self.button_list = None #เก็บข้อมูลปุ่ม
		self.button_frame = None # ตำแหน่งที่เก็บปุ่ม





	def popup(self):
		self.MGUI = Toplevel()
		self.MGUI.geometry('500x700')
		self.MGUI.title('Add Product')

		self.v_productid = StringVar()
		self.v_title = StringVar()
		self.v_price = StringVar()
		self.v_imagepath = StringVar()

		L = Label(self.MGUI,text='เพิ่มรายการสินค้า', font=(None,30))
		L.pack(pady=20)

		#-----------------------------------------
		L = Label(self.MGUI,text='รหัสสินค้า', font=(None,20)).pack()
	

		
		E1 = ttk.Entry(self.MGUI,textvariable=self.v_productid,font=(None,20))
		E1.pack(pady=10)

		#-----------------------------------------
		L = Label(self.MGUI,text='ชื่อสินค้าสินค้า', font=(None,20)).pack()


		
		E2 = ttk.Entry(self.MGUI,textvariable= self.v_title,font=(None,20))
		E2.pack(pady=10)

		#-----------------------------------------
		L = Label(self.MGUI,text='ราคา', font=(None,20)).pack()


		
		E3 = ttk.Entry(self.MGUI,textvariable= self.v_price,font=(None,20))
		E3.pack(pady=10)

		img = PhotoImage(file = 'default-product.png')
		self.ProductImage = Label(self.MGUI, textvariable=self.v_imagepath, image=img, compound = 'top') # ตรง compound คือให้มันแสดงที่อยู่ path เป็นตัวอักษรด้วย
		self.ProductImage.pack() 

		Bselect = ttk.Button(self.MGUI, text='เลือกรูปสินค้า (120 x 120 px)',command = self.selectfile)
		Bselect.pack(pady=10)

		Bsave = ttk.Button(self.MGUI, text='บันทึก',command = self.saveproduct)
		Bsave.pack(pady=10,ipadx=20,ipady=10)


		#E2.focus()


		self.MGUI.mainloop()


	def selectfile(self):
		self.MGUI.lift() #เพื่อบังคับให้หน้าต่าง GUI pop up ที่เราเลือก ขึ้นมาอยู่เลเยอร์บนสุด
		filetypes = (
				('PNG', '*.png'),
				('All files', '*.*')
			)
		DIR = os.getcwd() # เพื่อตั้งค่า folder default ที่เก็บรูปภาพ เป็นคำสั่งให้แสดง path ที่เก็บโปรแกรมอยู่
		select = filedialog.askopenfilename(title='เลือกไฟล์ภาพ',initialdir=DIR,filetypes=filetypes)
		img = PhotoImage(file= select)
		self.ProductImage.configure(image=img)
		self.ProductImage.image = img # สำคัญมาก

		self.v_imagepath.set(select)
		self.MGUI.focus_force() #บังคับให้ focus ที่ GUI นั้น ที่เป็นหน้าต่างย่อย ไม่ให้หายไป
		self.MGUI.grab_set()



	def saveproduct(self):
		v1 = self.v_productid.get()
		v2 = self.v_title.get()
		v3 = float(self.v_price.get())
		v4 = self.v_imagepath.get()
		Insert_product(v1,v2,v3,v4)
		self.v_productid.set('')
		self.v_title.set('')
		self.v_price.set('')
		self.v_imagepath.set('')
		View_product() # เรียกใช้ฟังก์ชัน

		# เรียกฟังก์ชันเคลียร์ปุ่ม
		self.clearbutton()
		self.create_button()


	def command(self):
		self.popup()



	# REFRESH หน้าแสดงปุ่ม
	def clearbutton(self):
		for b in self.button_list.values():
				# b = {'button':B, 'row':row, 'column':column} 
				b['button'].grid_forget() # ทำให้ปุ่ม index ที่ 1 ที่เก็
				#b['button'].destroy() # เราไม่ใช้ forget แล้ว เราจะ destroy คือลบทั้งหมดทิ้งไปเลย ค่อยแอดใหม่ทั้งแพ

	def create_button(self): # สร้างปุ่มใหม่ทั้งหมด หลังจาก destroy ไป
			print('CREATE_BUTTON')
			product = product_icon_list() # ดึงมาจาก productdb

			global button_dict # ประกาศ global เพื่อให้ dict อันนี้ใช้งานนอกฟังก์ชันได้
			button_dict = {} # สร้าง dict ขึ้นมาเพื่อเอาไว้เก็บ icon รายการสินค้า


			row = 0
			column = 0
			column_quan = 3 # ใส่จำนวนคอลัมน์ที่ต้องการให้มันแสดงบน GUI
			for i,(k,v) in enumerate(product.items()):
				if column == column_quan:
					column = 0 
					row += 1 

				print('IMG:', v['icon'])
				new_icon = PhotoImage(file=v['icon']) # ดึง icon มาจาก database
				B = ttk.Button(self.button_frame,text=v['name'],compound='top') # เอาปุ่มที่สร้างขึ้นมาใหม่หลังจากลบ ไปแปะที่ button frame 
				button_dict[v['id']] = {'button':B, 'row':row, 'column':column} # เอา id ของสินค้ามาใส่เป็น key ของ dict ชื่อ button_dict ปุ่มกดให้อ้างอิงจาก B row กับ column อ้างอิงจากบรรทัดบน
				B.configure(command=lambda m=k: AddMenu(m)) #เป็นคำสั่งของ TK
    

				B.configure(image= new_icon) # icon ใหม่ที่เรียกมาจาก databse
				B.image = new_icon # ต้องมาประกาศบรรทัดนี้ใหม่ด้วย ไม่งั้นรูปไม่ขึ้น
   

				B.grid(row=row, column=column)
				column += 1

			#self.button_list = button_dict


if __name__ == '__main__':
	test = Addproduct()
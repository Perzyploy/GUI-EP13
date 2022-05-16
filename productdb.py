import sqlite3

conn = sqlite3.connect('productdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

# v_membercode.set(memberinfo[0])
# v_fullname.set(memberinfo[1]) #ถูกset ให้แสดงค่าใน index ที่ 1 ของ allmember ซึ่งก็คือ ชื่อ-สกุล เอาไปแปะไว้ตรงช่อง entry ชื่อ-สกุล เพื่อให้เราไปลบค่าได้
# v_tel.set(memberinfo[2])
# v_usertype.set(memberinfo[3])
# v_point.set(memberinfo[4])







# สร้างตารางในการจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS product (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				productid TEXT,
				title TEXT,
				price REAL,
				image TEXT ) """)


c.execute("""CREATE TABLE IF NOT EXISTS product_status (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				product_id INTEGER,
				status TEXT) """)

def insert_product_status(pid,status):
	#pid = product id
	check = View_product_status(pid)
	if check == None:
		with conn:
			command = 'INSERT INTO product_status VALUES (?,?,?)'
			c.execute(command,(None,pid,status))
		conn.commit()
		print('status saved') # ให้เช็คสถานะ ถ้าไม่มี ให้เซฟลง sql ถ้ามีให้ปริ้นคำว่ามี

	else:
		print('pid exist')
		print(check)
		Update_product_status(pid,status)


def View_product_status(pid):
	#READ
	with conn:
		command = 'SELECT * FROM product_status WHERE product_id = (?)'
		c.execute(command,([pid]))
		result = c.fetchone()
	#print(result)
	return result # เพื่อดึงค่าจาก database ออกมาที่ python

def Update_product_status(pid,status):
	# UPDATE
	with conn:
		command = 'UPDATE product_status SET status = (?) WHERE product_id=(?)'
		c.execute(command,([status,pid]))
		conn.commit()
		print('updated:',(pid,status))

#################################################################
def Insert_product(productid,title,price,image):
	#CREATE
	# ตรวจสอบ productiid ที่มีแล้ว ห้ามซ้ำ
	with conn: #เป็นคำสั่งให้เปิดคอนเนคชั่นและให้ปิดอัตโนมัติ เหมือน open csv
		command = 'INSERT INTO product VALUES(?,?,?,?,?)' # SQL command ? ใส่ตามจำนวนข้อมูลที่จะกรอก มี 6 หััวข้อ
		c.execute(command,(None,productid,title,price,image))
	conn.commit() #SAVE DATABASE
	print('saved')

	#----- add status after insert product ------
	find = View_product_single(productid)
	insert_product_status(find[0],'show') # '' แปลว่า add status ให้ product ทุกตัวที่ใส่เพิ่มเข้ามาเป็นไม่โชว์ (หาจาก index 0) และ show icon ทุกครั้งที่มีการ add

def View_product():
	#READ
	with conn:
		command = 'SELECT * FROM product' #select star คือ เอาทั้งหมด
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result # เพื่อดึงค่าจาก database ออกมาที่ python



def View_product_table_icon():
	#READ
	with conn:
		command = 'SELECT ID, productid, title FROM product' # เลือก select เฉพาะบางอัน
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result #





def View_product_single(productid):
	#READ
	with conn:
		command = 'SELECT * FROM product WHERE productid = (?)'
		c.execute(command,([productid]))
		result = c.fetchone()
	print(result)
	return result # เพื่อดึงค่าจาก database ออกมาที่ python

'''
product = {'latte':{'name':'ลาเต้','price':30},
           'cappuccino':{'name':'คาปูชิโน','price':35},
           'espresso':{'name':'เอสเปรสโซ่','price':40},
           'greentea':{'name':'ชาเขียว','price':20},
           'icetea':{'name':'ชาเย็น','price':15},
           'hottea':{'name':'ชาร้อน','price':10},}
'''

def product_icon_list(): #เพื่อเก็บไอคอนของผลิตภัณฑ์ไว้ใน database
	with conn:
		command = 'SELECT * FROM product '
		c.execute(command)
		product = c.fetchall()

	with conn:
		command = "SELECT * FROM product_status WHERE status = 'show'"
		c.execute(command)
		status = c.fetchall()

	#print('R',result)
	#print('S',status)

	result = []

	for s in status:
		for p in product:
			if s[1] == p[0]:
				print(p,s[-1])
				result.append(p) #เพิ่มใน database

	result_dict = {}
	print(result)
	#(1, 'CF-1001', 'ลาเต้',25.0, path ของรูปภาพ icon)
	# เราจะดึงข้อมูลจาก data base มาทำเป็น dictionary ชุดใหม่ เพื่อเอาไว้อ้างอิงเวลาจะเปลี่ยนเมนูไอคอน
	for r in result: 
		result_dict[r[0]] = {'id':r[0],'productid':r[1],'name':r[2],'price':r[3],'icon':r[4]} # เราจะให้ id ของ product เป็น list รายการ

	return result_dict




if __name__ == '__main__': # มาจากคำสั่ง ifmain เป็น underscore 2 ตัวติดกัน
	
	x = product_icon()
	print(x)
	# เป็นฟังก์ชันที่เอาไว้เช็คว่าตอนนี้ไฟล์ที่กำลังรันอยู่นี้อยู่ในไฟล์จริงหรือไม่
	# Insert_product('CF-1001','ลาเต้',35,r'C:\Image\latte.png') #ที่เก็บไฟล์ภาพคือไดรฟ์ C
	# View_product() #มันจะยังไม่รันฟังก์ชันนี้ จนกว่าจะมีการเรียกใช้เงื่อนไขบางอย่าง
	#View_product_table_icon()
	#insert_product_status(1,'show')
	#print(View_product_status(1))
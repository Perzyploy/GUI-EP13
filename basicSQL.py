#basic-sql.py

import sqlite3

conn = sqlite3.connect('basicdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

# v_membercode.set(memberinfo[0])
# v_fullname.set(memberinfo[1]) #ถูกset ให้แสดงค่าใน index ที่ 1 ของ allmember ซึ่งก็คือ ชื่อ-สกุล เอาไปแปะไว้ตรงช่อง entry ชื่อ-สกุล เพื่อให้เราไปลบค่าได้
# v_tel.set(memberinfo[2])
# v_usertype.set(memberinfo[3])
# v_point.set(memberinfo[4])







# สร้างตารางในการจัดเก็บ
c.execute("""CREATE TABLE IF NOT EXISTS member (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				membercode TEXT,
				fullname TEXT,
				tel TEXT,
				usertype TEXT,
				points INTEGER ) """)

def Insert_member(membercode,fullname,tel,usertype,points):
	#CREAT
	with conn: #เป็นคำสั่งให้เปิดคอนเนคชั่นและให้ปิดอัตโนมัติ เหมือน open csv
		command = 'INSERT INTO member VALUES(?,?,?,?,?,?)' # SQL command ? ใส่ตามจำนวนข้อมูลที่จะกรอก มี 6 หััวข้อ
		c.execute(command,(None,membercode,fullname,tel,usertype,points))
	conn.commit() #SAVE DATABASE
	print('saved')


def View_member():
	#READ
	with conn:
		command = 'SELECT * FROM member'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result # เพื่อดึงค่าจาก database ออกมาที่ python


def Update_member(ID,field,newvalue):
	# UPDATE
	with conn:
		command = 'UPDATE member SET {} = (?) WHERE ID=(?)'.format(field)
		c.execute(command,([newvalue,ID]))
		conn.commit()
		print('updated')

def Delete_member(ID):
	#DELETE
	with conn:
		command = 'DELETE FROM member WHERE ID=(?)'
		c.execute(command,([ID]))
	conn.commit()
	print('deleted')







# res = View_member()
# print(res[1]) # สั่งให้แสดงข้อมูล index 1 ใน database แต่อย่าลืมคำสั่ง return นะ


#Update_member(2,'fullname','สมศักดิ์ เจริญรุ่งเรือง') # จะแก้ข้อมูลอันดับที่ 2 ชื่อสมชาย เก่งมาก เป็น สมศักดิ เจริญรุ่งเรือง

Delete_member(1) #ลบข้อมูลอันดับที่ 1

View_member()


#Insert_member('MB-1001','สมชาย เก่งมาก','0830124211','general',100)
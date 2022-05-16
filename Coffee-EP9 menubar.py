# GUI-Calculator.py
from tkinter import *
from tkinter import ttk, messagebox
import wikipedia
############### DATABASE #######
#วิธีการ import database

# วิธีที่ 1
from memberdb import *
View_member()

# วิธีที่ 2
#import memberdb
#memberdb.View_member()

# วิธีที่ 3
#import memberdb as db 
#db.View_member()
############# CSV ##############
import csv
from datetime import datetime
def writetocsv(data, filename='data.csv'):
    with open(filename,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)

#############GUI##############
GUI = Tk()
GUI.title('โปรแกรมจัดการ layout')
GUI.iconbitmap('cup.ico') # ใส่ icon ในหัวตาราง GUI ต้องใช้ไฟล์ชนิด ico เท่านั้น

W = 1200 #กว้าง
H = 600  #สูง

MW = GUI.winfo_screenwidth() # กว้างจอ
MH = GUI.winfo_screenheight() # สูงจอ
SX = (MW/2)-(W/2) # Start X หาจุดเริ่มต้นจอแนวแกน x
SY = (MH/2)-(H/2) # Start Y หาจุดเริ่มต้นจอแนวแกน x
SY = SY-50 # ลดระยะจากแกน y ลงมา 50 พิกเซล เรียกว่า diffup



# print('MW:',MW)
# print('MH:',MH)

#GUI.geometry('1200x600+500+0') #ตรงบวก 500 บวก 0 คือบวกพิกัดแนวแกน x และ y ตามลำดับ เพื่อฟิกตำแหน่งให้อยู่ในพิกัดนี้เสมอ
GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY)) #ทำให้ GUI ปรากฎกลางจอ
#xxxxxxxxxxxxxxxxxxx Menubarxxxxxxxxxxxxxxxxxxxxxxxx

menubar = Menu(GUI) # menu หลัก แถบหลัก ใส่ไว้ใน GUI
GUI.config(menu=menubar)

#---------------------------------------------
# File Menu
filemenu = Menu(menubar,tearoff=0) # ใส่ไว้ใน menubar ปิดการ tearoff ของเมนู
menubar.add_cascade(label ='File',menu=filemenu) # add menu ใส่ label ชื่อ File ไว้ตรง filemenu

def ExportDatabase():
    print('Export Database to CSV')


filemenu.add_command(label='Export',command=ExportDatabase)
#filemenu.add_command(label='Exit',command=lambda: print('Exit')) # ใช้การเขียนแลมด้าแทนการเขียนฟังก์ชัน เพื่อให้มันสั้นแค่บรรทัดเดียว แต่ใช้ได้กับแค่คำสั่งเดียว
filemenu.add_command(label='Exit',command=GUI.quit) #เป็นคำสั่งให้มัน exit GUI.quite เป็นคำสั่งสำเร็จรูปของ tk
#filemenu.add_command(label='Exit',command=GUI.destroy) # เป็นคำสั่ง exit อีกแบบ




#---------------------------------------------
# Member Menu
membermenu = Menu(menubar) # ใส่ไว้ใน menubar
menubar.add_cascade(label ='Member',menu=membermenu) # add menu ใส่ label ชื่อ File ไว้ตรง filemenu



#---------------------------------------------
# Help Menu
import webbrowser

helpmenu = Menu(menubar) # ใส่ไว้ใน menubar
menubar.add_cascade(label ='Help',menu=helpmenu)
contact_url= 'https://uncle-engineer.com'
helpmenu.add_command(label='Contact US',command=lambda : webbrowser.open(contact_url))

def About():
    ABGUI = Toplevel()
    ABGUI.iconbitmap('cup.ico') # ใส่ icon ในหัวตารางหน้าต่าง about ต้องใช้ไฟล์ชนิด ico เท่านั้น
    W = 300 #กว้าง
    H = 200  #สูง

    MW = GUI.winfo_screenwidth() # กว้างจอ
    MH = GUI.winfo_screenheight() # สูงจอ
    SX = (MW/2)-(W/2) # Start X หาจุดเริ่มต้นจอแนวแกน x
    SY = (MH/2)-(H/2) # Start Y หาจุดเริ่มต้นจอแนวแกน x
    ABGUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY)) #ทำให้ GUI ปรากฎกลางจอ
    L = Label(ABGUI,text='โปรแกรมร้านกาแฟ',fg='green',font=('Angsana New',30)).pack()
    L = Label(ABGUI,text='พ้ฒนาโดย JC',font=('Angsana New',30)).pack()
    ABGUI.mainloop()
    ABGUI.mainloop()

helpmenu.add_command(label='About',command=About)





#############TAB SETTING##############
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = Frame(Tab)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
icon_tab3 = PhotoImage(file='tab3.png')
icon_tab4 = PhotoImage(file='tab4.png')

Tab.add(T1, text='กุ้ง',image=icon_tab1,compound='left')
Tab.add(T2, text='wiki',image=icon_tab2,compound='left')
Tab.add(T3, text='CAFE',image=icon_tab3,compound='left')
Tab.add(T4, text='Member',image=icon_tab4,compound='left')

############TAB 1 - กุ้ง############

L1 = Label(T1,text='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar() #ตัวแปรพิเศษเอาไว้เก็บค่า

E1 = ttk.Entry(T1, textvariable= v_kilo, width=10,justify='right',font=('impact',30))
E1.pack(pady=20)

E1.focus()

def Calc(event=None):
    print('กำลังคำนวณ...กรุณารอสักครู่')
    kilo = float(v_kilo.get()) # .get() ดึงข้อมูลจากตัวแปรที่เป็น StringVar
    print(kilo * 10)
    calc_result = kilo * 299
    date = datetime.now()
    year = date.year + 543
    stamp = date.strftime('{}-%m-%d %H:%M:%S'.format(year)) #Thai Year
    data = [stamp, 'กุ้ง', '{:,.2f}'.format(calc_result)]
    writetocsv(data)
    messagebox.showinfo('รวมราคาทั้งหมด','ลูกค้าต้องจ่ายตังค์ทั้งหมด: {:,.2f} บาท (กิโลกรัมละ 299 บาท)'.format(calc_result))


B1 = ttk.Button(T1,text='คำนวณราคา',command=Calc)
B1.pack(ipadx=40,ipady=30)

E1.bind('<Return>',Calc) # ต้องใส่คำว่า event=None ไว้ในฟังชั่นด้วย

############TAB 2 - Wiki ############

FONT1 = ('Angsana New',25)

L2 = Label(T2,text='ค้นหาข้อมูล wikipedia',font=('Angsana New',25))
L2.pack()

v_search = StringVar() # .get()=ดึงข้อมูล .set('hello') เซ็ตข้อความให้เป็นแบบนั้น

E2 = ttk.Entry(T2, textvariable=v_search, font=FONT1)
E2.pack(pady=10)

wikipedia.set_lang('th') #ทำให้เป็นภาษาไทย

v_link = StringVar()

def Search():
    try:
        search = v_search.get() #ดึงข้อความจากช่องกรอกมา
        # text = wikipedia.summary(search)
        text = wikipedia.page(search)
        print(text)
        v_result.set(text.content[:1000])
        print('LINK:',text.url)
        v_link.set(text.url)
    except:
        v_result.set('ไม่มีข้อมูล กรุณาค้นหาใหม่')

    # เพิ่มฟังชั่นสำหรับเด้งไปอ่านบทความฉบับเต็มในเว็บบราวเซอร์

B2 = ttk.Button(T2,text='Search',image=icon_tab2,compound='left',command=Search)
B2.pack()

import webbrowser

def readmore():
    webbrowser.open(v_link.get())

B3 = ttk.Button(T2,text='อ่านต่อ',command=readmore)
B3.place(x=800,y=50)

v_result = StringVar()
v_result.set('--------Result--------')
result = Label(T2,textvariable=v_result,wraplength=550, font=(None,15))
result.pack()

############TAB 3 - Coffee ############

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New',15))

CF1 = Frame(T3)
CF1.place(x=50,y=100)

# ROW0
# header = ['No.', 'title', 'quantity','price','total']

allmenu = {}

product = {'latte':{'name':'ลาเต้','price':30},
           'cappuccino':{'name':'คาปูชิโน','price':35},
           'espresso':{'name':'เอสเปรสโซ่','price':40},
           'greentea':{'name':'ชาเขียว','price':20},
           'icetea':{'name':'ชาเย็น','price':15},
           'hottea':{'name':'ชาร้อน','price':10},}

def UpdateTable():
    table.delete(*table.get_children()) # แคลียร์ข้อมูลเก่าในตาราง
    for i,m in enumerate(allmenu.values(),start=1):
        # m = ['ลาเต้', 30, 1, 30]
        table.insert('','end',value=[ i ,m[0],m[1],m[2],m[3] ] )


def AddMenu(name='latte'):
    # name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'],product[name]['price'],1,product[name]['price']]
        
    else:
        # {'latte': ['ลาเต้', 30, 1, 30]}
        quan = allmenu[name][2] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['name'],product[name]['price'], quan ,total]
    print(allmenu)
    # ยอดรวม
    count = sum([ m[3] for m in allmenu.values()])
    v_total.set('{:,.2f}'.format(count))
    UpdateTable()



B = ttk.Button(CF1,text='ลาเต้',image=icon_tab3,compound='top',command=lambda m='latte': AddMenu(m))
B.grid(row=0,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='คาปูชิโน',image=icon_tab3,compound='top',command=lambda m='cappuccino': AddMenu(m))
B.grid(row=0,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='เอสเปรสโซ่',image=icon_tab3,compound='top',command=lambda m='espresso': AddMenu(m))
B.grid(row=0,column=2,ipadx=20,ipady=10)

# ROW1
B = ttk.Button(CF1,text='ชาเขียว',image=icon_tab3,compound='top',command=lambda m='greentea': AddMenu(m))
B.grid(row=1,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาเย็น',image=icon_tab3,compound='top',command=lambda m='icetea': AddMenu(m))
B.grid(row=1,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาร้อน',image=icon_tab3,compound='top',command=lambda m='hottea': AddMenu(m))
B.grid(row=1,column=2,ipadx=20,ipady=10)




######TABLE#######
CF2 = Frame(T3)
CF2.place(x=500,y=100)

header = ['No.', 'title', 'price','quantity','total']
hwidth = [50,200,100,100,100]

table = ttk.Treeview(CF2,columns=header, show='headings',height=15)
table.pack()

for hd,hw in zip(header,hwidth):
    table.column(hd,width=hw)
    table.heading(hd,text=hd)

# for hd in header:
#     table.heading(hd,text=hd)


L = Label(T3,text='Total:', font=(None,15)).place(x=500,y=450)

v_total = StringVar()
v_total.set('0.0')

LT = Label(T3,textvariable=v_total, font=(None,15))
LT.place(x=600,y=450)

def Reset():
    global allmenu
    allmenu = {}
    table.delete(*table.get_children())
    v_total.set('0.0')
    trstamp = datetime.now().strftime('%y%m%d%H%M%S') #GEN Transaction
    v_transaction.set(trstamp)

B = ttk.Button(T3,text='Clear',command=Reset).place(x=600,y=500)

# Transaction ID
v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S') #GEN Transaction
v_transaction.set(trstamp)
LTR = Label(T3,textvariable=v_transaction,font=(None,10)).place(x=950,y=70)


# Save Button
FB = Frame(T3)
FB.place(x=890,y=450)

def AddTransaction():
    # writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction, stamp, allmenu.values())
    for m in allmenu.values():
        # before: m = ['คาปูชิโน', 35, 1, 35]
        # after: m = ['12341234', '2022-02-17 21:04:19', 'คาปูชิโน', 35, 1, 35]
        m.insert(0,transaction)
        m.insert(1,stamp)
        writetocsv(m,'transaction.csv')
    Reset() #clear data


B = ttk.Button(FB,text='บันทึก',command=AddTransaction)
B.pack(ipadx=30,ipady=20)

# History New Windows

def HistoryWindow(event):
    HIS = Toplevel() # คล้ายกับ GUI = Tk()
    HIS.geometry('750x500')

    L = Label(HIS,text='ประวัติการสั่งซื้อ', font=(None,15)).pack()

    # History
    header = ['ts-id','datetime', 'title', 'price','quantity','total']
    hwidth = [100,100,200,100,100,100]

    table_history = ttk.Treeview(HIS,columns=header, show='headings',height=15)
    table_history.pack()

    for hd,hw in zip(header,hwidth):
        table_history.column(hd,width=hw)
        table_history.heading(hd,text=hd)

    # Update from CSV
    with open('transaction.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file) # file reader
        for row in fr:
            table_history.insert('',0,value=row)

    HIS.mainloop()

GUI.bind('<F1>',HistoryWindow)

#################TAB 4 Member#####################
# วิธีที่ 1

# def ET(GUI,text,strvar,font=('Angsana New',20)):
#     T = Label(GUI,text=text,font=(None,15)).pack() #เราจะแปะใน GUI หรือแปะใน Frame ก็ได้
#     E = ttk.Entry(GUI,textvariable=strvar,font=font)
#     return E #ถ้าเราไม่ pack entry เราจะใช้วิธี return E เอา


# # วิธีที่ 2

# def ET2(GUI,text,strvar,font=('Angsana New',20)):
#     T = Label(GUI,text=text,font=(None,15))  #No pack เราจะแปะใน GUI หรือแปะใน Frame ก็ได้
#     E = ttk.Entry(GUI,textvariable=strvar,font=font)
#     return (E,T) #return ทั้ง E และ T


#xxxxxxxxx วิธีที่ 3 ทำฟังก์ชันให้สร้าง Entry พร้อมกับ label หลายๆตัวได้พร้อมกัน

def ET3(GUI,text,font=('Angsana New',20)):
    v_strvar = StringVar()
    T = Label(GUI,text=text,font=(None,15)).pack() #เราจะแปะใน GUI หรือแปะใน Frame ก็ได้
    E = ttk.Entry(GUI,textvariable=v_strvar,font=font)
    return (E,T,v_strvar) #return ทั้ง E และ T และ v_strvar

# v_fullname = StringVar()
# E41 = ET(T4,'ชื่อ-สกุล',v_fullname) #ราสร้างฟังก์ชันขึ้นมาก่อน แล้วค่อยมาสร้าง Entry ให้มันมีการ return ค่าตามที่เขียนไว้ในฟังก์ชัน เราจะได้ประหยัดโค้ด
# E41.pack()


# v_tel = StringVar()
# E42,L = ET2(T4,'เบอร์โทร',v_tel)
# L.place(x=50,y=50)
# E42.place(x=50,y=80)



F41 = Frame(T4) #สร้างเฟรมชื่อ F41 ไปแปะไว้ที่ Tab 4 มาจากคำว่า frame in tab 4,No. 1
F41.place(x=50,y=50)

v_membercode = StringVar()
v_membercode.set('M-1001')
L = Label(T4,text='รหัสสมาชิก:',font=(None,13)).place(x=50,y=20)
LCode = Label(T4,textvariable=v_membercode,font=(None,13)).place(x=150,y=20)

E41,L,v_fullname = ET3(F41,'ชื่อ-สกุล') # เอา entry ไปแปะไว้บน frame
E41.pack()

E42,L,v_tel = ET3(F41,'เบอร์โทร')
E42.pack() 

E43,L,v_usertype = ET3(F41,'ประเภทสมาชิก')
E43.pack()
v_usertype.set('general') #set คำว่า general เป็นค่า default

E44,L,v_point = ET3(F41,'คะแนนสะสม')
E44.pack()
v_point.set('0') # ใส่ค่า default ของ point

# E43.bind('<Return>', lambda x: print(v_usertype.get()))



#xxxxxxxxxxxxx เขียนฟังก์ชันให้มีการบันทึกข้อมูลลงทั้งใน CSV และตาราง xxxxxxxxxxxxx

def SaveMember():
    code = v_membercode.get() #ให้ดึง code ที่อยู่ใน v_membercode มา คือคำว่า M-1001
    fullname = v_fullname.get()
    tel = v_tel.get()
    usertype = v_usertype.get()
    point = v_point.get()
    print(fullname, tel, usertype, point)
    writetocsv([code, fullname, tel, usertype, point],'member.csv') #เรียกฟังก์ชัน writetocsv จากด้านบนมาใช้ ให้มันบันทึกข้อมูลในส่วนของ value ตั้งชื่อไฟล์ว่า member.csv
    table_member.insert('',0,value=[code, fullname, tel, usertype, point]) #ให้มันอัพเดทตารางให้ด้วย
    UpdateTable_Member()

    # เพื่อทำให้หลังกดปุ่ม save มันจะเคลียร์ค่าในช่องกรอกให้ว่างและ set เป็นแบบ default
    v_fullname.set('') #เคลียร์ช่องกรอกให้เป็นช่องว่าง
    v_tel.set('') #เคลียร์ช่องกรอกให้เป็นช่องว่าง
    v_usertype.set('general') #เคลียร์ช่องกรอกให้มีค่าเริ่มต้นเป็นคำว่า general
    v_point.set('0') #เคลียร์ช่องกรอกให้มีค่าเริ่มต้นเป็นคำว่า 0


BSave = ttk.Button(F41,text='บันทึก',command=SaveMember)
BSave.pack()


#xxxxxxxxxxxx เขียนฟังก์ชันให้มีการกดแก้ไขข้อมูลได้ xxxxxxxxxxxxxxxxxxxxxxxxxxx

def EditMember(): # เมื่อมีการ double click จะปิดปุ่มบันทึก

    # ปล. data ใน allmember จะเป็นแบบนี้
    # {'M-1001': ['M-1001','Harry potter','0830124218','general''10'], 
    #  'M-1002': ['M-1002','Ron weasly','025653342','general','20'] 
    #  'M-1003': ['M-1003','Lucius Malfoy','0897839625','general','30'] }
    

    code = v_membercode.get() #เพราะ member code ที่เป็น index 0 ไม่ต้องแก้ไข ให้เป็นแบบ fix
    allmember[code][1] = v_fullname.get() #append ค่าใส่เข้าไปใน ดิก allmemeber โดย key = รหัสสมาชิก(code)+ชื่อ-สกุล(index 1) ,value = v_fullname.get
    allmember[code][2] = v_tel.get()
    allmember[code][3] = v_usertype.get()
    allmember[code][4] = v_point.get()
    UpdateCSV(list(allmember.values()),'member.csv') #ใช้เพื่อ update csv ให้แสดงผลเฉพาะ values ของ dict ที่ชื่อ allmember เซฟลงไฟล์ชื่อ member.csv
    UpdateTable_Member() # update ข้อความใน treeview ใหม่

    BEdit.state(['disabled']) #ปิดปุ่มแก้
    BSave.state(['!disabled']) # เปิดปุ่มบันทึก
    # set default
    v_fullname.set('') #เคลียร์ช่องกรอกให้เป็นช่องว่าง
    v_tel.set('') #เคลียร์ช่องกรอกให้เป็นช่องว่าง
    v_usertype.set('general') #เคลียร์ช่องกรอกให้มีค่าเริ่มต้นเป็นคำว่า general
    v_point.set('0') #เคลียร์ช่องกรอกให้มีค่าเริ่มต้นเป็นคำว่า 0

BEdit = ttk.Button(F41,text='แก้ไข',command=EditMember)
BEdit.pack()


#xxxxxxxxxxxxx ทำปุ่มสำหรับเคลียร์ข้อมูลช่องกรอกให้ว่าง xxxxxxxxxxxxxxxxxxxxxxxx

def NewMember():
    UpdateTable_Member()
    BEdit.state(['disabled']) #ปิดปุ่มแก้
    BSave.state(['!disabled']) # เปิดปุ่มบันทึก
    # set default
    v_fullname.set('') #เคลียร์ช่องกรอกให้เป็นช่องว่าง
    v_tel.set('') #เคลียร์ช่องกรอกให้เป็นช่องว่าง
    v_usertype.set('general') #เคลียร์ช่องกรอกให้มีค่าเริ่มต้นเป็นคำว่า general
    v_point.set('0') #เคลียร์ช่องกรอกให้มีค่าเริ่มต้นเป็นคำว่า 0


BNew = ttk.Button(F41,text='New',command=NewMember)
BNew.pack()



#xxxxxxxxxxxxxx ทำตารางโชว์สมาชิก xxxxxxxxxxxxxxx
F42 = Frame(T4)
F42.place(x=500,y=100)

header = ['Code', 'ชื่อ-สกุล', 'เบอร์โทร','ประเภทสมาชิก','คะแนนสะสม'] #สร้างหัวข้อตาราง อันนี้คิดว่าน่าจะเอาไว้กำหนดจำนวนคอลัมน์ แต่ไม่ได้ใช้สำหรับแสดงผลข้อความที่เป็นตัวอักษร เช่นอันนี้มี 5 ช่อง
hwidth = [50,200,100,100,100] #สร้างลิสต์เอาไว้เพื่อกำหนดความกว้างของชอ่ง หน่วนเป็น pixel

table_member = ttk.Treeview(F42,columns=header, show='headings',height=15) #สร้างตาราง โดยใช้ำคำสั่ง Treeview เอาไปใส่ในเฟรม CF2 สั่งให้ตารางมีข้อความหัวตาราง แส่ดงหัวตาราง และมีความสูงหัวตาราง
table_member.pack() # เอาตารางไปแปะ ปล. เวลาทำตารางที่ 2 ต้องตั้งชื่อเป็น table 2

for hd,hw in zip(header,hwidth): #for loop แบบ zip คือ เราจะให้มัน for loop พร้อมกัน 2 list 
    table_member.column(hd,width=hw) #ใช้เพื่อกำหนดความกว้างของคอลัมน์ ให้ดึงข้อมูลจาก list Hwidth
    table_member.heading(hd,text=hd) #ใช้เพื่อใส่ข้อความให้หัวคอลัมน์ ให้ดึงข้อมูลจาก list header



#xxxxxxxxx Update CSV ใหม่ ให้เขียนทับหลังมีการแก้ไขข้อมูล xxxxxxxxxxxxxxxxxxxxxxxxxxx
def UpdateCSV(data, filename='data.csv'):
    # data = [[a,b],[a,b]] ดาต้าจะอยู่ในรุปแบบ list ซ้อน list
    # การเขียนไฟล์ CSV เราจะแก้แค่บางบรรทัดไม่ได้ เราจะต้องลบท้งไฟล์ทิ้งและสร้างไฟล์ใหม่ทับ และเรียกค่าที่ไม่ต้องการลบให้มาเขียนบนไหล์ใหม่อีกรอบ
    with open(filename,'w',newline='',encoding='utf-8') as file: # ต้องเป็น w แทน a เพราะ a คือการ append , w คือการ replace
        fw = csv.writer(file) # fw = file writer
        fw.writerows(data) # writerows = replace with list คำว่า writerows มี s ด้วย จะได้ไม่ซ้ำกับฟังก์ชันเขียน csv ด้านบน


#xxxxxxxxxxxxxxx Delete ข้อมูลในตารางที่เลือก xxxxxxxxxxxxxxxxxxxxx
def DeleteMember(event=None):
    select = table_member.selection() #เลือก item 
    print(select)
    if len(select)!= 0:
        data = table_member.item(select)['values'] #กำหนดให้ data คือ item ที่ select เอาแค่เฉพาะส่วน values
        print(data)
        del allmember[data[0]] # ลบ data index 0 ของ allmember ในที่นี้แทนด้วยข้อมูล 1 แถว หรือข้อมูลทั้งแถบของสมาชิก 1 คนที่จะลบ
        UpdateCSV(list(allmember.values()),'member.csv') #ใช้เพื่อ update csv ให้แสดงผลเฉพาะ values ของ dict ที่ชื่อ allmember (ดิก allmemeber หลังจากมีการ delete ข้อมูลบางแถวออกไปแล้ว) เซฟลงไฟล์ชื่อ member.csv 
        # คำว่า list ที่ใส่ด้านหน้า เพื่อให้มันแสดงผลเฉพาะส่วน values ของดิก นาทีที่ 3.09.53
        UpdateTable_Member() # update ข้อความใน treeview ใหม่
    else:
        messagebox.showwarning('ไม่ได้เลือกรายการ','กรุณาเลือกรายการก่อนลบข้อมูล')
table_member.bind('<Delete>',DeleteMember) #ถ้าเราเลือก item และกดปุ่ม Delete 
# ปล. ถ้ามีการ .bind ต้องใส่ event เสมอ แต่ถ้ามีการกดปุ่มต้องใส่ event = none



#xxxxxxxxxxxxx Update ข้อมูลสมาชิกโดยการดับเบิ้ลคลิก xxxxxxxxxxxxxxxxxxxxxxxxxxx
def UpdateMemberInfo(event=None):

    select = table_member.selection() #เลือก item หรือบรรทัดที่ต้องการ
    code = table_member.item(select)['values'][0] #เอาแค่ values index 0 ก็คือข้อมูลสามชิก 1 แถว
    print(allmember[code])
    memberinfo = allmember[code]

    # เป็นการดึงเอาข้อมูลในบรรทัดที่ถูกเลือก กลับไปแสดงค่าบนช่องกรอก (Entry) ใหม่อีกครั้งนึง เพื่อให้เรากลับไปแก้ไขในช่องกรอกได้ โดยเราต้องเลือกชุดข้อมูลใน index ให้ตรงกับช่องที่เราจะเอาไปแปะคืน
    v_membercode.set(memberinfo[0])
    v_fullname.set(memberinfo[1]) #ถูกset ให้แสดงค่าใน index ที่ 1 ของ allmember ซึ่งก็คือ ชื่อ-สกุล เอาไปแปะไว้ตรงช่อง entry ชื่อ-สกุล เพื่อให้เราไปลบค่าได้
    v_tel.set(memberinfo[2])
    v_usertype.set(memberinfo[3])
    v_point.set(memberinfo[4])

    BEdit.state(['!disabled']) # เปิดปุ่มแก้
    BSave.state(['disabled']) # ปิดปุ่มบันทึก

table_member.bind('<Double-1>',UpdateMemberInfo) # เขียนคำสั่งให้ถ้ากด double click ให้เรียกฟังก์ชัน UpdateMemberInfo ขึ้นมาเพื่อแก้ไขข้อมูลสมาชิก



#xxxxxxxxxxxxxx Update Table xxxxxxxxxxxxxxxxxxx

last_member = '' # รอประกาศตัวแปรว่า last_member คืออะไรด้านล่าง ซึ่งมันจะเปลี่ยนตามข้อความ index 0 ของ row
allmember = {} # สร้าง dict เปล่าขึ้นมาเพื่อใส่ค่าไปเก็บไว้ในดิกอันนี้เพื่อให้อ่างอิงได้ ข้อมูลที่เก็บอยู่ใน allmember จะดึงมาจาก CSV ถ้ามีบันทึกสมาชิก 5 คน ก็จะมี 5 แถว หรือ 5 ชุดข้อมูล

def UpdateTable_Member():
    global last_member # ใส่ global เพราะเราอ้างอิง all member ที่อยู่นอกฟังก์ชัน
    with open('member.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file) # file reader
        table_member.delete(*table_member.get_children()) #ต้องมีการเคลีย์ข้อมูลในตารางก่อนถึงจะ insert ใหม่ได้
        for row in fr:
            table_member.insert('',0,value=row)
            code = row[0] # ดึงรหัสมา ตัว code แทนค่า index 0 ใน row (จาก value ของบรรทัด table_member.insert) คือ M-1001 นาทีที่ 2.45.48 อันนี้ดึงขึ้นมาเพื่อจะเอามาตั้งชื่อเป็น key ในดิก allmember
            allmember[code] = row # add values ใส่ในดิก allmember ของ key ชื่อ code (ซึ่งจากบรรทัดบน มันก็คือคำว่า M-1001 เอามาตั้งเป็นคีย์นั่นเอง) ส่วน value ก็คือ row ก็คือข้อมูลทั้งแถบที่เรา add ลงตาราง 
            # 2 บรรทัดบน เป็นการเพ่ิมค่าลงไปในดิก โดยวิธี append

    print('Last ROW:',row) #ทดลองปรินท์ข้อมูลแถวล่าสุดในตาราง last row บอก position row คือข้อมูลที่จะปรินท์ มาจากบรรทัด table_member.insert
    last_member = row[0] #แทนข้อมูล index 0 ของ row (row แบบบรรทัดล่าสุดด้วยนะ) เป็นการประกาศตัวแปรว่าให้ last_member แทนข้อความของ row ในตำแหน่ง index 0 ในที่นี้คือคำว่า M-1001
    # M-1001
    # ['M',1001+1] ราจะทำระบบให้มันรันเลขแบบบวกเพิ่ม 1 อัตโนมัต ต้องแยกออกเป็น M ที่เป็น string กบ 1001 ที่เป้น int ออกจากกัน
    next_member = int(last_member.split('-')[1]) + 1 # ตัวลำดับถัดไป จะต้องใช้คำส่ัง split M-1001 ออกเป็น string กับ int โดยใช้ '-' เป็นตัวแบ่ง และแปลง index ที่ 1 เป็น int (คือคำว่า 1001) และให้บวกเพิ่มอีก 1
    v_membercode.set('M-{}'.format(next_member)) # ให้แสดงผลตามเทมเพลทโดยใช้คำสั่ง .format
    print(allmember)


# POP UP Menu
member_rcmenu = Menu(GUI, tearoff=0) # rcmenu = rigth cliick menu
member_rcmenu.add_command(label='Delete',command=DeleteMember)
member_rcmenu.add_command(label='Update',command=UpdateMemberInfo)

# วิธีที่ 1 ใช้แบบแลมดา
table_member.bind('<Button-3>',lambda event: member_rcmenu.post(event.x_root, event.y_root)) #.bind คือการพ่วงกับปุ่มกดด ใช้การคลิกขวาจะมีการเรียก event ขึ้นมา ซึ่งจะแสดงตามแกน x y เป้น event ของการ bind ปุ่ม ซึ่งต้องไปแก้ def ข้างบนให้ event=None ด้วย ไม่งั้นมันเรียก event ชนกัน จะ error

# วิธีที่ 2 แบบเขียนฟังก์ชัน

def SearchName():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.google.com/search?q={}'.format(name)
    webbrowser.open(url)
member_rcmenu.add_command(label='Search Name',command=SearchName)



def SearcBBC():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.bbc.co.uk/search?q={}'.format(name)
    webbrowser.open(url)
member_rcmenu.add_command(label='Search BBC',command=SearchName)






BEdit.state(['disabled'])
UpdateTable_Member()
GUI.mainloop()
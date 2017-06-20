from tkinter import font
from tkinter import *
import urllib.request
import urllib
from PIL import Image,ImageTk
from io import BytesIO
import tkinter.messagebox
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

key = 'ivgVuV9%2BpIPYl3Gq%2F%2FsGzij9zmnKb3%2BAjlFJ%2BE61piuUo%2FgfsdUCHc7dZaUMFwIfwbXy%2FqpMYMj2VSxM7RSD8Q%3D%3D'
window = Tk()
window.geometry("720x650")
window.title("Performance Search")


def Search_date(): #기간별로 검색하는 기능
    global key

    time1 = '2017'+ Month1.get(ACTIVE) + Day1.get(ACTIVE)
    time2 = '2017'+ Month2.get(ACTIVE) + Day2.get(ACTIVE)

    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/period?'
    new_url = url + 'from=' + time1 + '&to=' + time2 + '&cPage=1&rows=50&gpsxfrom=&gpsyfrom=&gpsxto=&gpsyto=&keyword=&sortStdr='+sortStdr + '&serviceKey=' + key

    data=urllib.request.urlopen(new_url).read()
    d=str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("perforList")  # return list type
    #print(itemElements)
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realmName = perforList.find("realmName").text
        seq = perforList.find("seq").text
        area = perforList.find("area").text

        RenderText.insert(INSERT, "=========================================\n")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, title)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "장르 : ")
        RenderText.insert(INSERT, realmName)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "지역 : ")
        RenderText.insert(INSERT, area)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "시작일 : ")
        RenderText.insert(INSERT, startDate)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "마감일 : ")
        RenderText.insert(INSERT, endDate)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "일련번호: ")
        RenderText.insert(INSERT, seq)
        RenderText.insert(INSERT, '\n')


def Search_Area(): #지역별로 검색하는 기능
    global key

    sido = str(e3.get())
    hangul_sido = urllib.parse.quote(sido)
    gugun = str(e4.get())
    hangul_gugun = urllib.parse.quote(gugun)
    #startdate = '2017'+ Month1.get(ACTIVE) + Day1.get(ACTIVE)
    #enddate = '2017'+ Month2.get(ACTIVE) + Day2.get(ACTIVE)

    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area?'
    new_url = url + 'sido=' + hangul_sido + '&gugun=' + hangul_gugun + '&from=20170101&to=20171231&cPage=1&rows=50&gpsxfrom=&gpsyfrom=&gpsxto=&gpsyto=&keyword=&sortStdr='+ sortStdr + '&serviceKey=' + key

    data=urllib.request.urlopen(new_url).read()
    d=str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)
    #print(d)

    itemElements = tree.getiterator("perforList")  # return list type
    print(itemElements)
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realmName = perforList.find("realmName").text
        seq = perforList.find("seq").text
        area = perforList.find("area").text

        RenderText.insert(INSERT, "=========================================\n")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, title)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "장르 : ")
        RenderText.insert(INSERT, realmName)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "지역 : ")
        RenderText.insert(INSERT, area)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "시작일 : ")
        RenderText.insert(INSERT, startDate)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "마감일 : ")
        RenderText.insert(INSERT, endDate)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "일련번호: ")
        RenderText.insert(INSERT, seq)
        RenderText.insert(INSERT, '\n')


def Search_specific_data(): #상세정보 검색
    global key

    seq_num = str(e5.get())
    url = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/d/?'
    new_url = url + "seq=" + seq_num +"&serviceKey=" + key

    data = urllib.request.urlopen(new_url).read()
    d = str(data.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(d)

    itemElements = tree.getiterator("perforInfo")
    for perforList in itemElements:
        title = perforList.find("title").text
        startDate = perforList.find("startDate").text
        endDate = perforList.find("endDate").text
        place = perforList.find("place").text
        realmName = perforList.find("realmName").text
        price = perforList.find("price").text
        content = perforList.find("contents1").text
        buying_url = perforList.find("url").text
        phone = perforList.find("phone").text
        image = perforList.find("imgUrl").text

        image_url = image
        with urllib.request.urlopen(image_url) as u:
            raw_data = u.read()

        im = Image.open(BytesIO(raw_data))
        post_image = ImageTk.PhotoImage(im)

        poster.configure(image=post_image)
        poster.image = post_image



        SpecificData.insert(INSERT, "제목 : ")
        SpecificData.insert(INSERT, title)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "장르 : ")
        SpecificData.insert(INSERT, realmName)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "시작일 : ")
        SpecificData.insert(INSERT, startDate)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "마감일 : ")
        SpecificData.insert(INSERT, endDate)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "장소 : ")
        SpecificData.insert(INSERT, place)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "금액: ")
        SpecificData.insert(INSERT, price)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "구매 주소: ")
        SpecificData.insert(INSERT, buying_url)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "연락처: ")
        SpecificData.insert(INSERT, phone)
        SpecificData.insert(INSERT, '\n')
        SpecificData.insert(INSERT, "상세 정보: ")
        SpecificData.insert(INSERT, content)
        SpecificData.insert(INSERT, '\n')


def Send_mail():
    host = "smtp.gmail.com"
    port = "587"
    msgtext = SpecificData.get(0.0,END)

    senderAddr = put_from_email.get()
    recipientAddr = put_to_email.get()
    password = put_password.get()

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "공연/전시정보"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    msgPart = MIMEText(msgtext, 'plain')
    msg.attach(msgPart)

    s = mysmtplib.MySMTP(host, port)

    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, password)
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

def SearchButtonAction():
    RenderText.configure(state ='normal')
    RenderText.delete(0.0, END)
    Search_date()
    RenderText.configure(state='disabled')

def SearchButtonAction2():
    RenderText.configure(state ='normal')
    RenderText.delete(0.0, END)
    Search_Area()
    RenderText.configure(state='disabled')

def SearchButtonAction3():
    SpecificData.configure(state ='normal')
    SpecificData.delete(0.0, END)
    Search_specific_data()
    SpecificData.configure(state='disabled')

myfont = font.Font(window, size=25, weight = 'normal', family = 'Times')
Main = Label(window, fg = 'orange',font = myfont, text = '*공연/전시 검색 서비스*')
Main.pack()
Main.place(x=50, y=10)

b1 = Button(window, text = 'Search', command=SearchButtonAction)
b1.pack()
b1.place(x=400, y=55)

b2 = Button(window, text = 'Search', command=SearchButtonAction2)
b2.pack()
b2.place(x=400, y=95)

b3 = Button(window, text = 'Search', command=SearchButtonAction3)
b3.pack()
b3.place(x=115, y=135)

b4 = Button(window, text = 'Send!', command=Send_mail)
b4.pack()
b4.place(x=210, y=620)

l1 = Label(window, text = '언제부터')
l2 = Label(window, text = '언제까지')
l3 = Label(window, text = '시/도')
l4 = Label(window, text = '군/구')
l5 = Label(window, text = '일련번호')
l6 = Label(window, text = "e-mail")
l7 = Label(window, text = 'password')
l8 = Label(window, text = "to")
l9 = Label(window, text = '월')
l10 = Label(window, text = '일')
l11 = Label(window, text = '월')
l12 = Label(window, text = '일')

l1.place(x=0, y=60)
l2.place(x=200, y=60)
l3.place(x=0, y=100)
l4.place(x=200, y=100)
l5.place(x=0, y=140)
l6.place(x=0,y=590)
l7.place(x=0,y=620)
l8.place(x=220,y=590)
l9.place(x=90,y=60)
l10.place(x=165,y=60)
l11.place(x=290,y=60)
l12.place(x=365,y=60)

e3 = Entry(window)
e4 = Entry(window)
e5 = Entry(window,width=8)
put_from_email = Entry(window)
put_to_email = Entry(window)
put_password = Entry(window)


e3.place(x=50, y=100)
e4.place(x=250, y=100)
e5.place(x=50, y=140)
put_from_email.place(x=60,y=590)
put_to_email.place(x=250,y=590)
put_password.place(x=60,y=620)

def sel(): #정렬기능 설정
    global sortStdr
    sortStdr = str(sorted.get())

sorted = IntVar()

sort1 = Radiobutton(window,text='등록일순',variable= sorted,value=1,command=sel)
sort1.pack()
sort1.place(x=170,y=135)

sort2 = Radiobutton(window,text='공연명순',variable= sorted,value=2,command=sel)
sort2.pack()
sort2.place(x=250,y=135)

sort3 = Radiobutton(window,text='지역명순',variable= sorted,value=3,command=sel)
sort3.pack()
sort3.place(x=330,y=135)


def Month_and_Day_Select(): #기간설정하는 리스트박스와 스크롤바
    global Month1, Month2, Day1, Day2

    font1 = font.Font(size=12, weight='bold')
    Month1scroll = Scrollbar(window)
    Month1scroll.pack()
    Month1scroll.place(x=75, y=45)
    Month1 = Listbox(window, width=2, height=1, borderwidth=5, font=font1, yscrollcommand=Month1scroll.set)
    for i in range(1, 13, 1):
        if i<10:
            Month1.insert(i, '0'+str(i))
        else:
            Month1.insert(i,str(i))
    Month1.pack()
    Month1.place(x=50, y=55)
    Month1scroll.config(command=Month1.yview)

    Day1scroll = Scrollbar(window)
    Day1scroll.pack()
    Day1scroll.place(x=150, y=45)
    Day1 = Listbox(window, width=2, height=1, borderwidth=5, font=font1, yscrollcommand=Day1scroll.set)
    for i in range(1, 32, 1):
        if i < 10:
            Day1.insert(i,'0'+str(i))
        else:
            Day1.insert(i, str(i))
    Day1.pack()
    Day1.place(x=120, y=55)
    Day1scroll.config(command=Day1.yview)

    Month2scroll = Scrollbar(window)
    Month2scroll.pack()
    Month2scroll.place(x=275, y=45)
    Month2 = Listbox(window, width=2, height=1, borderwidth=5, font=font1, yscrollcommand=Month2scroll.set)
    for i in range(1, 13, 1):
        if i<10:
            Month2.insert(i, '0'+str(i))
        else:
            Month2.insert(i,str(i))
    Month2.pack()
    Month2.place(x=250, y=55)
    Month2scroll.config(command=Month2.yview)

    Day2scroll = Scrollbar(window)
    Day2scroll.pack()
    Day2scroll.place(x=350, y=45)
    Day2 = Listbox(window, width=2, height=1, borderwidth=5, font=font1, yscrollcommand=Day2scroll.set)
    for i in range(1, 32, 1):
        if i < 10:
            Day2.insert(i,'0'+str(i))
        else:
            Day2.insert(i, str(i))
    Day2.pack()
    Day2.place(x=325, y=55)
    Day2scroll.config(command=Day2.yview)

Month_and_Day_Select()

poster = Label(window, image=None, height=300, width=200)
poster.pack()
poster.place(x=450, y=10)

RenderTextScrollbar = Scrollbar(window)

RenderText = Text(window, width=52, height=30, borderwidth=10, relief='raised', yscrollcommand=RenderTextScrollbar.set)
RenderText.pack()
RenderText.place(x=10, y=170)
RenderTextScrollbar.config(command=RenderText.yview)
RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)

RenderText.configure(state='disabled')

SpecificData = Text(window, width=35, height=20, borderwidth=12, relief='raised')
SpecificData.pack()
SpecificData.place(x=415, y=300)

SpecificData.configure(state='disabled')

window.mainloop()

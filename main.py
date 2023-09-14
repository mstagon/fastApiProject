from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# from tkinter import *
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from PIL import ImageTk, Image
# import option
# import tkinter.ttk
# from tkinter import messagebox
#
#
# id = option.a
# dictionary = {}
# logincheck = ""
# atlogin = option.autologin
#
# w = Tk()
# w.geometry('850x500')
# w.iconbitmap('icon.ico')
# w.title('[S M U] e-campus 진도율 체크')
# w.resizable(False, False)
# s = requests.Session()
# l = ('티머니 둥근바람 ExtraBold', 13)
#
# th = tkinter.ttk.Style()
# th.configure('Treeview', rowheight=30)
#
# f2= Frame(w, width=500, height=500, bg="#fff3b4").place(x=350, y=0)
# f = Frame(w, width=350, height=500, bg="#263A77" ).place(x=0, y=0)
# Frame(w, width=250, height=400, bg='white').place(x=50, y=50)
#
# l1 = Label(w, text='Class_number', bg='white')
# l1.config(font=l)
# l1.place(x=80, y=180)
#
# l2 = Label(w, text='Password', bg='white')
# l2.config(font=l)
# l2.place(x=80, y=260)
#
# e1 = Entry(w, width=18, border=0)
# e1.config(font=l)
# e1.place(x=80, y=220)
#
# e2 = Entry(w, width=18, border=0, show='*')
# e2.config(font=l)
# e2.place(x=80, y=300)
#
# Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
# Frame(w, width=180, height=2, bg='#141414').place(x=80, y=252)
#
# imagea = Image.open("log.png")
# imageb = ImageTk.PhotoImage(imagea)
# l3 = Label(w, image=imageb,
#                border=0,
#                justify=CENTER)
# l3.place(x=115, y=100)
#
# def crawl(event):
#     if logincheck == "ok":
#         if event.widget.get() != "과목 선택":
#             curl = "https://ecampus.smu.ac.kr/report/ubcompletion/user_progress.php?id="+dictionary.get(event.widget.get())
#             req = s.get(curl)
#             soup = BeautifulSoup(req.text, 'html.parser')
#             table = soup.find('table', {'class': 'table table-bordered user_progress'})
#             df = pd.read_html(str(table))
#             dataframe = df[0].dropna()
#             dataframe = dataframe[['주','강의 자료', '진도율']]
#             tree1 = tkinter.ttk.Treeview(w, show='headings')
#             tree1.place(x=385,y=100)
#             tree1['columns'] = dataframe.columns.values.tolist()
#             tree1.column("# 1", anchor="center",minwidth=50, width=50, stretch=0)
#             tree1.heading("# 1", anchor="center",text="주차")
#             tree1.column("# 2", anchor="center",minwidth=300, width=300, stretch=0)
#             tree1.heading("# 2", anchor="center",text="강의 내용")
#             tree1.column("# 3", anchor="center",minwidth=70, width=70, stretch=0)
#             tree1.heading("# 3", anchor="center",text="진도율")
#             for index, row in dataframe.iterrows():
#                 tree1.insert("", 'end', text=index, values=list(row))
#
#     else:
#         messagebox.showinfo("error", "로그인을 해주세요.")
#
# def login():
#     global logincheck
#     global dictionary
#     snl = []
#     url = "https://ecampus.smu.ac.kr/login/index.php"
#     log = {
#         'username': option.cn,
#         'password': option.pw
#     }
#     log1 = {
#         'username': e1.get(),
#         'password': e2.get()
#     }
#     if atlogin == 0:
#         req = s.post(url, data=log1)
#     else:
#         req = s.post(url, data=log)
#     lurl = "https://ecampus.smu.ac.kr/" #로그인에 성공했다면 해당 사이트의 내용을 가져올 수 있음
#     res = s.get(lurl)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     username = soup.find('li', {'class': 'user_department hidden-xs'})
#     if username:
#         name = username.text
#         l4 = Label(w, text ="사용자명 : "+name+"            로그인 성공!", fg='white', border=0, bg="#263A77", font=('티머니 둥근바람 ExtraBold', 11),)
#         l4.place(x=50, y=452)
#         logincheck = "ok"
#     else:
#         logincheck = "error"
#         messagebox.showinfo("로그인 실패", "학번과 비밀번호를 확인해주세요.")
#     if id == '':
#         messagebox.showinfo("Error", "option.py의 필수설정을 확인해주세요")
#     else :
#         for i in range(0,len(id)):
#             gcurl = "https://ecampus.smu.ac.kr/course/view.php?id="+id[i]
#             getc = s.get(gcurl)
#             soup = BeautifulSoup(getc.text, 'html.parser')
#             cb = soup.find('a', {'href': gcurl})
#             sn = cb.text
#             snl.append(sn)
#     dictionary = dict(zip(snl, id))
#     combobox = tkinter.ttk.Combobox(w, width=50, values=list(snl))
#     combobox['state'] = 'readonly'
#     combobox.place(x=415, y=50)
#     combobox.bind("<<ComboboxSelected>>", crawl)
#     combobox.set("과목 선택")
#
#
#
#
#
#
# if atlogin == 1:
#     login()
#
#
#
# b1 = Button(w, text="L O G I N", width=20, height=3, fg='white', border=0, bg="#994422", activeforeground='white', activebackground="#994422", command=login)
# b1.config(font=('티머니 둥근바람 ExtraBold', 8))
# b1.place(x=100, y=365)
# l5 = Label(w, text =" ver 0.1.0 made by cms ", fg='black', border=0, bg="#fff3b4", font=('티머니 둥근바람 ExtraBold', 9),)
# l5.place(x=710, y=480)
#
# w.mainloop()
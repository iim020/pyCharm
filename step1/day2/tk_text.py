from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        text.delete(1.0, END)
        with open(filepath, 'r', encoding='utf-8') as f:
            text.insert(INSERT, f.read())

app = Tk()

# 스크롤 생성
scrollbar = Scrollbar(app)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(app, wrap=NONE)
text.pack()

# 스크롤바와 텍스트 위젯 연결
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

btn = Button(app, text='Open File', command=open_file)
btn.pack()

app.mainloop()

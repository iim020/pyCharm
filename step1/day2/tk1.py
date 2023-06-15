import tkinter
from tkinter import messagebox
import random

app = tkinter.Tk()

def make_lotto(num):
    result = []
    # num의 수 만큼 lotto 번호를 생성하여 리턴하는 함수
    for i in range(num):
        lotto_num = set()
        while len(lotto_num) < 6:  # 수정: make_lotto() -> lotto_num
            com = random.randint(1, 45)  # 1~45 랜덤값
            lotto_num.add(com)
        result.append(list(lotto_num))  # 수정: list(com) -> list(lotto_num)
    return result

def btn_click():
    nm = txt.get()
    lotto_num = make_lotto(int(nm))
    messagebox.showinfo('이름:', lotto_num)

txt = tkinter.Entry(app)
txt.grid(row=0, column=1)

lab = tkinter.Label(app, text="수량: ")
lab.grid(row=0, column=0)

btn = tkinter.Button(app, text="OK", command=btn_click)
btn.grid(row=1, column=1)

app.mainloop()
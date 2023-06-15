from tkinter import *
from bs4 import BeautifulSoup
from urllib import request
import requests


def save_images(url_entry, text):
    url = url_entry.get()
    print('img 저장', url)

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # 이미지 태그만 가져오기
    import os
    from urllib import request

    img_dir = "/images"
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)

    img_all = soup.find_all('img')
    arr = []
    for i, v in enumerate(img_all):
        if v.get('src'):
            img_url = v.get('src')
            request.urlretrieve(img_url, f"{img_dir}/{i}.png")
            arr.append(img_url)

    text.delete(1.0, END)
    text.insert(END, f"URL: {url}\n")
    text.insert(END, "Images saved.\n")
    for i, img_url in enumerate(arr):
        text.insert(END, f"Image {i + 1}: {img_url}\n")


app = Tk()
url_entry = Entry(app, width=100)
url_entry.pack()
save_btn = Button(app, text='Save Images', command=lambda: save_images(url_entry, text))
save_btn.pack()
text = Text(app, width=100, height=50)
text.pack()
app.mainloop()

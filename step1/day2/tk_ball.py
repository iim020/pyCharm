from tkinter import *
from PIL import Image, ImageTk

def create_ball(canvas):
    global ho_img
    img = Image.open('f.png')
    img = img.resize((50, 50), Image.ANTIALIAS)
    ho_img = ImageTk.PhotoImage(img)
    canvas.create_image(100, 250, image=ho_img, tag='redBall')

def move_left(event):
    canvas.move('redBall', -deltax, 0)
    canvas.after(20, canvas.update)

def move_right(event):
    canvas.move('redBall', deltax, 0)
    canvas.after(20, canvas.update)

def move_up(event):
    canvas.move('redBall', 0, -deltay)
    canvas.after(20, canvas.update)

def move_down(event):
    canvas.move('redBall', 0, deltay)
    canvas.after(20, canvas.update)

def jump(event):
    jump_height = 100  # 점프 높이 조절
    jump_duration = 500  # 점프 시간 조절
    jump_speed = jump_height / jump_duration  # 점프 속도 계산

    gravity = 0.5  # 중력 가속도 설정
    vertical_speed = jump_speed

    ground_y = 250  # 바닥의 y 좌표 설정

    def perform_jump():
        nonlocal vertical_speed
        nonlocal jump_height

        # 바닥에 도달하면 점프 동작 종료
        if canvas.coords('redBall')[1] >= ground_y:
            return

        canvas.move('redBall', 0, -vertical_speed)  # 점프하는 높이 조절
        vertical_speed -= gravity  # 중력 적용
        jump_height -= vertical_speed
        if jump_height > 0:
            canvas.after(20, perform_jump)
        else:
            canvas.move('redBall', 0, jump_height + vertical_speed)  # 정확한 위치 조정

    perform_jump()

deltax = 5
deltay = 5

app = Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack()
create_ball(canvas)
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)
canvas.bind('<space>', jump)  # 스페이스바로 점프
canvas.focus_set()

app.mainloop()

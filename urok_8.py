from tkinter import *


def place_image():
    height = window.winfo_screenheight()
    width = window.winfo_screenwidth()
    window.geometry(f'{width}x{height}')
    label_ph_h.place(x=0, y=0, width=width, height=height)


def on_close():
    if int(count_text['text']) > 0:
        count_text['text'] = int(count_text['text']) - 1
        count_text.place(x=250, y=25, width=400, height=100)
        window.after(1000, on_close)
    else:
        place_image()


window = Tk()
window.geometry('900x300')
window.title('Опасность')
window.config(bg='black')
window.resizable(width=False, height=False)

text = Label(text='Ваш компьютер заражен!!!!', fg='green', bg='black', font=('Courier New', 34))
text.place(x=100, y=100, width=700, height=100)

window.protocol('WM_DELETE_WINDOW', on_close)

count_text = Label(text='6', fg='green', bg='black', font=('Courier New', 40))
photo_h = PhotoImage(file='happy.png')
label_ph_h = Label(image=photo_h)

# window.attributes('-fullscreen', True, '-topmost', True)

window.mainloop()
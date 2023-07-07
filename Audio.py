import moviepy.editor as me
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

filename=''

def convert():
        global filename
        filetypes=(("Audio files","*.mp3 , *.waw , *.ogg"),("All files","*.*"))
        video=me.VideoFileClip(filename)
        audio=video.audio
        file=asksaveasfilename(filetypes=filetypes)
        audio.write_audiofile(f'{file}{format.get()}')
        label5=Label(root,text="تبدیل شد!!!",font=("Arial",18),fg="green")
        label5.config(bg="#ffe9ab")
        label5.pack()
        label5.place(x=450,y=300)
        
def select():
    global filename
    filetypes = (
        ('video files', '*.WEBM , *.MPG, *.MP2 , *.MPEG , *.MPE , *.MPV , *.MP4 , *.M4P , *.M4V , *.AVI , *.WMV , *.MOV , *.QT , *.FLV , *.SWF , *.AVCHD'),
        ('All files', '*.*')
    )
    filename=askopenfilename(filetypes=filetypes)
    label3.config(text="ویدیو انتخاب شد.",fg="green")
    label3.config(bg="#ffe9ab")
    label4=Label(root,text="فرمت خروجی:",font=("Arial",18))
    label4.config(bg="#ffe9ab")
    label4.pack()
    label4.place(x=125,y=250)
    options=[".mp3",".ogg",".wav"]
    format.set(".mp3")
    menu=OptionMenu(root,format,*options)
    menu.pack()
    menu.place(x=375,y=250)
    button3=Button(root,text="تبدیل",bg='light blue',font=("Harlow Solid",12),command=convert,width=10,height=1)
    button3.pack()
    button3.place(x=250,y=300)

root=Tk()
root.configure(bg='#ffe9ab') 
root.geometry("700x450")
root.minsize(600,350)
root.maxsize(600,350)
root.title("Video to Audio Converter")
label1=Label(root,text="تبدیل ویدیو به صدا",font=("Arial",32))
label1.config(bg="#ffe9ab")
label1.pack()
label2=Label(root,text="فایل ویدیویی را انتخاب کنید",font=("Arial",18))
label2.config(bg="#ffe9ab")
label2.pack()
label2.place(x=190,y=100)
button1=Button(root,text="انتخاب فایل",bg='light blue',font=("Harlow Solid",12),command=select,width=10,height=1)
button1.pack()
button1.place(x=250,y=200)
label3=Label(root,font=("Footlight MT",18,"bold"))
label3.pack()
label3.place(x=225,y=150)
format=StringVar()
root.mainloop()
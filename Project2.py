from tkinter import*
from tkinter import ttk,messagebox
import googletrans
import textblob
import pytesseract as tess
from PIL import Image

def extaract():
    path=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    tess.pytesseract.tesseract_cmd=path
    img=Image.open("C:\\Users\\palak\\AppData\\Local\\Programs\\Python\\Python310\\ca\\6.jpg")
    text1=tess.image_to_string(img)
    return (text1)

root=Tk()
text1=Text()
root.title("Translator")
root.geometry("1080x400")

def label_change():
    c1=combo2.get()
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    global language
    try:
        text_=text1.get(1.0,END)
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
          messagebox.showerror("googletrans","please try again")
                    

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

label1=Label(root,text="Extracted text",font="seoge 30 bold",bg="white",width=18,bd=3,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)
text1.insert(INSERT,extaract())
text1.pack()

combo2=ttk.Combobox(root,values=languageV,font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("Select Language")

label2=Label(root,text="English",font="seoge 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="Black",bd=5)
f1.place(x=610,y=118,width=440,height=210)

text2=Text(f1,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)


scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button
translate=Button(root,text="Translate",font="Roboto 15 bold",activebackground="blue",cursor="hand2",bd=5,bg='red',fg="white",command=translate_now)
translate.place(x=480,y=250)

label_change()


root.configure(bg="white")
root.mainloop()

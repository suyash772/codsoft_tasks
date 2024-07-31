from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabet= string.ascii_lowercase
    capital_alphabet= string.ascii_uppercase
    numbers= string.digits
    special_chars= string.punctuation

    all= small_alphabet+capital_alphabet+numbers+special_chars
    password_lenght=int(lenght_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabet,password_lenght))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabet+capital_alphabet,password_lenght))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_lenght))

    # password =random.sample(all,password_lenght)
    # passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

codsoft= Tk()

codsoft.configure(background='#da9100')

img= PhotoImage(file=r'C:\Users\a2z\Downloads\reset-password.png')
codsoft.iconphoto(False, img)

codsoft.title('Password Generator')


choice=IntVar()
Font=('Georgia',16,'bold')

passwordLabel = Label(codsoft, text='Password generator', font=('Southing', 20,"bold"),background='sky blue')
passwordLabel.grid(pady=20)

weakradioButton=Radiobutton(codsoft,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(codsoft,text='medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(codsoft,text='strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lenghtLabel=Label(codsoft, text=' Password Length', font=Font,bg='sky blue')
lenghtLabel.grid(pady=10)

lenght_Box= Spinbox(codsoft, from_=5, to=20, width=5, font=Font)
lenght_Box.grid(pady=5)

generateButton =Button(codsoft, text='Generate', font=Font,command=generator)
generateButton.grid(pady=5)

passwordField = Entry(codsoft, width=30,bd=2, font=('Georgia',10,'bold'))
passwordField.grid(pady=5)

copyButton =Button(codsoft, text='Copy', font=Font,command=copy)
copyButton.grid(pady=5)


codsoft.mainloop()
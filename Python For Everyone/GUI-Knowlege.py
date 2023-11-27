from tkinter import * # import all function inside main package
from tkinter import ttk

GUI = Tk()
GUI.title('memorize program by POONPHUBEJ')
GUI.geometry('500*500')

L1 = ttk.Label(GUI,text='Knowledge topics',font=('High Tower',18))
L1.pack()

E1 = ttk.Entry(GUI,font=('High Tower',20),width=50)
E1.pack()

L2 = ttk.Label(GUI,text='Detals',font=('High Tower',18))
L1.pack()

T1 = ttk.Entry(GUI,font=('High Tower',18),height=8,width=56)
T1.pack()

B1 = ttk.Button(GUI,text='record')
B1.pack(pady=10,ipadx=20,ipady=10)

GUI.mainloop()
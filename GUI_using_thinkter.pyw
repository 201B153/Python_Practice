
from tkinter import*
root=Tk()
root.title('myfirstGUI')
root.geometry('300x300')
Label(root,text="Enter your age").grid(row=0,column=0)
def fun():
      age=e1.get()
      if int(age)>=18:
          msg='adult'
      else:
          msg='minor'
      my_label=Label(root,text="you are "+msg)
      my_label.grid(row=1,column=1)
    
e1=Entry(root)
e1.grid(row=0,column=1)
b1=Button(root,text="Check",command=fun)
b1.grid(row=1,column=0)
#add font size color image only gif allowed add image for a button check how to scroll for tkinter
#associate any button to check status button

root.mainloop()

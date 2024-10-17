from tkinter import *

root = Tk()
label1 = Label(root, text="Hello, World!")
label1.pack(side=TOP)
button1 = Button(root, text="Click Here!")
button1.pack(side=TOP)
slider1 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider1.pack(side=TOP)
entry1 = Entry(root)
entry1.pack(side=TOP)
frame1 = Frame(root)
frame1.pack(side=TOP)

label2 = Label(frame1, text="x =")
label2.pack(side=LEFT)
entry2 = Entry(frame1)
entry2.insert(0, 100)
entry2.pack(side=LEFT)

root.mainloop()
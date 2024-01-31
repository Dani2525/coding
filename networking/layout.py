from tkinter import *

root = Tk() # create a root window 
# input field which accepts message and text box to display the messages

entry = Entry()
entry.pack(side=BOTTOM)

listbox= Listbox(root)
listbox.pack()
button = Button(root,text="Send")
button.pack(side=BOTTOM) #button on the side


root.mainloop()
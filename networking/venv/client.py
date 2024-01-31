import socket

from tkinter import *

def send(listbox,entry):
    message = entry.get() #accept the message fornm the entry and gets it 
    listbox.insert('end',"Client: "+message)# display the message in the listbox towards the end 
    entry.delete(0,END) # Deletes the message after it is send in the message box
    s.send(bytes(message,"utf-8")) #using the same socket to send the message and encoded
    recieve(listbox) # calling it here so the recieve is instant 

def recieve(listbox);
    message = s.rec(50) #saves message into message variable with buffer size of 50 
    listbox.insert('end',"Server"+message.decode('utf-8')) #message recieved from the server and displayed when you click te recieve button and cant run a loop as we already have another lopp as this is a single threaded application

root = Tk() # create a root window 

entry = Entry()
entry.pack(side=BOTTOM)
listbox= Listbox(root)
listbox.pack()
button = Button(root,text="Send", command=lambda :send(listbox,entry)) #executes the send message
button.pack(side=BOTTOM) #button on the bottom side
rbutton = Button(root,text="Recieve", command=lambda :recieve(listbox) #executes the send message
button.pack(side=BOTTOM) #button on the bottom side
root.title('Client') #naming the messaging window

s = socket.socket(socket.AF_INET6,socket.SOCKET_STREAM) 

HOST_NAME = socket.gethostbyname() 
PORT = 12345 # same port from server

#connect to socket we created
s.connect((HOST_NAME,PORT))

roor.mainloop()
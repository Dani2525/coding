import socket

from tkinter import *

def send(listbox,entry): # this function will be executed when user clicks the send button and accepts the listbox and entry variables are accepted and we can use them 
    message = entry.get() #accept the message fornm the entry and gets it 
    listbox.insert('end',"Server: "+message)# display the message in the listbox towards the end 
    entry.delete(0,END) # Deletes the message after it is send in the message box
    client.send(bytes(message,"utf-8")) # takes this line and conertes into bytes , encoded using utf-8 before being sent to client 

def recieve(listbox):
    message_from_client = client.recv(50) # recieves the message from the client in buffer 50
    listbox.insert('end',"Client:"+message_from_client.decode('utf-8')) #message recieved from the client and displayed when you click te recieve button and cant run a loop as we already have another lopp as this is a single threaded application

root = Tk() # create a root window 
# input field which accepts message and text box to display the messages


entry = Entry()
entry.pack(side=BOTTOM)
listbox= Listbox(root)
listbox.pack()
button = Button(root,text="Send", command=lambda :send(listbox,entry)) #executes the send message
button.pack(side=BOTTOM) #button on the bottom side
rbutton = Button(root,text="Recieve", command=lambda :recieve(listbox) #executes the send message
button.pack(side=BOTTOM) #button on the bottom side
root.title('Server') #naming the messaging window


s = socket.socket(socket.AF_INET6,socket.SOCKET_STREAM) #creating the socket- family type of the socket and what type of socket (TCP socket which is type stream as it uses a stream of data)

#ip and port number ip of the server- name of my host inside this local network hence computer
HOST_NAME = socket.gethostbyname() # THIS GETS HOSTNAME/IP
PORT = 12345 

#bind the hostname and port number
s.bind((HOST_NAME,PORT))

# listen to request from connection from client
s.listen(4)  # specifies number of unaccepted connections before before refusing new connections
# accept connections - keep listening for connections from client and then accept if found
client, address = s.accept() # accepts the connection 

root.mainloop()    
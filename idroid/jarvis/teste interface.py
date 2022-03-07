from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
         Frame. __init__(self, master=None)
         self.msg = Label(self, text="ola mundo")
         self.msg.pack()
         self.bye = Button (self, text="bye", command=self.quit)
         self.bye.pack ()
         self.pack()
app = Application()
app.master.title("meu primeiro app")
app.master.geometry("200x200+100+100")
mainloop()
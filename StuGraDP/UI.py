import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("")
        #setting window size
        width=600
        height=330
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_759=tk.Button(root)
        GButton_759["activebackground"] = "#626262"
        GButton_759["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GButton_759["font"] = ft
        GButton_759["fg"] = "#ffffff"
        GButton_759["justify"] = "center"
        GButton_759["text"] = "Select Sheet"
        GButton_759.place(x=10,y=10,width=155,height=30)
        GButton_759["command"] = self.GButton_759_command

        GMessage_79=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_79["font"] = ft
        GMessage_79["fg"] = "#333333"
        GMessage_79["justify"] = "center"
        GMessage_79["text"] = "DISPLAY CURRENTLY SELCTED SHEET HERE"
        GMessage_79.place(x=200,y=10,width=383,height=30)

        GLabel_600=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#333333"
        GLabel_600["justify"] = "center"
        GLabel_600["text"] = "current student no."
        GLabel_600["relief"] = "flat"
        GLabel_600.place(x=20,y=60,width=145,height=30)

        GButton_518=tk.Button(root)
        GButton_518["bg"] = "#858585"
        ft = tkFont.Font(family='Times',size=10)
        GButton_518["font"] = ft
        GButton_518["fg"] = "#ffffff"
        GButton_518["justify"] = "center"
        GButton_518["text"] = "Add Performance task"
        GButton_518.place(x=20,y=190,width=144,height=30)
        GButton_518["command"] = self.GButton_518_command

        GButton_291=tk.Button(root)
        GButton_291["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GButton_291["font"] = ft
        GButton_291["fg"] = "#fefefe"
        GButton_291["justify"] = "center"
        GButton_291["text"] = "Add Written Task"
        GButton_291.place(x=20,y=230,width=143,height=30)
        GButton_291["command"] = self.GButton_291_command

        GButton_571=tk.Button(root)
        GButton_571["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GButton_571["font"] = ft
        GButton_571["fg"] = "#fefefe"
        GButton_571["justify"] = "center"
        GButton_571["text"] = "Add Summative Task"
        GButton_571.place(x=20,y=270,width=142,height=30)
        GButton_571["command"] = self.GButton_571_command

        GMessage_628=tk.Message(root)
        GMessage_628["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=20)
        GMessage_628["font"] = ft
        GMessage_628["fg"] = "#333333"
        GMessage_628["justify"] = "center"
        GMessage_628["text"] = "future features here"
        GMessage_628.place(x=170,y=190,width=414,height=110)

        GLineEdit_774=tk.Entry(root)
        GLineEdit_774["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_774["font"] = ft
        GLineEdit_774["fg"] = "#333333"
        GLineEdit_774["justify"] = "center"
        GLineEdit_774["text"] = "Student !"
        GLineEdit_774.place(x=0,y=90,width=166,height=61)

    def GButton_759_command(self):
        print("command")


    def GButton_518_command(self):
        print("command")


    def GButton_291_command(self):
        print("command")


    def GButton_571_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

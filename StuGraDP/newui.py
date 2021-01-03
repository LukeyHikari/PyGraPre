import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("resertui.py")
        #setting window size
        width=750
        height=381
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_755=tk.Button(root)
        GButton_755["bg"] = "#a3a3a3"
        ft = tkFont.Font(family='Times',size=10)
        GButton_755["font"] = ft
        GButton_755["fg"] = "#f4f4f4"
        GButton_755["justify"] = "center"
        GButton_755["text"] = "Button1"
        GButton_755.place(x=20,y=210,width=186,height=30)
        GButton_755["command"] = self.GButton_755_command

        GButton_751=tk.Button(root)
        GButton_751["bg"] = "#a3a3a3"
        ft = tkFont.Font(family='Times',size=10)
        GButton_751["font"] = ft
        GButton_751["fg"] = "#ffffff"
        GButton_751["justify"] = "center"
        GButton_751["text"] = "Button2"
        GButton_751.place(x=20,y=250,width=186,height=30)
        GButton_751["command"] = self.GButton_751_command

        GButton_599=tk.Button(root)
        GButton_599["bg"] = "#a3a3a3"
        ft = tkFont.Font(family='Times',size=10)
        GButton_599["font"] = ft
        GButton_599["fg"] = "#ffffff"
        GButton_599["justify"] = "center"
        GButton_599["text"] = "Button3"
        GButton_599.place(x=20,y=290,width=185,height=30)
        GButton_599["command"] = self.GButton_599_command

        GButton_572=tk.Button(root)
        GButton_572["bg"] = "#878787"
        ft = tkFont.Font(family='Times',size=10)
        GButton_572["font"] = ft
        GButton_572["fg"] = "#ffffff"
        GButton_572["justify"] = "center"
        GButton_572["text"] = "Button4"
        GButton_572.place(x=220,y=210,width=189,height=30)
        GButton_572["command"] = self.GButton_572_command

        GButton_246=tk.Button(root)
        GButton_246["bg"] = "#a3a3a3"
        ft = tkFont.Font(family='Times',size=10)
        GButton_246["font"] = ft
        GButton_246["fg"] = "#ffffff"
        GButton_246["justify"] = "center"
        GButton_246["text"] = "Button5"
        GButton_246.place(x=220,y=250,width=190,height=30)
        GButton_246["command"] = self.GButton_246_command

        GButton_697=tk.Button(root)
        GButton_697["bg"] = "#a3a3a3"
        ft = tkFont.Font(family='Times',size=10)
        GButton_697["font"] = ft
        GButton_697["fg"] = "#ffffff"
        GButton_697["justify"] = "center"
        GButton_697["text"] = "Button6"
        GButton_697.place(x=220,y=290,width=190,height=30)
        GButton_697["command"] = self.GButton_697_command

        GButton_677=tk.Button(root)
        GButton_677["bg"] = "#a3a3a3"
        ft = tkFont.Font(family='Times',size=10)
        GButton_677["font"] = ft
        GButton_677["fg"] = "#ffffff"
        GButton_677["justify"] = "center"
        GButton_677["text"] = "Button7"
        GButton_677.place(x=120,y=330,width=189,height=30)
        GButton_677["command"] = self.GButton_677_command

        GMessage_302=tk.Message(root)
        GMessage_302["bg"] = "#8f8f8f"
        ft = tkFont.Font(family='Times',size=20)
        GMessage_302["font"] = ft
        GMessage_302["fg"] = "#ffffff"
        GMessage_302["justify"] = "center"
        GMessage_302["text"] = "INPUT AREA"
        GMessage_302.place(x=420,y=210,width=315,height=109)

        GButton_822=tk.Button(root)
        GButton_822["bg"] = "#a0a0a0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_822["font"] = ft
        GButton_822["fg"] = "#ffffff"
        GButton_822["justify"] = "center"
        GButton_822["text"] = "Button1"
        GButton_822.place(x=610,y=330,width=124,height=30)
        GButton_822["command"] = self.GButton_822_command

        GMessage_746=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_746["font"] = ft
        GMessage_746["fg"] = "#333333"
        GMessage_746["justify"] = "center"
        GMessage_746["text"] = "Message"
        GMessage_746.place(x=20,y=60,width=707,height=129)

    def GButton_755_command(self):
        print("command")


    def GButton_751_command(self):
        print("command")


    def GButton_599_command(self):
        print("command")


    def GButton_572_command(self):
        print("command")


    def GButton_246_command(self):
        print("command")


    def GButton_697_command(self):
        print("command")


    def GButton_677_command(self):
        print("command")


    def GButton_822_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

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
        root.configure(bg = '#383737')

        quarters = ["Quarter 1","Quarter 2","Quarter 3","Quarter 4"]
        quarter = tk.StringVar(root)
        quarter.set(quarters[0])
        dpdqt = tk.OptionMenu(root, quarter, *quarters)
        dpdqt.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdqt.place(x=20,y=15)
        dpdqt.pack
        def qtselect(*args):
            global dpqt
            dpqt = str(quarter.get())
            print(dpqt)
            return(dpqt)
        quarter.trace("w", qtselect)

        dpdsections = ["Aguinaldo"]
        dropsects = tk.StringVar(root)
        dropsects.set(dpdsections[0])
        dpdst = tk.OptionMenu(root, dropsects, *dpdsections)
        dpdst.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdst.place(x=140,y=15)
        dpdst.pack
        def stselect(*args):
            global dpst
            dpst = str(dropsects.get())
            print(dpst)
            return (dpst)
        dropsects.trace("w", stselect)

        dpdschooly = ["2020-2021"]
        dropschooly = tk.StringVar(root)
        dropschooly.set(dpdschooly[0])
        dpdsy = tk.OptionMenu(root, dropschooly, *dpdschooly)
        dpdsy.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdsy.place(x=260,y=15)
        dpdsy.pack
        def syselect(*args):
            global dpsy
            dpsy = str(dropschooly.get())
            print(dpsy)
            return dpsy
        dropschooly.trace("w", syselect)
        
        qtsecsydirectory= tk.Message(root)
        ft = tkFont.Font(family='Times', size=14)
        qtsecsydirectory["width"] = "10000"
        qtsecsydirectory["font"] = ft
        qtsecsydirectory["bg"] = "#8a8a8a"
        qtsecsydirectory["fg"] = "#f4f4f4"
        qtsecsydirectory["justify"] = "left"
        qtsecsydirectory["text"] = "Directory:" + " " + str(syselect()) + " " + str(stselect()) + " " + str(qtselect()) 
        qtsecsydirectory.place(x=380,y=15,width=350,height=32)
        qtsecsydirectory.pack

        GButton_755=tk.Button(root)
        GButton_755["bg"] = "#706a69"
        ft = tkFont.Font(family='Times',size=10)
        GButton_755["font"] = ft
        GButton_755["fg"] = "#f4f4f4"
        GButton_755["justify"] = "center"
        GButton_755["text"] = "Add Performance Task"
        GButton_755.place(x=20,y=210,width=186,height=30)
        GButton_755["command"] = self.GButton_755_command

        GButton_751=tk.Button(root)
        GButton_751["bg"] = "#706a69"
        ft = tkFont.Font(family='Times',size=10)
        GButton_751["font"] = ft
        GButton_751["fg"] = "#ffffff"
        GButton_751["justify"] = "center"
        GButton_751["text"] = "Add Written Task"
        GButton_751.place(x=20,y=250,width=186,height=30)
        GButton_751["command"] = self.GButton_751_command

        GButton_599=tk.Button(root)
        GButton_599["bg"] = "#706a69"
        ft = tkFont.Font(family='Times',size=10)
        GButton_599["font"] = ft
        GButton_599["fg"] = "#ffffff"
        GButton_599["justify"] = "center"
        GButton_599["text"] = "Find Student's Missing Acts."
        GButton_599.place(x=20,y=290,width=185,height=30)
        GButton_599["command"] = self.GButton_599_command

        GButton_572=tk.Button(root)
        GButton_572["bg"] = "#4f4d4d"
        ft = tkFont.Font(family='Times',size=10)
        GButton_572["font"] = ft
        GButton_572["fg"] = "#ffffff"
        GButton_572["justify"] = "center"
        GButton_572["text"] = "Create School Year"
        GButton_572.place(x=220,y=210,width=189,height=30)
        GButton_572["command"] = self.GButton_572_command

        GButton_246=tk.Button(root)
        GButton_246["bg"] = "#4f4d4d"
        ft = tkFont.Font(family='Times',size=10)
        GButton_246["font"] = ft
        GButton_246["fg"] = "#ffffff"
        GButton_246["justify"] = "center"
        GButton_246["text"] = "Add Students"
        GButton_246.place(x=220,y=250,width=190,height=30)
        GButton_246["command"] = self.GButton_246_command

        GButton_697=tk.Button(root)
        GButton_697["bg"] = "#706a69"
        ft = tkFont.Font(family='Times',size=10)
        GButton_697["font"] = ft
        GButton_697["fg"] = "#ffffff"
        GButton_697["justify"] = "center"
        GButton_697["text"] = "Record Missing Act."
        GButton_697.place(x=220,y=290,width=190,height=30)
        GButton_697["command"] = self.GButton_697_command

        GButton_677=tk.Button(root)
        GButton_677["bg"] = "#706a69"
        ft = tkFont.Font(family='Times',size=10)
        GButton_677["font"] = ft
        GButton_677["fg"] = "#ffffff"
        GButton_677["justify"] = "center"
        GButton_677["text"] = "Find Students with Missing Act."
        GButton_677.place(x=120,y=330,width=189,height=30)
        GButton_677["command"] = self.GButton_677_command

        GMessage_302=tk.Message(root)
        GMessage_302["bg"] = "#8a8a8a"
        ft = tkFont.Font(family='Times',size=20)
        GMessage_302["font"] = ft
        GMessage_302["fg"] = "#ffffff"
        GMessage_302["justify"] = "center"
        GMessage_302["text"] = "INPUT AREA"
        GMessage_302.place(x=420,y=210,width=315,height=109)

        GButton_822=tk.Button(root)
        GButton_822["bg"] = "#383737"
        ft = tkFont.Font(family='Times',size=10)
        GButton_822["font"] = ft
        GButton_822["fg"] = "#ffffff"
        GButton_822["justify"] = "center"
        GButton_822["text"] = "Export"
        GButton_822.place(x=610,y=330,width=124,height=30)
        GButton_822["command"] = self.GButton_822_command
        
        GMessage_746= tk.Message(root)
        ft = tkFont.Font(family='Times', size=20)
        GMessage_746["width"] = "10000"
        GMessage_746["font"] = ft
        GMessage_746["bg"] = "#8a8a8a"
        GMessage_746["fg"] = "#f4f4f4"
        GMessage_746["justify"] = "left"
        GMessage_746["text"] = "Display Box"
        GMessage_746.place(x=20,y=60,width=707,height=129)

    def GButton_755_command(self): #Add PT
        print("This is button 1")


    def GButton_751_command(self): #Add WT
        print("This is button 2")


    def GButton_599_command(self): #Find Stud Mis Act
        print("This is button 3")


    def GButton_572_command(self): #Create S.Y.
        print("This is button 4")


    def GButton_246_command(self): #Add Studs
        print("This is button 5")


    def GButton_697_command(self): #Record Missing Act.
        print("This is button 6")


    def GButton_677_command(self): #Find Student's Missing Act
        print("This is button 7")


    def GButton_822_command(self): #Export
        print("This is button 8")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

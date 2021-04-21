import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import StringVar
from tkinter import Entry
import exportgrade as exgrades
import sycreator
import incompleteactivitylister as iactlister
import studadd as sadd
import performancetaskkadder as ptadder
import writtentaskadder as wtadder
import time
root = None

class App:
    def __init__(self):
# Variables
        directorydisplaytext = StringVar()
        tracertext = ""
        self.displaytext = StringVar()

#       #Dropdowns
        quarters = ["Quarter 1","Quarter 2","Quarter 3","Quarter 4"]
        dropquarter = tk.StringVar(root)
        dropquarter.set(quarters[0])
        dpdqt = tk.OptionMenu(root, dropquarter, *quarters)
        dpdqt.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdqt.place(x=20,y=15)
        dpdqt.pack

        dpdsections = ["Agoncillo", "Aguinaldo"]
        dropsects = tk.StringVar(root)
        dropsects.set(dpdsections[0])
        dpdst = tk.OptionMenu(root, dropsects, *dpdsections)
        dpdst.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdst.place(x=140,y=15)
        dpdst.pack

        dpdschooly = ["2020-2021", "2021-2022"]
        dropschooly = tk.StringVar(root)
        dropschooly.set(dpdschooly[0])
        dpdsy = tk.OptionMenu(root, dropschooly, *dpdschooly)
        dpdsy.config(text="Quarter",width=10, font=("Helvetica",10),bg='#706a69',fg='white')
        dpdsy.place(x=260,y=15)
        dpdsy.pack

#       #Input Area Box
        self.inputareabox = tk.Entry(root, bg = "#808585", font= tkFont.Font(family = 'Times', size = 15), fg = "#ffffff", justify = "center")
        self.inputareabox.place(x=420,y=210,width=315,height=109)

#        #Diplay Box
        displaybox = tk.Message(root, bg = "#8a8a8a", width = "10000", font= tkFont.Font(family = 'Times', size = 20),
        fg = "#f4f4f4", justify = "left", textvariable = self.displaytext)
        displaybox.place(x=20,y=60,width=707,height=129)

#        #dropdown functions
        def qtselect(*args):
            global dpqt
            dpqt = str(dropquarter.get())
            return(dpqt)
        dropquarter.trace("w", qtselect)
        def stselect(*args):
            global dpst
            dpst = str(dropsects.get())
            return (dpst)
        dropsects.trace("w", stselect)
        def syselect(*args):
            global dpsy
            dpsy = str(dropschooly.get())
            return dpsy
        dropschooly.trace("w", syselect)

        ft = tkFont.Font(family='Times', size=14)
        qtsecsydirectory= tk.Message(root, width = "10000", font = ft, bg = "#8a8a8a", fg = "#f4f4f4",
        justify = "left", textvariable = directorydisplaytext)
        qtsecsydirectory.place(x=380,y=15,width=350,height=32)
        qtsecsydirectory.pack
        
        #Directory updater
        def dupdate(*args):
            directorydisplaytext.set("Directory:" + " " + str(syselect()) + " " + str(stselect()) + " " + str(qtselect()))
        dropschooly.trace("w",dupdate)
        dropsects.trace("w",dupdate)
        dropquarter.trace("w",dupdate)
        
        directorydisplaytext.set("Directory:" + " " + str(syselect()) + " " + str(stselect()) + " " + str(qtselect()))

# UI Functions
#        #Add PT

        def addptinitialcmd(*args):
            ttodisplay = "Recording Grades for Activity No. " + self.inputareabox.get()  
            self.displaytext.set(ttodisplay)
            anumber = int(self.inputareabox.get())
            self.inputareabox.delete(0,'end')
            self.inputareabox.unbind('<Return>')
            ptadder.ptaskadd(str(syselect()), str(stselect()), anumber, str(qtselect()))


        def addptcmd(*args):
            print("Adding Performance Task")
            self.displaytext.set("Please Input Activity Number(Ex: 1, 2, etc.)")
            self.inputareabox.bind('<Return>', addptinitialcmd)

#        #Add WT
        def addwtinitialcmd(*args):
            ttodisplay = "Recording Grades for Activity No. " + self.inputareabox.get()  
            self.displaytext.set(ttodisplay)
            anumber = int(self.inputareabox.get())
            self.inputareabox.delete(0,'end')
            self.inputareabox.unbind('<Return>')
            wtadder.wtaskadd(str(syselect()), str(stselect()), anumber, str(qtselect()))

        def addwtcmd(*args):
            print("Adding Written Task")
            self.displaytext.set("Please Input Activity Number(Ex: 1, 2, etc.)")
            self.inputareabox.bind('<Return>', addwtinitialcmd)

#       #Find w/ Stud Mis Act
        def findstudwmisactcmd(*args): 
            print("Finding Student With Missing Activities")

#       #Create S.Y.
        def createsysubcmd(*args):
            tracertext = str(self.inputareabox.get())
            self.inputareabox.delete(0,'end')
            self.inputareabox.unbind('<Return>')
            ttodisplay = sycreator.sycreate("True", str(syselect()), str(stselect()), tracertext)
            self.displaytext.set(ttodisplay)
            ttodisplay = ""

        def createsycmd(*args): 
            print("Creating School Year")
            self.displaytext.set("Number of Students in" + " " + str(stselect() + "?:"))
            self.inputareabox.bind('<Return>', createsysubcmd)              

#       #Add Studs
        def addstudscmd(*args): 
            sadd.addstuds(str(syselect()), str(stselect()))

#       #List Incomplete Acts.
        def listincactssubcmd(*args):
            inputtedtype = str(self.inputareabox.get())
            self.inputareabox.delete(0,'end')
            self.inputareabox.unbind('<Return>')
            ttodisplay = iactlister.listincacts(inputtedtype, str(syselect()), str(stselect()), str(qtselect()))
            self.displaytext.set("Incomplete Activities are Act No.:" + "\n" + str(ttodisplay))

        def listincactscmd(*args): 
            print("Finding Incomplete Activities")
            self.displaytext.set("Performance or Written?")
            self.inputareabox.bind('<Return>', listincactssubcmd)

#       #Find Student's Missing Act
        def findstudmisactcmd(*args): 
            print("Finding Student Missing Activities")

#       #Experimental export command
        def exportcmd(*args): 
            print("Exporting")
            exgrades.exportgrades(dpsy, dpst, dpqt)

# Main UI code
#        #Add Performance Task Button
        addperftask = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#f4f4f4",
        justify = "center", text = "Add Performance Task", command = addptcmd)
        addperftask.place(x=20,y=210,width=186,height=30)
        
#       #Add Written Task Button
        addwrittask = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff",
        justify = "center", text = "Add Written Task", command = addwtcmd)
        addwrittask.place(x=20,y=250,width=186,height=30)

#        #Create School Year Button
        createsybut = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff",
        justify = "center", text = "Create School Year", command = createsycmd)
        createsybut.place(x=220,y=210,width=189,height=30)

#        #Add Students Button
        addstudbut = tk.Button(root, bg = "#706a69", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff",
        justify = "center", text = "Add Students", command = addstudscmd)
        addstudbut.place(x=220,y=250,width=190,height=30)

#        #Find Student's Missing Acts. Button
        fstudsmisactbut = tk.Button(root, bg = "#4f4d4d", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff",
        justify = "center", text = "Find Student's Missing Act.", command = findstudmisactcmd)
        fstudsmisactbut.place(x=20,y=290,width=185,height=30)

#        #Find Students with Missing Acts. Button
        recmisactbut = tk.Button(root, bg = "#4f4d4d", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff",
        justify = "center", text = "Find Students w/ Missing Acts.", command = findstudwmisactcmd)
        recmisactbut.place(x=220,y=290,width=190,height=30)

#        #List Incomplete Activities Button
        findstudwithmisact = tk.Button(root, bg = "#4f4d4d", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff",
        justify = "center", text = "List Incomplete Activities", command = listincactscmd)
        findstudwithmisact.place(x=120,y=330,width=189,height=30)

#        #Export Button
        exportbut = tk.Button(root, bg = "#383737", font= tkFont.Font(family = 'Times', size = 10), fg = "#ffffff",
        justify = "center", text = "Export", command = exportcmd)
        exportbut.place(x=610,y=330,width=124,height=30)
#
  
    def get_inputbox(self):
        return self.inputareabox
    
    def get_displaybox(self):
        return self.displaytext

def main():
    root = tk.Tk()
# Window Properties
    root.title("PyGraPre")
    #setting window size
    width=750
    height=381
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    root.configure(bg = '#383737')
#    
    app = App()
    root.mainloop()

if __name__ == "__main__":
    main()
    
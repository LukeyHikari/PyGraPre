            qtsecsydirectory= tk.Message(root)
            ft = tkFont.Font(family='Times', size=14)
            qtsecsydirectory["width"] = "10000"
            qtsecsydirectory["font"] = ft
            qtsecsydirectory["bg"] = "#8a8a8a"
            qtsecsydirectory["fg"] = "#f4f4f4"
            qtsecsydirectory["justify"] = "left"
            qtsecsydirectory["text"] = "Directory:" + " " + str(syselect()) + " " + str(stselect()) + " " + str(qtselect()) 
            qtsecsydirectory.place(x=380,y=15,width=350,height=32)

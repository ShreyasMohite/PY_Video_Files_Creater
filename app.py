from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import touch
import tkinter.filedialog



class File:
    def __init__(self,root):
        self.root=root
        self.root.title("Video File Extention")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo448.ico")
        self.root.resizable(0,0)

        path=StringVar()
        filename=StringVar()
        filextention=StringVar()
#======================================================================================#

        def clear():
            filename.set("")
            path.set("")
            lab_filecreated.config(text="")
            lab_selectpath.config(text="Select Path")
            filextention.set("Select Video File Extention")

        def browse():
            #golbal files
            a=tkinter.filedialog.askdirectory(title="choose folder")
            path.set(a)
            if a:
                lab_selectpath.config(text="Path Is Selected")
            #files=a

        def genrate():
            try:
                if path.get()!="":
                    a=path.get()
                    lab_filecreated.config(text="File Created Successfully")

                    
                    if filextention.get()!="Select Video File Extention":
                        if filename.get()!="":

                            if filextention.get()=="3GPP2 multimedia file" and filename.get()!="":
                                touch.touch(a+"/{}.3g2".format(filename.get()))
                            
                            if filextention.get()=="3GPP multimedia file" and filename.get()!="":
                                touch.touch(a+"/{}.3gp".format(filename.get()))
                        

                            if filextention.get()=="AVI file" and filename.get()!="":
                                touch.touch(a+"/{}.avi".format(filename.get()))
                            

                            if filextention.get()=="Adobe Flash file" and filename.get()!="":
                                touch.touch(a+"/{}.flv".format(filename.get()))

                            if filextention.get()=="H.264 video file" and filename.get()!="":
                                touch.touch(a+"/{}.h264".format(filename.get()))

                            if filextention.get()=="Apple MP4 video file" and filename.get()!="":
                                touch.touch(a+"/{}.m4v".format(filename.get()))
                            
                            if filextention.get()=="Matroska Multimedia Container" and filename.get()!="":
                                touch.touch(a+"/{}.mkv".format(filename.get()))

                            if filextention.get()=="Apple QuickTime movie file" and filename.get()!="":
                                touch.touch(a+"/{}.mov".format(filename.get()))

                            if filextention.get()=="MPEG4 video file" and filename.get()!="":
                                touch.touch(a+"/{}.mp4".format(filename.get()))

                            if filextention.get()=="MPEG video file" and filename.get()!="":
                                touch.touch(a+"/{}.mpg".format(filename.get()))

                            if filextention.get()=="RealMedia file" and filename.get()!="":
                                touch.touch(a+"/{}.rm".format(filename.get()))
                            
                            if filextention.get()=="Shockwave flash file" and filename.get()!="":
                                touch.touch(a+"/{}.swf".format(filename.get()))

                            if filextention.get()=="DVD Video Object" and filename.get()!="":
                                touch.touch(a+"/{}.vob".format(filename.get()))
                            
                            if filextention.get()=="Windows Media Video file" and filename.get()!="":
                                touch.touch(a+"/{}.wmv".format(filename.get()))
                            
                        else:
                            tkinter.messagebox.showerror("Error","Please write a proper filename")

                    else:
                        tkinter.messagebox.showerror("Error","Please choose an extension ")
                else:
                    tkinter.messagebox.showerror("Error","Please choose path first")
            except Exception as e:
                print(e)

#======================================================================================#
        def on_enter1(e):
            but_browsepath['background']="black"
            but_browsepath['foreground']="cyan"
  
        def on_leave1(e):
            but_browsepath['background']="SystemButtonFace"
            but_browsepath['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_generate['background']="black"
            but_generate['foreground']="cyan"
  
        def on_leave3(e):
            but_generate['background']="SystemButtonFace"
            but_generate['foreground']="SystemButtonText"

#======================================================================================#
        mainframe=Frame(self.root,width=500,height=400,bd=4,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=300,bd=4,relief="ridge",bg="#70d6ff")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=90,relief="ridge",bd=3,bg="#272640")
        secondframe.place(x=0,y=300)

#======================================================================================#
        but_browsepath=Button(firstframe,text="Browse Path",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=browse)
        but_browsepath.place(x=160,y=15)
        but_browsepath.bind("<Enter>",on_enter1)
        but_browsepath.bind("<Leave>",on_leave1)

        lab_selectpath=Label(firstframe,text="Select Path",font=('times new roman',12),bg="#70d6ff")
        lab_selectpath.place(x=200,y=90)

        ent_path=Entry(firstframe,width=55,font=('times new roman',12),relief="ridge",bd=4,textvariable=path)
        ent_path.place(x=15,y=120)

        lab_filecreated=Label(firstframe,text="",font=('times new roman',12),bg="#70d6ff",fg="red")
        lab_filecreated.place(x=170,y=150)

        lab_selectfilename=Label(firstframe,text="Select FileName",font=('times new roman',12),bg="#70d6ff")
        lab_selectfilename.place(x=20,y=200)

        ent_filename=Entry(firstframe,width=30,font=('times new roman',12),relief="ridge",bd=4,textvariable=filename)
        ent_filename.place(x=200,y=200)


        lab_selectfilename=Label(firstframe,text="Select File Extention",font=('times new roman',12),bg="#70d6ff")
        lab_selectfilename.place(x=20,y=250)

        fileselect=["3GPP2 multimedia file","3GPP multimedia file",\
                    "AVI file","Adobe Flash file","H.264 video file",\
                    "Apple MP4 video file","Matroska Multimedia Container","Apple QuickTime movie file","MPEG4 video file",\
                    "MPEG video file","RealMedia file","Shockwave flash file","DVD Video Object","Windows Media Video file"]
        fileselect_combo=Combobox(firstframe,values=fileselect,font=('arial',12),width=25,state="readonly",textvariable=filextention)
        fileselect_combo.set("Select Video File Extention")
        fileselect_combo.place(x=200,y=250)
            

#======================================================================================#


        but_clear=Button(secondframe,text="Clear",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=clear)
        but_clear.place(x=30,y=15)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

        but_generate=Button(secondframe,text="Generate File",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=genrate)
        but_generate.place(x=290,y=15)
        but_generate.bind("<Enter>",on_enter3)
        but_generate.bind("<Leave>",on_leave3)



if __name__ == "__main__":
    root=Tk()
    app=File(root)
    root.mainloop()

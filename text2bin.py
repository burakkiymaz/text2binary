from tkinter import*
import webbrowser

class Uygulama(object):
    def __init__(self):
        self.arayuz()
        self.topmenu()

    def text2bin(self):

        self.giris2["state"] = "normal"
        def bolum (gelen):
            if int(gelen/2)==0:
                array.append(int(gelen%2))
            else:
                array.append(int(gelen%2))
                return bolum(int(gelen/2))
        k = self.giris1.get(1.0, "end")
        kelime = k.strip()
        klist=""
        for harf in kelime:
            array=[]
            asci = ord(harf)
            bolum(asci)
            karakter=""
            for i in range((array.__len__()-1),-1,-1):
                karakter+=str(array[i])
            klist+= karakter + " "
        self.giris2.delete(1.0, "end")
        self.giris2.insert(END,klist)
        self.giris2["state"] = "disabled"


    def bin2text(self):

        self.giris2["state"] = "normal"
        def bin2text(gelen):
            giden=[]
            binaryCumle=[]
            array=gelen.split(" ")
            for i in array:
                asci=0
                temp=i
                ttemp=[]
                for j in range(0,temp.__len__()):
                    ttemp.append(temp[j])
                    asci+=(int(ttemp[j])*(2**(temp.__len__()-1-j)))
                giden.append(asci)
            for j in giden:
                binaryCumle.append(chr(int(j)))
            return binaryCumle
        k = self.giris1.get(1.0, "end")
        kelimeInput = k.strip()
        harfler = bin2text(kelimeInput)
        cumle = ""
        for i in harfler:
            cumle+=i
        self.giris2.delete(1.0, END)
        self.giris2.insert(END,cumle)
        self.giris2["state"] = "disabled"


    def ttbButton(self):
        self.ttbcheck["state"] = "normal"
        self.bttcheck["state"] = "normal"
        self.ttbcheck["variable"] = self.var
        self.bttcheck["variable"] = self.yok
        self.ttbcheck["state"] = "disabled"
        self.bttcheck["state"] = "disabled"
        self.convert["command"] = self.text2bin


    def bttButton(self):
        self.bttcheck["state"] = "normal"
        self.ttbcheck["state"] = "normal"
        self.bttcheck["variable"] = self.var
        self.ttbcheck["variable"] = self.yok
        self.ttbcheck["state"] = "disabled"
        self.bttcheck["state"] = "disabled"
        self.convert["command"] = self.bin2text

    def burakKiymaz(self):
        def callback(event):
            webbrowser.open_new(r"http://www.burakkiymaz.com")
        bk = Toplevel()
        link = Label(bk, text="Visit my page here!\nhttp://www.burakkiymaz.com", fg="#00afc9", cursor="hand2", font="ubuntu 13 bold")
        link.pack(fill="both", expand = 1)
        link.bind("<Button-1>", callback)
        bk.geometry("300x100")
        bk.resizable(width=FALSE,height=FALSE)

    def topmenu(self):
        menu = Menu(pencere)
        pencere.config(menu = menu)

        about = Menu(menu, tearoff =0)
        menu.add_cascade(label = "About", menu = about)
        about.add_command(label="Who is Burak Kıymaz", command = self.burakKiymaz)
        about.add_command(label="Version 1.0.0", state = "disabled")




    def arayuz(self):
        self.var = IntVar()
        self.var.set(1)
        self.yok = IntVar()
        self.yok.set(0)


        self.baslik=Label(text="Text to Binary // Binary to Text", anchor = "n",font="ubuntu 12 bold", fg = "#00afc9")
        self.baslik.grid(row = 0, column = 0, columnspan = 2)

        self.ttbcheck = Checkbutton(variable = self.var, state = "disabled")
        self.ttbcheck.grid(row=1, column =0, sticky = "nws")

        self.bttcheck = Checkbutton(variable= self.yok, state = "disabled")
        self.bttcheck.grid(row=1, column =1, sticky = "nws")

        self.ttb = Button(text="Text to Binary",command=self.ttbButton,font="ubuntu 9 bold underline", fg = "#00afc9", bd = 0)
        self.ttb.grid(row=1, column = 0)

        self.btt = Button(text="Binary to Text",command=self.bttButton,font="ubuntu 9 bold underline", fg = "#00afc9", bd=0)
        self.btt.grid(row = 1, column = 1)

        self.giris1 = Text (width = 35,height = 11,font="ubuntu 10", fg = "#00afc9", bd=1,relief = SOLID)
        self.giris1.grid(row = 2, column = 0, columnspan = 2,padx = 5, pady = 5,)

        self.giris2 = Text ( width = 35, height = 11,state= "disabled",font="ubuntu 10", fg = "#00afc9", bd=1, relief = SOLID)
        self.giris2.grid(row =4 , column = 0,padx = 5, pady = 5,columnspan = 2)

        self.convert = Button(text = "Convert", command =self.text2bin,font="ubuntu 12 bold underline", fg = "#00afc9", bd=0)
        self.convert.grid(row = 3, column = 0, columnspan = 2)

        self.cıkısFrame=Frame()
        self.cıkısFrame.grid(row = 5, column = 0, columnspan = 2, ipady = 2)

        self.cikis = Button(self.cıkısFrame,text="Exit", command = pencere.quit,font="ubuntu 12 bold underline", fg = "white", bd=0, bg = "#00afc9", width = 32)
        self.cikis.pack(expand = 1)



pencere = Tk()
baslik = pencere.title("Text to Binary")
pencere.geometry("294x522+500+200")

uyg = Uygulama()
mainloop()

import customtkinter as ctk
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Stopwatch(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Stopwatch")
        self.geometry("450x600")
        self.resizable(False,False)

        self.running = False
        self.starttime = 0.0
        self.elaspedtime = 0.0
        self.lapcount = 1

        self.timelable = ctk.CTkLabel(self, text="00:00:00:00", font=ctk.CTkFont(family="Arial",size=54,weight="bold"))
        self.timelable.pack(pady=(40,20))

        self.buttonframe = ctk.CTkFrame(self, fg_color='transparent')
        self.buttonframe.pack(pady = 20)

        self.leftbutton = ctk.CTkButton(self.buttonframe, text='Start',width=120,height=40,command=self.leftclick,hover_color='green')
        self.rightbutton = ctk.CTkButton(self.buttonframe, text='Lap',width=120,height=40,command=self.rightclick,state='disabled')

        self.leftbutton.grid(row=0,column=0,padx=15)
        self.rightbutton.grid(row=0,column=1,padx=15)

        self.lapbox = ctk.CTkScrollableFrame(self, width = 380, height = 300,label_text='Laps',label_font=ctk.CTkFont(size=16,weight="bold"))
        self.lapbox.pack(pady=(20,20),fill = "both", expand=True)

    def formattime(self,totalseconds):
        h = int(totalseconds // 3600)
        s = int(totalseconds % 60)
        m = int((totalseconds % 3600)// 60)
        ms = int((totalseconds % 1) * 100)

        return f"{h:02d}:{m:02d}:{s:02d}.{ms:02d}"

    def update(self):
        if self.running:
            currenttotal = self.elaspedtime + (time.time() - self.starttime)
            self.timelable.configure(text=self.formattime(currenttotal))

            self.after(10,self.update)
    
    def leftclick(self):
        if not self.running:
            self.running = True
            self.starttime = time.time()

            self.leftbutton.configure(text='Stop',hover_color='red',fg_color='red')
            self.rightbutton.configure(state='enabled')

            self.update()

        else:
            self.running = False
            self.elaspedtime += time.time() - self.starttime

            self.leftbutton.configure(text='Start',fg_color='green',hover_color='green')
            self.rightbutton.configure(text='Reset')

    def rightclick(self):
        if self.running:
            currenttotal = self.elaspedtime + (time.time() - self.starttime)
            laptimer = self.formattime(currenttotal)

            laprecord = ctk.CTkLabel(self.lapbox,text = f"Lap {self.lapcount}: {laptimer}",font=ctk.CTkFont(family="Arial",size=14))
            laprecord.pack(anchor='w', pady = 2, padx=10)
            self.lapcount += 1                                                                                                      

        else:
            self.elaspedtime = 0.0
            self.lapcount = 1 
            self.timelable.configure(text="00:00:00:00")
            

            for widget in self.lapbox.winfo_children():
                widget.destroy()

            
            self.rightbutton.configure(text='Lap',state='disabled')


if __name__ == '__main__':
    app = Stopwatch()
    app.mainloop()
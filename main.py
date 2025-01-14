import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

#* Pre setup
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#* Global variable
sc = None
score_int = None

#* Team name
team_1 = ["Hello", 0]
team_2 = ["world", 0]

#* Font Family
title_f = ("Segoe UI Bold", 35)
normal_f = ("Segoe UI", 24)
s_normal_f = ("Segoe UI", 12)
score_f = ("Segoe UI", 60)

#* Main interface
class Control(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title(f"Score of {team_1[0]} and {team_2[0]}")

        SCore(self)
        Top(self)
        default_p = MainPage(self)
        default_p.pack(side="right", anchor="center", expand=True, fill="both")
        # BurgerMenu(self)

        self.mainloop()

class MainPage(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        ctk.CTkLabel(self, text="Hello World!", font=title_f).pack(side="bottom")
        t_1(self)

class BurgerMenu(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.configure(fg_color="blue",width=280,height=600)

        ctk.CTkLabel(self, text="Menu").place(x=0,y=0)
        ctk.CTkButton(self, text="close", command=self.close_menu, width=90, fg_color="#800001", hover_color="#320001").place(x=0, y=20)
        ctk.CTkButton(self, text="Exit", command=self.exit_app, width=90, fg_color="#800001", hover_color="#320001").place(x=100, y=20)

        self.place(x=0, y=0)

    def close_menu(self):
        self.place_forget()

    def exit_app(self):
        CloseDialog()

class t_1(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        global sc
        global score_int
        self.configure(fg_color="#333333", border_color="red", border_width=2, width=300, height=150)

        score_int=str()
        ctk.CTkLabel(self, text=f"team: {team_1[0]}", font=normal_f, anchor="w").place(x=12, y=12)
        sc = ctk.CTkLabel(self, text=f"score: {team_1[1]}", font=normal_f, anchor="w")
        sc.place(x=12, y=42)
        ctk.CTkEntry(self, textvariable=score_int, placeholder_text="Enter the number to added", font=s_normal_f, border_color="#ff6500").place(x=12, y=74)
        ctk.CTkButton(self, text="Add", width=32, fg_color="#ff6500", hover_color="#ff0000", command=self.add_point).place(x=160, y=74)


        self.place(x=1, y=1)

    def add_point(self):
        global team_1
        global sc
        global score_int
        i_var=int(score_int)
        team_1[1]+=i_var
        sc.configure(text=team_1[1])


#* Dialog Box
class CloseDialog(ctk.CTkToplevel):
    def __init__(self, master=None,):
        super().__init__(master)

        #* Setup
        self.geometry("600x200")
        self.minsize(width=600,height=200)
        self.maxsize(width=600, height=200)

        CloseButtons(self)
        ctk.CTkLabel(self, text="Are You Sure to Close?", font=normal_f).pack(side="left", anchor="center", pady=30)

        
class CloseButtons(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.configure(fg_color="#333333")
        ctk.CTkButton(self, text="Yes", corner_radius=0, command=lambda: exit(0), font=normal_f, width=120).pack(side="left", expand=True, fill="both")
        ctk.CTkButton(self, text="No", corner_radius=0, command=lambda: print("1"), font=normal_f, width=120).pack(side="right", expand=True, fill="both")

        self.pack(side="bottom", anchor="center", fill="x")

class Top(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(fg_color="#b40001", height=75, corner_radius=20)

        menu_p = Image.open("assets/menu.png")
        menu_p_ctk = ctk.CTkImage(light_image=menu_p, dark_image=menu_p, size=(20,20))
        ctk.CTkButton(self, text="menu_p_ctk", command=self.show_menu).place(x=20, y=25, anchor="w")
        name = ctk.CTkLabel(self, text="SCore v1.0", font=title_f)
        name.place(x=60,y=25, anchor="w")

        ver = ctk.CTkLabel(self, text="Version 1.0 Release", font=s_normal_f)
        ver.place(x=60, y=60, anchor="w")

        self.pack(side="top", anchor="w",fill='x', padx=5,pady=5)

    def show_menu(self):
        BurgerMenu()

#* Score Display
class SCore(ctk.CTkToplevel):
    def __init__(self, master=None) -> None:
        super().__init__()
        
        self.geometry("900x800")
        self.minsize(width=450, height=400)

        ctk.CTkLabel(self, text="Score of {t1} and {t2}".format(t1=team_1[0], t2=team_2[0]), font=normal_f,anchor="w").pack(side="top", anchor="center",fill="x")

if __name__ == "__main__":
    Control()


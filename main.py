import customtkinter as ctk

#* Pre setup
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#* Team name
team_1 = ["Hello", 0]
team_2 = ["world", 0]

#* Font Family
title_f = ("Segoe UI Bold", 35)
normal_f = ("Segoe UI", 24)
s_normal_f = ("Segoe UI", 12)
score_f = ("Segoe UI", 60)

#* Main code
class Control(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title(f"Score of {team_1[0]} and {team_2[0]}")

        Top(self)
        ctk.CTkLabel(self, text="Hello World!", font=title_f).pack()
        ctk.CTkLabel(self, text="Hello World!", font=normal_f).pack()
        ctk.CTkLabel(self, text="Hello World!", font=score_f).pack()

        self.mainloop()

class Top(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(fg_color="blue", height=100, corner_radius=20)

        name = ctk.CTkLabel(self, text="SCore v1.0", font=title_f)
        name.place(x=20,y=25, anchor="w")

        ver = ctk.CTkLabel(self, text="Version 1.0 Release", font=s_normal_f)
        ver.place(x=20, y=60, anchor="w")

        self.pack(side="top", anchor="w",fill='x', padx=5,pady=5)

if __name__ == "__main__":
    Control()


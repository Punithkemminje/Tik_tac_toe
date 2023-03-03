from tkinter import *
from tkinter import messagebox
import random

#---------------------------------------------- Color,font selection ----------------------------#
color = '#0af043'
bg_color = "#6161fa"
fg_color = "white"
font_t = ("Arial", 10,'bold')
# ----------------------- Class for game_play check and win check ------------------#
class Game_play :
    def __init__(self) :
        self.user1 = ""
        self.user2 = ""
        self.user1_text = "X"
        self.user2_text = "O"
        self.buttons = []

#----------------------------- To check match is draw ---------------------------------------------#
    def match_draw(self) :
        c = 0
        for i in self.buttons :
            if i['state'] == 'disabled' :
                c += 1
        if c == 9 :
            return True
        else :
            return False

    def disable_all_btn(self) :
        for i in self.buttons :
            i['state'] = DISABLED

#--------------------- check for button position ---------------------#
    def btn_text(self , t) :
        if (b1['text'] == t and b2['text'] == t and b3['text'] == t) :
            b1.config(bg=color)
            b2.config(bg=color)
            b3.config(bg=color)
            return True
        elif (b4['text'] == t and b5['text'] == t and b6['text'] == t) :
            b4.config(bg=color)
            b5.config(bg=color)
            b6.config(bg=color)
            return True
        elif (b7['text'] == t and b8['text'] == t and b9['text'] == t) :
            b7.config(bg=color)
            b8.config(bg=color)
            b9.config(bg=color)
            return True
        elif (b1['text'] == t and b4['text'] == t and b7['text'] == t) :
            b1.config(bg=color)
            b4.config(bg=color)
            b7.config(bg=color)
            return True
        elif (b2['text'] == t and b5['text'] == t and b8['text'] == t) :
            b5.config(bg=color)
            b2.config(bg=color)
            b8.config(bg=color)
            return True
        elif (b3['text'] == t and b6['text'] == t and b9['text'] == t) :
            b9.config(bg=color)
            b6.config(bg=color)
            b3.config(bg=color)
            return True
        elif (b1['text'] == t and b5['text'] == t and b9['text'] == t) :
            b1.config(bg=color)
            b5.config(bg=color)
            b9.config(bg=color)
            return True
        elif (b7['text'] == t and b5['text'] == t and b3['text'] == t) :
            b7.config(bg=color)
            b5.config(bg=color)
            b3.config(bg=color)
            return True
#----------------------- Check for win position -----------------------------#
    def win(self) :
        for i in range(9) :
            if self.btn_text("X") :
                s_label.config(text=f"{self.user1} won the match")
                restart_btn.place(x=80 , y=355)
                exit_btn.place(x=220,y=355)
                self.disable_all_btn()
            elif self.btn_text("O") :
                s_label.config(text=f"{self.user2} won the match")
                restart_btn.place(x=80 , y=355)
                exit_btn.place(x=220 , y=355)
                self.disable_all_btn()
            elif self.match_draw() :
                s_label.config(text="Match Draws")
                restart_btn.place(x=80 , y=355)
                exit_btn.place(x=220 , y=355)
                for i in self.buttons:
                    i.config(bg="#fafc5b")


window = Tk()
window.title("Tik Tac Toe")
window.config(bg=bg_color)
window.resizable(False,False)
window.geometry('350x400')

game_play = Game_play()

s_label = Label(text="Welcome to Tik Tac Toe" , height=5,bg=bg_color,fg=fg_color,font=font_t)
s_label.place(x=120 , y=30)
first_player = random.choice([1,2])
if first_player == 1:
    t_text = "O"
else:
    t_text = "X"


user1_label = Label(text="Player 1: ",bg=bg_color,fg=fg_color,font=font_t)
user1_label.place(x=80,y=100)
user1_entry = Entry(width=15)
user1_entry.place(x=170 , y=100)

user2_label = Label(text="Player 2: ",bg=bg_color,fg=fg_color,font=font_t)
user2_label.place(x=80,y=150)
user2_entry = Entry(width=15)
user2_entry.place(x=170 , y=150)

def place_btn():
    b1.place(x=10 , y=125)
    b2.place(x=120 , y=125)
    b3.place(x=230 , y=125)

    b4.place(x=10 , y=200)
    b5.place(x=120 , y=200)
    b6.place(x=230 , y=200)

    b7.place(x=10 , y=275)
    b8.place(x=120 , y=275)
    b9.place(x=230 , y=275)

def start() :
    global show_info_user1,show_info_user2
    if len(user1_entry.get())<1 or len(user2_entry.get())<1:
        messagebox.showwarning(title="Warning!!",message="Enter the Player name")
    else:
        play_btn.place_forget()
        game_play.user1 = user1_entry.get()
        game_play.user2 = user2_entry.get()
        user1_entry.place_forget()
        user2_entry.place_forget()
        user1_label.place_forget()
        user2_label.place_forget()
        s_label.config(text=f"Play: \t{f_player()}")
        show_info_user1.config(text=f"{game_play.user1}:   {game_play.user1_text}" , )
        show_info_user1.place(x=50 , y=10)
        show_info_user2.config(text=f"{game_play.user2}:   {game_play.user2_text}" , )
        show_info_user2.place(x=220,y=10)
        place_btn()

play_btn = Button(text="Play", width=12, height=2 , command=start)
play_btn.place(x=200 , y=250)

def f_player():
    if t_text=="O":
        return game_play.user1
    else:
        return game_play.user2


def text_selector() :
    global t_text
    if t_text == "X" :
        s_label.config(text=f"Play: \t{game_play.user1}")
        return "O"
    else:
        s_label.config(text=f"Play: \t{game_play.user2}")
        return "X"

def f1() :
    global t_text
    t_text = text_selector()
    b1.config(text=t_text , state=DISABLED)
    game_play.win()

def f2() :
    global t_text
    t_text = text_selector()
    b2.config(text=t_text , state=DISABLED)
    game_play.win()


def f3() :
    global t_text
    t_text = text_selector()
    b3.config(text=t_text , state=DISABLED)
    game_play.win()


def f4() :
    global t_text
    t_text = text_selector()
    b4.config(text=t_text , state=DISABLED)
    game_play.win()


def f5() :
    global t_text
    t_text = text_selector()
    b5.config(text=t_text , state=DISABLED)
    game_play.win()


def f6() :
    global t_text
    t_text = text_selector()
    b6.config(text=t_text , state=DISABLED)
    game_play.win()


def f7() :
    global t_text
    t_text = text_selector()
    b7.config(text=t_text , state=DISABLED)
    game_play.win()


def f8() :
    global t_text
    t_text = text_selector()
    b8.config(text=t_text , state=DISABLED)
    game_play.win()


def f9() :
    global t_text
    t_text = text_selector()
    b9.config(text=t_text , state=DISABLED)
    game_play.win()

def exit_win():
    window.destroy()

def restart():
    exit_btn.place_forget()
    s_label.place_forget()
    restart_btn.place_forget()
    s_label.config(text=f"Play: \t{f_player()}")
    s_label.place(x=120 , y=30)
    for i in game_play.buttons:
        i["state"] = "normal"
        i["text"] = ""
        i["bg"] = "white"
    place_btn()
# --------------------------- 1st row -----------------------------------------------------#

b1 = Button(width=12 , height=3 , command=f1)
b2 = Button(width=12 , height=3 , command=f2)
b3 = Button(width=12 , height=3 , command=f3)
# --------------------------------------- 2nd row ----------------------------------------#

b4 = Button(width=12 , height=3 , command=f4)
b5 = Button(width=12 , height=3 , command=f5)
b6 = Button(width=12 , height=3 , command=f6)

# -------------------------------------- 3rd row ---------------------------------------------#

b7 = Button(width=12 , height=3 , command=f7)
b8 = Button(width=12 , height=3 , command=f8)
b9 = Button(width=12 , height=3 , command=f9)

show_info_user1 = Label(bg=bg_color,fg=fg_color)
show_info_user2 = Label(text=f"{game_play.user2}:   {game_play.user2_text}" , bg=bg_color , fg=fg_color)

restart_btn = Button(text="Restart",width=8,bg="#80ff45",command=restart)
exit_btn = Button(text="Exit",command=exit_win,width=8,bg="#fc3059")
game_play.buttons = [b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9]

window.mainloop()

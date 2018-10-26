from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk


root = Tk()
#Styling

#Both Team's Scores
bluescore = IntVar()
redscore = IntVar()

#Changes the score for anyteam
def score_change(team, operation, amount):
    if operation == 'plus':
        team.set(team.get() + int(amount))
    elif operation == 'minus':
        team.set(team.get() - int(amount))

def score_set(team, amount):
    team.set(int(amount))



#+1 Red Button  
redPlus = Button(root, width=20, text="+1 Red")
redPlus.bind("<Button-1>", lambda event: score_change(redscore, 'plus', 1))
redPlus.place(relx=0.60, rely=0.85)

#-1 Red Button
redMinus = Button(root, width=20, text="-1 Red")
redMinus.bind("<Button-1>", lambda event: score_change(redscore, 'minus', 1))
redMinus.place(relx=0.60, rely=0.9)

#+10 Red Button
redPlus = Button(root, width=20, text="+10 Red")
redPlus.bind("<Button-1>", lambda event: score_change(redscore, 'plus', 10))
redPlus.place(relx=0.70, rely=0.85)

#-10 Button
redPlus = Button(root, width=20, text="-10 Red")
redPlus.bind("<Button-1>", lambda event: score_change(redscore, 'minus', 10))
redPlus.place(relx=0.70, rely=0.9)

#Reset Red Button
redPlus = Button(root, width=20, text="Reset")
redPlus.bind("<Button-1>", lambda event: score_set(redscore, 0))
redPlus.place(relx=0.64, rely=0.08)



#+1 Blue Button  
bluePlus = Button(root, width=20, text="+1 Blue")
bluePlus.bind("<Button-1>", lambda event: score_change(bluescore, 'plus', 1))
bluePlus.place(relx=0.10, rely=0.85)

#-1 Blue Button
blueMinus = Button(root, width=20, text="-1 Blue")
blueMinus.bind("<Button-1>", lambda event: score_change(bluescore, 'minus', 1))
blueMinus.place(relx=0.10, rely=0.9)

#+10 Red Button
redPlus = Button(root, width=20, text="+10 Red")
redPlus.bind("<Button-1>", lambda event: score_change(bluescore, 'plus', 10))
redPlus.place(relx=0.20, rely=0.85)

#-10 Button
redPlus = Button(root, width=20, text="-10 Red")
redPlus.bind("<Button-1>", lambda event: score_change(bluescore, 'minus', 10))
redPlus.place(relx=0.20, rely=0.9)

#Reset Red Button
redPlus = Button(root, width=20, text="Reset")
redPlus.bind("<Button-1>", lambda event: score_set(bluescore, 0))
redPlus.place(relx=0.125, rely=0.08)



#Red score on Screen
redLabel = Label(root, textvariable = redscore)
redLabel.configure(foreground="red", font=("TkDefaultFont", 320))
redLabel.place(relx=0.61, rely=0.15)

#Blue Score on Screen
blueLabel = Label(root, textvariable = bluescore)
blueLabel.configure(foreground="blue", font=("TkDefaultFont", 320))
blueLabel.place(relx=0.1, rely=0.15)

#Red name tag
redNameLabel = Label(root, text="RED")
redNameLabel.configure(foreground="red", font=("TkDefaultFont", 60))
redNameLabel.place(relx=0.63, rely=0.125)

#Blue name tag
blueNameLabel = Label(root, text="BLUE")
blueNameLabel.configure(foreground="blue", font=("TkDefaultFont", 60))
blueNameLabel.place(relx=0.11, rely=0.125)

#Kings Kids Logo
logoFile = Image.open("Kings-Kids.png")
logoImg = ImageTk.PhotoImage(logoFile)
logo = Label(root, image=logoImg)
logo.place(relx=0.41, y=0.1)

root.mainloop()

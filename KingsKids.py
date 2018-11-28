from http.server import HTTPServer, BaseHTTPRequestHandler
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import threading
import socket

ip = socket.gethostbyname(socket.gethostname())
def score_change(team, operation, amount):
    if operation == 'plus':
        team.set(team.get() + int(amount))
    elif operation == 'minus':
        team.set(team.get() - int(amount))
def score_set(team, amount):
    team.set(int(amount))

bluescore = 0
redscore = 0
def scoreBoard():
    root = Tk()
    #Both Team's Scores
    global bluescore
    global redscore
    bluescore = IntVar()
    redscore = IntVar()
    #Changes the score for anyteam

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

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        if self.path == "/":
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)[:3]
        if post_data.decode("utf-8")[0] == "b":
            if post_data.decode("utf-8")[1] == "p":
                if post_data.decode("utf-8")[2] == "1":
                    score_change(bluescore, 'plus', 1)
                elif post_data.decode("utf-8")[2] == "2":
                    score_change(bluescore, 'plus', 10)
            elif post_data.decode("utf-8")[1] == "m":
                if post_data.decode("utf-8")[2] == "1":
                    score_change(bluescore, 'minus', 1)
                elif post_data.decode("utf-8")[2] == "2":
                    score_change(bluescore, 'minus', 10)
        if post_data.decode("utf-8")[0] == "r":
            if post_data.decode("utf-8")[1] == "p":
                if post_data.decode("utf-8")[2] == "1":
                    score_change(redscore, 'plus', 1)
                elif post_data.decode("utf-8")[2] == "2":
                    score_change(redscore, 'plus', 10)
            elif post_data.decode("utf-8")[1] == "m":
                if post_data.decode("utf-8")[2] == "1":
                    score_change(redscore, 'minus', 1)
                elif post_data.decode("utf-8")[2] == "2":
                    score_change(redscore, 'minus', 10)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
print(ip)
httpd = HTTPServer((ip, 8080), Serv)
t = threading.Thread(target=scoreBoard)
t.daemon = True
t.start()
httpd.serve_forever()

from tkinter import *
import random
from tkinter import messagebox


# Импортируем библиотеку с помощью которой будем выполнять запрос
import requests 

# Выполняем запрос с помощью которого мы получим слова
first_reply = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt') 

# Декодируем их, так как используется кодировка "windows-1251"
russian_words = first_reply.content.decode('cp1251')
list_words = russian_words.splitlines()
list_words

numbers = [int(random.random()*1000000) for x in range(100)]
words4print = []
for i in numbers: words4print.append(list_words[i])
root = Tk()
root.title("DieMonkeytype")
root.geometry("1200x500+300+200")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
time = 60
check = {'r':0, 'w':0}
speed = 0
'''
def symbols():
    s_len = len(s)
    l3.config(text= "Количество введённых символов: {}".format(s_len))
    root.after(50, symbols)
'''

def start():
    global time, word, i
    b1['state']='disabled'
    entry.config(state="normal")
    entry.focus_set() 
    i=0
    word = words4print[i]
    canvas.create_text(150, 50, text=word, font=("Helvetica", 24), tags="text_id")
    if time > 0:
        time -= 1
        l4.config(text= int(time))
        root.after(1000, timer)
    if not time: 
        l1.config(text= "Время вышло!",font = 'Helvetica 22', fg= "red")
        entry['state']='disabled'
        b1['state']='disabled'
        canvas.delete("text_id")
        return 0


def проверить(event=None):
  global word
  введенный_текст = entry.get().strip()
  if введенный_текст == word:
    check['r']+=1
    canvas.delete("text_id")
  else:
    check['w']+=1
  обновить_текст()

def обновить_текст():
  global word, i
  i+=1
  word = words4print[i]
  l2.config(text=words4print[(i+1):(i+6)])
  entry.delete(0, END) 
  canvas.delete("text_id")
  canvas.create_text(150, 50, text=word, font=("Helvetica", 24), tags="text_id")
  stats.delete("stats_id")
  stats.create_text(250, 50, text=f"Правильно введенных слов: {check.get('r')} \nНеправильно введенных слов {check.get('w')}", font=("Helvetica", 18), tags="stats_id")

def speed_update():
    global speed, time
    speed = int((check.get('r')/(61-time))*60)
    stats.delete("speed_id")
    stats.create_text(700, 50, text=f"Скорость: {speed} слов в минуту", font = ("Helvetica", 22), tags="speed_id")
    while time!=0: root.after(500, speed_update)
        
l1= Label(text = "Вводите появляющиеся слова, разделяя пробелами", width = 50, font = 'Helvetica 16')
l1.place(x = 180, y = 10)
l2 = Label(root, text=words4print[:6], wraplength=800, font = 'Helvetica 16')
l2.place(x = 370, y = 120)
l3= Label(text = "Статистика: ", width = 30, font = 'Helvetica 22')
l3.place(x = 75, y = 300)
stats = Canvas(root)
stats.pack()
stats.place(x=100,y=330, width = 900, height=100)
stats.create_text(250, 50, text=f"Правильно введенных слов: {check.get('r')} \nНеправильно введенных слов {check.get('w')}", font=("Helvetica", 18), tags="stats_id")
stats.create_text(700, 50, text=f"Скорость: {speed} слов в минуту", font = ("Helvetica", 22), tags="speed_id")
l4= Label(text = int(time), width = 5, font = 'Helvetica 25')
l4.place(x = 800, y = 10)

entry = Entry(root, font=('Helvetica',20))
entry.place(x=120, y=200, width = 350, height=60)

canvas = Canvas(root, width=120, height=100)
canvas.pack()
canvas.place(x=10, y=82, width = 350, height=100)


b1= Button(text = "Начать игру", command = start, width = 15, height = 2)
b1.place(x = 500, y = 220)
#symbols()
entry.bind("<space>", проверить) 


speed_update()
entry.config(state="disabled")
root.mainloop()
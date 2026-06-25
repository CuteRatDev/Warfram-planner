import random
import sqlite3
from tkinter import *
from tkinter.font import BOLD

connmd = sqlite3.connect('mastery.db')
connmd.row_factory = sqlite3.Row  # lets you access columns by name, like a dict
cur = connmd.cursor()

def warframe_random():
    cur.execute('SELECT * FROM warframes WHERE has_build = 0')
    no_build_warframes = cur.fetchall()

    if not no_build_warframes:
        result_label.config(text="No frames without a build!")
        return

    pick = random.choice(no_build_warframes)
    result_label.config(text=f"Build and fashion: {pick['name']}")
    print(dict(pick))


tlrh = Tk()
tlrh.geometry('1080x720')
tlrh.title('Tenno Lil Rat Helper')
tlrh.config(bg='#B482BA')

test_label = Label(tlrh, text="Tenno Lil Rat Helper", font=("Arial", 30, BOLD), fg='#CF345D', bg='#B482BA')
test_label.pack()

random_wf_bt = Button(tlrh, text="Random build selection", bg='pink', command=warframe_random)
random_wf_bt.pack()

result_label = Label(tlrh, text="", font=("Arial", 18), fg='#CF345D', bg='#B482BA')
result_label.pack()

tlrh.mainloop()
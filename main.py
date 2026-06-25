import random
import json
from tkinter import *
from tkinter.font import BOLD

with open('mastery.json', 'r') as file:
    mastery_json = json.load(file)
print((mastery_json['warframe'][1]))
no_build_warframe = []
def warframe_random():
    numframe = 0
    for war in mastery_json['warframe']:
        war = (mastery_json['warframe'][numframe])
        if not war['has_build']:
            no_build_warframe.append((mastery_json['warframe'][numframe]))
        numframe += 1
    random_weapon_selc = random.choice(no_build_warframe)
    print(random_weapon_selc)



tlrh = Tk()
tlrh.geometry('1080x720')
tlrh.title('Tenno Lil Rat Helper')
tlrh.config(bg='#B482BA')
test_label = Label(tlrh, text="Tenno Lil Rat Helper",font=("Arial", 30, BOLD), fg='#CF345D', bg='#B482BA')
test_label.pack()

randon_wf_bt = Button(tlrh,
    text="Random build selection",
    bg='pink',
    command=warframe_random,
                      )
randon_wf_bt.pack()


tlrh.mainloop()


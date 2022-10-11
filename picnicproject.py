from tkinter import *
import random

root = Tk()
root.title("List")
root.geometry("400x400")

random_food_list = Label(root, text = "Food Items- Bread, Pizza, Water, Jam, Blanket, Chips, Juice")
item = Label(root, text = "Put Item number _ in the bag")

def randomList():
    randomList = random.sample(range(0, 6),1)
    item["text"] = "Put Item number " + str(randomList) + " in the bag"

btn = Button(root, text = "Generate Random Food Item ", command=randomList)
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)

random_food_list.place(relx = 0.5, rely = 0.4, anchor=CENTER)
item.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()
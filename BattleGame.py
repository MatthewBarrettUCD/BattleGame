import sys
import tkinter

class player:
    def __init__(self, name, fighter):
        self.name = name
        self.fighter = fighter
        self.heatlh = 100
    
    def updateHealth(health,amount):
        health = health + amount

    def printInfo(self):
        print("Player name: " + self.name + ", Fighter: " + self.fighter)

class fighter:
    def __init__(self, name, attack, defense, strength, cardio):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.strength = strength
        self.cardio = cardio
    
    def printInfo(self):
        print("\n",self.name,"\n\nAttack - " ,self.attack, "\nDefense - " ,self.defense, "\nStrength - " ,self.strength, "\nCardio - ",self.cardio)



#defaultFighters = {"Jon Jones":fighter("Jon Jones",9,8,9,8),"Daniel Cormier":fighter("Daniel Cormier",9,7,6,9),"Luke Rockhold":
#fighter("Luke Rockhold",9,5,8,7),"Francis Ngannou":fighter("Francis Ngannou",10,6,8,4)}

points = 20
namecounter = 0
fightername = ""
fighterstats = {"Attack":0,"Defense":0, "Strength":0, "Cardio":0}
stats = ["Attack", "Defense", "Strength", "Cardio"]

def nextScreen():
    global namecounter
    global fightername
    if namecounter == 0:
        fightername += ent.get()
        namecounter += 1
        lbl.configure(text = "Welcome to Mixed Martial Madness!\nPlease enter a name for you fighter:\nSurname:")
        ent.delete(0,"end")
    else:
        fightername += " "
        fightername += ent.get()
        lbl.configure(text = "Welcome " + fightername)
        btn.pack_forget()
        ent.pack_forget()
        lbl.pack_forget()
        statSelection()

def statSelection():
    r=0
    global points
    tkinter.Button(window, text = "-", command = lambda: decreaseStat("Attack")).grid(row=r, column=0)
    tkinter.Label(window, text = "Attack").grid(row=r, column=1)
    tkinter.Button(window, text = "+", command = lambda: increaseStat("Attack")).grid(row=r, column=2)
    lblx = tkinter.Label(window, text = fighterstats["Attack"]).grid(row=r, column=3)
    r += 1
    tkinter.Button(window, text = "-", command = lambda: decreaseStat("Defense")).grid(row=r, column=0)
    tkinter.Label(window, text = "Defense").grid(row=r, column=1)
    tkinter.Button(window, text = "+", command = lambda: increaseStat("Defense")).grid(row=r, column=2)
    tkinter.Label(window, text = fighterstats["Defense"]).grid(row=r, column=3)
    r += 1
    tkinter.Button(window, text = "-", command = lambda: decreaseStat("Strength")).grid(row=r, column=0)
    tkinter.Label(window, text = "Strength").grid(row=r, column=1)
    tkinter.Button(window, text = "+", command = lambda: increaseStat("Strength")).grid(row=r, column=2)
    tkinter.Label(window, text = fighterstats["Strength"]).grid(row=r, column=3)
    r += 1
    tkinter.Button(window, text = "-", command = lambda: decreaseStat("Cardio")).grid(row=r, column=0)
    tkinter.Label(window, text = "Cardio").grid(row=r, column=1)
    tkinter.Button(window, text = "+", command = lambda: increaseStat("Cardio")).grid(row=r, column=2)
    tkinter.Label(window, text = fighterstats["Cardio"]).grid(row=r, column=3)
    r += 1
    tkinter.Label(window, text = "Available points").grid(row=r, column=1)
    tkinter.Label(window, text = points).grid(row=r, column=3)

def increaseStat(stat):
    global points
    if points != 0 and fighterstats[stat] != 10:
        points -= 1
        fighterstats[stat] += 1
        statSelection()

def decreaseStat(stat):
    global points
    if fighterstats[stat] != 0:
        points += 1
        fighterstats[stat] -= 1
        statSelection()


window = tkinter.Tk()
window.title("Mixed Martial Madness")
window.geometry("300x300")
window.configure(background = "sienna2")

lbl = tkinter.Label(window, text="Welcome to Mixed Martial Madness!\nPlease enter a name for you fighter:\nFirst Name:", bg ="sienna2")

ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Enter", command = lambda: nextScreen())

lbl.pack()
ent.pack()
btn.pack()

window.mainloop()

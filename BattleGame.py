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
    def __init__(self, name, attack, defense, reach, cardio):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.reach = reach
        self.cardio = cardio
    
    def printInfo(self):
        print("\n",self.name,"\n\nAttack - " ,self.attack, "\nDefense - " ,self.defense, "\nReach - " ,self.reach, "\nCardio - ",self.cardio)

def intro():
    print("Welcome to Mixed Martial Madness!")
    player(input("Please enter your name!"), input("Please choose your fighter"))


defaultFighters = {"Jon Jones":fighter("Jon Jones",9,8,9,8),"Daniel Cormier":fighter("Daniel Cormier",9,7,6,9),"Luke Rockhold":
fighter("Luke Rockhold",9,5,8,7),"Francis Ngannou":fighter("Francis Ngannou",10,6,8,4)}

window = tkinter.Tk()
window.title("Mixed Martial Madness")
window.geometry("300x300")
window.configure(background = "sienna2")

lbl = tkinter.Label(window, text="Welcome to Mixed Martial Madness!\nPlease enter your name:", bg ="sienna2")

ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Enter")

lbl.pack()
ent.pack()
btn.pack()

window.mainloop()

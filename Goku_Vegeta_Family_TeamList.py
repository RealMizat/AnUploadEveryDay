import tkinter as tk
from tkinter import ttk

#def callbackFunc():
    #resultString.set("{} - {}".format(goku.get(), vegeta.get()))

root = tk.Tk()
root.geometry('400x500')

goku_units = ['TEQ SSJ Goku LR', 'INT Gohan LR', 'STR Pan LR']

vegeta_units = ['INT Super Vegeta Cell', 'ALG SSJ2 Vegeta Revived']

def update_goku():
    clear_listbox
    for unit in goku_units:
        lb_goku.insert("end", unit)

def update_vegeta():
     clear_listbox
     for unit in goku_units:
        lb_vegeta.insert("end", unit)

def add_goku_fam():
    update_goku()

def add_vegeta_fam():
    update_vegeta()


    

def clear_listbox():
    lb_tasks.delete(0, "end")

gokuFam = tk.Label(root, text = 'Goku Family')
gokuFam.grid(row = 1, column =1)

vegetaFam = tk.Label(root, text = 'Vegeta Family')
vegetaFam.grid(row = 1, column = 3)

#hybridSaiyan = tk.Label(root, text = 'Hybrid Saiyan')

add_goku_button = tk.Button(root, command = update_goku)
add_goku_button.grid(row = 2, column = 1)

add_vegeta_button = tk.Button(root, command = update_vegeta)
add_vegeta_button.grid(row = 2, column = 3)

lb_goku = tk.Listbox(root, bg = 'gray', fg = 'black')
lb_goku.grid(row = 4, column = 1)

lb_vegeta = tk.Listbox(root, bg = 'gray', fg = 'black')
lb_vegeta.grid(row = 4, column = 3)

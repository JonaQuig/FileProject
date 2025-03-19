from tkinter import *
import tkinter as tk

window = Tk()
window.geometry('700x420')
window.title("File: Movie Field")

# Declare StringVar variables
name_var = tk.StringVar()
director_var = tk.StringVar()

# Defining a function that will
# get the name and director and
# print them on the screen
def submit():
    name = name_var.get()
    director = director_var.get()
    print("Movie: " + name)
    print("Director: " + director)
    name_var.set("")
    director_var.set("")

# Widgets
movie_label = tk.Label(window, text='Movie', font=('calibre', 10, 'bold'))
movie_entry = tk.Entry(window, textvariable=name_var, font=('calibre', 10, 'normal'))
director_label = tk.Label(window, text='Director', font=('calibre', 10, 'bold'))
director_entry = tk.Entry(window, textvariable=director_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(window, text='Submit', command=submit)

content = tk.Label(window, text='Content', font=('calibre', 10, 'bold'))

# Grid placement
movie_label.grid(row=0, column=0)
movie_entry.grid(row=0, column=1)
director_label.grid(row=1, column=0)
director_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)
content.grid(row=4, column=0)

# Call mainloop
window.mainloop()
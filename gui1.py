from tkinter import *
import tkinter as ttk

window = Tk()

window.title("Main_Screen")
window.geometry('400x400')
w = Label(window, text="What file would you like to visit?")

w.pack()


window.mainloop()




#def manage_text_file(file_path):
 #   while True:
  #      try:
   #         with open(file_path, 'r+') as file:
    #            content = file.readlines()
     #           print("Current content:")
      #          for line in content:
       #             print(line.strip())
        #        new_info = input(GREEN + "Enter new information to add (or leave empty): ")
         #       if new_info:
          #          content.append(new_info + '\n')
           #     delete_info = input("Enter information to delete (or leave empty): " + RESET)
            #    new_content = []
             #   for line in content:
              #      new_line = line.replace(delete_info, "")
               #     new_content.append(new_line)
                #content = new_content  # Replace with new_content
#file_path =
#manage_text_file(file_path)
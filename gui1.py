from tkinter import *
# base window
root = Tk()
root.geometry('600x500')
root.title('Main Screen')

options = []

def load_file():
    try:
        with open('listbox_options.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
options = load_file()
def save_file():
    with open('listbox_options.txt', 'w') as file:
        for option in options:
            file.write(option + '\n')

# for file
def add_file():
    entry = File_Entry.get()
    if entry:
        options.append(entry)
        listbox.insert(END, entry)
        save_file()
def delete_file():
    selected_option = listbox.curselection()
    if selected_option:
        selected_index = selected_option[0]
        selected_item = listbox.get(selected_index)
        options.remove(selected_item)
        listbox.delete(selected_index)
        save_file()
File_Entry = Entry(root)
File_Entry.pack()

Add_button = Button(root, text='Add File', command=add_file)
Add_button.pack()

Delete_button = Button(root, text='Delete File', command=delete_file)
Delete_button.pack()

Label(root, text='What file would you like to visit?').pack(pady=20)

listbox = Listbox(root)
listbox.pack()

RClose_Button = Button(root, text='Close', command=root.destroy)
RClose_Button.place(x=530, y=445)

for option in options:
    listbox.insert(END, option)

def open_selected_window():
    selected = listbox.curselection()
    if selected:
        selected_option = listbox.get(selected[0])
        new_opened_window(selected_option)
Button(root, text="Open Window", command=open_selected_window).pack(pady=20)

label_objects = []
y_position = 100

def new_opened_window(selected_option):
    new_window = Toplevel(root)
    new_window.title(selected_option)
    new_window.geometry('450x500')
    Label(new_window, text=f'{selected_option}').pack(pady=10)
    Button(new_window, text='Close', command=new_window.destroy).place(x=380, y=445)
    window_entry = Entry(new_window, width=28)
    window_entry.place(x=10, y=50)
    delete_entry = Entry(new_window, width=28)
    delete_entry.place(x=260, y=50)

    file_name_window = f"{selected_option}.txt" #create .txt file if not already there
    try:
        with open(file_name_window, 'r'):
            pass
    except FileNotFoundError:
        with open(file_name_window, 'w'):
            pass

    def load_labels():
        try:
            with open(file_name_window, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    labels = load_labels()
    y_position = 100
    for label_text in labels:
        hidden_label = Label(new_window, text=label_text)
        hidden_label.place(x=10, y=y_position)
        label_objects.append(hidden_label)
        y_position += 20

    def add_hidden_label():
        global y_position
        text = window_entry.get()
        if text:
            hidden_label = Label(new_window, text=text)
            hidden_label.place(x=10, y=y_position)
            label_objects.append(hidden_label)
            y_position += 20 # make sure next entry on next hidden label/line
            window_entry.delete(0, END)
            with open(file_name_window, 'a') as file: # append/add to the file
                file.write(text + '\n')

    def delete_label():
        text_to_delete = delete_entry.get()
        labels_to_delete = []
        for label in label_objects:
            if label['text'] == text_to_delete:  # if the text in the label is equivalent to the entries text...
                labels_to_delete.append(label)
        if labels_to_delete:
            for label_to_delete in labels_to_delete:
                label_to_delete.destroy()
                label_objects.remove(label_to_delete)
                global y_position
                y_position -= 20
            with open(file_name_window, 'w') as file: # rewrite file so that it doesn't hold deleted items
                for label in label_objects:
                    file.write(label['text'] + '\n')
        delete_entry.delete(0, END)

    hid_add_button = Button(new_window, text='Add', command=add_hidden_label)
    hid_add_button.place(x=10, y =75)

    label_del_button = Button(new_window, text='Delete', command=delete_label)
    label_del_button.place(x=260, y =75)

root.mainloop()

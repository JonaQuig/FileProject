def manage_text_file(file_path):
    try:
        with open(file_path, 'r+') as file:
            content = file.readlines()  # Read lines for easier manipulation
            print("Current content:")
            for line in content:
                print(line.strip()) # strip to remove extra newline characters
            new_info = input("Enter new information to add (or leave empty): ")
            if new_info:
                content.append(new_info + '\n')  # Add a newline character
            delete_info = input("Enter information to delete (or leave empty): ")
            if delete_info:
                for line in content:
                    content = line.replace(delete_info, "")

            file.seek(0)
            file.truncate()
            file.writelines(content) # write the updated content

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Creating a new file.")
        with open(file_path, 'w') as file:
            new_info = input("Enter initial information for the new file (or leave empty): ")
            if new_info:
                file.write(new_info + '\n')

file_path = "Movie_Dictionary.txt"
manage_text_file(file_path)
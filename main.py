RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
def manage_text_file(file_path):
    while True:  # Start File add/delete loop
        try:
            with open(file_path, 'r+') as file:
                content = file.readlines()
                print("Current content:")
                for line in content:
                    print(line.strip())
                new_info = input(GREEN + "Enter new information to add (or leave empty): ")
                if new_info:
                    content.append(new_info + '\n')
                delete_info = input("Enter information to delete (or leave empty): " + RESET)
                new_content = []
                for line in content:
                    new_line = line.replace(delete_info, "")
                    new_content.append(new_line)
                content = new_content  # Replace with new_content

                file.seek(0)  # Reset: Move file pointer to beginning
                file.truncate()  # Clear: Remove existing content
                file.writelines(content)  # Update file with new content

        except FileNotFoundError:
            print(f"File '{file_path}' not found. Creating a new file.")
            with open(file_path, 'w') as file:
                new_info = input("Enter initial information for the new file (or leave empty): ")
                if new_info:
                    file.write(new_info + '\n')

        continue_choice = input(BLUE + "Would you like to keep adding/deleting? (yes/no): " + RESET).lower()
        if continue_choice != 'yes':
            break  # leave loop if not yes

file_path = "Movie_Dictionary.txt"
manage_text_file(file_path)
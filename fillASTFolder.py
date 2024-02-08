import shutil
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger

def main():
    # Hide the main tkinter window
    Tk().withdraw()
    
    # Ask to select a file
    source_file_path = askopenfilename(title="Select a file")
    if not source_file_path:  # If the user cancels the selection
        print("No file selected. Exiting...")
        return

    # Ask for the number of question copies
    num_question_copies = askinteger("Input", "How many question copies?")
    if not num_question_copies:
        print("Invalid number of question copies. Exiting...")
        return

    # Ask for the number of assignment folders
    num_assignment_folders = askinteger("Input", "How many assignment folders?")
    if not num_assignment_folders:
        print("Invalid number of assignment folders. Exiting...")
        return

    # Get the directory of the selected file
    destination_folder_path = os.path.dirname(source_file_path)

    # Loop through each assignment folder
    for a in range(1, num_assignment_folders + 1):
        # Ensure the destination folder exists
        assignment_folder_path = os.path.join(destination_folder_path, f"A{a}")
        os.makedirs(assignment_folder_path, exist_ok=True)
        
        # Copy the file as per the number of question copies
        for q in range(1, num_question_copies + 1):
            new_file_name = f"A{a}Q{q}" + os.path.splitext(source_file_path)[1]
            destination_file_path = os.path.join(assignment_folder_path, new_file_name)
            
            # Copy the file
            shutil.copy(source_file_path, destination_file_path)
            print(f"Copied to: {destination_file_path}")

    print("Copying completed.")

if __name__ == "__main__":
    main()

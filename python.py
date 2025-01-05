import os
import shutil
import zipfile
from datetime import datetime

# Log file to record operations
LOG_FILE = "file_manager.log"

def log_operation(operation, status, details=""):
    """Log operations with timestamp, operation name, status, and details."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {operation} - {status} - {details}\n")

def create_file(file_name):
    try:
        with open(file_name, 'w') as f:
            pass
        log_operation("Create File", "Success", f"File '{file_name}' created.")
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        log_operation("Create File", "Error", str(e))
        print(f"Error creating file: {e}")

def edit_file(file_name):
    try:
        content = input("Enter content to append to the file: ")
        with open(file_name, 'a') as f:
            f.write(content + "\n")
        log_operation("Edit File", "Success", f"Content added to '{file_name}'.")
        print(f"Content added to '{file_name}'.")
    except Exception as e:
        log_operation("Edit File", "Error", str(e))
        print(f"Error editing file: {e}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            print(f"\nContents of '{file_name}':\n")
            print(f.read())
        log_operation("Read File", "Success", f"File '{file_name}' read.")
    except Exception as e:
        log_operation("Read File", "Error", str(e))
        print(f"Error reading file: {e}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        log_operation("Delete File", "Success", f"File '{file_name}' deleted.")
        print(f"File '{file_name}' deleted successfully.")
    except Exception as e:
        log_operation("Delete File", "Error", str(e))
        print(f"Error deleting file: {e}")

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        log_operation("Copy File", "Success", f"File '{source}' copied to '{destination}'.")
        print(f"File '{source}' copied to '{destination}'.")
    except Exception as e:
        log_operation("Copy File", "Error", str(e))
        print(f"Error copying file: {e}")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        log_operation("Move File", "Success", f"File '{source}' moved to '{destination}'.")
        print(f"File '{source}' moved to '{destination}'.")
    except Exception as e:
        log_operation("Move File", "Error", str(e))
        print(f"Error moving file: {e}")

def create_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        log_operation("Create Folder", "Success", f"Folder '{folder_name}' created.")
        print(f"Folder '{folder_name}' created successfully.")
    except Exception as e:
        log_operation("Create Folder", "Error", str(e))
        print(f"Error creating folder: {e}")

def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        log_operation("Delete Folder", "Success", f"Folder '{folder_name}' deleted.")
        print(f"Folder '{folder_name}' deleted successfully.")
    except Exception as e:
        log_operation("Delete Folder", "Error", str(e))
        print(f"Error deleting folder: {e}")

def add_file_to_folder(file_name, folder_name):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            log_operation("Create Folder", "Success", f"Folder '{folder_name}' created.")
        destination = os.path.join(folder_name, file_name)
        shutil.move(file_name, destination)
        log_operation("Add File to Folder", "Success", f"File '{file_name}' moved to '{folder_name}'.")
        print(f"File '{file_name}' moved to folder '{folder_name}'.")
    except Exception as e:
        log_operation("Add File to Folder", "Error", str(e))
        print(f"Error adding file to folder: {e}")

def create_zip(folder_name, zip_name):
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for root, _, files in os.walk(folder_name):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_name))
        log_operation("Create Zip", "Success", f"Folder '{folder_name}' zipped as '{zip_name}'.")
        print(f"Folder '{folder_name}' zipped as '{zip_name}'.")
    except Exception as e:
        log_operation("Create Zip", "Error", str(e))
        print(f"Error creating zip file: {e}")

def main():
    while True:
        print("\nFile Manager")
        print("1. Create File")
        print("2. Edit File")
        print("3. Read File")
        print("4. Delete File")
        print("5. Copy File")
        print("6. Move File")
        print("7. Create Folder")
        print("8. Delete Folder")
        print("9. Add File to Folder")
        print("10. Create Zip File")
        print("11. Exit")
        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            file_name = input("Enter the file name: ")
            create_file(file_name)
        elif choice == "2":
            file_name = input("Enter the file name: ")
            edit_file(file_name)
        elif choice == "3":
            file_name = input("Enter the file name: ")
            read_file(file_name)
        elif choice == "4":
            file_name = input("Enter the file name: ")
            delete_file(file_name)
        elif choice == "5":
            source = input("Enter the source file name: ")
            destination = input("Enter the destination file name: ")
            copy_file(source, destination)
        elif choice == "6":
            source = input("Enter the source file name: ")
            destination = input("Enter the destination path: ")
            move_file(source, destination)
        elif choice == "7":
            folder_name = input("Enter the folder name: ")
            create_folder(folder_name)
        elif choice == "8":
            folder_name = input("Enter the folder name to delete: ")
            delete_folder(folder_name)
        elif choice == "9":
            file_name = input("Enter the file name: ")
            folder_name = input("Enter the folder name: ")
            add_file_to_folder(file_name, folder_name)
        elif choice == "10":
            folder_name = input("Enter the folder name to zip: ")
            zip_name = input("Enter the zip file name (with .zip extension): ")
            create_zip(folder_name, zip_name)
        elif choice == "11":
            log_operation("Exit", "Success", "User exited the program.")
            print("Exiting File Manager. Goodbye!")
            break
        else:
            log_operation("Invalid Choice", "Error", f"User entered invalid choice: {choice}")
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Initialize log file
    with open(LOG_FILE, "w") as log:
        log.write("File Manager Log\n")
        log.write("=" * 50 + "\n")
    main()
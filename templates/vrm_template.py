import os
import subprocess

# Import modules from the defaults directory
from defaults.create_common_files import create_common_files
from defaults.create_gitignore import create_gitignore

def create_file(path, content=''):
    """Create a file with the given content."""
    with open(path, 'w') as file:
        file.write(content)

def create_project_structure(target_directory):
    """Create the project structure based on the project type."""
    # Common Directories
    directories = [
        'vrm-project/blends', 'vrm-project/files', 
        'vrm-project/metadata', 'vrm-project/scripts', 'vrm-project/vrms/beta',
        '.github/workflows', '.github/ISSUE_TEMPLATE'
    ]

     # Check if the target directory already exists
    if os.path.exists(target_directory):
        while True:
            user_input = input(f"The directory '{target_directory}' already exists. Do you want to proceed? (yes/no): ")
            if user_input.lower() == 'yes':
                break
            elif user_input.lower() == 'no':
                print("Exiting.")
                return
            else:
                print("Please enter 'yes' or 'no'.")

    # Create the directories in the specified target directory
    for directory in directories:
        os.makedirs(os.path.join(target_directory, directory), exist_ok=True)
        
    # Create common files in the target directory
    os.chdir(target_directory)
    create_common_files()

    # Create .gitignore file
    create_gitignore()

    print("Project structure created successfully.")

def install_frontend_libraries():
    """Install frontend libraries for a web project."""
    # try:
        # subprocess.run(["npm", "install", "react", "react-dom", "three"], check=True)
        # Add other libraries as needed
    # except Exception as e:
        # print(f"Error installing libraries: {e}")

if __name__ == "__main__":
    target_directory = os.environ.get("TARGET_DIRECTORY")
    create_project_structure(target_directory)
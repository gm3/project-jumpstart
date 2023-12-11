import os
import subprocess
from common_setup import create_common_files
from create_gitignore import create_gitignore

def create_file(path, content=''):
    """Create a file with the given content."""
    with open(path, 'w') as file:
        file.write(content)

def create_project_structure():
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

def create_common_files():
    """Create common files for any project type."""
    # Common files are created here
    create_file('README.md', '# Project Title\n\nDescription of the project.\n')
    create_file('LICENSE', 'MIT License\n\n[Your License Details Here]\n')
    create_file('.env.example', '# Environment variables template\n')
    create_file('CONTRIBUTING.md', '# Contributing Guidelines\n')
    create_file('CODE_OF_CONDUCT.md', '# Code of Conduct\n')
    create_file('.github/ISSUE_TEMPLATE/bug_report.md', '# Bug Report Template\n')
    create_file('.github/ISSUE_TEMPLATE/feature_request.md', '# Feature Request Template\n')
    create_gitignore()
    print("Created common files")

def install_frontend_libraries():
    """Install frontend libraries for a web project."""
    # try:
        # subprocess.run(["npm", "install", "react", "react-dom", "three"], check=True)
        # Add other libraries as needed
    # except Exception as e:
        # print(f"Error installing libraries: {e}")

if __name__ == "__main__":
    target_directory = input("Enter the target directory for your project: ")
    create_project_structure(target_directory)
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
        'cli', 'cli/commands', 'cli/utils','frontend/src', 'frontend/public', 
            'backend/src', 'backend/controllers', 'backend/models', 'backend/routes', 'backend/utils',
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    create_common_files()
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
    create_project_structure()
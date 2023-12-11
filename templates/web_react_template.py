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
        'frontend/src', 'frontend/public',
        'backend/src', 'backend/controllers', 'backend/models', 'backend/routes', 'backend/utils',
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

    # Create web project files
    create_web_project_files()

    # Install frontend libraries
    try:
        subprocess.run(["npm", "install", "react"], check=True)
        # Add other libraries as needed
    except Exception as e:
        print(f"Error installing libraries: {e}")

    print("Project structure created successfully.")

def create_web_project_files():
    """Create files specific to a web project."""
    create_file('frontend/src/App.js', '// Main frontend application file\n')
    create_file('frontend/public/index.html', '<!-- Entry HTML file -->\n')
    create_file('backend/src/server.js', '// Main server file\n')
    create_file('Dockerfile', '# Docker configuration\n')
    create_file('docker-compose.yml', '# Docker Compose configuration\n')
    create_file('.github/workflows/main.yml', '# GitHub Actions CI/CD workflow\n')
    create_file('package.json', '{\n  "name": "new-project",\n  "version": "1.0.0"\n}')
    # Other web project files...

if __name__ == "__main__":
    target_directory = os.environ.get("TARGET_DIRECTORY")
    create_project_structure(target_directory)

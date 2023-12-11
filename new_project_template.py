import os
import subprocess
# Import the template functions with aliases
from templates.web_react_template import create_project_structure as create_web_react_project
from templates.cli_template import create_project_structure as create_cli_project
from templates.vrm_template import create_project_structure as create_vrm_project

# Import modules from the defaults directory
from defaults.create_common_files import create_common_files
from defaults.create_gitignore import create_gitignore

def prompt_project_type():
    """Prompt the user to select the project type."""
    print("Select the project type:")
    print("1. Web/React Project")
    print("2. CLI Tool")
    print("3. VRM Project")  # Corrected the numbering
    choice = input("Enter your choice (1, 2, 3): ")
    return choice

def main():
    target_directory = input("Enter the target directory for your project: ")
    os.environ["TARGET_DIRECTORY"] = target_directory
    project_type = prompt_project_type()
    if project_type == "1":
        create_web_react_project(target_directory)  # Pass the target_directory
    elif project_type == "2":
        create_cli_project(target_directory)  # Pass the target_directory
    elif project_type == "3":
        create_vrm_project(target_directory)  # Pass the target_directory

if __name__ == '__main__':
    main()

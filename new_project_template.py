import os
import subprocess
# Import the template functions
from templates.web_react_template import create_project_structure
from templates.cli_template import create_project_structure
from templates.vrm_template import create_project_structure

# Import modules from the defaults directory
from defaults.create_common_files import create_common_files
from defaults.create_gitignore import create_gitignore

def prompt_project_type():
    """Prompt the user to select the project type."""
    print("Select the project type:")
    print("1. Web/React Project")
    print("2. CLI Tool")
    print("4. VRM Project")
    choice = input("Enter your choice (1, 2, 3): ")
    return choice

def main():
    project_type = prompt_project_type()
    if project_type == "1":
        create_web_react_project()
    elif project_type == "2":
        create_cli_project()
    elif project_type == "3":
        create_vrm_project()
        

if __name__ == '__main__':
    main()

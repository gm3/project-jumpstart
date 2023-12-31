import os
# Import modules from the defaults directory
from defaults.create_common_files import create_common_files
from defaults.create_gitignore import create_gitignore

def create_file(path, content=''):
    """Create a file with the given content."""
    # Ensure the directory exists before creating a file
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        file.write(content)

def create_project_structure(target_directory):
    """Create the project structure based on the project type."""
    # Common Directories
    directories = ['src', 'assets', 'public','.github/workflows', '.github/ISSUE_TEMPLATE']

    # Check if the target directory already exists
    if os.path.exists(target_directory):
        user_input = input(f"The directory '{target_directory}' already exists. Do you want to proceed? (yes/no): ")
        if user_input.lower() != 'yes':
            print("Exiting.")
            return

    # Create the directories in the specified target directory
    for directory in directories:
        full_path = os.path.join(target_directory, directory)
        os.makedirs(full_path, exist_ok=True)

    # Create common files in the target directory
    create_static_website(target_directory)

    # Create common files in the target directory
    os.chdir(target_directory)
    create_common_files()

    # Create .gitignore file
    create_gitignore()

    print("Project structure created successfully.")

def create_static_website(target_directory):
    # Create common files
    index_html_path = os.path.join(target_directory, 'src', 'index.html')
    styles_css_path = os.path.join(target_directory, 'src', 'styles.css')
    workflows_path = os.path.join(target_directory, '.github/workflows', 'main.yml')
    package_json_path = os.path.join(target_directory, 'package.json')

     # Raw HTML and CSS content
     # Read HTML and CSS from external files
    with open('defaults/static_website/template.html', 'r') as file:
        raw_html = file.read()

    with open('defaults/static_website/template.css', 'r') as file:
        raw_css = file.read()

    # Creating files
    create_file(index_html_path, raw_html)
    create_file(styles_css_path, raw_css)
    create_file(workflows_path, '# GitHub Actions CI/CD workflow\n')
    create_file(package_json_path, '{\n  "name": "new-project",\n  "version": "1.0.0"\n}')


if __name__ == "__main__":
    target_directory = os.environ.get("TARGET_DIRECTORY")
    create_project_structure(target_directory)

# Project Jumpstart

Project Jumpstart is a Python script designed to streamline the creation of new development projects. It automates the setup of a typical project structure, allowing you to focus on the actual development right from the start.

## Features

- Generates a basic project structure for projects
- Easy to extend with more project templates.

![image](https://github.com/gm3/project-jumpstart/assets/7612104/e585f52c-0bca-474d-8636-4f667fd945c9)


## Usage
To use this script, follow these steps:

1. **Clone or Download the Script**: First, clone this repository or download the script to your local machine.

2. **Run Script**: Open your terminal or command prompt and navigate to the directory where the script is located. Run `python3 new_project_tempalte.py` from the command line.

3. **Select Project Type**: The script will prompt you to select the type of project you want to create. Input the number corresponding to your desired project type:
   - `1`: Web/React Project
   - `2`: CLI Tool
   - `3`: VRM Project

4. **Follow the Prompts**: After selecting a project type, the script will guide you through any additional steps or information needed to set up the project.

5. **Project Creation**: The script will create the necessary project structure and files in your current directory.


## Extending

To add a new project template:
1. Create a new `.py` file in the `templates/` directory with your project structure logic.
2. Import and integrate the new template into the main script following the existing pattern.

## Contributing

We welcome pull requests for new features, bug fixes, and additional project configurations. Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

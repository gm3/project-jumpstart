# Project Jumpstart

Project Jumpstart is a Python script designed to streamline the creation of new development projects. It automates the setup of a typical project structure, allowing you to focus on the actual development right from the start.

## Features

- Generates a basic project structure for projects
- Easy to extend with more project templates.

![image](https://github.com/gm3/project-jumpstart/assets/7612104/e585f52c-0bca-474d-8636-4f667fd945c9)


## Usage
To use this tool, follow these steps:

`sudo apt update`

`sudo apt install npm`

**Clone or Download the Script**: First, clone this repository or download the script to your local machine.

**Run Script**: Open your terminal or command prompt and navigate to the directory where the script is located. Run `python3 new_project_tempalte.py` from the command line. You can use arements like this:

```
new_project_template.py --help
```

**Here is an example CLI command:**

```
python3 new_project_template.py new_project_name -t web_react
```

**How the CLI is defined in new_project_tempalte.py:**

```
parser.add_argument(
        'target_directory', nargs='?', default=None,
        help='The target directory for the project. \nExample: /path/to/project')

    parser.add_argument(
        '-t', '--type', choices=['web_react', 'cli', 'vrm', 'static_website'],
        help='The type of project to create. Options include: \n'
             'web_react - To create a Web/React project.\n'
             'cli - To create a CLI tool project.\n'
             'vrm - To create a VRM project.\n'
             'static_website - To create a Static Website project.')
```

**Select Project Type**: The script will prompt you to select the type of project you want to create. Input desired project type, currently we have a few starter templates that need work:
   - `web_react`: Web/React Project
   - `cli`: CLI Tool
   - `vrm`: VRM Project
   - `static_website`: a Static Website
    
**Follow the Prompts**: IF the script is used without arguments, it will prompt the user for the `target_directory`, and `project_type` After selecting a project type, the script will guide you through any additional steps or information needed to set up the project.

**Project Creation**: The script will create the necessary project structure and files in your current directory.


## Extending

To add a new project template:
1. Create a new `.py` file in the `templates/` directory with your project structure logic.
2. Import and integrate the new template into the main script following the existing pattern.

## Contributing

We welcome pull requests for new features, bug fixes, and additional project configurations. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

import argparse
import os
from templates.web_react_template import create_project_structure as create_web_react_project
from templates.cli_template import create_project_structure as create_cli_project
from templates.vrm_template import create_project_structure as create_vrm_project
from templates.static_website_template import create_project_structure as create_static_website_project

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Project Initialization Script: This script initializes different types of projects like Web/React, CLI tools, VRM projects, and Static Websites. You can specify the project type and target directory either via command line arguments or through interactive prompts if the arguments are not provided.',
        formatter_class=argparse.RawTextHelpFormatter)

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

    return parser.parse_args()

def prompt_for_missing_info(target_directory, project_type):
    """Prompt for any missing information."""
    if not target_directory:
        target_directory = input("Enter the target directory for your project: ")
    if not project_type:
        project_type = input("Enter the project type (web_react, cli, vrm, static_website): ")
    return target_directory, project_type

def main():
    args = parse_arguments()
    target_directory, project_type = prompt_for_missing_info(args.target_directory, args.type)

    if project_type == "web_react":
        create_web_react_project(target_directory)
    elif project_type == "cli":
        create_cli_project(target_directory)
    elif project_type == "vrm":
        create_vrm_project(target_directory)
    elif project_type == "static_website":
        create_static_website_project(target_directory)
    else:
        print("Invalid project type. Please choose from 'web_react', 'cli', 'vrm', 'static_website'.")

if __name__ == '__main__':
    main()

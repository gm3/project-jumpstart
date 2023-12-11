import os
import subprocess

def create_file(path, content=''):
    """Create a file with the given content."""
    with open(path, 'w') as file:
        file.write(content)

def create_common_files():
    """Create common files for the project."""
    create_file('README.md', '# Project Title\n\nDescription of the project.\n')
    create_file('LICENSE', 'MIT License\n\n[Your License Details Here]\n')
    create_file('.env.example', '# Environment variables template\n')
    create_file('CONTRIBUTING.md', '# Contributing Guidelines\n')
    create_file('CODE_OF_CONDUCT.md', '# Code of Conduct\n')
    create_file('.github/ISSUE_TEMPLATE/bug_report.md', '# Bug Report Template\n')
    create_file('.github/ISSUE_TEMPLATE/feature_request.md', '# Feature Request Template\n')

# Call this function from the main execution block or another function
if __name__ == "__main__":
    create_common_files()

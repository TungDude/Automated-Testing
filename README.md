# Automated-Testing
Take-Home Assignment: Test Automation Challenge

## Prerequisites

1. Install Python (version 3.x) if you don't already have it. You can download it from [python.org](https://www.python.org/).
2. Make sure `pip` (Python's package manager) is installed. It usually comes with Python.
3. Install `virtualenv` if it's not already installed:

   ```bash
   pip install virtualenv

## Setting up the project

1. Clone the repository to your local machine, Using [this](https://github.com/TungDude/Automated-Testing.git) url.
   
   ```bash
   git clone <url>
   
3. Navigate to the project directory.
4. Create a virtual environment.
   
   ```bash
   python -m venv venv
   
5. Activate the virtual environment.
   
   - macOS/Linux
     
     ```bash
     source venv/bin/activate
     
   - Windows
     
     ```bash
     venv\Scripts\activate
     
7. Install the required libraries from requirements.txt

## Running tests with PyTest

1. Ensure the virtual environment is activated.
2. Run the test using this command at the root of the project directory.
   
   ```bash
   pytest -v tests/test_nocnoc.py
   
4. When you are finished with testing, deactivate the virtual environment.
   
   ```bash
   deactivate

### Feel free to reach out for any questions or issues.

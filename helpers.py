import os, sys

def check_venv():
    """
    Check if the script/notebook is running in the correct virtual environment.
    Check for the existence of a local .venv directory, then check if this script is being run from within it.
    """

    if not os.path.exists('.venv'):
        print('No virtual environment found.')
        print('Make sure to follow the instructions, including the `python -m venv .venv` command!')
        print('You may need to restart Visual Studio Code after creating the virtual environment.')
        print('On Mac or Linux, you may need to use `python3` instead of `python`, i.e. `python3 -m venv .venv`.')
        return False
    elif not sys.prefix.endswith('.venv'):
        print('Please run this script from within the virtual environment.')
        print('Check if, in the right top of the notebook, your .venv virtual environment is selected.')
        print('If not, select it from the dropdown menu.')
        print('You may need to restart Visual Studio Code after creating the virtual environment before you can select it.')
        return False
    else:
        return True

def check_pandas():
    """
    Check if pandas is installed.
    """

    try:
        import pandas
        return True
    except ImportError:
        print('pandas is not installed.')
        print('Make sure to follow the instructions, including the `pip install pandas` command.')
        print('You need to install pandas in your virtual environment from the terminal.')
        print('If you don\'t see a green (.venv) in your terminal, try manually activating the virtual environment first:')
        print('Run `source .venv/bin/activate` on Mac or Linux, or `./.venv/Scripts/Activate.ps1` on Windows.')
        return False

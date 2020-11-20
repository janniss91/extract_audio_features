# Extraction of Audio Features for Speech Language Identification

## Setup

For the setup of this repository simply type:

    make

This will

- set up a virtual environment for this repository,
- install all necessary project dependencies.

If this does not work, make sure you have the package `virtualenv` installed for your python interpreter (`pip install virtualenv`).

## Virtual Environment

After having run the `make` command you will have installed a virtual environment.  
Always work in this environment to make sure to use the correct python interpreter and have access to the relevant dependencies.

To enter the environment in a shell, type:

    . env/bin/activate

If you work in an IDE like e.g. Pycharm, make sure that it also makes use of the correct Python interpreter.

To deactivate the virtual environment, type:

    deactivate

## Clean and Re-install

To reset the repository to its inital state, type:

    make dist-clean

This will remove the virtual environment and all dependencies.  
With the `make` command you can re-install them.

To remove temporary files like .pyc or .pyo files, type:

    make clean
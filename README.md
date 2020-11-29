# Extraction of Audio Features for Speech Language Identification

This repository aims at feature extraction from WAV files.

The following features can be extracted:

- MFCCs
- Delta-MFCCs (1st and 2nd order)

Additionally, the following information is retrieved from the audio files:

- file name
- duration of the audio
- number of samples
- sampling rate

## Python Version and Dependencies

It is recommended that you use **Python 3.8** to set up your virtualenv (see setup section).

The following dependencies will be installed:

- librosa (0.8.0)

## Setup

For the setup of this repository simply type:

    make

This will

- set up a virtual environment for this repository,
- install all necessary project dependencies.

If this does not work, make sure you have the package `virtualenv` installed for your python interpreter (`pip install virtualenv`).

## Extract Audio Features

To have features extracted from a series of audio files, `extract_mfcc.py` takes a list of file names as an argument.

For example:

    python3 extract/extract_mfcc.py path/file1.wav path/file2.wav

For all audio files in a directory:

    python3 extract/extract_mfcc.py path/*

## Clean and Re-install

To reset the repository to its inital state, type:

    make dist-clean

This will remove the virtual environment and all its dependencies.  
With the `make` command you can re-install them.

To remove temporary files like .pyc or .pyo files, type:

    make clean

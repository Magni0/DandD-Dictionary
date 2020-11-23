# D&D Dictionary

## What It Is

This application uses [this](https://www.dnd5eapi.co/) 5th edition dungeons and dragons API to provide a player with any infomation in the official books in a neat an easy to digest format. The player can also save the info into a text file to refer to later if they wish. Players now no longer need to carry around 5 books to play D&D.

## Installation

1. Navigate to the dir you wish to have the software and clone it with this command:

    `git clone https://github.com/Magni0/DandD-Dictionary.git`

2. Create an new virtual enviroment with this command:

    `python -m venv venv`

    If python isnt installed it can be downloaded [here](https://www.python.org/downloads/) for windows or

    ```bash
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install python3.8
    ```

    for linux

3. Activate the virtual enviroment:

    for windows (cmd)

    `source venv\Scripts\activate.bat`

    for linux (bash)

    `source venv/bin/activate`

4. Install dependencies:

    `pip3 install -r requirements.txt`

    If you don't have pip then a guide for it can be found [here](https://pip.pypa.io/en/stable/installing/)

5. Then the app can be run by:

    `python {pathtofile}/main.py`

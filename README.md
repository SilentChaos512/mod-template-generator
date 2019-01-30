# Mod Template Generator

Creates some common files and folder, substituting values like mod ID where needed. Creates everything needed for a basic, functioning mod. You can also edit the template files (in the `template` folder) if you know what you are doing.

This program goes through every file in the `template` directory and looks for text in the form of `$SOME_KEY$`, replacing it with the value in `config.json`. For example, anywhere a file contains `$MOD_ID$`, it is replaced by the `MOD_ID` listed in the config. The modified files can be found in the `output` directory (which will be created when you run the program). Empty directories are also copied.

Make sure `PACKAGE` matches the `USER_NAME` and `MOD_ID` configs, otherwise the directory names will not match the packages, and imports will fail. The package should be in the form `something.username.modid`.

## Requirements

- Python 3
- Knowledge of how to edit a JSON file and run a Python program

## How To Use

1. Edit config.json. This is where you set values like the mod ID.
2. Run generate.py (`py ./generate.py`)

## Editing Templates

Files and directories can be added or removed to the template as you see fit. New values can be added to the config as well, and they can be substituted into templates. No modifications of `generate.py` required.

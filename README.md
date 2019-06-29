# Mod Template Generator

Creates some common files and folder, substituting values like mod ID where needed. Creates everything needed for a basic, functioning mod. You can also edit the template files (in the `template` folder) if you know what you are doing.

This program goes through every file in the `template` directory and looks for text in the form of `$SOME_KEY$`, replacing it with the value in `config.json`. For example, anywhere a file contains `$MOD_ID$`, it is replaced by the `MOD_ID` listed in the config. The modified files can be found in the `output` directory (which will be created when you run the program). Empty directories are also copied.

Make sure `PACKAGE` matches the `USER_NAME` and `MOD_ID` configs, otherwise the directory names will not match the packages, and imports will fail. The package should be in the form `something.username.modid`.

The included template has everything needed to get a mod running. If you are using IntelliJ, you just need to import the build.gradle and let ForgeGradle do its thing.

## License Notes

This project is licensed under the **Unlicense**. The template contains a copy of the **MIT license**. If you wish to use a different license, be sure to replace it.

## Requirements

- Python 3
- Knowledge of how to edit a JSON file and run a Python program

## How To Use

1. Edit config.json. This is where you set values like the mod ID.
2. Run generate.py (`py ./generate.py`)
3. When you are happy with the results, move the contents of the `output` directory somewhere else, so your code does not get nuked if you run the program again
4. Enjoy not typing lots of boilerplate code

## Editing Templates

Files and directories can be added or removed to the template as you see fit. New values can be added to the config as well, and they can be substituted into templates. No modifications of `generate.py` required.

# The Config

Details of the config JSON, including where most variables are used. Most of it should be self-explanatory. One important note: the program will crash if it tries to do variable substitutions on binary files. If you add such files to the template, be sure to add the file extension to `ignoredExtensions`.

## Variables

This is a list of variables found in the default `config.json`. You can add additional variables by just adding them to the config. When the template files are being copied to the output directory, any text surrounded by dollar signs ($) on both sides will be substituted with a variable's value. For example, any place you see `$MOD_ID$`, that will be changed to the value of the `MOD_ID` variable.

- **MC_VERSION** - The Minecraft version
- **MC_VERSION_RANGE** - Range of valid Minecraft versions, used in `mods.toml`
- **FORGE_VERSION** - The Forge version
- **FORGE_VERSION_RANGE** - Range of valid Forge versions, used in `mods.toml`
- **MCP_MAPPINGS_CHANNEL** - MCP channel, should be `snapshot` or `stable`
- **MCP_MAPPINGS_VERSION** - MCP mappings, including MC version
- **PACKAGE_GROUP** - Should match `PACKAGE`, but without the part unique to the mod (ie, just com/net/etc + your username)
- **PACKAGE** - The full package path for your mod. This is where the main mod class is located by default
- **USER_NAME** - Your username, used in `build.gradle` and `mods.toml`. This can have capital letters in it if you like.
- **MOD_ID** - The mod ID of the mod. Used in quite a few places. The main mod class stores this in a constant.
- **MOD_CLASS** - The name of your main mod class. Used in a lot of places.
- **MOD_NAME** - User-readable name of the mod (can have capital letters, spaces, symbols, etc), used in `mods.toml`. The main mod class also stores this in a constant.

## Other Settings

- `ignoredExtensions` - Files with these extensions will be **copied, but no variable substitutions are made**. This should include binary files, like JARs.
- `ignoredFiles` - Files with these names will **not be copied or processed**. The template contains many placeholder files, because Git ignores empty directories. You should not need to modify this.

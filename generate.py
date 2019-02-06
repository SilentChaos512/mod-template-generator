import io
import json
import os
import re
import shutil

from datetime import datetime

with open('config.json') as f:
    CONFIG: dict = json.load(f)

if not CONFIG:
    print("config.json is missing!")
    exit(1)


def add_config(key: str, val):
    """ Adds an additional value not present in config.json to the config """
    if not key in CONFIG.keys():
        CONFIG[key] = str(val)


# Add some additional metadata to the config, such as current year
add_config('PACKAGE_PATH', CONFIG['PACKAGE'].replace('.', os.sep))
add_config('YEAR', datetime.now().year)


# Ask user to agree to Minecraft EULA. This creates the eula.txt and sets the
# value to true if the user agrees.
print('This program can generate the eula.txt file for you.')
print('Read the EULA here: (https://account.mojang.com/documents/minecraft_eula)')
if input('Do you agree to the Minecraft EULA? (y/n): ').startswith('y'):
    CONFIG['EULA_COMMENT'] = "User agreed to the EULA when running SilentChaos512's mod template generator"
    CONFIG['EULA_AGREED_TO'] = 'true'
else:
    CONFIG['EULA_COMMENT'] = "User did not agree to EULA"
    CONFIG['EULA_AGREED_TO'] = 'false'


def filtered_config():
    """ Get only the string values from the config """
    return [(k, v) for (k, v) in CONFIG.items() if isinstance(v, str)]


# Print config values, exclusing ignoredExtensions (or anything that is not a str)
print('read config.json:')
for key, value in filtered_config():
    print('  ' + key + ' -> ' + value)


def get_output_path(template_path: str):
    """ Convert the template path to its output path """
    return substitute_config_values(
        template_path
        .replace('template', 'output')
        .replace('ModClass.java', CONFIG['MOD_CLASS'] + '.java')
    )


def make_output_dir(root: str, dir: str):
    """ Create the output subdirectory if it does not exist """
    output_path = get_output_path(os.path.join(root, dir))
    print('makedir: ' + output_path)
    if not os.path.exists(output_path):
        os.makedirs(output_path)


def hasNoProcessExtension(file_name: str):
    """ Determine if the file should not be processed, just copied directly """
    m = re.search(r'(?<=\.)[^.]+', file_name)
    return m.group() in CONFIG['ignoredExtensions'] if m else False


def isIgnoredFile(file_name: str):
    """ Determine if the file is 'ignored', meaning it will not copy to the output directory """
    return file_name in CONFIG['ignoredFiles']


def process_file(root: str, file_name: str):
    """ Process a file, performing substitutions where appropriate """
    print('read file: ' + file_name)

    full_input_path = os.path.join(root, file_name)
    full_output_path = get_output_path(os.path.join(root, file_name))

    if (isIgnoredFile(file_name)):
        # Ignore file, do not copy
        print("ignored: " + full_input_path)
    elif hasNoProcessExtension(file_name):
        # No processing, just copy
        print('processing not allowed, copying file: ' + full_input_path)
        print('copied to: ' + full_output_path)
        shutil.copyfile(full_input_path, full_output_path)
    else:
        # Process file normally, performing substitutions on copy
        with open(full_input_path, encoding='utf8') as f:
            text = f.read()
        text = substitute_config_values(text)

        print('write file: ' + full_output_path)

        with open(full_output_path, 'w', encoding='utf8') as f:
            f.write(text)


def substitute_config_values(text: str):
    """ Substitute values from the config, ignoring non-str values from the config """
    for key, val in filtered_config():
        text = text.replace('$' + key + '$', val)
    return text


for root, dirs, files in os.walk('template'):
    for dir in dirs:
        make_output_dir(root, dir)

    for file_name in files:
        process_file(root, file_name)

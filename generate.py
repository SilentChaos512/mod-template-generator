import io
import json
import os
import re
import shutil

with open('config.json') as f:
    CONFIG = json.load(f)

if not CONFIG:
    print("config.json is missing!")
    exit(1)


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


def hasIgnoredExtension(file_name: str):
    """ Determine if the extension is 'ignored' and the file should be copied directly """
    m = re.search(r'(?<=\.)[^.]+', file_name)
    return m.group() in CONFIG['ignoredExtensions'] if m else False


def process_file(root: str, file_name: str):
    """ Process a file, performing substitutions where appropriate """
    print('read file: ' + file_name)

    full_input_path = os.path.join(root, file_name)
    full_output_path = get_output_path(os.path.join(root, file_name))

    if hasIgnoredExtension(file_name):
        print('processing not allowed, copying file: ' + full_input_path)
        print('copied to: ' + full_output_path)
        shutil.copyfile(full_input_path, full_output_path)
    else:
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

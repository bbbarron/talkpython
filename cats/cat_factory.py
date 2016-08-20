"""
cat_factory.py
This program is part of the Talk Python to Me series of tutorials.
bbarron
"""
import os
import platform
import subprocess

import catpics_service


def main():
    print_the_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


def print_the_header():
    print('---------------------------------------')
    print('              Cat Factory      ')
    print('---------------------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    print('Contacting server and downloading cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('downloading cat ' + name)
        catpics_service.get_cat(folder, name)
    print('Done!')


def display_cats(folder):
    # open folder
    print('Display cats in OS window')
    if platform.system() == "Darwin":
        subprocess.call(['open', folder])
    elif platform.system() == "Linux":
        subprocess.call(['xdg-open', folder])
    elif platform.system() == "Windows":
        subprocess.call(['explorer', folder])
    else:
        print('Sorry, we can"t handle your OS ' + platform.system())


if __name__ == '__main__':
    main()

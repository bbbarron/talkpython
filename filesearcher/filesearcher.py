'''
filesearcher.py File searching app. Provided as part of Talk Python to Me
course in python. Adapted by B. Barron 8/27/2016

Modified to ignore hidden and non-text based files which tripped a Unicode
error on Mac OSX.

'''


import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:  # Iterate through the matches, and then give a count at the end
        match_count += 1
        print(m)
        print('--------- MATCH -------------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line))
        print('match: ' + m.text.strip())
        print()

    print("Found {:,} matches.".format(match_count))


def print_header():
    print('-------------------------------------')
    print('           FILE SEARCH APP')
    print('-------------------------------------')


def get_folder_from_user():  # Reject blank entries and return full file path
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():  # return lowercase
    text = input('What are you searching for [single or partial words only]? ')
    return text.lower()


def search_folders(folder, text):  # Make a list of all the items in the directory
    items = os.listdir(folder)

    for item in items:

        full_item = os.path.join(folder, item)

        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)

        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    try:
        with open(filename, 'r', encoding='utf-8') as fin:
            line_num = 0
            for line in fin:
                line_num += 1
                if line.lower().find(search_text) >= 0:
                    m = SearchResult(line=line_num, file=filename, text=line)
                    # matches.append(m)
                    yield m

    except UnicodeDecodeError:
        pass


if __name__ == '__main__':
    main()

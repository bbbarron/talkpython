import jrnl

"""
Journal application to create a modest daily journal
Talk Python to Me class
August 10, 2016
journal_app.py
bbarron

"""


def main():
    print_header()
    event_loop()


def print_header():
    print()
    print('----------------------------------')
    print('          Journal App')
    print('----------------------------------')
    print()


def event_loop():
    cmd = 'QUIT'
    journal_name = 'default'
    journal_data = jrnl.load(journal_name) # This loads a list of journal entries
    print('What would you like to do?')
    while cmd != 'x' and cmd:
        cmd = input('Type [A]dd, [L]ist, or e[X]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'l':
            list_entries(journal_data)
        elif cmd != 'x' and cmd:
            print(" Sorry, I don't understand {}".format(cmd))
    print('Done...Goodbye!')
    jrnl.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries:')
    print()
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))
    print()


def add_entry(data):
    text = input('Type your entry, <enter> to quit:')
    jrnl.add_entry(text, data)


if __name__ == "__main__":
    main()
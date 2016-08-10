"""
Journal application to create a modest daily journal
Talk Python to Me class
August 10, 2016
journal_app.py
bbarron

"""

import journal


def print_header():
    print()
    print('----------------------------------')
    print('          Journal App')
    print('----------------------------------')
    print()


def event_loop():
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)
    )
    print('What would you like to do?')
    while cmd != 'x':
        cmd = input('Type [A]dd, [L]ist, or e[X]it:')
        cmd = cmd.lower().strip()
        print (cmd)
        if cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'l':
            list_entries(journal_data)
        elif cmd != 'x':
            print(" Sorry, I don't understand {}".format(cmd))
    print('Done...Goodbye!')
    journal.save(jou)

def add_entry(data):
    text = input('Type your entry, <enter> to quit:')
    data.append(text)


def list_entries(data):
    print('Your journal entries:')
    print()
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx+1, entry))
    print()


def main():
    print_header()
    event_loop()
    add_entry(data)
    list_entries(data)



main()
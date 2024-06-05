import datetime

from Note.Note import Note
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = Note('asda', [1,2], 3)
    a.updated_at = datetime.datetime.now()
    print(a.updated_at)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import argparse
import ls

def main():
    hidden = False

    parser = argparse.ArgumentParser(
             description='List files and directories')
    parser.add_argument('path', metavar='PATH',
           nargs='?',
           default='.',
           help='directory for which to list the contents')
    parser.add_argument('--all', '-a', 
           action='store_true',
           help='Show all')

    options = parser.parse_args()

    hidden = options.all
    path = options.path

    ls.list_files(path, hidden=hidden)


if __name__ == '__main__':
    main()
"""
Easy Snippet

Usage:
    easy-snippet repository list
    easy-snippet repository new <name> <repository>
    easy-snippet repository delete <name>
    easy-snippet repository edit <name> <repository>
    easy-snippet repository tree <name>
    easy-snippet get [--xclip] <repository> <path>
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)

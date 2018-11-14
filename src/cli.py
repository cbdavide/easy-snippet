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
from github import query

import conf

if __name__ == '__main__':
    # arguments = docopt(__doc__)
    url = 'https://api.github.com/repos/SuprDewd/CompetitiveProgramming/contents'
    auth = (conf.USER, conf.PRIVATE_TOKEN)

    test = ['perrito', 'asdasperrito asdasd perritodf', 'hamburguesaper']
    # tr = query.beautiful_tree( url, auth )
    query.search( test, 'perrito' )
    # for t in tr:
        # print( t )

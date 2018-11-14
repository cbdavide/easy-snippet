import re
import requests

PIPE = '|'
BRANCH = '__'
SEPARATOR = ' '
MAX_DEPTH_LEVEL = 10

def beautify(name, level, full_path):
    prfx = ""
    if level > 0:
        level *= 2
        prfx = "{}{}{} ".format(level * SEPARATOR, PIPE, BRANCH)

    return "{}{}".format(prfx, name)

def identity(name, level, full_path):
    return full_path

def tree(repository_url, callback, level, limit, auth=None):
    """
        This function traverses the file directory of a repository hosted on,
        github and returns a generator with its contents.
    """
    if level >= limit: return

    if auth is not None:
        r = requests.get( repository_url, auth=auth )
    else:
        r = requests.get( repository_url )

    for item in r.json():

        yield callback(item.get('name'), level, item.get('path'))

        if item.get('type') == 'dir':
            new_url = "{}/{}".format(repository_url, item.get('name'))
            subtree = tree( new_url, callback, level + 1, limit, auth )

            for branch in subtree:
                yield branch

def beautiful_tree(repository_url, auth=None, limit=MAX_DEPTH_LEVEL):
    return tree(repository_url, beautify, 0, limit, auth=auth)

def search(file_generator, pattern):

    regex = re.compile(pattern)

    for file in file_generator:
        print(10 * "*")

        result = regex.finditer( file )
        for r in result:
            print( bool( r ), r )

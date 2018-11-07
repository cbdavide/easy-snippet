import requests

PIPE = '|'
BRANCH = '__'
SEPARATOR = ' '

def beautify(name, times, full_path):
    prfx = ""
    if times > 0:
        prfx = "{}{}{} ".format(times*SEPARATOR, PIPE, BRANCH)

    return "{}{}".format(prfx, name)

def identity(name, times, full_path):
    return full_path

def tree(repository_url, callback, auth=None, times=0):
    """
        This function traverses the file directory of a repository hosted on,
        github and returns a generator with its contents.
    """

    if auth is not None:
        r = requests.get( repository_url, auth=auth )
    else:
        r = requests.get( repository_url )

    for item in r.json():

        yield callback(item.get('name'), times, item.get('path'))

        if(item.get('type') == 'dir'):
            new_url = "{}/{}".format(repository_url, item.get('name'))
            subtree = tree(new_url, callback, auth, times + 2 )

            for branch in subtree:
                yield branch


if __name__ == '__main__':
    url = 'https://api.github.com/repos/SuprDewd/CompetitiveProgramming/contents'
    tr = tree(url, beautify)
    for t in tr:
        print( t )

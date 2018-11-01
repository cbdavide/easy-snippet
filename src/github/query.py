import requests

PIPE = '|'
BRANCH = '__'
SEPARATOR = ' '

def tree(repository_url, auth=None, times=0):
    """
        This function traverses the file directory of a repository hosted on,
        github and returns a generator with its contents.
    """

    if auth is not None:
        r = requests.get( repository_url, auth=auth )
    else:
        r = requests.get( repository_url )

    for item in r.json():
        prfx = ""
        if times > 0:
            prfx = "{}{}{} ".format(times*SEPARATOR, PIPE, BRANCH)

        yield "{}{}".format(prfx, item.get('name'))

        if(item.get('type') == 'dir'):
            subtree = tree(repository_url + '/' + item.get('name'), auth, times + 2 )

            for branch in subtree:
                yield branch


if __name__ == '__main__':
    tr = tree('https://api.github.com/repos/SuprDewd/CompetitiveProgramming/contents')
    for t in tr:
        print( t )

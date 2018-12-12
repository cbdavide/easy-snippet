from decorators import get

@get('SELECT * FROM repository')
def get_repositories(repostories):
    print(repostories)

if __name__ == '__main__':
    get_repositories()

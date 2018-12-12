
from entity import Repository
from decorators import get

class RepositoryDao:

    @classmethod
    @get('SELECT * FROM repository')
    def get_repositories(self, repostories):
        for repository in repostories:
            yield Repository(repository[0], repository[1])


if __name__ == '__main__':

    for r in RepositoryDao.get_repositories():
        print(r)

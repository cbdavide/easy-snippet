
from entity import Repository
from decorators import get


class RepositoryDao:

    @classmethod
    @get('SELECT * FROM repository')
    def getRepositories(**kwargs):
        for repository in kwargs.get('result', []):
            yield Repository(repository[0], repository[1])

    @classmethod
    @get('SELECT * FROM repository WHERE user=?')
    def getRepositoriesByUser(**kwargs):
        for repository in kwargs.get('result', []):
            yield Repository(repository[0], repository[1])


if __name__ == '__main__':

    for r in RepositoryDao.getRepositoriesByUser(params=('cbdavide',)):
        print(r)

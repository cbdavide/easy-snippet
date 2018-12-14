
from entity import Repository
from decorators import query


class RepositoryDao:

    @staticmethod
    @query('SELECT * FROM repository')
    def getRepositories(**kwargs):
        return Repository.fromList(kwargs.get('result', []))

    @staticmethod
    @query('SELECT * FROM repository WHERE user=?')
    def getRepositoriesByUser(**kwargs):
        return Repository.fromList(kwargs.get('result', []))


if __name__ == '__main__':

    for r in RepositoryDao.getRepositoriesByUser(params=('cbdavide',)):
        print(r)

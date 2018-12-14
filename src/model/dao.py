
from decorators import query
from decorators import insert

from entity import Repository


class RepositoryDao:

    @staticmethod
    @query('SELECT * FROM repository')
    def getRepositories(**kwargs):
        return Repository.fromList(kwargs.get('result', []))

    @staticmethod
    @query('SELECT * FROM repository WHERE user=?')
    def getRepositoriesByUser(**kwargs):
        return Repository.fromList(kwargs.get('result', []))

    @staticmethod
    @insert('INSERT INTO repository VALUES (?,?)')
    def insert(**kwargs):
        print(kwargs.get('result', []))


if __name__ == '__main__':

    # RepositoryDao.insert(params=('anotheruser', 'repo123'))
    # RepositoryDao.insert(params=[
    #     ('usera', 'repoa'),
    #     ('userb', 'repob'),
    #     ('userc', 'repoc')
    # ])
    for r in RepositoryDao.getRepositoriesByUser(params=('cbdavide',)):
        print(r)

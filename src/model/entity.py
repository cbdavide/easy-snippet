
class Repository:

    def __init__(self, user, name):
        self.user = user
        self.name = name

    @classmethod
    def fromList(cls, repositories):
        for user, name in repositories:
            yield cls(user, name)

    def __str__(self):
        return "{}/{}".format(self.user, self.name)

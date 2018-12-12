
class Repository:

    def __init__(self, user, name):
        self.user = user
        self.name = name

    def __str__(self):
        return "{}/{}".format(self.user, self.name)

import json

class Client:

    def __init__(self):
        self.id = 0
        self.name = ''
        self.users = []    # creates a new empty list of users

    def addUser(self, user):
        self.users.append(user)

    def setId(self, id):
        self.id=id
    
    def setName(self, name):
        self.name=name

    def toJSON(self):
        return json.dumps(self.__dict__)



class UserEntity(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age
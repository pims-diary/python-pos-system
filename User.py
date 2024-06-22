class User:
    def __init__(self, user):
        self.user = user

    @property  # this is also automatically the getter
    def username(self):
        return self.user['username']

    @username.setter
    def username(self, value):
        self.user['username'] = value

    @property  # this is also automatically the getter
    def password(self):
        return self.user['password']

    @password.setter
    def password(self, value):
        self.user['password'] = value

    @property  # this is also automatically the getter
    def name(self):
        return self.user['name']

    @name.setter
    def name(self, value):
        self.user['name'] = value

    @property  # this is also automatically the getter
    def role(self):
        return self.user['role']

    @role.setter
    def role(self, value):
        self.user['role'] = value

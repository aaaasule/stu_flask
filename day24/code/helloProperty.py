# -*- encoding: utf-8 -*-
import hashlib


class Student(object):

    def __init__(self, _password=None):
        self._password = _password

    @property
    def password(self):
        return self._password
        # raise Exception("Can not access")

    @password.setter
    def password(self, value):
        self._password = hashlib.new('md5', value.encode('utf8')).hexdigest()

    @password.getter
    def password(self):
        pass


if __name__ == "__main__":
    student = Student()
    student.password = "11111111"
    print(student.password)

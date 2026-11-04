class X:
    def who_am_i(self):
        print("I am X")

class Y(X):
    def who_am_i(self):
        print("I am Y")

class Z(X):
    def who_am_i(self):
        print("I am Z")

class P(Z, Y):
    pass

class Q(Z, Y):
    def who_am_i(self):
        print("I am Q")

class R(P, Q):
    pass

r = R()
r.who_am_i()
print(R.__mro__)

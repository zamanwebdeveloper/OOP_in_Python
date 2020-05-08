# Inheritance - Indirect
class A:
    def frist(self):
        print('method - A')
class B(A):
    def second(self):
        print('method - B')
class C(B):
    def third(self):
        print('method - C')
D = C()
D.frist()
D.second()
D.third()
test

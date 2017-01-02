class X:
    def __init__(self):
        print('x')
class A(X):
    def __init__(self):
        super(A,self).__init__()
        print('\ta')
class B(X):
    def __init__(self):
        super(B,self).__init__()
        print('\tb')
def test():
    a = A()
    b = B()
test()
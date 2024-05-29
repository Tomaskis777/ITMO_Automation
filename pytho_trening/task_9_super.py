class A:

    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        self.y = ('x + 5')
        super().__init__()

    print('B')
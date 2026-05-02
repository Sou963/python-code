class something:
    def __init__(self):
        print('This is something class')

class rewrite(something):
    def __init__(self):
        super().__init__()
        print('This is rewrite class')

obj1=rewrite()

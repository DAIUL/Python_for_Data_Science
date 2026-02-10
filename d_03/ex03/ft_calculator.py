class calculator:
    '''
    Docstring pour calculator
    '''
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        values = [x+object for x in self.vector]
        self.vector = values
        print(self.vector)
        return None

    def __mul__(self, object) -> None:
        values = [x*object for x in self.vector]
        self.vector = values
        print(self.vector)
        return None

    def __sub__(self, object) -> None:
        values = [x-object for x in self.vector]
        self.vector = values
        print(self.vector)
        return None

    def __truediv__(self, object) -> None:
        if object != 0:
            values = [x/object for x in self.vector]
            self.vector = values
        print(self.vector)
        return None

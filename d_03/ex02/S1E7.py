from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, first_name, is_alive=True,
                 family_name='Baratheon', eyes='brown', hairs='dark'):
        '''
        Docstring pour __init__
        '''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''
        Docstring pour __str__
        '''
        return self.first_name

    def __repr__(self):
        '''
        Docstring pour __repr__
        '''
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        '''
        Docstring pour die
        '''
        self.is_alive = False


class Lannister(Character):
    '''Representing the Lannister family.'''
    def __init__(self, first_name, is_alive=True,
                 family_name='Lannister', eyes='bleu', hairs='light'):
        '''
        Docstring pour __init__
        '''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''
        Docstring pour __str__
        '''
        return self.first_name

    def __repr__(self):
        '''
        Docstring pour __repr__
        '''
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        '''
        Docstring pour die
        '''
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True,
                         family_name='Lannister', eyes='bleu', hairs='light'):
        return cls(first_name, is_alive=True,
                   family_name='Lannister', eyes='bleu', hairs='light')

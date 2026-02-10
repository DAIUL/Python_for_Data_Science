from abc import ABC, abstractmethod


class Character(ABC):
    '''
    Docstring pour Character
    '''

    def __init__(self, first_name, is_alive=True):
        '''
        Docstring pour __init__
        '''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    '''
    Docstring pour Stark
    '''

    def die(self):
        '''
        Docstring pour die
        '''
        self.is_alive = False

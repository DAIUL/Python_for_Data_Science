from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Docstring pour King'''
    def die(self):
        '''Docstring for die'''
        self.is_alive = False

    def set_eyes(self, color):
        '''
        Docstring pour set_eyes
        '''
        self.eyes = color

    def set_hairs(self, color):
        '''
        Docstring pour set_hairs
        '''
        self.hairs = color

    def get_eyes(self):
        '''
        Docstring pour get_eyes
        '''
        return self.eyes

    def get_hairs(self):
        '''
        Docstring pour get_hairs
        '''
        return self.hairs

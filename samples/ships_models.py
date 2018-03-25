from ship import Ship

class Encouracado(Ship):

    def __init__(self, position):

        SIZE = 4
        NAME = 'Encouracado'
        self.structure = {'size':SIZE, 'name': NAME, 'head': position}
        Ship.__init__(self, self.structure)


class PortaAvioes(Ship):

    def __init__(self, position):

        SIZE = 5
        NAME = 'PortaAvioes'
        self.structure = {'size':SIZE, 'name': NAME, 'head': position}
        Ship.__init__(self, self.structure)


class Submarino(Ship):

    def __init__(self, position):

        SIZE = 3
        NAME = 'Submarino'
        self.structure = {'size':SIZE, 'name': NAME, 'head': position}
        Ship.__init__(self, self.structure)


class Destroyer(Ship):

    def __init__(self, position):

        SIZE = 3
        NAME = 'Destroyer'
        self.structure = {'size':SIZE, 'name': NAME, 'head': position}
        Ship.__init__(self, self.structure)


class BarcoDePatrulha(Ship):

    def __init__(self, position):

        SIZE = 2
        NAME = 'BarcoDePatrulha'
        self.structure = {'size':SIZE, 'name': NAME, 'head': position}
        Ship.__init__(self, self.structure)

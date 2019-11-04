class Banda():
    def __init__(self,id, nome,genero):
        self.__id=id
        self.__nome=nome
        self.__genero=genero
        
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def genero(self):
        return self.__genero
class Disco():
    def __init__(self,id_banda,id_disco,titulo,ano,preco):
        self.__id_banda=id_banda
        self.__id_disco=id_disco
        self.__titulo=titulo
        self.__ano=ano
        self.__preco=preco

    @property
    def id_banda(self):
        return self.__id_banda

    @property
    def id_disco(self):
        return self.__id_disco

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano

    @property
    def preco(self):
        return self.__preco
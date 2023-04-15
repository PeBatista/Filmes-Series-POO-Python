class Programa():
    def __init__(self,nome,ano):
        self._nome = nome # protegido _ e privado __
        self._ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def ano(self):
        return self._ano
    
    def curtir(self):
        self._likes += 1 

class BomDia():
    def __str__(self) -> str:  
        return f"Bom dia, nome de sua instância: {self.nome}"

class Filme(Programa):
    def __init__(self, nome, ano,duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    @property
    def duracao(self):
        return self._duracao
    
    def __str__(self):
        return f"Série: {self.nome} // {self.ano} // e tem {self._duracao} minutos"

    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
    
    @property
    def temporadas(self):
        return self._temporadas
    
    def __str__(self):
        return f"Série: {self.nome} // {self.ano} // e tem {self._temporadas} temporadas"
    
    
class Playlist(BomDia):
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self,lista):
        return self._programas[lista]   

    def __len__(self):
        return len(self._programas)
    


# from conta import Serie, Filme, Playlist, caso estivesse dentro de outra página


breaking_bad = Serie("Breaking Bad", 2013, 6)
vingadores = Filme("Vingadores 2",2018,"1:30")   
lista = [breaking_bad, vingadores]
playlist1 = Playlist("Filmes e Series Tops", lista)

print(f"Playlist tal: {playlist1} tem {len(playlist1)} programas adicionados")




        




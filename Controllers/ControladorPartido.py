from Models.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorPartido():

    def __init__(self):
        print("Creando ControladorPartido")
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listar todos los partidos")
        return self.repositorioPartido.findAll()

    def create(self,infoPartido):
        print("Crear un partido")
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self,id):
        print("Mostrando un partido con id ",id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self,id,infoPartido):
        print("Actualizando partido con id ",id)
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]

        return self.repositorioPartido.save(partidoActual)

    def delete(self,id):
        print("Elimiando partido con id ",id)
        return self.repositorioPartido.delete(id)
from Models.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa
class ControladorMesa():

    def __init__(self):
        print("Creando ControladorMesa")
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        print("Listar todas las mesas")
        return self.repositorioMesa.findAll()

    def create(self,infoMesa):
        print("Crear una mesa")
        nuevoMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)

    def show(self,id):
        print("Mostrando una mesa con id ",id)
        elMesa = Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__

    def update(self,id,infoMesa):
        print("Actualizando mesa con id ",id)
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero de mesa"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad de inscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self,id):
        print("Elimiando mesa con id ",id)
        return self.repositorioMesa.delete(id)
from Models.Resultado import Resultado
from Repositorios.RepositorioResultado import RepositorioResultado
from Models.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Models.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorResultado():

    def __init__(self):
        print("Creando ControladorResultado")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        print("Listar todos los resultados")
        return self.repositorioResultado.findAll()

    def create(self,infoResultado,id_candidato,id_mesa):
        print("Crear un resultado")
        nuevoResultado = Resultado(infoResultado)
        candidatoActual = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesaActual = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = candidatoActual
        nuevoResultado.mesa = mesaActual
        return self.repositorioResultado.save(nuevoResultado)

    def show(self,id):
        print("Mostrando un resultado con id ",id)
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self,id,infoResultado,id_candidato,id_mesa):
        print("Actualizando resultado con id ",id)
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        candidatoActual = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesaActual = Mesa(self.repositorioMesa.findById(id_mesa))
        return self.repositorioResultado.save(resultadoActual)

    def delete(self,id):
        print("Elimiando resultado con id ",id)
        return self.repositorioResultado.delete(id)
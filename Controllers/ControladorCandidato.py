from Models.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorCandidato():

	def __init__(self):
		print("Creando ControladorCandidato")
		self.repositorioCandidato = RepositorioCandidato()

	def index(self):
		print("Listar todos los Candidatos")
		return self.repositorioCandidato.findAll()

	def create(self,infoCandidato):
		print("Crear un candidato")
		nuevoCandidato=Candidato(infoCandidato)
		return self.repositorioCandidato.save(nuevoCandidato)

	def show(self,id):
		print("Mostrando un Candidato con id ",id)
		elCandidato = Candidato(self.repositorioCandidato.findById(id)) 
		return elCandidato.__dict__

	def update(self,id,infoCandidato):
		print("Actualizando Candidato con id ",id)
		candidatoActual=Candidato(self.repositorioCandidato.findById(id)) 
		candidatoActual.cedula=infoCandidato["cedula"] 
		candidatoActual.numero_resoluciòn = infoCandidato["numero_resolucion"] 
		candidatoActual.nombre = infoCandidato["nombre"] 
		candidatoActual.apellido = infoCandidato["apellido"] 
		return self.repositorioCandidato.save(candidatoActual)
	
	def delete(self,id):
		print("Elimiando Candidato con id ",id)
		return self.repositorioCandidato.delete(id)
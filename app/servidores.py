import pandas as pd
from settings import escolaridade


def get_escolaridade(x):
	return escolaridade.Escolaridade.get(x['ESCOLARIDADE'].strip(), x['ESCOLARIDADE'].strip()) 
  

class Servidores:
	_instance = None
	_data = None
	
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Servidores, cls).__new__(cls)
			print("* * * * *  CRIOU A INSTÂNCIA")
			
		return cls._instance
		

	def carrega(self, csv):
		#url_csv = "https://docs.google.com/spreadsheets/d/1SBmAivb0M5xJ5giQ9noQ41A2Pr1S8_YoZQ9_z2tqMnM/edit#gid=1740862460"
		#link = url_csv.replace("/edit#gid=", "/export?format=csv&gid=")
		#print("Carregando do drive...")
		#print("CSV escolhido (local): " + csv)
		#self._data = pd.read_csv(link, low_memory=False, sep=";")
		self._data = pd.read_csv(csv, low_memory=False, encoding="UTF-16", sep=";")
		self._data['ESCOLARIDADE_'] = self._data.apply(lambda x: get_escolaridade(x), axis=1)
		
		#print(self._data)
		return self._data

	
	def todos(self):
		return self._data
		
	
	def efetivos(self, data=None):
		print(self._data)
		if data is None: data = self._data			
		return data[data["SITUAÇÃO VÍNCULO"].isin(["ATIVO PERMANENTE", "EXCEDENTE A LOTACAO", "ATIVO EM OUTRO ORGAO", "CEDIDO/REQUISITADO"])]


	def taes(self, data=None):
		if data is None: data = self._data		
		return data[data["CARGO"].str.contains("PROFESSOR") == False]	

		
	def docentes(self, data=None):
		if data is None: data = self._data		
		return data[data["CARGO"].str.contains("PROFESSOR")]	


	def aposentados(self, data=None):
		if data is None: data = self._data		
		return data[data["SITUAÇÃO VÍNCULO"] == "APOSENTADO"]


	def sexo_masculino(self, data=None):
		if data is None: data = self._data		
		return data[data["SEXO"] == "Mas"]


	def sexo_feminino(self, data=None):
		if data is None: data = self._data		
		return data[data["SEXO"] == "Fem"]


	def _por_situacao(self, servidores, situacoes):
		return self._data[self._data["SITUAÇÃO VÍNCULO"].isin(situacoes)]
	

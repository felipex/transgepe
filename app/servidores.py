import pandas as pd


class Servidores:
	_instance = None
	_data = None
	
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Servidores, cls).__new__(cls)
			print("* * * * *  CRIOU A INSTÂNCIA")
			
		return cls._instance
		

	def carrega(self, csv):
		self._data = pd.read_csv(csv, low_memory=False, encoding="UTF-16", sep=";")
		return self._data

	
	def efetivos(self, data=None):
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
	

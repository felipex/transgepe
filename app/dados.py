import pandas as pd

def servidores(csv):
	return carrega_servidores(csv)
	

def carrega_servidores(csv):
	data = pd.read_csv(csv, low_memory=False, encoding="UTF-16", sep=";")
	return data


def aposentados(csv):
	data = servidores(csv)
	return data[data["SITUAÇÃO VÍNCULO"] == "APOSENTADO"]


def servidores_com_funcao(servidores):
	return servidores[servidores["NÍVEL FUNÇÃO"] != "S/nivel funcao"]


def taes_com_funcao(servidores):
	return servidores[servidores["CARGO"].str.contains("PROFESSOR") == False]


def docentes_com_funcao(servidores):
	return servidores[servidores["CARGO"].str.contains("PROFESSOR")]

def servidores_por_situacao(servidores, situacoes):
	return servidores[servidores["SITUAÇÃO VÍNCULO"].isin(situacoes)]
	
def servidores_por_nome(servidores, nome):
	return servidores[servidores["NOME SERVIDOR"].str.contains(nome, case=False)]

def servidores_por_cargo(servidores, cargo):
	return servidores[servidores["CARGO"].str.contains(cargo, case=False)]


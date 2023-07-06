import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import dados
from common import header, filtros, c_css
from servidores import Servidores


### ------ FILTROS

def filtra_por_carreira(servidores, state):
	if state["carreira"] == 'TAES':
		return dados.taes_com_funcao(servidores)
	elif state.carreira == 'Docente':
		return dados.docentes_com_funcao(servidores)

	return servidores

def filtra_por_situacao(servidores, state):
	return dados.servidores_por_situacao(servidores, pd.Series(state["situacao"]))


def filtra_por_nome(servidores, state):
	return dados.servidores_por_nome(servidores, state["nome"])

def filtra_por_cargo(servidores, state):
	return dados.servidores_por_cargo(servidores, state["cargo"])

### ------ Filtro geral
def filtra(servidores, state):
	filtrados = filtra_por_carreira(servidores, state)
	filtrados = filtra_por_situacao(filtrados, state)
	filtrados = filtra_por_nome(filtrados, state)
	filtrados = filtra_por_cargo(filtrados, state)
	
	return filtrados


### ------ Funções dos gráficos
def atualiza_dashboard(servidores):
	servidores_filtrados = filtra(servidores, st.session_state)
	#labels(servidores_filtrados)
    #labels(servidores_filtrados)
	
	#col1, col2 = st.columns(2)
	#with col1:
	#	chart = funcs_por_sexo(servidores_filtrados)
	#	st.altair_chart(chart, use_container_width=True, theme="streamlit")
	
	#filtrados2 = filtra_por_carreira(servidores, st.session_state)
	#with col2:
		#chart2 = geral_por_sexo(filtrados2)
		#st.altair_chart(chart2, use_container_width=True, theme="streamlit")
	#	geral_por_sexo2(filtrados2)

	data = servidores_filtrados[["NOME SERVIDOR", "SITUAÇÃO VÍNCULO", "UORG", "CARGO", "ESCOLARIDADE"]]		
	st.dataframe(data)



def main():

	c_css()

	### Pega todos os servidores	st.write(servidores)    
	header()
	#servidores = dados.servidores("./dw/UFCA202212.csv")
	servidores = Servidores().todos()
	filtros(servidores)
	
	#labels(servidores)
	atualiza_dashboard(servidores)

#st.set_page_config(
#	page_title="Efetivos",
#	page_icon="👋",
#)
	
main()


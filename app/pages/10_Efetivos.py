import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from servidores import Servidores
from common import header, c_css

# Variável Global

#Servidores().carrega("./dw/UFCA_2022_12.csv.zip")
servidores = Servidores().efetivos()
#######################################

def funcs_por_sexo(data):
	chart = alt.Chart().mark_bar().encode(
		alt.X('count():Q', title="Quantidade"),
		alt.Y('SEXO:O', title=""),
		color=alt.Color("SEXO:N", legend=None)
	)
	texts = chart.mark_text(dx=10, align="center", baseline="middle").encode(
		text="count()"
	)

	c = alt.layer(chart, texts, data=data).facet(
		row="NÍVEL FUNÇÃO:N"
	)
	return c



def jornada_de_trabalho(data):
	st.vega_lite_chart(data, {
	    "title": {
			"text": "Jornada de Trabalho",
			"offset": 10,
			"fontSize": 18
		},
	    "layer": [
		{
		  "mark": {"type": "bar"},
		  "encoding": {
		    "y": {"field": "JORNADA TRABALHO", "type": "nominal", "title": "Jornada de Trabalho"},
		    "x": {"aggregate": "count", "stack": True, "type": "quantitative", "title": "Quantidade"},
		    "color": {"field": "JORNADA TRABALHO", "type": "nominal", "legend": False},
		  }
		},
		{
		  "mark": {"type": "text"},
		  "encoding": {
		    "text": {"aggregate": "count", "type": "quantitative"},
		  }
		}]
		
	})

def jornada_de_trabalho(data):
	chart = alt.Chart().mark_bar().encode(
		alt.X('count():Q', title="Quantidade"),
		alt.Y('JORNADA TRABALHO:O', title=""),
		#color=alt.Color('ESCOLARIDADE:N', legend=None)
	).properties(
		title = "Jornada de Trabalho"
	)
	texts = chart.mark_text(dx=10, align="center", baseline="middle").encode(
		text="count()"
	)
	
	c = alt.layer(chart, texts, data=data)
	return c


def escolaridade(data):
	chart = alt.Chart().mark_bar().encode(
		alt.X('count():Q', title="Quantidade"),
		alt.Y('ESCOLARIDADE_:O', title=""),
		#color=alt.Color('ESCOLARIDADE:N', legend=None)
	).properties(
		title = "Escolaridade"
	)
	texts = chart.mark_text(dx=10, align="center", baseline="middle").encode(
		text="count()"
	)
	
	c = alt.layer(chart, texts, data=data)
	return c

def lotacoes(data):
	chart = alt.Chart().mark_bar().encode(
		alt.X('count():Q', title="Quantidade"),
		alt.Y('GRUPO UORG:O', title=""),
		#color=alt.Color('ESCOLARIDADE:N', legend=None)
	).properties(
		title = "Lotações"
	)
	texts = chart.mark_text(dx=10, align="center", baseline="middle").encode(
		text="count()"
	)
	
	c = alt.layer(chart, texts, data=data)
	return c


def cor_etnia(data):
	chart = alt.Chart().mark_bar().encode(
		alt.X('count():Q', title="Quantidade"),
		alt.Y('COR ORIGEM ETNICA:O', title=""),
		#color=alt.Color('ESCOLARIDADE:N', legend=None)
	).properties(
		title = "Cor/Origem Étnica"
	)
	texts = chart.mark_text(dx=10, align="center", baseline="middle").encode(
		text="count()"
	)
	
	c = alt.layer(chart, texts, data=data)
	return c


def idade(data):
	chart = alt.Chart().mark_bar().encode(
		alt.X('count():Q', title="Quantidade" ),
		alt.Y('IDADE:O', title="",sort="descending"),
		#color=alt.Color('ESCOLARIDADE:N', legend=None)
	).properties(
		title = "Idade"
	)
	texts = chart.mark_text(dx=10, align="center", baseline="middle").encode(
		text="count()"
	)
	
	c = alt.layer(chart, texts, data=data)
	return c

### ------ FILTROS
def filtros(servidores):
	with st.sidebar:
		st.markdown("#### Filtros")
		carreiras = st.selectbox(
			"Carreira:",
			("Todos", "TAES", "Docente"),
			#on_change=onchange_carreira,
			key="carreira")



def filtra_por_carreira(servidores, state):
	efetivos = Servidores().efetivos()
	if state["carreira"] == 'TAES':
		return Servidores().taes(efetivos)
	elif state.carreira == 'Docente':
		return Servidores().docentes(efetivos)

	return servidores



### ------ Filtro geral
def filtra(servidores, state):
	filtrados = filtra_por_carreira(servidores, state)
	return filtrados


### ------ Funções dos gráficos
def atualiza_dashboard(servidores):
	servidores_filtrados = filtra(servidores, st.session_state)
	
	tab1, tab2, tab3 = st.tabs(["Resumo", "Funções", "Listagem"])

	
	with tab1:
		labels(servidores_filtrados)
		
		container = st.container()
		col1, col2 = container.columns(2)
		
		with col1:
			chart = escolaridade(servidores_filtrados)
			st.altair_chart(chart, use_container_width=True, theme="streamlit")

		with col2:		
			chart = jornada_de_trabalho(servidores_filtrados)
			st.altair_chart(chart, use_container_width=True, theme="streamlit")

		container = st.container()
		col1, col2 = container.columns(2)
		
		with col1:
			chart = lotacoes(servidores_filtrados)
			st.altair_chart(chart, use_container_width=True, theme="streamlit")

		with col2:		
			chart = cor_etnia(servidores_filtrados)
			st.altair_chart(chart, use_container_width=True, theme="streamlit")


		container = st.container()
		col1, col2 = container.columns(2)
		
		with col1:
			chart = idade(servidores_filtrados)
			st.altair_chart(chart, use_container_width=True, theme="streamlit")


	with tab2:	
		col1, col2 = st.columns(2)
		with col1:
			chart = funcs_por_sexo(servidores_filtrados)
			st.altair_chart(chart, use_container_width=True, theme="streamlit")
		

	with tab3:
		st.dataframe(servidores_filtrados)
		
	
	

def label(title, value, percent):
	st.markdown(f"<div class='label'><span class='title'>{title}:</span> <br/><span class='value'>{value}</span> <span class='percent'>({percent:.2f}%)</span></div>", unsafe_allow_html=True)

def label2(title, value):
	st.markdown(f"<div class='label'><span class='title'>{title}:</span> <br/><span class='value'>{value}</span> </div>", unsafe_allow_html=True)


def labels(servidores):
	with st.container() as metricas:
		col1, col2, col3 = st.columns(3)
		total = len(servidores)
		with col1:
			label2("Servidores", total)
		with col2:
			masc = len(Servidores().sexo_masculino(servidores))
			masc_p = 100* masc/total
			label("Homens", masc, masc_p)
		with col3:	
			fem = len(Servidores().sexo_feminino(servidores))
			fem_p = 100* fem/total
			label("Mulheres", fem, fem_p)


def main():

	st.set_page_config(layout="wide")
	c_css()
	header()
		
	filtros(servidores)

	atualiza_dashboard(servidores)

	
main()


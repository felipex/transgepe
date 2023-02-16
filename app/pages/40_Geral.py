import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import dados
from common import header, filtros, c_css


def funcs_por_sexo(data):
	chart = alt.Chart().mark_bar().encode(
		alt.X('count():Q', title="Quantidade"),
		alt.Y('SEXO:O', title=""),
		color='SEXO:N'
	)
	texts = chart.mark_text(dx=10, align="center", baseline="middle").encode(
		text="count()"
	)

	c = alt.layer(chart, texts, data=data).facet(
		row="NÍVEL FUNÇÃO:N"
	)
	return c


def geral_por_sexo(data):
	chart = alt.Chart().mark_arc(innerRadius=50, outerRadius=140).encode(
			theta=alt.Theta('count():Q', stack=True),
			color=alt.Color('SEXO:N')
	)
	texts = chart.mark_text(radiusOffset=15, radius=140).encode(
		text=alt.Text("count()"),
	)

	fig = alt.layer(chart, texts, data=data)
	return fig
	

def geral_por_sexo2(data):
	st.vega_lite_chart(data, {
	    "layer": [
		{
		  "mark": {"type": "arc", "innerRadius": 50, "outerRadius": 140},
		  "encoding": {
		    "color": {"field": "SEXO", "type": "nominal"},
		    "theta": {"aggregate": "count", "stack": True, "type": "quantitative"}
		  }
		},
		{
		  "mark": {"type": "text", "radius": 140, "radiusOffset": 15},
		  "encoding": {
		    "color": {"field": "SEXO", "type": "nominal"},
		    "text": {"aggregate": "count", "type": "quantitative"},
		    "theta": {"aggregate": "count", "stack": True, "type": "quantitative"}
		  }
		}]
		
	})
	

### ------ FILTROS

### ---- Deixa só quem tem função
def filtra_por_funcao_e_carreira(servidores, state):
	servidores_com_funcao = dados.servidores_com_funcao(servidores)
	if state["carreira"] == 'TAES':
		return dados.taes_com_funcao(servidores_com_funcao)
	elif state.carreira == 'Docente':
		return dados.docentes_com_funcao(servidores_com_funcao)

	return servidores_com_funcao


def filtra_por_carreira(servidores, state):
	if state["carreira"] == 'TAES':
		return dados.taes_com_funcao(servidores)
	elif state.carreira == 'Docente':
		return dados.docentes_com_funcao(servidores)

	return servidores

def filtra_por_situacao(servidores, state):
	return dados.servidores_por_situacao(servidores, pd.Series(state["situacao"]))

### ------ Filtro geral
def filtra(servidores, state):
	filtrados = filtra_por_carreira(servidores, state)
	filtrados = filtra_por_situacao(filtrados, state)
	return filtrados


### ------ Funções dos gráficos
def atualiza_dashboard(servidores):
	servidores_filtrados = filtra(servidores, st.session_state)
	labels(servidores_filtrados)
    #labels(servidores_filtrados)
	
	col1, col2 = st.columns(2)
	with col1:
		chart = funcs_por_sexo(servidores_filtrados)
		st.altair_chart(chart, use_container_width=True, theme="streamlit")
	
	filtrados2 = filtra_por_carreira(servidores, st.session_state)
	with col2:
		#chart2 = geral_por_sexo(filtrados2)
		#st.altair_chart(chart2, use_container_width=True, theme="streamlit")
		geral_por_sexo2(filtrados2)


def labels(servidores):
	with st.container() as metricas:
		col1, col2, col3 = st.columns(3)
		with col1:
			st.metric("Servidores:", len(servidores))
		with col2:
			st.metric("Homens:", len(servidores[servidores["SEXO"]=="Mas"]))
		with col3:	
			st.metric("Mulheres:", len(servidores[servidores["SEXO"]=="Fem"]))


def main():

	c_css()

	### Pega todos os servidores	st.write(servidores)    
	header()
	servidores = dados.servidores("./dw/UFCA202212.csv")
	filtros(servidores)
	
	#labels(servidores)
	atualiza_dashboard(servidores)

#st.set_page_config(
#	page_title="Efetivos",
#	page_icon="👋",
#)
	
main()


import streamlit as st
import os
import servidores
import requests

def muda_base():
	#servidores.Servidores().carrega()
	print(st.session_state["base"])

def get_bases():
	remote_files = "http://vps36332.publiccloud.com.br/static/files.json" 

	req = requests.get(remote_files)
	return req.json()


def header():
	col1, col2 = st.columns([1,2])
	with col1:
		st.image("./ufca.png", width=200)
	with col2:
		st.markdown("## Força de Trabalho")

		bases = get_bases()
	
		keys = list(bases.keys())
		select = st.selectbox("Base:", keys, key="base_", on_change=muda_base, index=len(keys)-1)

		st.session_state["base"] = bases[select]
		servidores.Servidores().carrega(st.session_state["base"])
		
		


def filtros(servidores):
	with st.container() as filtros:
		st.markdown("### Filtros")
		col1, col2 = st.columns([1,2])
		with col1:	
			carreiras = st.selectbox(
				"Carreira:",
				("Todos", "TAES", "Docente"),
				#on_change=onchange_carreira,
				key="carreira")
		with col2:		
			st.multiselect("Situação", servidores["SITUAÇÃO VÍNCULO"].unique().tolist(), key="situacao", default=["ATIVO PERMANENTE"])




def c_css():	
	with open("custom.css") as f:
		st.write(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)
		#element-container css-1b6t8kw e1tzin5v3


import streamlit as st
import os
import servidores

def muda_base():
	#servidores.Servidores().carrega()
	print(st.session_state["base"])

def header():
	col1, col2 = st.columns([1,2])
	with col1:
		st.image("./ufca.png", width=200)
	with col2:
		st.markdown("## Força de Trabalho")
#		st.markdown("**Base Dezembro/2022** - *Fonte: DW-Siape*")
		
		files = os.listdir("dw")
		bases = []
		meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
		for f in files:
			filename = f.split(".")[0]
			parts = filename.split("_")
			if len(parts) == 3:
				bases.append(meses[int(parts[2])-1] + "/" +parts[1])
		default = st.session_state["base"] if "base" in st.session_state.keys() else None
		if default is None:
			default = st.session_state["base"] = "./dw/"+files[len(files)-1]
			
		select = st.selectbox("Base:", bases, key="base_", on_change=muda_base, index=len(bases)-1)
		
		st.session_state["base"] = "./dw/"+files[bases.index(select)]
		servidores.Servidores().carrega(st.session_state["base"])
		
		st.write(st.session_state["base"])
		


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


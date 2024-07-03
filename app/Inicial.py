import streamlit as st
from common import header, c_css
import os
import re
import sys

sys.path.join("./app/")
c_css()


header()

	
#st.header("Painel da Força de Trabalho da UFCA")

def selo(header, text, link="#"):
	return	st.write(f"""
			<a href='{link}'>
			<div class='selo'>
			<h5>{header}</h5>
			<span>{text}<span>
			</div>
			</a>
			""", unsafe_allow_html = True)

col1, col2 = st.columns(2)

with col1:
	with st.container() as container:
		selo("Efetivos", "Informações sobre os servidores que estão ativos na UFCA.", "/Efetivos")

with col2:
	with st.container() as container:
		selo("Aposentados", "Listagem dos servidores aposentados pela UFCA.", "/Aposentados")


with col1:
	with st.container() as container:
		selo("QRSTA", "Quadro de Referência de Servidores Ativos. Aumentando só pra testar", "QRSTA")


with col2:
	with st.container() as container:
		selo("Geral", "Informação de todos os servidores da UFCA.", "Geral")


st.markdown("----")

